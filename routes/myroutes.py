from config import app

@app.route('/')
def greet():
    return "Hello Flask app is running!!!"

