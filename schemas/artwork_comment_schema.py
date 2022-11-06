from main import ma

class ArtworkCommentSchema(ma.Schema):
    class Meta:
        fields = ("id", "artwork_id", "comment_id")

artwork_comment_schema = ArtworkCommentSchema()
artwork_comments_schema = ArtworkCommentSchema(many=True)
