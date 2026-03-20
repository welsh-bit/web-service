from flask import Flask

app = Flask(__name__)

# View counter
view_count = 0

@app.route('/')
def index():
    global view_count
    view_count += 1
    return f'''
    <html>
    <body>
        <h1>Welcome to My Webpage</h1>
        <p>This page has been viewed <strong>{view_count}</strong> times.</p>
        <a href="/home">Go to Home</a>
    </body>
    </html>
    '''

@app.route('/home')
def home():
    return f'''
    <html>
    <body>
        <h1>Home Page</h1>
        <p>This webpage has been viewed <strong>{view_count}</strong> times total.</p>
        <a href="/">Go to Index</a>
    </body>
    </html>
    '''


@app.route('/about')
def about():
    return "<h1>About Page</h1><p>웹사이트와 관련된 정보를 나열하는 페이지!</p><h2>이 웹사이트는 2026년 3월 13일(금)에 제작되었음.</h2>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1><p>이메일로 연락가능</p><p>전화번호:xxx-xxxx-xxxx</p>"

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)