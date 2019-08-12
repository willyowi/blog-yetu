from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db,photos
from flask_login import login_required,current_user
from ..models import User,Blog,Comment
from .forms import UpdateProfile
from ..request import get_quote
#rout about
@main.route('/about')
def about():
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    #update
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    

    return render_template("profile/update.html", user = user )


@main.route('/')
def index():

    name = "Blog"
    quote=get_quote()
  
    # all_blogs = Blogs.get_all_blogs()
    
    return render_template('index.html',name = name,quote = quote)

    # return '<h1> Hello World </h1>'


#route new blog
@main.route('/new_blog', methods = ['GET','POST'])
@login_required

def new_blog():    
  blogform = BlogForm()


  if blogform.validate_on_submit():

        blog_title=blogform.title.data
        blog=blogform.blog_data.data
        url=blogform.photo_url.data

        new_blog=Blog(title=blog_title, blog_content = blog, date_posted=datetime.now())
        new_blog.save_blog()

        new_blog.save_blog()
        return redirect(url_for('main.view_blog',id=new_blog.id))

  return render_template('new_blog.html', blogform = blogform)

@main.route('/blog/<int:id>', methods=['GET','POST'])
def view_blog(id):
    get_blog=Blog.query.get(id)

    if get_blog is None:
        abort(404)

    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        user_name = comment_form.name.data
        user_email = comment_form.email.data
        user_comment = comment_form.comment_data.data

        new_comment = Comment(name=user_name,email=user_email,comment_content=user_comment,date_comment = datetime.now(),blog_id=id)
        new_comment.save_comment()

        return redirect(url_for('main.view_blog',id=id))
    
    get_comments = Comment.get_blog_comments(id)

    


    return render_template('blog.html', get_blog=get_blog,get_comments=get_comments,comment_form=comment_form)

 