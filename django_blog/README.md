# Authentication System Documentation
## 1. Overview
The authentication system allows users to:Register a new account with a username and email
Login with their credentials
Logout securely
View their profile once logged in
We use Django’s built-in authentication views for login and logout, and a custom registration form extending UserCreationForm to include an email field.

## 2. Components
### 2.1 Registration
Form: CustomUserCreationForm in accounts/forms.py
Extends Django’s UserCreationForm
Fields: username, email, password1, password2
View: register in accounts/views.py
Handles POST requests to create new users
Redirects to login page after successful registration
Template: accounts/templates/accounts/register.html
Renders the registration form using {{ form.as_p }}
Interaction:User navigates to /accounts/register/
Fills in username, email, and password
Submits the form
If valid, user is created and redirected to login
### 2.2 Login
View: LoginView from Django (django.contrib.auth.views.LoginView)
URL: /accounts/login/ (included via django.contrib.auth.urls)
Template: templates/registration/login.html
Renders login form with username and password fields
Interaction:
User navigates to /accounts/login/
Enters username and password
Submits the form
If credentials are correct, the user is logged in and can access protected pages
### 2.3 Logout
View: LogoutView from Django (django.contrib.auth.views.LogoutView)
URL: /accounts/logout/ (included via django.contrib.auth.urls)
Template: templates/registration/logged_out.html
Interaction:
User clicks the “Logout” link
Django ends the session and displays a logged-out page
### 2.4 Profile Display
View: profile in accounts/views.py
Decorated with @login_required to ensure only logged-in users can access it
Template: accounts/templates/accounts/profile.html
Displays username and email
Interaction:
User navigates to /accounts/profile/ after login
Sees their username and email displayed
## 3. How to Test Each Feature
Feature	Steps to Test
#### Registration	
1. Go to /accounts/register/
2. Enter a new username, email, password, confirm password
3. Submit form
4. Verify you are redirected to /accounts/login/ and user exists in the database
#### Login	
1. Go to /accounts/login/
2. Enter valid username and password
3. Submit form
4. Verify you are logged in and can access /accounts/profile/
#### Logout	
1. While logged in, go to /accounts/logout/
2. Verify the session ends and logged-out page is shown
3. Try accessing /accounts/profile/ to confirm login is required
#### Profile	
1. Log in
2. Go to /accounts/profile/
3. Verify your username and email are displayed correctly
4. Notes

All templates use CSRF protection ({% csrf_token %}) for security
Only authenticated users can access the profile page
Login and logout use Django’s built-in session management
Registration uses a custom form to allow collecting additional user data (email)


# BUILDING Phase 1
A full-featured blog application built with Django, implementing complete CRUD operations with user authentication and a responsive frontend.

## Features

### Authentication System
- User Registration: with automatic login
- Secure Login/Logout: with session management
- User Profiles: displaying post statistics
- Protected Views: only authenticated users can create/edit/delete posts

### Blog CRUD Operations
- Create: Authenticated users can write new blog posts
- Read: Public viewing of all posts, detailed post pages
- Update: Post authors can edit their own posts
- Delete: Post authors can delete their own posts with confirmation

### Frontend Features
- Responsive Design: with clean, modern interface
- Dynamic Navigation: changes based on authentication state
- Form Validation: with user-friendly error messages
- Pagination: for blog post listings
- Character Counters: for post creation

##  Project Structure
django_blog/
├── blog/ 
│ ├── migrations/ 
│ ├── templates/blog/ 
│ │ ├── base.html
│ │ ├── post_list.html 
│ │ ├── post_detail.html 
│ │ ├── post_form.html 
│ │ ├── post_confirm_delete.html 
│ │ ├── login.html 
│ │ ├── register.html 
│ │ └── profile.html
│ ├── init.py
│ ├── admin.py 
│ ├── apps.py
│ ├── forms.py 
│ ├── models.py 
│ ├── tests.py
│ ├── urls.py 
│ └── views.py 
├── static/ 
│ ├── css/
│ │ └── styles.css 
│ └── js/
│ └── scripts.js 
├── templates/
│ └── registration/ 
├── manage.py
└── requirements.txt 