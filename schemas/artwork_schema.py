from main import ma

class ArtworkSchema(ma.Schema):
    class Meta:
        fields = ("id", "artwork_name", "description", "date", "artwork_id")

artwork_schema = ArtworkSchema()
artworks_schema = ArtworkSchema(many=True)