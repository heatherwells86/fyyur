from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
import json

db = SQLAlchemy()


class Venue(db.Model):
    __tablename__ = 'venue'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String)
    image_link = Column(String)
    facebook_link = Column(String)
    website = Column(String)
    genres = Column(String, nullable=False)
    seeking_talent = Column(Boolean, default=False)
    seeking_description = Column(String)

    shows = db.relationship('Show', backref='venue', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Artist(db.Model):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    phone = Column(String)
    genres = Column(String, nullable=False)
    image_link = Column(String)
    facebook_link = Column(String)
    website = Column(String)
    seeking_venue = Column(Boolean, default=False)
    seeking_description = Column(String)

    shows = db.relationship('Show', backref='artist', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Show(db.Model):
    __tablename__ = 'show'

    id = Column(Integer, primary_key=True)
    artist_id = Column(Integer, db.ForeignKey('artist.id'), nullable=False)
    venue_id = Column(Integer, db.ForeignKey('venue.id'), nullable=False)
    start_time = Column(DateTime, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()