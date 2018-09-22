# from django.db import models
from mongoengine import *
connect('tumblelog')
# Create your models here.


class TestModel(Document):
    
    # point out collection( similar with table )!!!!
    
    meta = {
        'collection': 'Wow',
        # all ur documents will be stored into collection named "Wow"
        'strict': False
      }
    
    test_key = StringField(required=True)
    test_value = StringField(max_length=50)