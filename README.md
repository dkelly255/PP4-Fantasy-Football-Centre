Entity Relationship Diagrams:

Articles:
Fields: Key, Name, Type
Title (Unique) - Char[200]
(1TM - Foreign Key) Author - Take from User Model
Creation Date - DateTime
Updated Date - DateTime
Content - TextField
Featured Image - Cloudinary Image
Excerpt - TextField
(MTM) Likes - User Model
Slug (unique) - SlugField
Status - Integer

Comments:
Key, Name, Type, Extra Info
Foreign Key - post, Post Model, Cascade on delete
name, CharField, Max length 80
email, EmailField
body, TextField
created_on, DateTimeField, auto_now_add True
approved, BooleanField, default False