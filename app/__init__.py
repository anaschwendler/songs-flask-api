from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

from flask import request, jsonify, abort

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Song

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/songs/', methods=['POST', 'GET'])
    def songs():
        if request.method == "POST":
            title = str(request.data.get('title', ''))
            artist = str(request.data.get('artist', ''))
            if title and artist:
                song = Song(title=title, artist=artist)
                song.save()
                response = jsonify({
                    'id': song.id,
                    'title': song.title,
                    'date_created': song.date_created,
                    'date_modified': song.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            songs = Song.get_all()
            results = []

            for song in songs:
                obj = {
                    'id': song.id,
                    'title': song.title,
                    'artist': song.artist,
                    'date_created': song.date_created,
                    'date_modified': song.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/songs/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def song_manipulation(id, **kwargs):
     # retrieve a buckelist using it's ID
        song = Song.query.filter_by(id=id).first()
        if not song:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            song.delete()
            return {
                "message": "song {} deleted successfully".format(song.id)
             }, 200
        elif request.method == 'PUT':
            title = str(request.data.get('title', ''))
            artist = str(request.data.get('artist', ''))
            song.title = title
            song.artist = artist
            song.save()
            response = jsonify({
                'id': song.id,
                'title': song.title,
                'artist': song.artist,
                'date_created': song.date_created,
                'date_modified': song.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': song.id,
                'title': song.title,
                'artist': song.artist,
                'date_created': song.date_created,
                'date_modified': song.date_modified
            })
            response.status_code = 200
            return response

    return app
