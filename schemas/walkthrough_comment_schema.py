from main import ma

class WalkthroughCommentSchema(ma.Schema):
    class Meta:
        fields = ("id","walkthrough_id", "comment_id")

walkthrough_comment_schema = WalkthroughCommentSchema()
walkthrough_comments_schema = WalkthroughCommentSchema(many=True)
