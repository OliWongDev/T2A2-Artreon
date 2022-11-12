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
#### Register Artist

    #### Register User

    #### Login User

    #### Login Artist

    ### Users (/users)

    #### Get all users

    #### Get single user

    #### Get user by alias

    #### Update user details

    #### Delete user

    #### Get all user comments by alias

### Artist(s) (/artists)

    #### Get all artists

    #### Get single artist

    #### Get admin artist (main creator)

    #### Update artist details

    #### Delete artist 

    #### Get artworks made by artist

    #### Get Q&As made by artist

    #### Get walkthroughs made by artist

    #### Get emails sent by artist

### Artworks (/artworks)

    #### Get all artworks

    #### Post an artwork

    #### Get one artwork

    #### Update an artwork

    #### Delete an artwork

    #### Post a comment on an artwork

    #### Update own comment on an artwork

    #### Delete own comment

### Q&As (/qandas)

    #### Get all Q&As

    #### Post Q&A

    #### Get single Q&A

    #### Delete Q&A

    #### Update Q&A

    #### Post comment on Q&A

    #### Update comment on Q&A

    #### Delete comment on Q&A

### Walkthroughs (/walkthroughs)

    #### Get all walkthroughs

    #### Add walkthrough

    #### Get single walkthrough

    #### Delete walkthrough

    #### Update walkthrough

    #### Get all walkthrough comments on a walkthrough

    #### Add a walkthrough comment

    #### Update a walkthrough comment

    #### Delete a walkthrough comment

    #### Check artwork has a walkthrough linked to it.

### Emails (/emails)

    #### Get all emails

    #### Create an email

    #### Get single email

## Entity Relation Diagram

## Services

## Model Relations

## Implementation of Relations

## Software Management Process

## Review