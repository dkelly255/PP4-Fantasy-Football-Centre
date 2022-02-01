# Fantasy Football Centre
Fantasy Football Centre (FFC) is a Django-based web application that will allow users to browse, read, and comment on Fantasy Football Content:

![Title](readme/home.png)


# UX Planes
I have designed the site using the five planes of UX approach, each of which is reviewed in detail in the following sections
## Strategy
The strategy for the site is to offer a one-stop shop to users interested in Fantasy Football where they can obtain content in the form of Articles, and can have the ability to post their own comments on the subject matter to engage in discussion within a braoder community of Fantasy Football enthusiasts. 

The strategic aim of the site is to address the following user stories:

### As a site user I can:
- Create and register for an account so that I can add my own comments and likes to the articles and content
- View a list of the site's articles so that I can select one to read
- View an organised list of artciles so that I can select which article I wish to view
- Open an article so that I can read the full content
- Add my own comments to articles so that I can join in the discussion on current fantasy football hot topics and issues

### As a site administrator I can:
- Have full CRUD (Create, Read, Update, Delete) abilities so that I can manage the content of the website
- Create draft articles so that I can complete the articles at a later time
- Approve or reject comments so that I can ensure no unacceptable comments are posted on the site

### As both a site user and administrator I can:

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

### Model, View, Template
### Requirements.txt 
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

# Features
## Existing Features

### - Home Page

The Home page is constructed primarily using customised Bootstrap, and is where the site users will intially land upon visiting the site. The Home page is designed to enable users to seamlessly access the site's content, via a combination of the intuitively laid out navigation bar & clickable links to site articles. The page is also fully responsive, utilising bootstrap responsiveness/scaling features to ensure a positive UX on devices of all screen-sizes. A snapshot of the home page feature is shown below:

![Home page](readme/features-home.png)

### - Nav Bar
The Nav bar contains links to the main functionality sections of the site, and contains a highlight to both show the user which page they are currently on, as well as highlighting when the user scrolls over a clickable link. The Nav bar is also fully responsive from ultra-wide down to mobile device screen sizes below 300 pixels in width, and contains the site tag line "The Centre of the action" to the right hand side to help promote a positive UX for site visitors:

![Nav](readme/features-nav.png)

### - Footer
The site footer contains "Constructed By" label crediting the site to (fictional) FFC Devs, as well as clickable links to various external Social Media sites where users can connect. The links will always open in a new tab, and the footer is fully resposive using media queries from large screens down to small mobile devices. It contains a combination of blue backgrounds, with white text and borders to ensure high contrast ratios and for consistency with the site's design & color scheme.

![Footer](readme/features-footer.png)

### - Signup Form
The Sign Up form is built using Crispy Forms, and consists of a brief, but concise invitation & instruction set to the user to direct them on how to create an account with the site. There is an additional prompt on the form reminding the user that they should "Sign In" rather than "Sign Up" if they already have an account, and following that, there are four fields the user can fill in to supply the required details for creation of a new account - Username, Email, Password, and a confirmation of the password.


![Signup](readme/features-signup.png)

### - Login Form

The Login form is also built using Crispy Forms, and gives two fields for completion to authenticate the user for access to the site features such as leaving comments or liking articles. There is an additional notification to the user on the Login form that they must be logged in to like an article or leave a comment, and that if they have not yet created an account that they must Sign Up first.

![Login](readme/features-login.png)

### - Logout Form

The Lougout form screenshot is shown below, illustrating the simple & intuitive nature of this feature, whereby the user is prompted with a confirmation that they wish to log out of the site, and a button they can click to confirm they wish to do so. A defensive design principle has been used for this form, so that a user cannot log out mistakenly with a single click, the confirmation button will help provide a positive UX where the user is less likely to log out accidentally.

![Logout](readme/features-logout.png)

### - Article Display

This feature enables the user to drill down into the contents of the site by clicking on the title of any article. Upon clicking, the detailed article view will load, showing the article's main image, followed by the textual content. This feature is the heart of the site functionality, and is where site visitors can browse & digest the Fantasy Football content on a regular basis. The formatting is again put together using custom bootstrap, and the design ensures a positive UX by having an uncluttered, clear area of focus for the site visitor.

![Article](readme/features-article.png)

### - Add a comment

This additional functionality allows a user to add comments to the site articles. This adds a degree of interactivity to the site, and acts as a discussion board where users can discuss and debate current topics of interest in relation to Fantasy Football. Note, from a site security & administration perspective - a user must be signed in to leave a comment, and the comments must be individually approved by a site superuser/admin before they will be publicly visible below the articles.

![Comment](readme/features-comment.png)

### - Add a Like/Unlike

This feature allows a user who is signed in to like (or unlike) an article by clicking on the like/heart icon under each article. When a user clicks the button it will increment the like count by one, and when a user clicks the icon a second time, it will decrement the like counter by one to "unlike" the previous like. When the article has been liked, the heart icon will turn solid red, and if it is unliked, the icon will return to its hollow red outline format:

![Like](readme/features-likeunlike.png)

### - Comment Counter

The comment counter is present under all articles created on the site, and performs the role of allowing site visitors to see at a glance how many comments have been lodged under each article, giving a sense of how much discussion and debate an article may have generated. Each time a comment has been approved by the administrator/superuser, the comments counter will increment by one:

![Counter](readme/features-commentcounter.png)

### - Administration Area

The administration area is a key feature of the Fantasy Football Centre web application, and allows the site administrator/super-user to control many key site activities to keep the application in working order. The administration area has been craeted using Django's administration functionality, and contains many key functions, illlustrated in the snapshot below, and reviweed in detail in the remainder of the feature walkthrough section of this readme document:

![Admin](readme/features-admin.png)

### - Add an article

A key feature within the administration area is the ability to add articles. The articles form the majority of the site content, and this option allows a superuser or administrator to add new articles when required to keep the site current and up to date with recent events of interest to the site's target audience. As you can see from the screenshot below, there are fields allowing the Article attributes to be built out, including - title, slug, author, a hero image, an excerpt and the actual article body/content. Changing the article status from "draft" to "published" will trigger the article's publication on the live site.

![Add Article](readme/features-addarticle.png)

### - Edit an article
Additionally, the "Change Post" option will allow a Superuser or Administrator to edit the content of a pre-existing article. This is a useful feature for when Articles either contain erroneous information, or need to be augmented with additional late-breaking news relative to the Article's content. This feature can also be used to correct any typographical or grammatical errors that may have accidentally made their way into previously published articles.

![Edit Article](readme/features-editarticle.png)

### - Delete an article
The "Delete an article feature" grants a user with the correct permissions the ability to remove previously published articles from the site's content. This feature ensures that the site content can be maintained & kept current, and would allow reacting to any unexpected or accidental misinformation or errors that may require an article to be deleted from the site. The superuser/admin must check the box to the left of the article they wish to delete, and then select the delete option from the drop-down menu & confirm.

![Delete Article](readme/features-deletearticle.png)

### - Approve a comment
The application also contains features which help with the management of the comments posted on articles in the site. Before any comment can be publicly displayed, it must be approved by an administrator, to minimize the risk of offensive or illegal comments being posted. When an administrator or superuser wants to approve a comment, he or she can simply select the comment from the menu, check the appropriate selection box, and then select "approve comments" from the dropdown menu:

![Approve Comment](readme/features-approvecomment.png)

### - Delete a comment
![Delete Comment](readme/features-deletecomment.png)

## Future Features 
In addition to the existing features there are several additional features which can be added to augment the application in future and are yet to be implemented:

### - Notifications

A future feature for site implementation would be the addition of a notifications choice for users. This would allow users who wish to avail of the option to receice notifications when a new article is posted to the site, and/or when their comments have had replies in the discussion areas. This feature is currently out of scope due to project deadlines, but will hopefully be added at a future time to improve the User Experience and broaden the suite of features offered by the site.

### -  Membership Tiers Addition

This would involve adding functionality to the site whereby existing users have the choice to upgrade their account to a "Premium Member" - which would in turn give them access to additional premium features not accessible to a default user. 

### - Premium articles & Analysis

Following on from the Member's area would be additional members-only articles, and access to player data & analysis to help premium members gain an edge with their fantasy football management. This would require changes to existing models, and the addition of new models and in the interest of project deadlines is currently out of scope for the current release.

### - Forgotten Password Functionality

This would give users the ability to reset their password should they wish to do so in the event of forgetting their existing login credentials, thereby improving the User Experience and adding a further dimension to the functionality of the site

### - Social Media Sign-ins

The addition of the ability to sign-in via a user's existing social media account/s (Google, Facebook, Instagram etc) would add further functionality to the site and broaden the User Experience, however in the interests of project timelines this set of features is currently out of project scope for the current release.

# Testing

## User Workflow Testing:
Test Case | Expected Result | Actual Result | Pass/Fail
 ------------- | ------------- | ------------ | ------------- 
  Register an account | Expected result | To be tested | TBD
  Sign in | Expected result | To be tested | TBD
  Open an article | Expected result | To be tested | TBD
  Post a comment | Expected result | To be tested | TBD
  Like an article | Expected result | To be tested | TBD
  Unlike an article | Expected result | To be tested | TBD
  Close an article | Expected result | To be tested | TBD
  Sign out | Expected result | To be tested | TBD

## Admin Workflow Testing:
Test Case | Expected Result | Actual Result | Pass/Fail
 ------------- | ------------- | ------------ | ------------- 
  Create an article | Expected result | To be tested | TBD
  Delete an article | Expected result | To be tested | TBD
  Approve a comment | Expected result | To be tested | TBD
  Reject a comment | Expected result | To be tested | TBD
  Add an email address | Expected result | To be tested | TBD
  Verify an email address | Expected result | To be tested | TBD
  Add a user | Expected result | To be tested | TBD
  Delete a user | Expected result | To be tested | TBD
  Change a password | Expected result | To be tested | TBD
 

# Bugs

## Resolved Bugs

### Connection Refused - Error code 111

This bug was initially present when trying to sign-up a new user for an account after providing the user's email & password details. 

![Error Snapshot](readme/bug1.png)

The error is caused when an email Backend is missing from the Settings.py file, and has been solved by adding the email backend and the default "from" email using the following code:

- `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`
- `DEFAULT_FROM_EMAIL = 'your choice of email'`

In keeping with the Agile methodology I am using to manage this project, the issue has now been moved to "closed" in Github's issues tracker:

![Error resolution](readme/bug1_closed.png)

## Unresolved Bugs

An additional bug is currently present where the CSS styles are not being properly applied in the live deployed (Heroku) site. 

![Bug2](readme/bug2-deployedcssstyles.png)

The styles are correct in the Development Environment (Gitpod) site:

![Bug2](readme/bug2-deployedcssstylesgit.png)

This bug is currently under investigation for resolution


# Technologies Used

## - Cloudinary
## - Crispy Forms
## - Summernote
## - APIs & Configuration

# Deployment
The application was deployed via Heroku, and a link to the live deployment can be found by clicking [here](https://fantasyfootballcentre.herokuapp.com/)

An extended list of detailed steps & instructions for deployment is covered in the section below:

## Github Deployment
Note - please ensure you have created a GitHub repository prior to proceeding to the "Heroku" deployment section below to ensure no rework or deployment issues

## Heroku Deployment
The Steps for deployment to Heroku are as follows - Please note these steps are correct and current as at the time of application release (March 2022) but may be subject to change in future:

- Navigate to [Heroku](https://id.heroku.com/login) and create an account

![Heroku Account Creation](readme/heroku-intro.png)

- From the Heroku dashboard select the “Create new app” button.

![New App creation](readme/heroku-newapp.png)

- Choose a name for the application - I have chosen Fantasy Football Centre but please note that the name must be unique.

![App name selection](readme/heroku-name.png)

- Select your region 

![Region confirmation](readme/heroku-region.png)

- Then click “Create app” - this will trigger a page with all the information for setting up the app.

![App creation confirmation](readme/heroku-create.png)

Settings Tab:

- Config Vars - It is important to get your settings section done before you deploy  your code, the first section being the "config vars" - also known as "environment variables", are where sensitive data that needs to be kept private is stored. In the case of this website & app the  required "CLOUDINARY_URL", "DATABASE_URL", and "SECRET_KEY" config vars are shown below:

![Settings Tab](readme/heroku-configvars.png)

- Buildpacks - The next step is to add buildpacks - These install further dependencies that we need. Click “Add buildpack”, add the Python buildpack first and then click “Save changes”. 

![Buildpacks](readme/heroku-buildpacks.png)

Deployment Tab: 

- Select Github here, and then we  can confirm that we want to connect to Github & search for the equivalent Github repository name, followed by “Search”. 

![Github Deployment](readme/heroku-deploy.png)

- Next, click “connect” to link up the Heroku app to our Github repository code, and scroll down to see two options - for manual or automatic deployment
- If you choose to enable automatic deployment then Heroku will rebuild the app every time you push a new change to your code in Github. 
- Alternatively you can choose to  manually deploy using the "deploy branch" option
- Finally, you will see the “App was successfully deployed” message  
and a button for the deployed link. 

## Local Deployment
Additionally - if you would like to make a local copy of the Github repository, you can clone it by typing the following command in your IDE terminal:

- `git clone https://github.com/dkelly255/fantasy-football-centre.git`

Alternatively, if you use Gitpod, you can click the button below to generate a new workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/dkelly255/fantasy-football-centre)

# Credits
## Content
## Code
## Media



