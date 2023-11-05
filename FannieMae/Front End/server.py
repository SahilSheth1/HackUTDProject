from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    gmi = request.form.get('gmi')
    ccp = request.form.get('ccp')
    cp = request.form.get('cp')
    slp = request.form.get('slp')
    av = request.form.get('av')
    dp = request.form.get('dp')
    la = request.form.get('la')
    mmp = request.form.get('mmp')
    cs = request.form.get('cs')
    return f'You entered: {gmi}, {ccp}, {cp}, {slp}, {av}, {dp}, {la}, {mmp}, {cs}'

if __name__ == "__main__":
    app.run(debug = True)