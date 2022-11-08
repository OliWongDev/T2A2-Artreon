from main import ma

class WalkthroughSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "date", "artist_id", "artwork_id")
        ordered = True

walkthrough_schema = WalkthroughSchema()
walkthroughs_schema = WalkthroughSchema(many=True)