# Artreon

Welcome to Artreon! A model clone of the popular service Patreon where artists can express greater control over what content is viewable to paid and free subscribers. 

## User Guide



## Installation and Setup

## Key Components

## The Problem

For this particular problem I aimed to draw into what potential user stories for this service would look like from the three main viewpoints of the artist, the paid user and the free user. This is modelled from an AGILE framework where the user stories will dictate what the platform looks like so that the end result is something that is of actual benefit to them. 

### Free Users

"I want a service to view my favourite artist's art that they produce but I am not interested in learning how to make the art that they make"

The user story here is that the free user should be able to view the artworks and receive emails made if they have be authenticated, but they will not be able to view the walkthroughs/q&as that are associated with the artist's Artreon. By doing this, they are still a part of the in-house community to follow the artist's artistic journey. 

### Paid Users

"I want a service to view my favourite artist's art but I would also like to learn from them with walkthroughs/q&as to become a better artist myself. I would subscribe for this service."

The paid user is therefore defined as a user that is more invested in the personal learning journey side of the platform and less from a sole consumer standpoint. As such, the paid user is able to make comments, view walkthroughs/q&as and receive emails on top of the free user authorizations.

### Artist

"I want a service that allows me to handle what I allow my subscribers to view depending on their subscription. Further, I would like a service that requires authentication so that I can preserve my artwork from google searches and only for my loyal community.

The artist in this case acknowledges that with the depth of the internet, there is a need to have greater control over what is shared and publicly available for their content. It is their ultimate goal to monetise their art/knowledge and form a community of subscribers who can interact with the artist with certain privileges.

## Why do we need to solve this problem?

The problem is something that needs to be solved for a few key reasons: 

### Google Searches

As mentioned in the artist's user story, the range of access available in search engines means that it is quite easy for personal content to be taken and not credited. This is a barrier for an artist to post content on the internet, especially if their intention is for it to be preserved for certain users. 

With Artreon, the artist can post their artwork behind an authentication system so that it cannot be accessed by a public user. Further, with added tools the platform could allow the artist to properly monetise original custom pieces to people they actually want to sell to rather than attend to this service on a different platform.

### Online Community Building

Internet communities that are deeply intimate can transform a simple service into a platform of user satisfaction. We have seen many examples of social media sites that develop user access to people/ideas/content that is simply not available geographically. 

Artreon aims to develop a community of art-lovers of an individual artist into a thriving system that allows an artist to monetise their work and personally reach the people who made the decision to sign up and/or subscribe. The community is theirs, and it is not abased by what alternatives (in this case artworks) are seen on platforms such as Instagram.

### Interactive Learning

For a user who wants to not just be a consumer, but to learn skills from someone who's art you admire, Artreon is an attractive proposition. Paid users get to learn the exact methods/tools used to create awesome artwork with walkthrough videos and Q&A sessions. 

In future, added features could increase interactivity between the artist and protege such as reviews and booking 1 on 1 tutorial sessions. 

### Patreon as an alternative

The Artreon API is largely developed and inspired from Patreon (A large platform where creators and users come together to share exclusive content in exchange for a subscription). The use case for Patreon is broad, and potentially too broad for the user story. If we narrowed it down, Patreon is largely a one-way service where any type of creator releases what they would like and the subscribers remain simply consumers.

Artreon like mentioned above, identifies the need firstly to make an artist-centric platform and secondly to make sure that the space is kept intimate for buoyant communities to develop.

## Entity Relation Diagram

![Entity Relation Diagram](/docs/ERD%20Artreon%20FINAL.jpg)

## Model Relations



## Implementation of Relations


## PostgreSQL - The Database Management System of Choice

For this API, I have chosen PostgreSQL as my database management system (DBMS) for handling the queries of data that may be performed on the platform.

### Components of PostgreSQL

PostgresQL is a object-relational database that utilises structured query language (SQL) to make queries on the data that we have set up in our API. It is largely open-source would be able to scale my data to large lengths if the platform were to increase its artists and user information. It has a long history dating back since 1996, and has been proven to be an industry standard for large relational databases.

### Why for this project?

The reasons for why PostgreSQL was learned for my project are: relational database, JSON data acceptance, open-source, no license required, an industry standard and a personal desire to enhance my learning of it.

#### Relational Database

The API that I have built intends to take certain data and relate this to other data in the database. For that, our solution is a relational database that sets up rules to help preserve the integrity of our data. In a relational database, tables can be linked by foreign keys that help to set up the rules for new and seeded data being entered into our database. For example, in Artreon we cannot have an artwork being posted without an artist attached to it. Postgres makes these simple rules easy to actually implement and this is most useful for tracking bugs in our source code. 

Further, the ability to categorise our relations into simple tables initially means that we can handle complex interrelated queries depending on what the end users desire.

#### JSON Data

My API project will utilise JSON data as a return result in its skeleton format as of 14/11/22 and likely moving forward. As such, PostgreSQL handles this nicely when returning queries inside the code and from POSTMAN when requests are made. Because of this flexible data handling, PostgreSQL serves as a great tool for holding the API's data as well as its future potential to be adapted with different structured data objects.

#### Open Source

PostgreSQL is open-source meaning that it is licensed to users to use freely and change what they need to in order for their potential app to work the way they would like. Again, this proves that PostgreSQL is adaptable to future problems or solutions that arise for my API. Further, this means it is more likely to have a community behind that can help collaborate on this project or offer insight that might not be publicly available otherwise.

#### No License Required

Under PostgreSQL currently, there is no license required to use the service meaning that it is free for a beginner user such as myself to attempt to implement a RESTful API. This is unlike certain other DBMSs such as Oracle which require fees for a license. This is not a large issue for me as good software is always worth paying for, but to be able to use an industry standard DBMS with a low barrier to entry is a preferable choice before moving into different DBMSs for a more specific solution.

#### Industry Standard/Personal Interest

For my personal growth as a junior software developer, I am thrilled to have learnt how PostgreSQL handles relations and data to underpin a RESTful API. Through much diligence and occassionally frustration, I am proud to say that I feel comfortable working with PostgreSQL and working through all its idiosynchrasies.

Further, PostgreSQL is an industry standard tool for database management on relational databases. It has brought me a lot of confidence knowing that I can work with a relational database and bring that skillset to my future career.

### Drawbacks







## SQLAlchemy - Object Relational Mapper

For this API, I have opted to use SQLAlchemy as the object relational mapper for my Python-coded query elements in order to work with my PostgreSQL database management system. 

### What is an Object Relational Mapper (ORM)

Firstly, we need to understand what an ORM is!

An ORM (Object Relational Mapper) is a database abstraction layer that permits source code objects (in this case Python) to be translated into SQL queries. If we are able to access the Flask application's database queries from Python, this is likely to be simpler and safer than utilising SQL queries directly. 

On top of this, we are able to define our models and schemas inside Python that will map to our database but also can be accessed when needed. This ultimately makes our code DRYer because we are able to make fundamental changes to our database structures when needed within the source code exclusively.

### How does SQLAlchemy work?

In the SQLAlchemy documentation, the developers describe two distinct components underneath the hood. 

The first is the Core which allows the expression of SQL in an object-oriented fashion meaning that we are able to use our Python code in Artreon in order to express the queries we want. The core also grants us the use of schemas which can be taken as the blueprints of how the data will appear. This part within our Flask application is taken care of within the core engine. This component is largely responsible for the DML (Data Manipulation Language) such as INSERT/UPDATE/DELETE that would equate to posting an artist, deleting a comment or updating a user's details.

Finally, SQLAlchemy has an in-built but optional object relational mapper library that is used primarily to work with any object models that are mapped to the schema. We have primarily used this package for our smaller scale application. 
References:

- https://www.sqlalchemy.org/features.html

- https://docs.sqlalchemy.org/en/14/intro.html

### Functionality of SQLAlchemy in Artreon

SQLAlchemy is used consistently within Artreon to define the models (db.model), map the relations to other tables (db.relationships), controllers (db.select), command line functionality to populate the database (db_commands.cli.command) and instantiate sessions to commit data to the database (db.commit, db.delete, db.add).

#### Models

SQLAlchemy models allow us to use Python classes to set what our tables of data should contain in our database. For example, the User class is a SQLAlchemy model that has columns detailing the user information in various datatypes that are applicable to both Python and SQL. The interoperability makes it simple for us to query a future table. This includes a low-level way to mark what foreign tables we will map our data to with the db.ForeignKeys utility. The models are also useful in allowing simple convertable constraints to our data such as not accepting a nullable entry for a row or imposing that a unit of data must be unique.

#### Relationships

Using the db.relationships function, we are able to define on the models what relations our table will map to and how it will handle the removal of data upon this relationship. For example, an artist if deleted should have their artworks removed. We are able to simply define what a parent/child relationship is with a cascade delete inside the parent model. We are also able to describe through our code what association each relation has to each other (One to Many for example) so that the database accepts that an artist can make many artworks, but one artwork cannot be made by many artists. 

#### Controller Selection Queries (DQL)

The controllers we use are essentially calling the route/request/query that we would like to perform and executing it. Inside this controller, we need to find what the query is so that we output the desired information. Using SQLAlchemy, we can call queries that return the JSON data we want, we can see if a database item exists and we can spring off of this to deny queries that do not meet the expectations. For example, authorization in Artreon relies heavily on the SQLAlchemy query to make sure that an artist is making a DML query on their manipulatable data e.g an artist cannot update another artist's details as SQLAlchemy is checking the artist id match to confirm that it is acceptable to do.

#### Command Line Seeding

In order for someone to check the functionality of the API, we have the option to manually POST data to the database. However, it is of valuable reward for us to have the ability to seed a database with fake data. This can be done through the command line interface as part of SQLAlchemy's package. If we manually make some data that can be seeded with "flask db seed" we can begin working on testing other queries that require data to be populated, particularly DML. For example, we will know if a model's fields aren't correct with this handy feature!

#### Sessions

Finally, we can use the db sessions to ensure our data is committed to the database in the event we use Pythonic Data Manipulation Language (DML). The session represents a "holding zone" for us to manipulate the data and the new data is flushed into the database when committed. In Artreon, we use db.commit to upload new data to the database when a user updates their comment on an artwork and it takes either the changed description or holds the old description under the session.

REFERENCES:
- https://docs.sqlalchemy.org/en/14/orm/session_basics.html#what-does-the-session-do

### What are the advantages of SQLAlchemy? Why is it implemented in Artreon?

The advantages in particular that are relevant to Artreon are sanitisation, DRY code and compatibility:

#### Sanitisation/SQL Injections:

SQLAlchemy offers Artreon a simple-to-implement way of protecting against an SQL injection. An SQL injection is a common hacker technique of importing SQL language into an unintended field that can override the database's structure maliciously to where there is a risk of all data being deleted. This could have grave consequences for Artreon, particularly where an artist's entire collection of content is deleted.

By using Python objects to pass these queries, the window for this sort of attack to occur is contained within the Python code provided the API is set up correctly. 

REFERENCES:
- https://www.w3schools.com/sql/sql_injection.asp
- https://www.oreilly.com/library/view/essential-sqlalchemy-2nd/9781491916544/preface02.html

#### DRY Code:

As we have used an MVC (Model, View, Controller) model in a modularised format, the fundamental structure of our data is largely located in one place. This promotes a simple system where repetition is minimized if we have to add new fields to our models that will roll out across the program. This is assisted by SQLAlchemy's use of python objects to define the models that integrate the backbone of our program.

#### Compatibility:

SQLAlchemy provides adaptable compatability with PostgreSQL, Python language and Marshmallow to create an API that is RESTful in Artreon. In future commits, it would be very possible to migrate this logic to other backend frameworks (e.g Django), DBMSs, deserializer integrators or other languages. Further, within the ORM itself SQLAlchemy can unintentionally assist to set up other n functions such as the authentication of users/artists and the authorization of paid users/free users

REFERENCES:
- https://towardsdatascience.com/building-and-deploying-a-login-system-backend-using-flask-sqlalchemy-and-heroku-8b2aa6cc9ec3

### What are the key drawbacks to SQLAlchemy's ORM?

The key drawbacks to SQLAlchemy are that there is not much scope for complex data queries involving numerous tables however for the purposes of this relatively small Flask application these are not necessary.

There are also some concerns about efficiency in the official documentation for querying large data sets as the unit of work (synchronizing pattern in an SQLAlchemy session that stores the list of changes made to a series of objects before flushing to db) is inclusive of attributes on objects (e.g artwork.artwork_title) and for each row they must acquire a "last inserted id". This is described as a "large degree of automation" and that using the SQLAlchemy ORM is "not intended for high-bulk inserts".

REFERENCES:
- https://www.educative.io/courses/quick-start-full-stack-web-development/xoqE7wqKk93
- https://docs.sqlalchemy.org/en/14/glossary.html#term-unit-of-work
- https://docs.sqlalchemy.org/en/14/faq/performance.html#i-m-inserting-400-000-rows-with-the-orm-and-it-s-really-slow

## Endpoints

### Disclaimer (Authorization):
Unfortunately, the authorization protocol I have tried to set up was unable to be completed in time. I took an extra day over the due date to see if I could get it to work because it would've been awesome but I was unable to discern between my users and artists for authorization purposes. My goal was to originally have two groups: Users (paid user & free user) who would be able to view +  comment on certain models and Artists (admin and non-admin) where the non-admin cannot post walkthroughs/emails/q&as but can post artworks. 

Upon trying to implement these authorization functions, taking a JWT identity (my only knowledge of authorization tools thus far in my career) would prove problematic. For example, if a user has the same id value as an artist, they would be able to access artist privileges such as posting an artwork; not the goal. I also struggled to access the inner values of the data which lead to me not being able to authorize a paid user over a free user despite emulating Coder Academy API examples that worked with the same logic.

My temporary but committed solution to this problem has been to set up 4 authorization functions: authorize_user, authorize_artist, authorize_precise_user, authorize_precise_artist. The first two allow any user/artist to make the request necessary and the last two allow the precise/user artist (somewhat reliably, id user and artist matching errors can occur) to make the correct adjustment on their account/comments/artwork/walkthroughs/q&as.

As such, I have left this section with a few directions so that the user of this API can view what they need to without ill-advised error codes coming up. I have sorted the routes into 4 categories Inauthenticated, Basic Authentication , User and Artist so that the person who would like to view this project can do so in a less-frustrating manner. The descriptions of the authentication/authorization are likely to be assumed for if the project was running as intended, and are going to be left as such for now.

- Inauthenticated --> No JWT tokens required to perform request.
- Basic Authentication --> JWT token required to perform request, but can be an artist or user. 
- User --> A user's JWT token is required to perform the request. Can be specific
- Artist --> An artist's JWT token is required to perform the request. Can be specific.

### Seed Helper:

This section is to assist the person using this API with easy access to credentials after seeding the database with the fake data. To log in, please enter the email and password in raw JSON format into POSTMAN with either '127.0.0.1:5000/auth/artist-login' or '127.0.0.5000/auth/user-login'. From there, use the bearer token returned in POSTMAN to properly perform the required requests.

FREE USER:
- "user_alias": "Free2View"
- "email": "free2view@gmail.com"
- "password": "freeloader"
- As a free user, they have no seeded comments or other content.

PAID USER:
- "user_alias": "BanksyInTraining"
- "email": "lucasbanks@gmail.com"
- "password": "iknowwhoheis"
- The user id is 4, they have posted artwork comments id 1 and 4 but no Q&A comments or walkthrough comments.

ARTIST:
- "artreon_alias": "GraphicGod"
- "email": "graphicgod@artreon.com"
- "password": "artist_password"
- The artist id is 1, and they have posted 4 artworks (id 1-4), 3 emails (id 1-3), 3 walkthroughs (id 1-3) and 3 Q&As (id 1-3)

### INAUTHENTICATED

#### 127.0.0.1:5000/auth/register-user

**Register User**

- METHODS = POST
- INPUTS = user_alias, first_name, last_name, email, has_subscription, password
- OUTPUT = user (201)
- AUTHENTICATION = NO
- AUTHORIZATION = NO
- ERROR HANDLING = Same email (409, Integrity Error), unauthorized (401)

#### 127.0.0.1:5000/auth/login-user

**Login User**

- METHODS = POST
- INPUTS = email, password
- OUTPUT = email, bearer token (200)
- AUTHENTICATION = NO
- AUTHORIZATION = NO
- ERROR HANDLING = Invalid log in (404)

#### 127.0.0.1:5000/auth/login-artist

**Login Artist**

- METHODS = POST
- INPUTS = email, password
- OUTPUT = email, bearer token (200)
- AUTHENTICATION = NO
- AUTHORIZATION = NO
- ERROR HANDLING = Invalid log in (404)

### BASIC AUTHENTICATION

#### 127.0.0.1:5000/users

**Get all users**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All users seeded in the database and any created consequentially (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = n/a

#### 127.0.0.1:5000/users/<int:id>

**Get single user**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Single user seeded in the database or any created consequentially (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = user id not in database (404, not found)

#### 127.0.0.1:5000/users/<string:user_alias>

**Get user by alias**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Single user seeded in the database or any created consequentially (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = user_alias not in database (404, not found)

#### 127.0.0.1:5000/users/<string:user_alias>/comments

**Get all user comments by alias**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All comments made by a specific user (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated (401)
    
#### 127.0.0.1:5000/artists

**Get all artists**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All artists on database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = Inauthenticated (401)

#### 127.0.0.1:5000/artists/<int:id>

**Get single artist**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Single artist on the database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = artist id not found in database (404, not found), inauthenticated (401)

#### 127.0.0.1:5000/artists/<string:artreon_alias>

**Get admin artist (artreon_alias = GraphicGod) or single artist**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Single artist on database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = artist alias not found in database (404), inauthenticated (401)

#### 127.0.0.1:5000/artists/<string:artreon_alias>/artworks

**Get artworks made by artist**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All artworks made by the artist selected (200)
- AUTHENTICATION = YES
- AUTHORIZATION = NO
- ERROR HANDLING = artist not found (404), inauthenticated (401)

#### 127.0.0.1:5000/artists/<string:artreon_alias>/qandas

**Get Q&As made by artist**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All Q&As made by the artist (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated or free user (401), artist not found (404)

#### 127.0.0.1:5000/artists/<string:artreon_alias>/walkthroughs

**Get walkthroughs made by artist**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All walkthroughs made by the artist (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated or free user (401), artist not found (404)

#### 127.0.0.1:5000/artists/<string:artreon_alias>/emails

**Get emails sent by artist**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All emails sent by the artist (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated (401), artist not found (404)

#### 127.0.0.1:5000/artworks

**Get all artworks**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All artworks on the database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated (401)

#### 127.0.0.1:5000/artworks/<int:id>

**Get one artwork**
- METHODS = GET
- INPUTS = n/a
- OUTPUT = Retrieves a specific artwork in the database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = Unauthorized (401), Not found (404)

#### 127.0.0.1:5000/walkthroughs

**Get all walkthroughs**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Retrieves all walkthroughs on the database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = NO
- ERROR HANDLING = Unauthorized (401)

#### 127.0.0.1:5000/walkthroughs/<int:id>

**Get single walkthrough**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Retrieve all walkthroughs on database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

#### 127.0.0.1:5000/walkthroughs/<int:id>/comments

**Get all walkthrough comments on a walkthrough**
- METHODS = GET
- INPUTS = n/a
- OUTPUT = Retrieves all comments on a walkthrough (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

#### 127.0.0.1:5000/emails

**Get all emails**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Returns all emails (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated (401)

#### 127.0.0.1:5000/emails/<int:id>

**Get single email**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Returns single email content to view (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = unauthorized (401), email not found (404)






### USERS

#### 127.0.0.1:5000/users/<string:user_alias>

**Update user details**

- METHODS = PUT/PATCH
- INPUTS = user_alias, first_name, last_name, email, has_subscription, password
- OUTPUT = New user details repeated (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = user alias not found in database (404, not found), inauthenticated (401)

**Delete user**

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful deletion message to repeat that the resource was deleted (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = user alias not found in database (404, not found), inauthenticated (401)

#### 127.0.0.1:5000/artworks/<int:id>/comments

**Create a comment on an artwork**

- METHODS = POST
- INPUTS = description(string)
- OUTPUT = Repeat of the comment (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be a paid user
- ERROR HANDLING = Unauthorized (401), artwork/comment not found (404)

#### 127.0.0.1:5000/artworks/<int:id>/comments/<int:artwork_comment_id>

**Update own comment on an artwork**

- METHODS = PUT/PATCH
- INPUTS = description(string)
- OUTPUT = Repeat of comment (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same/paid user
- ERROR HANDLING = Unauthorized (401), artwork/comment not found (404)

**Delete own comment**

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful deletion message(200) 
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = Unauthorized (401), artwork/comment not found (404)

#### 127.0.0.1:5000/qandas

**Get all Q&As**

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All Q&As returned (200)
- AUTHENTICATION = YES
- AUTHORIZATION = Yes, must be paid user
- ERROR HANDLING = Unauthorized(401)

#### 127.0.0.1:5000/qandas/<int:id>/comments

**Create comment on Q&A**

- METHODS = POST
- INPUTS = description (string)
- OUTPUT = Returned new Q&A comment (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized(401), Q&A not found(404)

#### 127.0.0.1:5000/qandas/<int:id>/comments/<int:q_and_a_comment_id>

**Update comment on Q&A**

- METHODS = PUT/PATCH
- INPUTS = description (string)
- OUTPUT = Returned updated Q&A comment (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = Unauthorized (401), Q&A/comment not found (404)

**Delete comment on Q&A**

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Returned successful delete message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = Unauthorized (401), Q&A/comment not found (404)

#### 127.0.0.1:5000/walkthroughs/<int:id>

**Delete walkthrough**

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful delete message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

**Update walkthrough**

- METHODS = PUT/PATCH
- INPUTS = description(string)
- OUTPUT = Updated walkthrough (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist 
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

#### 127.0.0.1:5000/walkthroughs/<int:id>/comments

**Create a walkthrough comment**

- METHODS = POST
- INPUTS = description(string)
- OUTPUT = Returned walkthrough comment on walkthrough (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

#### 127.0.0.1:5000/walkthroughs/<int:id>/comments/<int:walkthrough_comment_id>

**Update a walkthrough comment**

- METHODS = PUT/PATCH
- INPUTS = description(string)
- OUTPUT = Returned updated walkthrough comment (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized (401), walkthrough/comment not found (404)

**Delete a walkthrough comment**

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Returned successful delete message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = Unauthorized (401), walkthrough/comment not found (404)





### ARTISTS

#### 127.0.0.1:5000/auth/register-artist

**Register Artist**

- METHODS = POST
- INPUTS = artreon_alias(str), password(str), email(str), artist_bio(str)
- OUTPUT = artist (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be artist
- ERROR HANDLING = same email, artreon_alias(409, Integrity Error), unauthorized(401)

#### 127.0.0.1:5000/artists/<int:id>

**Update artist details**

- METHODS = PUT/PATCH
- INPUTS = artreon_alias(string), password, email, artist_bio
- OUTPUT = Returns the new output (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = artist not same artist (401), artist not found (404), inauthenticated (401)

**Delete artist**

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Returns deletion message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = artist not same artist (401), artist not found (404)

#### 127.0.0.1:5000/artworks

**Create an artwork**

- METHODS = POST
- INPUTS = artwork_name(string), description(string)
- OUTPUT = Artwork created successfully message (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES must be an artist
- ERROR HANDLING = Unauthorized (401)

#### 127.0.0.1:5000/artworks/<int:id>

**Update an artwork**

- METHODS = PUT/PATCH
- INPUTS = artwork_name(string), description(string)
- OUTPUT = New artwork output (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized (401), Not found (404)

**Delete an artwork**

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful deletion message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized (401), Not found (404)

#### 127.0.0.1:5000/qandas

**Post Q&A**

- METHODS = POST
- INPUTS = q_and_a_content(string)
- OUTPUT = Returned Q&A (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be artist
- ERROR HANDLING = Unauthorized(401)

#### 127.0.0.1:5000/qandas/<int:id>

**Delete Q&A**

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful delete message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized(401), Q&A not found(404)

**Update Q&A**

- METHODS = PUT/PATCH
- INPUTS = q_and_a_content (string)
- OUTPUT = Returned Q&A (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized(401), Q&A not found(404)

#### 127.0.0.1:5000/walkthroughs

**Create walkthrough**

- METHODS = POST
- INPUTS = description(string), artwork_id(foreign key)
- OUTPUT = Returns created walkthrough (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be artist and related to an artwork
- ERROR HANDLING = Unauthorized (401), artwork not found (404)

#### 127.0.0.1:5000/emails

**Create an email**

- METHODS = POST
- INPUTS = Email title (string), email content (string)
- OUTPUT = Success message for email created (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be artist
- ERROR HANDLING = unauthorized (401)











## Services


## Software Management Process

## Minimum Viable Product Omissions

## Review