from flask import request
from app import app
from app.controler import DosenController
from app.controler import UserController
from flask import request

@app.route('/')
def index():
    return "hello flask jancok"


@app.route('/dosen', methods=["GET", "POST"])
def dosen():
    if request.method == "GET":
        return DosenController.index()
    else:
        return DosenController.save()

@app.route('/dosen/<id>', methods=['PUT','DELETE'])
def dosenDetail(id):
    if request.method == 'PUT':
        return DosenController.ubah(id)
    else:
        return DosenController.hapus(id)

@app.route('/createadmin', methods=["POST"])
def admins():
    return UserController.buatAdmin()


@app.route('/file-upload', methods=["POST"])
def upload():
    return UserController.upload()