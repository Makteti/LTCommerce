# app/__init__.py

from bottle import Bottle, template, request, redirect
from .models import Item, init_app

app = Bottle()

def my_url_for(endpoint):
    return f'/{endpoint}'

@app.route('/')
def index():
    items = Item.select()
    return template('views/index', items=items)

@app.route('/add', method='POST')
def add_item():
    name = request.forms.get('name')
    Item.create(name=name)
    return redirect('/')

@app.route('/delete/<item_id:int>', method='POST')
def delete_item(item_id):
    item = Item.get(Item.id == item_id)
    item.delete_instance()
    return redirect('/')

@app.route('/change_status/<item_id:int>', method='POST')
def change_status(item_id):
    item = Item.get(Item.id == item_id)
    item.status = 'Unavailable' if item.status == 'Available' else 'Available'
    item.save()
    return redirect('/')

init_app(app)
