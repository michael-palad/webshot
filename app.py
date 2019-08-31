from flask import Flask, render_template, request
from redis import Redis
from rq import Queue
from tasks import create_url_screenshot

app = Flask(__name__)
redis = Redis()
q = Queue(connection=redis)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        url = request.form.get('url')
        
        q.enqueue(create_url_screenshot, name, url)
        return 'Screenshot being taken for {} ({})'.format(name, url)
    return render_template('index.html')




