# Testing

## Manual Testing - User Workflows:
Test Case | Expected Result | Actual Result | Pass/Fail
 ------------- | ------------- | ------------ | ------------- 
  Register an account | When clicking the "Sign Up" option, a user should be presented with the sign up form. Upon population of the required fields within the form, the user should receive a confirmation email if they have specified an email address during sign-up, and should have a newly created account. | User account created as expected | Pass
  Sign in | Upon clicking the "Login" option from the navigation bar, the "Sign In" form should display to the user, prompting a username & password. Upon entering these details, a user should be logged into the site| Log in option & form functions as expected | Pass
  Open an article | When a user clicks on the title of an article, the detailed content of the article should load, together with the articles image, the excerpt, and the most recent time of editing - allowing a user to read the content of the article | Open article functionality operates as expected | Pass
  Post a comment | Clicking into the "Leave a comment" section below an article should allow a user to compose & submit a comment in relation to the article content. Upon clicking of the submit button, a notification should be displayed to the user informing them that their comment has been submitted for approval | Post Comment functionality operates as expected | Pass
  Like an article | Clicking the "like" icon under an article should increment the like count on the article by one. This functionality should only be available to users who are signed in - Users who are not signed in should be unable to add a like to an article. | Like functionality operates as expected for users - and will only permit likes from signed in users | Pass
  Unlike an article | Clicking the "like" icon under an article for a *second time* should *decrement* the like count on the article by one. This functionality should only be available to users who are signed in - Users who are not signed in should be unable to remove (or add) a like to an article. | Functionality operates as expected| Pass
  Sign out | When logged in and clicking on the "Logout" option from the navigation bar, a user should be presented with the "Sign Out" screen - asking the user for a confirmation that they do wish to sign out, and a "Sign Out" button which the user can click to formalise their Sign Our | Functionality operates as expected  | Pass
  Navigation Bar & Signin Status | The Navigation bar should have two statuses - firstly, signed in, where the menu options should consist of "Home" and "Logout"... and secondly, signed out, where the menu options should consist of "Home", "Signup", and "Login" | Fucntionality operates as expected | Pass

## Manual Testing - Administrative Workflows:
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

