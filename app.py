from flask import Flask,url_for,render_template,request
from flaskext.markdown import Markdown

# Init App
app = Flask(__name__)
Markdown(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
