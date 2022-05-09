from app.model.dosen import Dosen
from app import response, app, db
from flask import request

def index():
    try:
        dosen = Dosen.query.all()
        data = formatarray(dosen)
        return response.success(data, "success")
    except Exception as e:
        print(e)

def formatarray(datas):
    array=[]

    for i in datas:
        array.append(singleObject(i))
    return array

def singleObject(data):
    data= {
        'id' : data.id,
        'nidn' : data.nidn,
        'nama' : data.nama,
        'phone' : data.phone,
        'alamat' : data.alamat
    }
    return data


def save():
    try:
        nidn = request.form.get("nidn")
        nama = request.form.get("nama")
        phone = request.form.get("phone")
        alamat = request.form.get("alamat")

        dosens = Dosen(nidn = nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosens)
        db.session.commit()

        return response.success("", 'berhasil menambahkan data dosen')
        
    except Exception as e:
        print(e)


def ubah(id):
    try:
        nidn=request.form.get('nidn')
        nama=request.form.get('nama')
        phone=request.form.get('phone')
        alamat=request.form.get('alamat')

        input = [
            {
                'nidn': nidn,
                'nama' : nama,
                'phone' : phone,
                'alamat' : alamat
            }
        ]
        dosen = Dosen.query.filter_by(id=id).first()

        dosen.nidn=nidn
        dosen.nama = nama
        dosen.phone = phone
        dosen.alamat = alamat

        db.session.commit()

        return response.success(input, "sukses update data")
    except Exception as e:
        print(e)


def hapus(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.badRequest([],"Data yang dimaksud tidak ada ....")
        db.session.delete(dosen)
        db.session.commit()

        return response.success("", 'berhasil menghapus data dosen yang dimaksud')


    except Exception as e:
        print(e)

