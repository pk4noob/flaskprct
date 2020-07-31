from flask import Flask
from extensions.extensions import ma, db


class Product(db.Model):
    __tablename__ = 'PRoduct'

    category_id = db.Column(db.Integer(), db.ForeignKey(
        'category_id'), nullable=False, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def savedb(self):
        db.session.add(self)
        db.session.commit()

    def deletedb(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.savedb()


class Category(db.Model):
    __tablename__ = 'categoryy'
    name = db.Column(db.String(), nullable=False)

    def savedb(self):
        db.session.add(self)
        db.session.commit()

    def deletedb(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.savedb()
