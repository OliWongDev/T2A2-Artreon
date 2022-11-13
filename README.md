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

### Community Building

Communities 

### Interactive Learning

### Patreon as an alternative

## PostgreSQL - The Database Management System of Choice

- Don't say this is the DBMS that I'm proficient in.
## SQLAlchemy - Object Relational Mapper
- SQLAlchemy

## Endpoints

### Authentication/Authorization (/auth)

#### 127.0.0.1:5000/auth/register-artist

*Register Artist*

- METHODS = POST
- INPUTS = artreon_alias(str), password(str), email(str), artist_bio(str)
- OUTPUT = artist (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be artist
- ERROR HANDLING = same email(409, Integrity Error), unauthorized(401)

#### 127.0.0.1:5000/auth/register-user

##### Register User

- METHODS = POST
- INPUTS = user_alias, first_name, last_name, email, has_subscription, password
- OUTPUT = user (201)
- AUTHENTICATION = NO
- AUTHORIZATION = NO
- ERROR HANDLING = Same email (409, Integrity Error), unauthorized (401)

#### 127.0.0.1:5000/auth/login-user

##### Login User

- METHODS = POST
- INPUTS = email, password
- OUTPUT = email, bearer token (200)
- AUTHENTICATION = NO
- AUTHORIZATION = NO
- ERROR HANDLING = Invalid log in (404)

#### 127.0.0.1:5000/auth/login-artist

##### Login Artist
- METHODS = POST
- INPUTS = email, password
- OUTPUT = email, bearer token (200)
- AUTHENTICATION = NO
- AUTHORIZATION = NO
- ERROR HANDLING = Invalid log in (404)

### Users (/users)
    
#### 127.0.0.1:5000/users

##### Get all users
- METHODS = GET
- INPUTS = n/a
- OUTPUT = All users seeded in the database and any created consequentially (200)
- AUTHENTICATION = n/a
- AUTHORIZATION = n/a
- ERROR HANDLING = n/a
#### 127.0.0.1:5000/users/<int:id>

##### Get single user
- METHODS = GET
- INPUTS = n/a
- OUTPUT = Single user seeded in the database or any created consequentially (200)
- AUTHENTICATION = n/a
- AUTHORIZATION = n/a
- ERROR HANDLING = user id not in database (404, not found)

#### 127.0.0.1:5000/users/<string:user_alias>

##### Get user by alias
- METHODS = GET
- INPUTS = n/a
- OUTPUT = Single user seeded in the database or any created consequentially (200)
- AUTHENTICATION = n/a 
- AUTHORIZATION = n/a
- ERROR HANDLING = user_alias not in database (404, not found)

##### Update user details

- METHODS = PUT/PATCH
- INPUTS = user_alias, first_name, last_name, email, has_subscription, password
- OUTPUT = New user details repeated (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = user alias not found in database (404, not found), inauthenticated (401)

##### Delete user

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful deletion message to repeat that the resource was deleted (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = user alias not found in database (404, not found), inauthenticated (401)

#### 127.0.0.1:5000/users/<string:user_alias>/comments

##### Get all user comments by alias
- METHODS = GET
- INPUTS = n/a
- OUTPUT = All comments made by a specific user (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated (401)

### Artist(s) (/artists)
    
#### 127.0.0.1:5000/

##### Get all artists
- METHODS = GET
- INPUTS = n/a
- OUTPUT = All artists on database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = Inauthenticated (401)

#### 127.0.0.1:5000/artists/<int:id>

##### Get single artist
- METHODS = GET
- INPUTS = n/a
- OUTPUT = Single artist on the database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = artist id not found in database (404, not found), inauthenticated (401)

#### 127.0.0.1:5000/artists/<string:artreon_alias>

##### Get admin artist (artreon_alias = GraphicGod) or single artist
- METHODS = GET
- INPUTS = n/a
- OUTPUT = Single artist on database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = artist alias not found in database (404), inauthenticated (401)

##### Update artist details

- METHODS = PUT/PATCH
- INPUTS = artreon_alias(string), password, email, artist_bio
- OUTPUT = Returns the new output (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = artist not same artist (401), artist not found (404), inauthenticated (401)

##### Delete artist 

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Returns deletion message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = artist not same artist (401), artist not found (404)

#### 127.0.0.1:5000/artists/<string:artreon_alias>/artworks

##### Get artworks made by artist

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All artworks made by the artist selected (200)
- AUTHENTICATION = YES
- AUTHORIZATION = NO
- ERROR HANDLING = artist not found (404), inauthenticated (401)

#### 127.0.0.1:5000/artists/<string:artreon_alias>/qandas

##### Get Q&As made by artist

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All Q&As made by the artist (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = inauthenticated or free user (401), artist not found (404)

#### 127.0.0.1:5000/artists/<string:artreon_alias>/walkthroughs

##### Get walkthroughs made by artist
- METHODS = GET
- INPUTS = n/a
- OUTPUT = All walkthroughs made by the artist (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = inauthenticated or free user (401), artist not found (404)

#### 127.0.0.1:5000/artists/<string:artreon_alias>/emails

##### Get emails sent by artist
- METHODS = GET
- INPUTS = n/a
- OUTPUT = All emails sent by the artist (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated (401), artist not found (404)

### Artworks (/artworks)

#### 127.0.0.1:5000/artworks

##### Get all artworks

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All artworks on the database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated (401)

##### Create an artwork

- METHODS = POST
- INPUTS = artwork_name(string), description(string)
- OUTPUT = Artwork created successfully message (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES must be an artist
- ERROR HANDLING = Unauthorized (401)

#### 127.0.0.1:5000/artworks/<int:id>

##### Get one artwork
- METHODS = GET
- INPUTS = n/a
- OUTPUT = Retrieves a specific artwork in the database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = Unauthorized (401), Not found (404)

##### Update an artwork

- METHODS = PUT/PATCH
- INPUTS = artwork_name(string), description(string)
- OUTPUT = New artwork output (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized (401), Not found (404)

##### Delete an artwork

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful deletion message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized (401), Not found (404)

#### 127.0.0.1:5000/artworks/<int:id>/comments

##### Create a comment on an artwork

- METHODS = POST
- INPUTS = description(string)
- OUTPUT = Repeat of the comment (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be a paid user
- ERROR HANDLING = Unauthorized (401), artwork/comment not found (404)

#### 127.0.0.1:5000/artworks/<int:id>/comments/<int:artwork_comment_id>

##### Update own comment on an artwork

- METHODS = PUT/PATCH
- INPUTS = description(string)
- OUTPUT = Repeat of comment (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized (401), artwork/comment not found (404)

##### Delete own comment

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful deletion message(200) 
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = Unauthorized (401), artwork/comment not found (404)

### Q&As (/qandas)

#### 127.0.0.1:5000/qandas

##### Get all Q&As

- METHODS = GET
- INPUTS = n/a
- OUTPUT = All Q&As returned (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized(401)

##### Post Q&A

- METHODS = POST
- INPUTS = q_and_a_content(string)
- OUTPUT = Returned Q&A (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be artist
- ERROR HANDLING = Unauthorized(401)

#### 127.0.0.1:5000/qandas/<int:id>

##### Get single Q&A
- METHODS = GET 
- INPUTS = n/a
- OUTPUT = Retrieved Q&A (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized(401), Q&A not found(404)

##### Delete Q&A

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful delete message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized(401), Q&A not found(404)

##### Update Q&A

- METHODS = PUT/PATCH
- INPUTS = q_and_a_content (string)
- OUTPUT = Returned Q&A (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized(401), Q&A not found(404)

#### 127.0.0.1:5000/qandas/<int:id>/comments

##### Create comment on Q&A
- METHODS = POST
- INPUTS = description (string)
- OUTPUT = Returned new Q&A comment (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized(401), Q&A not found(404)

#### 127.0.0.1:5000/qandas/<int:id>/comments/<int:q_and_a_comment_id>

##### Update comment on Q&A

- METHODS = PUT/PATCH
- INPUTS = description (string)
- OUTPUT = Returned updated Q&A comment (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = Unauthorized (401), Q&A/comment not found (404)

##### Delete comment on Q&A

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Returned successful delete message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = Unauthorized (401), Q&A/comment not found (404)

### Walkthroughs (/walkthroughs)

#### 127.0.0.1:5000/walkthroughs

##### Get all walkthroughs

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Retrieves all walkthroughs on the database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES
- ERROR HANDLING = Unauthorized (401)

##### Create walkthrough

- METHODS = POST
- INPUTS = description(string), artwork_id(foreign key)
- OUTPUT = Returns created walkthrough (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be artist and related to an artwork
- ERROR HANDLING = Unauthorized (401), artwork not found (404)

#### 127.0.0.1:5000/walkthroughs/<int:id>

##### Get single walkthrough

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Retrieve all walkthroughs on database (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

##### Delete walkthrough

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Successful delete message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

##### Update walkthrough

- METHODS = PUT/PATCH
- INPUTS = description(string)
- OUTPUT = Updated walkthrough (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same artist 
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

#### 127.0.0.1:5000/walkthroughs/<int:id>/comments

##### Get all walkthrough comments on a walkthrough
- METHODS = GET
- INPUTS = n/a
- OUTPUT = Retrieves all comments on a walkthrough (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

##### Create a walkthrough comment

- METHODS = POST
- INPUTS = description(string)
- OUTPUT = Returned walkthrough comment on walkthrough (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized (401), walkthrough not found (404)

#### 127.0.0.1:5000/walkthroughs/<int:id>/comments/<int:walkthrough_comment_id>

##### Update a walkthrough comment

- METHODS = PUT/PATCH
- INPUTS = description(string)
- OUTPUT = Returned updated walkthrough comment (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user
- ERROR HANDLING = Unauthorized (401), walkthrough/comment not found (404)

##### Delete a walkthrough comment

- METHODS = DELETE
- INPUTS = n/a
- OUTPUT = Returned successful delete message (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be same user
- ERROR HANDLING = Unauthorized (401), walkthrough/comment not found (404)

#### 127.0.0.1:5000/walkthroughs/check/<int:artwork_id>

##### Check artwork has a walkthrough linked to it

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Returned walkthrough if it exists, searching by artwork (200)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be paid user 
- ERROR HANDLING = No walkthrough found (404), unauthorized (401)

### Emails (/emails)

#### 127.0.0.1:5000/emails

##### Get all emails

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Returns all emails (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = inauthenticated (401)

##### Create an email

- METHODS = POST
- INPUTS = Email title (string), email content (string)
- OUTPUT = Success message for email created (201)
- AUTHENTICATION = YES
- AUTHORIZATION = YES, must be artist
- ERROR HANDLING = unauthorized (401)

#### 127.0.0.1:5000/emails/<int:id>

##### Get single email

- METHODS = GET
- INPUTS = n/a
- OUTPUT = Returns single email content to view (200)
- AUTHENTICATION = YES
- AUTHORIZATION = n/a
- ERROR HANDLING = unauthorized (401), email not found (404)

## Entity Relation Diagram



## Services

## Model Relations

## Implementation of Relations

## Software Management Process

## Minimum Viable Product Omissions

## Review