from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Item

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@main_bp.route('/add', methods=['POST'])
def add_item():
    name = request.form.get('name')
    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/change_status/<int:item_id>')
def change_status(item_id):
    item = Item.query.get(item_id)
    if item.status == 'Available':
        item.status = 'Unavailable'
    else:
        item.status = 'Available'
    db.session.commit()
    return redirect(url_for('main.index'))
