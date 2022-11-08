from main import ma

class ArtworkSchema(ma.Schema):
    class Meta:
        fields = ("id", "artwork_name", "description", "date", "artist_id")
        ordered = True
