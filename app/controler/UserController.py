from app.model.user import User
from app.model.gambar import Gambar
from app import response, app, db, uploadconfig
from flask import request
import os
import uuid
from werkzeug.utils import secure_filename


def upload():
    try:
        judul = request.form.get('judul')
        file = request.files['file']

        if 'file' not in request.files:
            return response.badRequest([], 'file tidak tersedia')

        if file.filename == "":
            return response.badRequest([], "file tidak tersedia")
        
        if file and uploadconfig.allowed_file(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.name)
            renamefile = "Flask-"+str(uid)+filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))

            uploads = Gambar(judul=judul, pathname=renamefile)
            db.session.add(uploads)
            db.session.commit()

            return response.success(
                {
                    'judul':judul,
                    'patname':renamefile
                }, "sukses upload file"
            )
        
        else:
            return response.badRequest([],"file tidak diizinkan")
    except Exception as e:
        print(e)

def buatAdmin():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        level = 1

        users = User(name = name, email=email, level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success("", 'berhasil menambahkan data admin')
        
    except Exception as e:
        print(e)