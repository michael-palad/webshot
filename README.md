# Webshot

A Python Flask app that can take screenshots of a website utilizing a background worker.

1. Create a virtual environment: python -m venv venv
2. Install requirements: pip install -r requirements.txt
3. Install redis-server: sudo apt-get install redis-server
4. export environment variable: export FLASK_APP=app.py
5. Run the worker: rq worker
6. Make sure redis is running: redis-server
7. Run Flask: flask run
