from flask import Flask, render_template, request
from tasks import create_url_screenshot

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        return 'You entered {}'.format(url)
    return render_template('index.html')




