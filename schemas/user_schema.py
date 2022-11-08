from main import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_alias","first_name", "last_name", "join_date", "email", "has_subscription", "password")
        ordered = True

