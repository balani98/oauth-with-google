upload_location="C:\\Users\\deepanshu.balani\\Desktop\\Part 1\\api\\static"
from flask import Flask,jsonify,request,make_response
import logging
from datetime import datetime,timedelta
import os
from flask_cors import CORS,cross_origin
from werkzeug. utils import secure_filename
import jwt
app = Flask(__name__)
#these are hardcoded for demo purpose only
userEmail='admin@gmail.com'
userPassword='Admin1234@'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER']=upload_location
app.config['SECRET_KEY']='mysecret'
#params['upload_location']
cors = CORS(app)
@app.route('/uploader',methods=['POST'])
def uploader():
    f=request.files['image']
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
    result={
           "filename":secure_filename(f.filename),
           "message":"uploaded successfully"
           }
    return result
@app.route('/login',methods=['POST'])
def login():
   data = request.get_json()
   if data['email']==userEmail and data['password']==userPassword:
        payload = {
            'exp': datetime.now() + timedelta(days=0, seconds=5),
            'iat': datetime.now(),
            'email': userEmail
        }
        token = jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
        return jsonify({'token':str(token),'success':True})
   return make_response(jsonify(
                    {"message": 'Incorrect Email or Password'}
                ),
                401,)
   

if __name__=="__main__":
    app.run(debug=True)
