from flask import Blueprint, jsonify,render_template
from  flask_login import current_user,login_required
from .models import Music,Comment
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from flask import current_app

from . import db
views=Blueprint('views',__name__)
@views.route('/')
@login_required
def home():
    music=Music.query.all()
    return render_template("home.html",user=current_user, musics=music)

@views.route('/upload',methods=['POST'])
@login_required
def upload():
    title = request.form['title']
    music_file = request.files['music']
    image_file = request.files['image']

    music_filename = secure_filename(music_file.filename)
    image_filename = secure_filename(image_file.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']

# Check if the upload folder exists, and if not, create it
    os.makedirs(upload_folder, exist_ok=True)

    music_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], music_filename))
    image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename))

    new_music = Music(title=title, music_file=music_filename, image_file=image_filename, user_id=1)  
    db.session.add(new_music)
    db.session.commit()
    return redirect(url_for('views.home'))
@views.route('/comment/<int:music_id>', methods=['POST'])
def comment(music_id):
    content = request.form['content']
    new_comment = Comment(content=content, user_id=1, music_id=music_id)  # Assume user_id is 1 for now
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('views.home'))

@views.route('/delete-comment/<int:comment_id>', methods=['POST'])
def delete_comment(comment_id):
    print(comment_id)
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('views.home'))


