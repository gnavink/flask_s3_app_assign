from flask import request
from config import s3_app,client

@s3_app.route('/upload-image',methods=['POST'])
def upload_image():
    bucket='navins3bucket123'
    content_type=request.mimetype
    obj=request.files['file']
    filename=obj.filename
    client.put_object(Body=obj,
          Bucket=bucket,
          Key=filename,
          ContentType=content_type
    )

    return {'message': 'file uploaded'}, 200

@s3_app.route("/download-file/<string:filename>",methods=["GET"])
def getFileToDownload(filename):
      client.download_file('navins3bucket123',filename,   "c:\\new-downloads\\"+filename)
      return {"message ": "check the download folder"}, 200