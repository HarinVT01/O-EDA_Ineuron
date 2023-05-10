import os
from flask import render_template, url_for, redirect, Blueprint,current_app
from eda_app import db
from flask_login import current_user
from eda_app.models import Card
from eda_app.cards.forms import CardForm,UploadForm
from werkzeug.utils import secure_filename

cards = Blueprint('cards',__name__)

@cards.route("/home",methods=['GET','POST'])
def home():  
    eda_cards=Card.query.all()
    return render_template('home.html',title='HOME',eda_cards=eda_cards)


@cards.route("/add_card",methods=['GET','POST'])
def add_card():
    form = CardForm()
    if form.validate_on_submit():
        card = Card(title=form.title.data, description=form.description.data,author=current_user)
        db.session.add(card)
        db.session.commit()
        # flash('Your post has been created!', 'success')
        return redirect(url_for('cards.home'))
    return render_template('add_card.html', title='Home',form=form, legend='Add Card')

# @cards.route("/add_link",methods=['GET','POST'])
# def add_card():
#     form = CardForm()
#     if form.validate_on_submit():
#         card = Card(title=form.title.data, description=form.description.data,author=current_user)
#         db.session.add(card)
#         db.session.commit()
#         # flash('Your post has been created!', 'success')
#         return redirect(url_for('cards.home'))
#     return render_template('add_link.html', title='Home',form=form, legend='Add Link')

@cards.route("/upload",methods=['GET','POST'])
def upload_data():
    form=UploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.fileName.data.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'],'static','datasets', filename)
        data_file=form.fileName.data
        data_file.save(file_path)
        return redirect(url_for('cards.home'))
    return render_template('upload_data.html', title='Upload',form=form, legend='Upload Dataset')

@cards.route("/eda",methods=['GET','POST'])
def eda():
     return render_template('eda_report.html', title='EDA')