from main import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "join_date", "email", "has_subscription", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)