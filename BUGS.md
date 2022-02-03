# Bugs

## Resolved Bugs

### 1. Connection Refused - Error code 111

This bug was initially present when trying to sign-up a new user for an account after providing the user's email & password details. 

![Error Snapshot](readme/bug1.png)

The error is caused when an email Backend is missing from the Settings.py file, and has been solved by adding the email backend and the default "from" email using the following code:

- `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`
- `DEFAULT_FROM_EMAIL = 'your choice of email'`

In keeping with the Agile methodology I am using to manage this project, the issue has now been moved to "closed" in Github's issues tracker:

![Error resolution](readme/bug1_closed.png)

## Unresolved Bugs

### 2. CSS Styles

An additional bug is currently present where the CSS styles are not being properly applied in the live deployed (Heroku) site. 

![Bug2](readme/bug2-deployedcssstyles.png)

The styles are correct in the Development Environment (Gitpod) site:

![Bug2](readme/bug2-deployedcssstylesgit.png)

This bug is currently under investigation for resolution

### 3. Account created email notification

Upon creation of a new account, a user will receive a notification that a confirmation email has been sent to the email they used during signup. However, currently the email is not sent or received. 

![Bug3](readme/bug3-emailnotification.png)

This bug is also currently under investigation for resolution