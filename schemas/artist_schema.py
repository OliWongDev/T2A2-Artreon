from main import ma

class ArtistSchema(ma.Schema):
    class Meta:
        fields = ("id", "artreon_alias", "password", "email", "is_admin", "artist_bio")

artist_schema = ArtistSchema()