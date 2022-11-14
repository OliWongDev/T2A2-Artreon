from main import db, ma
from marshmallow import fields

class Walkthrough(db.Model):
    __tablename__ = "walkthroughs"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    date = db.Column(db.Date(), nullable=False)

    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.id"), nullable=False)

    artist = db.relationship("Artist", back_populates="walkthroughs")
    artwork = db.relationship("Artwork", back_populates="walkthrough")
    walkthrough_comments = db.relationship("WalkthroughComment", back_populates="walkthrough", cascade="all, delete")

class WalkthroughSchema(ma.Schema):
    artist = fields.Nested("ArtistSchema", only=["artreon_alias"])
    artwork = fields.Nested("ArtworkSchema", only=["id", "artwork_name"])
    walkthrough_comments = fields.List(fields.Nested("WalkthroughCommentSchema", only=["id", "description", "user.user_alias"]))
    class Meta:
        fields = ("id", "description", "date", "artist", "artwork", "walkthrough_comments")
        ordered = True

# __permissions__ = dict(
#         artist_role=["read", "update", "post", "delete"],
#         paid_user_role=["read"]
#     )