import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from data.db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    school = sqlalchemy.Column(sqlalchemy.String, ForeignKey('schools.id'))
    role = sqlalchemy.Column(sqlalchemy.String)
    date_of_birth = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<Colonist> {self.id} {self.name} {self.email}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_pusersassword, password)


class Student(User):
    class_id = sqlalchemy.Column(sqlalchemy.String, ForeignKey('classes.id'))


class Teacher(User):
    subject = sqlalchemy.Column(sqlalchemy.String)
