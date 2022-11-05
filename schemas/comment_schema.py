from main import ma

class CommentSchema(ma.Schema):
    class Meta:
        fields = ("id", "date", "user_id")

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)