from config import app,s3_app
import routes

if __name__=="__main__":
    #app.run(debug=True,host="0.0.0.0")
    s3_app.run(debug=True,host="0.0.0.0")