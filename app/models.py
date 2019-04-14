from app import db

class Song(db.Model):
    """This class represents the song table."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    artist = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, title, artist):
        """Initialize with title and artist."""
        self.title = title
        self.artist = artist

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod # return static list of songs
    def get_all():
        return Song.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self): # official string of the object, __str__ is informal
        return '<Song: {} - {}>'.format(self.title, self.artist)
