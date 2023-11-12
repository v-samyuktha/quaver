from flask_restful import Resource, fields, marshal_with, reqparse
from flask import render_template, redirect, request, make_response
from application.models import Song

#Listens at /api/songs?name="song name"
class SongAPI(Resource):
    def get(self):
        if request.args.get("name"):
            result = Song.query.filter_by(title=request.args.get("name")).first()
            if result is None:
                return None
            song = result.__dict__.copy()
            song.pop("_sa_instance_state")
            return song
        
        else:
            details = Song.query.all()
            song_list = []
            for song in details:
                song_dict = song.__dict__.copy()
                song_dict.pop("_sa_instance_state", None)
                song_list.append(song_dict)
            return song_list