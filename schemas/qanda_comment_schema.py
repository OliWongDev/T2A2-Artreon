from main import ma

class QAndACommentSchema(ma.Schema):
    class Meta:
        fields = ("id", "qanda_id", "date", "comments_id")

q_and_a_comment_schema = QAndACommentSchema()
q_and_a_comment_schema = QAndACommentSchema(many=True)