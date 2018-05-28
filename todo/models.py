''' flask api models '''

import datetime

from argon2 import PasswordHasher
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from peewee import *

from . import db_proxy


# DATABASE = SqliteDatabase('todo.db')
HASHER = PasswordHasher()

class User(Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    
    class Meta:
        database = db_proxy

    @classmethod
    def create_user(cls, username, email, password, **kwargs):
        email = email.lower()
        try:
            cls.select().where(
                (cls.email==email)|(cls.username**username)
            ).get()
        except cls.DoesNotExist:
            user = cls(username=username, email=email)
            user.password = user.set_password(password)
            user.save()
            return user
        else:
            raise Exception("User with that email or username already exists")

    # @staticmethod
    # def verify_auth_token(token):
    #     serializer = Serializer(config.SECRET_KEY)
    #     try:
    #         data = serializer.loads(token)
    #     except (SignatureExpired, BadSignature):
    #         return None
    #     else:
    #         user = User.get(User.id==data['id'])
    #         return user    
            
    @staticmethod
    def set_password(password):            
        return HASHER.hash(password)

    def verify_password(self, password):
        return HASHER.verify(self.password, password) 

    # def generate_auth_token(self, expires=3600):  
    #     serializer = Serializer(config.SECRET_KEY, expires_in=expires)
    #     return serializer.dumps({'id': self.id})


class Todo(Model):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    created_by = ForeignKeyField(rel_model=User, null=False)
    
    class Meta:
        database = db_proxy

def init_db():
    db_proxy.connect()
    db_proxy.create_tables([User, Todo], safe=True)
    db_proxy.close()

        
    