import os
import glob
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
        return render_template('message.html', name=name, url=url)
    
    return render_template('index.html')


@app.route('/screenshots')
def screenshots():
    #screencaps_dir = os.path.join(os.path.dirname(app.instance_path), 'static/screenshots')
    #image_files = os.listdir(screencaps_dir)
    image_files = [image_file for image_file in glob.glob('static/screenshots/*.png') if not image_file.endswith('_tn.png')]
    image_files.sort(key=os.path.getmtime, reverse=True)
    image_names = [image_name.split('.png')[0].rsplit('/', 2)[-1] for image_name in image_files]
    return render_template('screenshots.html', image_names=image_names)





