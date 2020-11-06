from tinydb import TinyDB, Query


class BBDD:
    db = TinyDB('static/db.json')
    def insert(nombre, edad, email):
        db.insert({'nombre': nombre, 'edad': edad, 'email': email})

    print(db.all())