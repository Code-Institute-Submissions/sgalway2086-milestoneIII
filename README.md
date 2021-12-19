# Milestone 3

# User Experience (UX)
 
## User Stories
 
### For a new user

1. An easy to learn layout, and access to recipes easily and quickly

2. Access to creating an account and easy navigation through the site

3. Strong front page that explains what the purpose of the site is
 
### As a returning user
 
1. To be able to see new additions to the site and explore the recipes. The use of an account can create a more engaging experience to a returning user, as content can be saved

2. Access to delete or edit previous recipes they have created

### For a site owner

1. Promote a brand of cooking tools

2. Attract those looking for cooking tools and possibly market to those unsure

3. Create a positive reputation based on a high quality site and experience
 
### For a mobile user

1. Similar to a new and previous user but with the need of a clean, mobile friendly layout and ability to perform all functions (reading, submitting, editing, searching etc)

2. An uncompromised user experience that always remains simple to understand, for new and returning mobile users.

# Design
 
## Fonts
* Dancing Script by Google fonts is used due to its rather elegant appearance, bringing to mind the idea of fine dining and sophistication to users, which is suitable for a recipe site
* Kaisei Tokumin is used for the main body of the website due to a clean, easily readable appearance while still invoking a lot of the sophistication and elegance of the dancing script.
## Icons
* Icons will be used to represent options to the player such as next to login/register, for social media links and for deleting items, to create an easy intuitive layout for the user.
## Colours
* A dark grey, a very light grey and off white will make up the main body of the website, trying to keep with the sophisticated look of the fonts and afford maximum readability
## Styling
* The sites styling will be done in a way as to attract a user towards being able to explore the site immediately, with content available front page with not even the need to scroll enticing users, and then being able to reach the search bar easily, enticing users immediately

# Wireframes

## Index Page

![Desktop Index Page](/documentation/wireframe1.png "Desktop Index Page")

## Index Page Mobile

![Mobile Index Page](/documentation/wireframe8.png "Mobile Index Page")

## Submit Form

![Submit Form](/documentation/wireframe2.png "Submit Form")

## Submit Form In Action

![Submit Form Used](/documentation/wireframe3.png "Submit Form Used")

## Recipe Page

![Recipe Page](/documentation/wireframe4.png "Recipe Page")

## Search Page

![Search Page](/documentation/wireframe5.png "Search Page")

## Search Page Mobile

![Search Page](/documentation/wireframe9.png "Search Page Mobile")

## Profile
![Profile](/documentation/wireframe6.png "Profile")

## Profile Mobile
![Profile Mobile](/documentation/wireframe10.png "Profile Mobile")

## Login
![Login](/documentation/wireframe7.png "Login")


# Technology Used

## Google Fonts
* Google Fonts "Dancing Script" and “Kaisei Tokumin” font were used for this project. Dancing Script made a very elegant looking font for the title and header, that creates a very sophisticated, fitting look for a recipe site and Kaisei Tokumin made a very strong text for the body due to its easy readability and strong aesthetics.

## FontAwesome
* Various FontAwesome logos were utilised to create a more clean user interface and to give representation of certain functions on the cite, for example a minus symbal on the submit recipe page to remove a step

## Gitpod
* The version control on Gitpod was used to create commits and version control the project and was used as the primary IDE for the project.

## Github
* Github was used to store all versions committed from Gitpod and to manage the Gitpod account

## Heroku
* Heroku was used to create an app and make the website live, linking to gitpod and allowing the use of automatic deployments when a commit is made from gitpod.

## MongoDB
* MongoDB was used to create a database and two collections for the site, one for recipes and the other for users. This is automatically used to store these respective elements when the user interacts with the website

## JQuery
* JQuery was used to write custom javascript files for the submission page of the site due to its flexible syntax and ability to simplify certain functions in the javascript language

## Pymongo
* Pymongo and its technologies (specifically werkzeug) were used to create the websites ability to interact with the database. It created a smooth and simple interacting between the front and backend and was essential to ensure that everything worked correctly.

## Jinja
* Jinja was used for the creation of templates within the project, and for looping through database information, making the site vastly more dynamic. The ability to vary a sites contents based on content from front or back end makes it a very powerful tool for creating a dynamic data interaction for a user

## Microsoft Paint
* Microsoft Paint was used to create various wireframes of different sizes of the site, using it as a reference for the styling and creating of the websites pages.

## Favicon.cc
* This site was used to make the favicon for the site

# Features

* Use of media queries to resize the screen correctly
* Search function for the user to search for a specific recipe that might interest them
* A randomizer function to add a fun element to the user and due to its uniqueness keep users returning for when they’re unsure of what they want for a meal
* Ability to create, login, and logout of an account
* Using the aforementioned account, find previously submitted recipes and edit or delete
* A set of python code that compresses the steps and instructions into a single string apiece, seperated by a set break point that is added and removed upon loading or sending a recipe. This is useful as it theoretically garuantees unlimited entries in certain fields.


# Testing User Stories

## New User

* A new user will be presented right away with a description of the site, the purpose and has access to start exploring the contents of the site immediately in the large nav bar.

* All functions are easy to understand due to the clear, and visible icon usage on the page and descriptions present for all parts


## Returning user

* The log in function is available right from when the site is accessed, and recent sites are on the frong page leading to giving a returning user new content to enjoy

* The ability to edit, delete, add and search websites is very fun to explore for a user and is rather enticing


## Site owner

* For a site owner, having the brand of cooking utensils named on the front page was paramount. Nestling it within the description, with a rather upbeat tone creates a positive view of the company and the links to the social media site are sure to attract new users.

## Mobile User

* For a mobile user, the site can be navigated very smoothly and with a small collapsable navbar, which proves to be very useful for navigation, and all the sites functions remain perfecty operational and aesthetically pleasing on mobile.


# Testing

## HTML Validation

All the HTML was run through the w3c validator, without showing any errors unrelated to the the present jinja code (which is normal as the validators are not designed to parse code with the jinja code. Nothing related to the html within the nine pages proved to be problematic.

## CSS Validation

The CSS passed without issue

![CSS Validation](/documentation/wireframes/validatedcss.png "CSS Validation")

## Python Validation

All code was run through and linted carefully to be pep8 compliant and without error

# Further Testing

## Technical Tests

* During the design and testing process, every function and possible operation was tested multiple times (including in various orders in order to ensure that no possible operations could cause errors within the system). This was paramount as sometimes it can happen that a certain combination to break the site, necessating being thorough with this process.

* Various tests were carried out with a large variety of devices, to ensure compatability to the highest level possible. Two computers, and three mobile phones were used to test this website and throughly test its usability.

* Multiple browsers were also used during the testing process. Google Chrome, Safari, Samsung Internet and firefox were tested.

* Placement of buttons and options were examined thoroughly, to ensure they all work and do not cause any issues with navigating the files.

* Database testing was carried out enormously, specifically the send and retrieve function to ensure it works without errors.

# Deployment

## heroku Pages

The project was deployed to github pages in this way:
1. Log into heroku
2. Click new and create an app
3. Add all details from the github repository to make its var config file complete to allow it interaction

Switch to MongoDB

1. Log into mongoDB
2. Set up the database with all collections in place
3. Create a key to place within the env.py file

Switch back to heroku

4. Add the key to heroku also with the password given
5. Set up the database
6. Connect to github
7. Select repository
8. Set to deploy automatically

## Bugs Fixed
1. There was originally a bug in which the string created by the submission form would not generate correctly and removed too little of the string leaving undesirable characters (specifically a ' } ') from the end of the {space} string that was removed. This was fixed simply by increasing the removal by 1 anad then applying this to other parts of the string removal.

2. There were a few bugs resulting from a previous submission system, such as for example when adding another step to the form, originally it would reload the page thus losing the values from some other forms. THis was solved with a rather rudimentary fix using a second form, but this was cumbersome and was eventually switched over to a much more efficient javascript function

3. The edit form could be accessed with just a link without the need to be logged in. This was resolved by adding a check to see whether the session had a user property and matching it to the recipes uploader, allowing if this was the case.

4. At first the javascript ran into some difficulties with operating, and the step and ingredient properties were not obtainable within the python code. This was resolved by using a make list function, as with multiple of the same name, using a basic get function could not work.

## Existing Bugs

1. There is currently a small bug on the mobile version with the nav bar where if the search button is clicked the anchor element highlighted on mobile devices seems to take on a rather odd shape but this does not affect performance and is purely a visual bug.

2. The submit form can sometimes miss the very last of the dynamic forms if it is still selected when submit is clicked though this was not replicable reliably in testing.

# Credits
## content
* All code written by Stephen Galway

## Acknowlegements
* My mentor Aaron for providing many valuable insights on improving the website and the various 
testers who offered advice to make the website more user friendly. Also to the staff at the tutor support who were a fantastic help throughout the project


