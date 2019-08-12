from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    blog = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    bio = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # pass_secure = db.Column(db.String(255))

   

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # def set_password(self,password):
    #     self.password_hash = generate_password_hash(password)
        

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    blog_content = db.Column(db.String())
    posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.order_by('id').all()
        return blogs
    @classmethod
    def get_single_blog(cls,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

  


class Comment(db.Model):
    
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    comment_content = db.Column(db.String())
    date_comment = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_blog_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).order_by('id').all()
        return comments
    
    @classmethod
    def get_single_comment(cls,id_blog,id):
        comment = Comment.query.filter_by(blog_id=id_blog,id=id).first()

        return comment        
