from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/portofolio')
def portofolio():
    return render_template('portofolio.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

