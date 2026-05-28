'''
    config db, initialize data, set&get functions
'''
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, text

class Base(DeclarativeBase):
    '''
        Base class
    '''
    pass
db = SQLAlchemy(model_class=Base)

class User(db.Model):
    '''
        User table
    '''
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

def insert_user(user):
    '''
        insert user into db
    '''
    r = db.session.execute(db.select(User).filter_by(**user)).scalar_one_or_none()
    if r is None:
        u = User(**user)
        db.session.add(u)
        db.session.commit()

def get_user(username):
    '''
        select user from db
    '''
    query = f"select username,password from user where username='{username}'"
    user = db.session.execute(text(query)).fetchone()
    return user
