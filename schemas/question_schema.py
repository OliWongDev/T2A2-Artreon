from main import ma

class QuestionSchema(ma.Schema):
    class Meta:
        fields = ("id", "is_answered", "date", "user_id")

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)