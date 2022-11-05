from main import ma

class WalkthroughSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "date", "artist_id", "artwork_id")

walkthrough_schema = WalkthroughSchema()
walkthroughs_schema = WalkthroughSchema(many=True)