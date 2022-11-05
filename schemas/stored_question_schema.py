from main import ma

class StoredQuestionSchema(ma.Schema):
    class Meta:
        fields = ("id", "question_id", "q_and_a_id")

stored_question_schema = StoredQuestionSchema()
stored_questions_schema = StoredQuestionSchema(many=True)