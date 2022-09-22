from mongoengine import Document
from mongoengine import (
    DateTimeField,
    StringField,
    IntField,
    EmailField,
    ReferenceField,
    ListField,
    FileField,
    ImageField,
    DateField
)

class User(Document):
    name = StringField()
    email = EmailField()
    password = StringField()

    def to_json(self, *args, **kwargs):
        return {"name":self.name, "email":self.email}

class Book(Document):
    name = StringField()
    category = StringField()
    rent = IntField()


class Transaction(Document):
    user = ReferenceField('User', reverse_delete_rule='CASCADE')
    book = ReferenceField('Book', reverse_delete_rule='CASCADE')
    issued_date = DateField()
    return_date = DateField()
    total_rent = IntField(default=0)
