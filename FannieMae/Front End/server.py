from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    gmi = float(request.form.get('gmi'))
    ccp = float(request.form.get('ccp'))
    cp = float(request.form.get('cp'))
    slp = float(request.form.get('slp'))
    av = float(request.form.get('av'))
    dp = float(request.form.get('dp'))
    la = float(request.form.get('la'))
    mmp = float(request.form.get('mmp'))
    cs = int(request.form.get('cs'))

    goodCredit = "Good"

    if cs < 640:
        goodCredit = "Bad"

    ltv = round((av - dp) / av, 2)

    pmiRate = 1.01
    pmiNeeded = False

    if ltv > 0.8:
        av = round(av * 1.01, 2)
        pmiNeeded = True

    monthlyDebt = round(ccp + cp + mmp + slp, 2)

    dti = round(monthlyDebt / gmi, 2)

    fedti = round(mmp / gmi, 2)

    approved = False

    if ltv < 0.9 and dti < 0.43 and fedti < 0.28:
        approved = True

    return render_template('results.html', gmi=f"{gmi:.2f}", ccp=f"{ccp:.2f}", cp=f"{cp:.2f}", slp=f"{slp:.2f}", av=f"{av:.2f}", dp=f"{dp:.2f}", la=f"{la:.2f}", mmp=f"{mmp:.2f}", cs=f"{cs:.2f}", goodCredit=goodCredit, pmiRate=f"{pmiRate:.2f}", ltv=f"{ltv:.2f}", monthlyDebt=f"{monthlyDebt:.2f}", dti=f"{dti:.2f}", fedti=f"{fedti:.2f}", approved=approved)

if __name__ == "__main__":
    app.run(debug=True)
