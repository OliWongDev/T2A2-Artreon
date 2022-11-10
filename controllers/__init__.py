from controllers.artists_controller import artists
from controllers.artwork_comments_controller import artwork_comments
from controllers.artworks_controller import artworks
from controllers.auth_controller import auth
from controllers.comments_controller import comments
from controllers.emails_controller import emails
from controllers.q_and_as_controller import q_and_as
from controllers.q_and_a_comments_controller import q_and_a_comments
from controllers.users_controller import users
from controllers.walkthrough_comments_controller import walkthrough_comments
from controllers.walkthroughs_controller import walkthroughs

registerable_controllers = [
    artists,
    artwork_comments,
    artworks,
    auth,
    comments,
    emails,
    q_and_as,
    q_and_a_comments,
    users,
    walkthrough_comments,
    walkthroughs
]