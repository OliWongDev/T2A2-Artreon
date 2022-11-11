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
from models.users import User
from models.walkthrough_comments import WalkthroughComment
from models.walkthroughs import Walkthrough
from flask_seeder import Seeder

import datetime

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables are created")


@db_commands.cli.command("seed")
def seed_db():
    
    # 1 x Artist
    
    admin_artist_seed_local = Artist(
        artreon_alias = "Graphic God",
        password = bcrypt.generate_password_hash("artist_password").decode("utf-8"),
        email = "graphicgod@artreon.com",
        is_admin = True,
        artist_bio = "Hi there! I'm Graphic God and welcome to my Artreon where you can see my wonderful artworks. If you want to learn how I do it all become a paid user and join the art revolution!",
    )

    db.session.add(admin_artist_seed_local)
    db.session.commit()
    print("(1) Admin/Main Artist seeded!")

    # 1 x Non-Admin Artist
    non_admin_artist_local = Artist(
        artreon_alias = "Collaber",
        password = bcrypt.generate_password_hash("collab").decode("utf-8"),
        email = "collaber@gmail.com",
        is_admin = False,
        artist_bio = "I just post art every now and then.",
    )

    db.session.add(non_admin_artist_local)
    db.session.commit()
    print("(2) Non-Admin Artist seeded!")

    # 2 x Free User
    free_users_seed_local = [
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

    db.session.add_all(free_users_seed_local)
    db.session.commit()
    print("(3) 2 x free users seeded!")

    # 3 x Paid User

    paid_users_seed_local = [
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
    db.session.add_all(paid_users_seed_local)
    db.session.commit()
    print("(4) 3 x Paid Users seeded")

    # 4 x Emails

    emails_seed_local = [
        Email(
            email_title = "Big things coming soon!",
            email_content =     """ Just wanted to get a quick message out to the users of my Artreon that big things are coming soon and I've got a whole slew of collabed pieces almost ready to present for you all.
                                    Exciting times.

                                    Graphic God
                                """,
            send_date = datetime.date.today(),
            artist = admin_artist_seed_local
        ),

        Email(
            email_title = "Free Membership Offer",
            email_content =     """ It's December and therefore the holiday season so I'm offering my free users a one month premium trial throughout the month. 
                                    Enjoy your end of year celebrations wherever you may be.

                                    Graphic God
                                """,
            send_date = datetime.date.today(),
            artist = admin_artist_seed_local
        ),

        Email(
            email_title = "Check out my interview with the Artreon podcast!",
            email_content =     """ Howdy!
                                    I did an interview with the kind folks from Artreon about my experience on the platform, you can check it out here!
                                    *LINK*


                                    Graphic God
                                """,
            send_date = datetime.date.today(),
            artist = admin_artist_seed_local
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
            artist = admin_artist_seed_local
        )
    ]
    db.session.add_all(emails_seed_local)
    db.session.commit()
    print("(5) 4 x Emails seeded!")
    

    # 4 x Artworks

    artworks_seed_local = [
        Artwork(
            artwork_name = "Triumph",
            description = "A grizzly feline racecar driver wins their final race. Tile mosaic.",
            date = datetime.date.today(),
            artist = admin_artist_seed_local,
        ),

        Artwork(
            artwork_name = "The First Spray",
            description = "A young graffiti artist makes their first tag underneath a moving train. Drawn with fine line.",
            date = datetime.date.today(),
            artist = admin_artist_seed_local,
        ),

        Artwork(
            artwork_name = "White Depression",
            description = "A subtle look at a depressed mind. Painted with oil.",
            date = datetime.date.today(),
            artist = admin_artist_seed_local,
        ),

        Artwork(
            artwork_name = "French Burgers",
            description = "A subtle look at a depressed mind. Painted with oil.",
            date = datetime.date.today(),
            artist = admin_artist_seed_local,
        ),
    ]
    db.session.add_all(artworks_seed_local)
    db.session.commit()
    print("(6) x Artworks seeded!")

    # 3 x Q&As
    q_and_as_seed_local = [
        QAndA(
            q_and_a_content =   """ Q1: What is your favourite piece?
                                    A1: I really enjoyed working on the White Depression piece, I think it explains deeply what the gift of art has done for me :)

                                    Q2: What is one thing you can't leave the house without?
                                    A2: I refuse to leave my bedroom let alone my house without my pencil, you never know when a good idea might hit.

                                    Q3: Why aren't you doing graffiti anymore? I used to love the urban murals.
                                    A3: This is mainly down to time as it takes a lot of effort to make a large piece. It's also good to branch out into other styles to keep it fresh.
                            
                            """,
            date = datetime.date.today(),
            artist = admin_artist_seed_local,
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
            artist = admin_artist_seed_local,
                            
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
            artist = admin_artist_seed_local,
            
        )
    ]
    db.session.add_all(q_and_as_seed_local)
    db.session.commit()
    print("(7) 3 x Q&As seeded!")

    # 3 x Walkthroughs
    
    walkthroughs_seed_local = [
        Walkthrough(
            description = "A video tutorial of my 'White Depression' piece. Bring your canvases!",
            date = datetime.date.today(),
            artist = admin_artist_seed_local,
            artwork = artworks_seed_local[2],
        ),

        Walkthrough(
            description = "A video tutorial for 'French Burgers'. After watching this, stippling will become 2nd nature",
            date = datetime.date.today(),
            artist = admin_artist_seed_local,
            artwork = artworks_seed_local[3],
        ),

        Walkthrough(
            description = "Here's the video for 'Triumph'! A lot going on here so take it slow :)",
            date = datetime.date.today(),
            artist = admin_artist_seed_local,
            artwork = artworks_seed_local[0],
        ),
    ]

    db.session.add_all(walkthroughs_seed_local)
    db.session.commit()
    print("(8) 3 x Walkthroughs seeded!")

    # 3 x Artwork Comments
    artwork_comments_seed_local_1 = ArtworkComment(
            artwork = artworks_seed_local[1]
        )
    
    artwork_comments_seed_local_2 = ArtworkComment(
            artwork = artworks_seed_local[1]
    )

    artwork_comments_seed_local_3 = ArtworkComment(
            artwork = artworks_seed_local[2]
        )

    artwork_comments_seed_local_4 = ArtworkComment(
            artwork = artworks_seed_local[3]
    )

    db.session.add(artwork_comments_seed_local_1)
    db.session.add(artwork_comments_seed_local_2)
    db.session.add(artwork_comments_seed_local_3)
    db.session.add(artwork_comments_seed_local_4)
    db.session.commit()
    print("(9) 3 x Artwork Comments seeded")

    # 3 x Walkthrough comments to map

    walkthrough_comments_seed_local_1 = WalkthroughComment(
            walkthrough = walkthroughs_seed_local[0]
        )

    walkthrough_comments_seed_local_2 = WalkthroughComment(
            walkthrough = walkthroughs_seed_local[1]
        )

    walkthrough_comments_seed_local_3 = WalkthroughComment(
            walkthrough = walkthroughs_seed_local[2]
        )

    db.session.add(walkthrough_comments_seed_local_1)
    db.session.add(walkthrough_comments_seed_local_2)
    db.session.add(walkthrough_comments_seed_local_3)
    db.session.commit()
    print("(10) 3 x Walkthrough Comments seeded!")


    # 3 x Q&A comments to map

    q_and_a_comments_seed_local_1 = QAndAComment(
            q_and_a = q_and_as_seed_local[0]
        )

    q_and_a_comments_seed_local_2 = QAndAComment(
            q_and_a = q_and_as_seed_local[1]
        )

    q_and_a_comments_seed_local_3 = QAndAComment(
            q_and_a = q_and_as_seed_local[2]
        )
    
    db.session.add(q_and_a_comments_seed_local_1)
    db.session.add(q_and_a_comments_seed_local_2)
    db.session.add(q_and_a_comments_seed_local_3)
    db.session.commit()
    print("(11) 3 x Q&A Comments seeded")

    # 10 x comments to map
    comments_seed_local = [
        Comment(
            description = "Artwork Comment 1",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[1],
            artwork_comment = artwork_comments_seed_local_1
        ),
        
        Comment(
            description = "Artwork Comment 2",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[0],
            artwork_comment = artwork_comments_seed_local_2
        ),

        Comment(
            description = "Artwork Comment 3",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[2],
            artwork_comment = artwork_comments_seed_local_3
        ),

        Comment(
            description = "Artwork Comment 4",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[1],
            artwork_comment = artwork_comments_seed_local_4
        ),

        Comment(
            description = "Q&A Comment 1",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[1],
            q_and_a_comment = q_and_a_comments_seed_local_1
        ),
        
        Comment(
            description = "Q&A Comment 2",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[2],
            q_and_a_comment = q_and_a_comments_seed_local_2
        ),

        Comment(
            description = "Q&A Comment 3",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[0],
            q_and_a_comment = q_and_a_comments_seed_local_3
        ),

        Comment(
            description = "Walkthrough Comment 1",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[0],
            walkthrough_comment = walkthrough_comments_seed_local_1
        ),

        Comment(
            description = "Walkthrough Comment 2",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[0],
            walkthrough_comment = walkthrough_comments_seed_local_2
        ),

        Comment(
            description = "Walkthrough Comment 3",
            date = datetime.datetime.today(),
            user = paid_users_seed_local[2],
            walkthrough_comment = walkthrough_comments_seed_local_3
        )
    ]

    db.session.add_all(comments_seed_local)
    db.session.commit()
    print("(12) 10 x Comments were seeded")

# Seed Drop Command
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print('Tables are dropped')

    