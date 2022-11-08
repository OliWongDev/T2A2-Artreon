from main import db
from flask import Blueprint
# from main import Bcrypt
from models.artists import Artist
from models.artwork_comments import ArtworkComment
from models.artworks import Artwork
from models.comments import Comment
from models.emails import Email
from models.q_and_as import QAndA
from models.q_and_a_comments import QAndAComment
from models.questions import Question
from models.stored_questions import StoredQuestion
from models.users import User
from models.walkthrough_comments import WalkthroughComment
from models.walkthroughs import Walkthrough
import datetime

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables are created")

@db_commands.cli.command("seed")
def seed_db():
    
    # 1 x Artist
    artist = Artist(
        artreon_alias = "Graphic God",
        password = "artist_password",
        email = "graphicgod@artreon.com",
        is_admin = True,
        artist_bio = "Hi there! I'm Graphic God and welcome to my Artreon where you can see my wonderful artworks. If you want to learn how I do it all become a paid user and join the art revolution!"
    )

    db.session.add(artist)

    # 2 x Free User
    freeuser1 = User(
        user_alias = "Free2View",
        first_name = "Alex",
        last_name = "Smith",
        join_date = datetime.date.today(),
        email = "free2view@gmail.com",
        has_subscription = False,
        password = "freeloader"
    )

    freeuser2 = User(
        user_alias = "Consumer Not Creator",
        first_name = "Jason",
        last_name = "Zhao",
        join_date = datetime.date.today(),
        email = "artmuncher@gmail.com",
        has_subscription = False,
        password = "artshouldbefree"
    )

    db.session.add(freeuser1)
    db.session.add(freeuser2)

    # 3 x Paid User

    paiduser1 = User(
        user_alias = "Art Begunner",
        first_name = "Ellie",
        last_name = "Jackson",
        join_date = datetime.date.today(),
        email = "learningellie@gmail.com",
        has_subscription = True,
        password = "lovelearning123"
    )

    paiduser2 = User(
        user_alias = "BanksyInTraining",
        first_name = "Lucas",
        last_name = "Ramirez",
        join_date = datetime.date.today(),
        email = "lucasbanks@gmail.com",
        has_subscription = True,
        password = "iknowwhoheis"
    )

    paiduser3 = User(
        user_alias = "Graphic God Disciple",
        first_name = "Fiona",
        last_name = "Singh",
        join_date = datetime.date.today(),
        email = "fionas@gmail.com",
        has_subscription = True,
        password = "gospel"
    )

    db.session.add(paiduser1)
    db.session.add(paiduser2)
    db.session.add(paiduser3)

    # 4 x Artworks

    artwork1 = Artwork(
        artwork_name = "Triumph",
        description = "A grizzly feline racecar driver wins their final race. Tile mosaic.",
        date = datetime.date.today(),
        artist_id = 1
    )

    artwork2 = Artwork(
        artwork_name = "The First Spray",
        description = "A young graffiti artist makes their first tag underneath a moving train. Drawn with fine line.",
        date = datetime.date.today(),
        artist_id = 1
    )    

    artwork3 = Artwork(
        artwork_name = "White Depression",
        description = "A subtle look at a depressed mind. Painted with oil.",
        date = datetime.date.today(),
        artist_id = 1
    )

    artwork4 = Artwork(
        artwork_name = "French Burgers",
        description = "A burger with a snaily twist. Stippled.",
        date = datetime.date.today(),
        artist_id = 1
    )

    db.session.add(artwork1)
    db.session.add(artwork2)
    db.session.add(artwork3)
    db.session.add(artwork4)

    # 5 x comments to map
    comment1 = Comment(
        description = "Wow, this is a fresh twist!",
        date = datetime.datetime.today(),
        user_id = 4
        )
    
    comment2 = Comment(
        description = "Oooo I'd like to purchase this one, would look good on my wall.",
        date = datetime.datetime.today(),
        user_id = 3
        )

    comment3 = Comment(
        description = "Da Vinci could do better, but you're pretty good",
        date = datetime.datetime.today(),
        user_id = 5
        )

    comment4 = Comment(
        description = "It's confusing, but it makes sense at the same time",
        date = datetime.datetime.today(),
        user_id = 4
        )

    comment5 = Comment(
        description = "You make art objective.",
        date = datetime.datetime.today(),
        user_id = 5
        )

    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)
    db.session.add(comment5)

# 3 x Artwork Comments
    artwork_comment1 = ArtworkComment(
        artwork_id = 2, 
        comment_id = 3,
    )

    artwork_comment2 = ArtworkComment(
        artwork_id = 4,
        comment_id = 5,
    )

    artwork_comment3 = ArtworkComment(
        artwork_id = 2,
        comment_id = 4
    )

    db.session.add(artwork_comment1)
    db.session.add(artwork_comment2)
    db.session.add(artwork_comment3)
    
    # 3 x Q&As
    q_and_a1 = QAndA(
        q_and_a_content =   """ Q1: What is your favourite piece?
                                A1: I really enjoyed working on the White Depression piece, I think it explains deeply what the gift of art has done for me :)

                                Q2: What is one thing you can't leave the house without?
                                A2: I refuse to leave my bedroom let alone my house without my pencil, you never know when a good idea might hit.

                                Q3: Why aren't you doing graffiti anymore? I used to love the urban murals.
                                A3: This is mainly down to time as it takes a lot of effort to make a large piece. It's also good to branch out into other styles to keep it fresh.
                        
                        """,
        date = datetime.date.today()
    )

    q_and_a2 = QAndA(
        q_and_a_content =   """ Q1: Would you start again with a pencil or a brush?
                                A1: I think that a brush is the way I would go, it expands the horizons quicker than a pencil. No choice is bad one though.

                                Q2: Who are you listening to at the moment?
                                A2: Whilst making art I've been really loving classical music of late such as Beethoven and Bach. It seems to bring out more creativity.

                                Q3: Do you do collabs?
                                A3: Absolutely! Nothing like a working with an art buddy on something we're both passionate about :)
                        
                        """,
        date = datetime.date.today()
                        
    )

    q_and_a3 = QAndA(
        q_and_a_content =   """ Q1: Do you do customs?
                                A1: For now no, but if I have the time I will open this option up again. We can negotiate a price and an output type to your enjoyment.

                                Q2: How do you break out of an art slump?
                                A2: Firstly, I get away from the art space and leave it for as long as it needs. I am also usually needing some hours outdoors when I get into a rut so walking is another thing I'll do.

                                Q3: How do you respond to haters?
                                A3: What's important to me are my users; free and paid that continue to follow my journey. I do my best to remember that when I doubt myself.
                        
                        """,
        date = datetime.date.today()
    )

    db.session.add(q_and_a1)
    db.session.add(q_and_a2)
    db.session.add(q_and_a3)

    # 3 x Q&A comments to map
    q_and_a_comment1 = QAndAComment(
        q_and_a_id = 2,
        comment_id = 5
    )

    q_and_a_comment2 = QAndAComment(
        q_and_a_id= 1,
        comment_id = 1
    )

    q_and_a_comment3 = QAndAComment(
        q_and_a_id = 3,
        comment_id = 4
    )

    db.session.add(q_and_a_comment1)
    db.session.add(q_and_a_comment2)
    db.session.add(q_and_a_comment3)

    # 3 x Walkthroughs
    
    walkthrough1 = Walkthrough(
        description = "A video tutorial of my 'White Depression' piece. Bring your canvases!",
        date = datetime.date.today(),
        artist_id = 1,
        artwork_id = 3
    )

    walkthrough2 = Walkthrough(
        description = "A video tutorial for 'French Burgers'. After watching this, stippling will become 2nd nature",
        date = datetime.date.today(),
        artist_id = 1,
        artwork_id = 4
    )

    walkthrough3 = Walkthrough(
        description = "Here's the video for 'Triumph'! A lot going on here so take it slow :)",
        date = datetime.date.today(),
        artist_id = 1,
        artwork_id = 1
    )

    db.session.add(walkthrough1)
    db.session.add(walkthrough2)
    db.session.add(walkthrough3)

    # 3 x Walkthrough comments to map
    walkthrough_comment1 = WalkthroughComment(
        walkthrough_id = 1,
        comment_id = 1
    )

    walkthrough_comment2 = WalkthroughComment(
        walkthrough_id = 2,
        comment_id = 2
    )

    walkthrough_comment3 = WalkthroughComment(
        walkthrough_id = 3,
        comment_id = 3,
    )

    db.session.add(walkthrough_comment1)
    db.session.add(walkthrough_comment2)
    db.session.add(walkthrough_comment3)

    # 9 x Questions
    question1 = Question(
        question_content = "Would you start again with a pencil or a brush?",
        is_answered = True,
        date = datetime.date.today(),
        user_id = 3,
    )

    question2 = Question(
        question_content = "What is one thing you can't leave the house without?",
        is_answered = True,
        date = datetime.date.today(),
        user_id = 4,
    )

    question3 = Question(
        question_content = "Why aren't you doing graffiti anymore? I used to love the urban murals.",
        is_answered = True,
        date = datetime.date.today(),
        user_id = 4,
    )

    question4 = Question(
        question_content = "Would you start again with a pencil or a brush?",
        is_answered = True,
        date = datetime.date.today(),
        user_id = 5
    )

    question5 = Question(
        question_content = "Who are you listening to at the moment?",
        is_answered = True,
        date = datetime.date.today(),
        user_id = 4,
    )

    question6 = Question(
        question_content = "Do you do collabs?",
        is_answered = True,
        date = datetime.date.today(),
        user_id = 5
    )

    question7 = Question(
        question_content = "Do you do customs?",
        is_answered = True,
        date = datetime.date.today(),
        user_id = 3,
    )

    question8 = Question(
        question_content = "How do you break out of an art slump?",
        is_answered = True,
        date = datetime.date.today(),
        user_id = 3,
    )

    question9 = Question(
        question_content = "How do you respond to haters?",
        is_answered = True,
        date = datetime.date.today(),
        user_id = 3
    )

    db.session.add(question1)
    db.session.add(question2)
    db.session.add(question3)
    db.session.add(question4)
    db.session.add(question5)
    db.session.add(question6)
    db.session.add(question7)
    db.session.add(question8)
    db.session.add(question9)


    # 3 x Stored Questions
    stored_question1 = StoredQuestion(
        question_id = 5,
        q_and_a_id = 2
    )

    stored_question2 = StoredQuestion(
        question_id = 6,
        q_and_a_id = 2,
    )

    stored_question3 = StoredQuestion(
        question_id = 9,
        q_and_a_id = 3,
    )

    db.session.add(stored_question1)
    db.session.add(stored_question2)
    db.session.add(stored_question3)

    # 4 x Emails

    email1 = Email(
        email_title = "Big things coming soon!",
        email_content =     """ Just wanted to get a quick message out to the users of my Artreon that big things are coming soon and I've got a whole slew of collabed pieces almost ready to present for you all.
                                Exciting times.

                                Graphic God
                            """,
        send_date = datetime.date.today(),
        artist_id = 1
    )

    email2 = Email(
        email_title = "Free Membership Offer",
        email_content =     """ It's December and therefore the holiday season so I'm offering my free users a one month premium trial throughout the month. 
                                Enjoy your end of year celebrations wherever you may be.

                                Graphic God
                            """,
        send_date = datetime.date.today(),
        artist_id = 1
    )

    email3 = Email(
        email_title = "Check out my interview with the Artreon podcast!",
        email_content =     """ Howdy!
                                I did an interview with the kind folks from Artreon about my experience on the platform, you can check it out here!
                                *LINK*


                                Graphic God
                            """,
        send_date = datetime.date.today(),
        artist_id = 1
    )

    email4 = Email(
        email_title = "Recommended Artreons to follow",
        email_content =     """ Salut,
                                I've been wanting to let my loyal users know about some other artists that I really like on Artreon. Believe it or not I'm not the only one!
                                1. PotteryPavilion
                                2. SculptorTrash6
                                3. TramStopSketchKid
                                
                                Keep on drawing my arty friends.

                                Graphic God
                            """,
        send_date = datetime.date.today(),
        artist_id = 1
    )

    db.session.add(email1)
    db.session.add(email2)
    db.session.add(email3)
    db.session.add(email4)
    db.session.commit()

    print('Tables are seeded')

# Seed Drop Command
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print('Tables are dropped')