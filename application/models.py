from .database import db

class User(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)

# Song-Artist relationship table
song_artist_association = db.Table('song_artist_association', db.Model.metadata,
    db.Column('song_id', db.Integer, db.ForeignKey('songs.song_id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.artist_id'))
)

class Song(db.Model):
    __tablename__ = 'songs'
    song_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    duration = db.Column(db.String(20))
    release_date = db.Column(db.Date)
    genre = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    artists = db.relationship('Artist', secondary=song_artist_association, back_populates='songs')

class Artist(db.Model):
    __tablename__ = 'artists'
    artist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    songs = db.relationship('Song', secondary=song_artist_association, back_populates='artists')

'''
class PlaylistSong(db.Model):
    __tablename__ = 'playlist_songs'
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'))
    position = db.Column(db.Integer)
    playlist = db.relationship('Playlist', back_populates='songs')

class Playlist(db.Model):
    __tablename__ = 'playlists'
    playlist_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    songs = db.relationship('PlaylistSong', order_by='PlaylistSong.position', back_populates='playlists')
'''