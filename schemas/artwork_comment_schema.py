from main import ma

class ArtworkCommentSchema(ma.Schema):
    class Meta:
        fields = ("id", "artwork_id", "comment_id")
        ordered = True

