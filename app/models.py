from peewee import Model, SqliteDatabase, CharField

db = SqliteDatabase('warehouse.db')

class BaseModel(Model):
    class Meta:
        database = db

class Item(BaseModel):
    name = CharField()
    status = CharField(default='Available')

def init_app(app):
    app.db = db
    app.db.connect()
    app.db.create_tables([Item], safe=True)
