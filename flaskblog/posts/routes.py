from flask import Blueprint

from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import CreatePostForm
from flaskblog.users.actions import save_pic


from flask_login import current_user, login_required



posts = Blueprint('posts', __name__)

@posts.route('/post/new', methods=['GET', 'POST'])
@posts.route('/create_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been posted")
        return redirect(url_for('application.home'))
    return render_template('create_post.html', title="New Post", form=form)

@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post, legend="New Post")

@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user != post.author:
        abort(403)
    form = CreatePostForm()
    if form.validate_on_submit():
        post.content = form.content.data
        post.title = form.title.data
        db.session.commit() #already in database, dont need to add, only modify exiting database
        flash('Post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.content.data = post.content
        form.title.data = post.title
    return render_template('create_post.html', title="Update Post", form=form, legend="Update Post")

@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user != post.author:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted', 'success')
    return redirect(url_for('application.home'))
