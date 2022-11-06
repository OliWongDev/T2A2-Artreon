from controllers.artists_controller import artists
from controllers.artwork_comments_controller import artwork_comments
from controllers.artworks_controller import artworks
from controllers.comments_controller import comments
from controllers.emails_controller import emails
from controllers.q_and_as_controller import q_and_as
from controllers.qanda_comments_controller import qanda_comments
from controllers.questions_controller import questions
from controllers.stored_questions_controller import stored_questions
from controllers.users_controller import users
from controllers.walkthrough_comments_controller import walkthrough_comments
from controllers.walkthroughs_controller import walkthroughs

registerable_controllers = [
    artists,
    artwork_comments,
    artworks,
    comments,
    emails,
    q_and_as,
    emails,
    q_and_as,
    qanda_comments,
    questions,
    stored_questions,
    users,
    walkthrough_comments,
    walkthroughs
]