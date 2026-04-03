from flask import Flask, render_template

app = Flask(__name__)

stats = {"view_count": 0}

@app.route('/')
def index():
    stats["view_count"] += 1

    return render_template('index.html', count=stats["view_count"])

@app.route('/home')
def home():
    return render_template('home.html', count=stats["view_count"])

if __name__ == '__main__':
    app.run(debug=True)