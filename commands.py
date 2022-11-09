from main import db
from flask import Blueprint
from main import bcrypt
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
    admin_artist = Artist(
        artreon_alias = "Graphic God",
        password = bcrypt.generate_password_hash("artist_password").decode("utf-8"),
        email = "graphicgod@artreon.com",
        is_admin = True,
        artist_bio = "Hi there! I'm Graphic God and welcome to my Artreon where you can see my wonderful artworks. If you want to learn how I do it all become a paid user and join the art revolution!"
    )

    db.session.add(admin_artist)
    db.session.commit()

    # 1 x Non-Admin Artist
    non_admin_artist = Artist(
        artreon_alias = "Collaber",
        password = bcrypt.generate_password_hash("collab").decode("utf-8"),
        email = "collaber@gmail.com",
        is_admin = False,
        artist_bio = "I just post art every now and then."
    )

    db.session.add(non_admin_artist)
    db.session.commit()

    # 2 x Free User
    free_users = [
        User(
            user_alias = "Free2View",
            first_name = "Alex",
            last_name = "Smith",
            join_date = datetime.date.today(),
            email = "free2view@gmail.com",
            has_subscription = False,
            password = bcrypt.generate_password_hash("freeloader").decode("utf-8")
        ),

        User(
            user_alias = "Consumer Not Creator",
            first_name = "Jason",
            last_name = "Zhao",
            join_date = datetime.date.today(),
            email = "artmuncher@gmail.com",
            has_subscription = False,
            password = bcrypt.generate_password_hash("artshouldbefree").decode("utf-8")
        )
    ]

    db.session.add_all(free_users)
    db.session.commit()

    # 3 x Paid User

    paid_users = [
        User(
            user_alias = "Art Begunner",
            first_name = "Ellie",
            last_name = "Jackson",
            join_date = datetime.date.today(),
            email = "learningellie@gmail.com",
            has_subscription = True,
            password = bcrypt.generate_password_hash("lovelearning123").decode("utf-8")
        ),

        User(
            user_alias = "BanksyInTraining",
            first_name = "Lucas",
            last_name = "Ramirez",
            join_date = datetime.date.today(),
            email = "lucasbanks@gmail.com",
            has_subscription = True,
            password = bcrypt.generate_password_hash("iknowwhoheis").decode("utf-8")
        ),

        User(
            user_alias = "Graphic God Disciple",
            first_name = "Fiona",
            last_name = "Singh",
            join_date = datetime.date.today(),
            email = "fionas@gmail.com",
            has_subscription = True,
            password = bcrypt.generate_password_hash("gospel").decode("utf-8")
        ),
    ]
    db.session.add_all(paid_users)
    db.session.commit()

    # 4 x Emails

    emails = [
        Email(
            email_title = "Big things coming soon!",
            email_content =     """ Just wanted to get a quick message out to the users of my Artreon that big things are coming soon and I've got a whole slew of collabed pieces almost ready to present for you all.
                                    Exciting times.

                                    Graphic God
                                """,
            send_date = datetime.date.today(),
            artist_id = admin_artist.id
        ),

        Email(
            email_title = "Free Membership Offer",
            email_content =     """ It's December and therefore the holiday season so I'm offering my free users a one month premium trial throughout the month. 
                                    Enjoy your end of year celebrations wherever you may be.

                                    Graphic God
                                """,
            send_date = datetime.date.today(),
            artist_id = admin_artist.id
        ),

        Email(
            email_title = "Check out my interview with the Artreon podcast!",
            email_content =     """ Howdy!
                                    I did an interview with the kind folks from Artreon about my experience on the platform, you can check it out here!
                                    *LINK*


                                    Graphic God
                                """,
            send_date = datetime.date.today(),
            artist_id = admin_artist.id
        ),

        Email(
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
            artist_id = admin_artist.id
        )
    ]
    db.session.add_all(emails)
    db.session.commit()
    

    # 4 x Artworks

    artworks = [
        Artwork(
            artwork_name = "Triumph",
            description = "A grizzly feline racecar driver wins their final race. Tile mosaic.",
            date = datetime.date.today(),
            artist_id = admin_artist
        ),

        Artwork(
            artwork_name = "The First Spray",
            description = "A young graffiti artist makes their first tag underneath a moving train. Drawn with fine line.",
            date = datetime.date.today(),
            artist_id = admin_artist
        ),

        Artwork(
            artwork_name = "White Depression",
            description = "A subtle look at a depressed mind. Painted with oil.",
            date = datetime.date.today(),
            artist_id = admin_artist
        ),

        Artwork(
            artwork_name = "French Burgers",
            description = "A burger with a snaily twist. Stippled.",
            date = datetime.date.today(),
            artist_id = admin_artist
        ),
    ]
    db.session.add_all(artworks)
    db.session.commit()

    # 9 x Questions
    questions = [
        Question(
            question_content = "Would you start again with a pencil or a brush?",
            is_answered = True,
            date = datetime.date.today(),
            user = paid_users[0]
        ),

        Question(
            question_content = "What is one thing you can't leave the house without?",
            is_answered = True,
            date = datetime.date.today(),
            user = paid_users[1]
        ),

        Question(
            question_content = "Why aren't you doing graffiti anymore? I used to love the urban murals.",
            is_answered = True,
            date = datetime.date.today(),
            user = paid_users[1]
        ),

        Question(
            question_content = "Would you start again with a pencil or a brush?",
            is_answered = True,
            date = datetime.date.today(),
            user = paid_users[2]
        ),

        Question(
            question_content = "Who are you listening to at the moment?",
            is_answered = True,
            date = datetime.date.today(),
            user = paid_users[1]
        ),

        Question(
            question_content = "Do you do collabs?",
            is_answered = True,
            date = datetime.date.today(),
            user = paid_users[2]
        ),

        Question(
            question_content = "Do you do customs?",
            is_answered = True,
            date = datetime.date.today(),
            user = paid_users[0]
        ),

        Question(
            question_content = "How do you break out of an art slump?",
            is_answered = True,
            date = datetime.date.today(),
            user = paid_users[0]
        ),

        Question(
            question_content = "How do you respond to haters?",
            is_answered = True,
            date = datetime.date.today(),
            user = paid_users[0]
        )
    ]
    db.session.add_all(questions)
    db.session.commit()

    # 3 x Q&As
    q_and_as = [
        QAndA(
            q_and_a_content =   """ Q1: What is your favourite piece?
                                    A1: I really enjoyed working on the White Depression piece, I think it explains deeply what the gift of art has done for me :)

                                    Q2: What is one thing you can't leave the house without?
                                    A2: I refuse to leave my bedroom let alone my house without my pencil, you never know when a good idea might hit.

                                    Q3: Why aren't you doing graffiti anymore? I used to love the urban murals.
                                    A3: This is mainly down to time as it takes a lot of effort to make a large piece. It's also good to branch out into other styles to keep it fresh.
                            
                            """,
            date = datetime.date.today(),
            artist = admin_artist
        ),

        QAndA(
            q_and_a_content =   """ Q1: Would you start again with a pencil or a brush?
                                    A1: I think that a brush is the way I would go, it expands the horizons quicker than a pencil. No choice is bad one though.

                                    Q2: Who are you listening to at the moment?
                                    A2: Whilst making art I've been really loving classical music of late such as Beethoven and Bach. It seems to bring out more creativity.

                                    Q3: Do you do collabs?
                                    A3: Absolutely! Nothing like a working with an art buddy on something we're both passionate about :)
                            
                            """,
            date = datetime.date.today(),
            artist = admin_artist
                            
        ),

        QAndA(
            q_and_a_content =   """ Q1: Do you do customs?
                                    A1: For now no, but if I have the time I will open this option up again. We can negotiate a price and an output type to your enjoyment.

                                    Q2: How do you break out of an art slump?
                                    A2: Firstly, I get away from the art space and leave it for as long as it needs. I am also usually needing some hours outdoors when I get into a rut so walking is another thing I'll do.

                                    Q3: How do you respond to haters?
                                    A3: What's important to me are my users; free and paid that continue to follow my journey. I do my best to remember that when I doubt myself.
                            
                            """,
            date = datetime.date.today(),
            artist = admin_artist
        )
    ]
    db.session.add_all(q_and_as)
    db.session.commit()

    # 3 x Walkthroughs
    
    walkthroughs = [
        Walkthrough(
            description = "A video tutorial of my 'White Depression' piece. Bring your canvases!",
            date = datetime.date.today(),
            artist = admin_artist,
            artwork = artworks[2]
        ),

        Walkthrough(
            description = "A video tutorial for 'French Burgers'. After watching this, stippling will become 2nd nature",
            date = datetime.date.today(),
            artist = admin_artist,
            artwork = artworks[3]
        ),

        Walkthrough(
            description = "Here's the video for 'Triumph'! A lot going on here so take it slow :)",
            date = datetime.date.today(),
            artist = admin_artist,
            artwork = artworks[0]
        ),
    ]

    db.session.add_all(walkthroughs)
    db.session.commit()

    # 9 x comments to map
    comments = [
        Comment(
            description = "Artwork Comment 1",
            date = datetime.datetime.today(),
            user = paid_users[1]
        ),
        
        Comment(
            description = "Artwork Comment 2",
            date = datetime.datetime.today(),
            user = paid_users[0]
        ),

        Comment(
            description = "Artwork Comment 3",
            date = datetime.datetime.today(),
            user = paid_users[2]
        ),

        Comment(
            description = "Q&A Comment 1",
            date = datetime.datetime.today(),
            user = paid_users[1]
        ),

        Comment(
            description = "Q&A Comment 2",
            date = datetime.datetime.today(),
            user = paid_users[1]
        ),
        
        Comment(
            description = "Q&A Comment 3",
            date = datetime.datetime.today(),
            user = paid_users[2]
        ),

        Comment(
            description = "Walkthrough Comment 1",
            date = datetime.datetime.today(),
            user = paid_users[0]
        ),

        Comment(
            description = "Walkthrough Comment 1",
            date = datetime.datetime.today(),
            user = paid_users[0]
        ),

        Comment(
            description = "Walkthrough Comment 2",
            date = datetime.datetime.today(),
            user = paid_users[0]
        ),
    ]

    db.session.add_all(comments)
    db.session.commit()

    # 3 x Stored Questions

    stored_questions = [
        StoredQuestion(
            question = questions[4],
            q_and_a = q_and_as[0]
        ),

        StoredQuestion(
            question = questions[5],
            q_and_a  = q_and_as[1]
        ),

        StoredQuestion(
            question = questions[8],
            q_and_a = q_and_as[2]
        )
    ]
    db.session.add_all(stored_questions)
    db.session.commit()

    # 3 x Artwork Comments
    artwork_comments = [
        ArtworkComment(
            artwork = artworks[1],
            comment = comments[0]
        ),

        ArtworkComment(
            artwork = artworks[3],
            comment = comments[1]
        ),

        ArtworkComment(
            artwork = artworks[2],
            comment = comments[2]
        )
    ]
    db.session.add_all(artwork_comments)
    db.session.commit()



    # 3 x Walkthrough comments to map

    walkthrough_comments = [
        WalkthroughComment(
            walkthrough = walkthroughs[0],
            comment = comments[6]
        ),

    WalkthroughComment(
            walkthrough = walkthroughs[1],
            comment = comments[7]
        ),

    WalkthroughComment(
            walkthrough = walkthroughs[2],
            comment = comments[8]
        )
    ] 
    db.session.add_all(walkthrough_comments)
    db.session.commit()



    # 3 x Q&A comments to map
    q_and_a_comments = [
        QAndAComment(
            q_and_a = q_and_as[0],
            comment = comments[3]
        ),

        QAndAComment(
            q_and_a = q_and_as[1],
            comment = comments[4]
        ),

        QAndAComment(
            q_and_a = q_and_as[2],
            comment = comments[6]
        )
    ]

    db.session.add_all(q_and_a_comments)
    db.session.commit()

    print('Tables are seeded')

# Seed Drop Command
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print('Tables are dropped')

    