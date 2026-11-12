from flask import Flask, jsonify
from database.db import init_db  
from routes.upload_route import upload_bp  
from routes.download_route import download_bp  
import os  

app = Flask(__name__)  

UPLOAD_FOLDER = 'uploads'  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  

if not os.path.exists(UPLOAD_FOLDER):  
    os.makedirs(UPLOAD_FOLDER)  

init_db()  

app.register_blueprint(upload_bp, url_prefix='/uploads')  
app.register_blueprint(download_bp, url_prefix='/downloads')  

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API de Upload e Download funcionando!",
        "status": "online",
        "rotas": {
            "upload": "POST /uploads/upload",
            "download": "GET /downloads/download/<filename>"
        }
    })

if __name__ == '__main__':  
    app.run(debug=True)  
