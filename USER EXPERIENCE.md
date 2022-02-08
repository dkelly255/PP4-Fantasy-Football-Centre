# UX Planes
I have designed the site using the five planes of UX approach, each of which is reviewed in detail in the following sections
## Strategy
The strategy for the site is to offer a one-stop shop to users interested in Fantasy Football where they can obtain content in the form of Articles, and can have the ability to post their own comments on the subject matter to engage in discussion within a braoder community of Fantasy Football enthusiasts. 

The strategic aim of the site is to address the following **User Stories**:

### **As a site user I can:**
- Create and register for an account so that I can add my own comments and likes to the articles and content
- View a list of the site's articles so that I can select one to read
- View an organised list of artciles so that I can select which article I wish to view
- Open an article so that I can read the full content
- Add my own comments to articles so that I can join in the discussion on current fantasy football hot topics and issues

### **As a site administrator I can:**
- Have full CRUD (Create, Read, Update, Delete) abilities so that I can manage the content of the website
- Create draft articles so that I can complete the articles at a later time
- Approve or reject comments so that I can ensure no unacceptable comments are posted on the site

### **As both a site user and administrator I can:**

- View a count of likes on each article so that I can guage general user sentiment on the site content
- View other user's comments on articles so that I can understand other site user's perspective's an opinions on the content


## Scope

To deliver the scope of the project, an Agile approach to Software Development has been pursued for the project implementation, with the user stories above being managed via Github's Kanban board functionality.

A view of the Kanban board with the user stories having been brought through "To Do", "In Progress", and "Done" columns as follows:

![Title](readme/kanban.png)

## Structure

The website is structured using the Django Framework functionality, with a home page, a login option, and a signup page. The home page contains the main content of the site, housing the Fantasy Football Articles, together with the comments that have been posted by other users/viewers.

The core website data  will be stored in Heroku's PostgreSQL add-on, and website static files and media/images will be stored on the Cloudinary Platform. I have made the decision to store website images on Cloudinary rather than Heroku due to the fact that Heroku is an ephemeral file system, and the Dyno system it utilizes can cause problems in situations where the project has been idle or if it has not been accessed for a certain length of time. Cloudinary is a persistent file store, and will therefore minimise the likelihood of such issues occurring and interrupting or deteriorating the User Experience, ensuring site visitors have less chance of seeing broken image links when browsing the site. In terms of the Cloudinary design choice, it is also less complicated to setup than other persistent file stores (such as Amazon S3 or Microsoft Azure) so will fit well for the scope of this project.

## Code Structure

### - *Model, View, Template*

Generically the project is structured using the "Model, View, Template" software design pattern. 

- The Model supports with database management, being a data access layer which primarily handles data. 
- The Views are used toe xecute the business logic and interact with the model to carry data and render a template
- The Templates are the presentation layers, which handle the User Interface aspects of the application.

The diagram below (sourced from [javatpoint.com](https://www.javatpoint.com/django-mvt)) illustrates the MVT structure & control flow used for this project:

![MVT](readme/mvt.png)

### Requirements.txt 

The project structure includes a requirements.txt in keeping with Python Standards & best practices - as per this overview from [idkrtm.com](https://www.idkrtm.com/what-is-the-python-requirements-txt/), the requirements.txt file is used for specifiying which Python packages are required to run the overall project.

The current packages and dependencies list for the project are shown below:

![Requirements](readme/requirements.png)

### Procfile

## Database Structure

The site's content will utilise a simple database structure, consisting of two main models - one for the Fantasy Football Articles, and one for the comments that users can add to those articles

The Entity Relationship Diagram for the Articles Table is shown below, with the field names, types, and key status. 

Note the Foreign Key will be the "Author" field, and that the "Likes" field will also need to have a many to many relationship:

![Articles table ERD](readme/erd_articles.png)

The Entity Relationship Diagram for the Comments Table is shown below, with the field names, types, key status, and additional information. 

Note the Foreign Key will be the "Post" field, and that this will need to cascade on delete, so that when a post is removed, the comments on that post are also removed, that is, the deletion is cascaded through the models.

![Comments table ERD](readme/erd_comments.png)

### - PostgreSQL:
### - Cloudinary
### - Crispy Forms
### - Summernote
### - APIs & Configuration

## Skeleton

The wireframes below illustrate the skeleton of the site, including the home page, login page, signup page, together with the various nav bars and footers that underpin the site structure:

- Wireframe 1 - Home Page

![Home page](readme/wireframe-home.png)

- Wireframe 2 - Article detail & comments 

![Article page](readme/wireframe-article.png)

- Wireframe 3 - Signup Page

![Article page](readme/wireframe-signup.png)

- Wireframe 4 - Login page

![Article page](readme/wireframe-login.png)

- Wireframe 5 - Administration page

![Article page](readme/wireframe-admin.png)


## Surface

The Bootstrap framework has been used to construct the Surface of the website, with the following design choices helping to deliver the optimum user experience:

- Typography
- Imagery
- Color Palette
- Summernote - WYSIWYG editor for admin panel