from main import ma

class QAndASchema(ma.Schema):
    class Meta:
        fields = ("id", "q_and_a_content", "date")

q_and_a_schema = QAndASchema()
q_and_as_schema = QAndASchema(many=True)
