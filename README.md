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

# Database Model

![Database Model](/documentation/databasemodel.png "Database Model")

## Database Information

* The recipe section of the database is divided into three categories. The first category is one the user has no interaction with. The second being one the user can interact with, and the third one the user interacts with, but undergoes modification when submitted/retrieved/edited. The choice to go with the third model, with the use of {space} to seperate the steps and ingredients was one of practicality, with this essentially allowing the user a dynamic number of steps. If it was a set list, of for example 10 in the model, it would essentially restrict users to 10 or below steps, and if one was to try make this less of a problem, adding multiple areas of the database to accomidate this would become cumbersome very quickly. The {space} system to break apart steps and ingredients works on both a practical, and user level due to it allowing more freedom to add to the site without constraints.

* The account model is based on user information moreso, so it uses a MongoDB generated _id, and then a user created username and password. The password is hashed and hidden with werkzeug security features to prevent the possibility of being exposed.

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

## Werkzeug
* Security features from Werkzeug were used to ensure security for user passwords, and increase the overall security of the site.

## Google Chrome Development Tools
* Used heavily to test site responsiveness across many different screen sizes, and to inspect any possible layout irregularities with its ability to examine code line by line, and add or remove in the environment to see how it displays.

# Features

* Use of media queries to resize the screen correctly
* Search function for the user to search for a specific recipe that might interest them
* A randomizer function to add a fun element to the user and due to its uniqueness keep users returning for when they’re unsure of what they want for a meal
* Ability to create, login, and logout of an account
* Using the aforementioned account, find previously submitted recipes and edit or delete
* A set of python code that compresses the steps and instructions into a single string apiece, seperated by a set break point that is added and removed upon loading or sending a recipe. This is useful as it theoretically garuantees unlimited entries in certain fields.


# Testing User Stories

## New User

* A new user will be presented right away with a description of the site, the purpose and has access to start exploring the contents of the site immediately in the large nav bar. The layout is simple and intuitive and very clearly labeled, with a burger icon on mobile which is universally recognisable to mobile users. 

* All functions are easy to understand due to the clear, and visible icon usage on the page and descriptions present for all parts.

* The option to interact with the site with an account are very present within the bar, and with reference accross the site it means the user will know they have this option immediately


## Returning user

* The log in function is available right from when the site is accessed, and recent sites are on the front page leading to giving a returning user new content to enjoy, thus giving the best engagement to a returning user who has an idea of what the site is about without the need to navigate unnecessary menus. This creates a very streamlined and easy experience for the returning user.

* The ability to edit, delete, add and search recipes on the website is of enjoyment to a user and creates a lot of engagement due to access to previously made content, and other users content.


## Site owner

* For a site owner, having the brand of cooking utensils named on the front page was paramount. Nestling it within the description, with a rather upbeat tone creates a positive view of the company and the links to the social media site are sure to attract new users.

* A recommendation, and a competition listed on the front page means that people will be enticed by the brand of cooking tools, thus creating business and being satisfying to the site owner.

* A high quality, enjoyable site to use that will create both a positive reputation and name for it and the tools and company in question that are being promoted.

## Mobile User

* For a mobile user, the site can be navigated very smoothly and with a small collapsable navbar, which proves to be very useful for navigation, and all the sites functions remain perfecty operational and aesthetically pleasing on mobile.

* The site is completely useable for a mobile user without any concessions and all forms and uses of the desktop site are accessable on mobile.


# Testing

## HTML Validation

All the HTML was run through the w3c validator, without showing any errors unrelated to the the present jinja code (which is normal as the validators are not designed to parse code with the jinja code. Nothing related to the html within the nine pages proved to be problematic.

## CSS Validation

The CSS passed without issue, and was formatted using a formatter

![CSS Validation](/documentation/validatedcss.PNG "CSS Validation")

## Python Validation

All code was run through and linted carefully to be pep8 compliant and without error, specific attention was paid to ensure that nothing was at the incorrect indentation to prevent any code related errors


# Deployment

1. go to the terminal and install Pymongo, by typing pip3 install Flask-PyMongo

2. Add to the app.py with from flask import Flask, and from flask_PyMongo import PyMongo

3. Go to MongoDb, and log in

4. After login, go to create new cluster

5. Set up the details of the desired app, choose a cloud provider and the region closest for the servers and then create cluster

6. Click on the name of the deployed app and click collections

7. When on the collections page, go and create the desired models in the 'collections' with field and values for the data

8. Create all needed collections.

9. Go to 'Database Access' and then click on 'Add new database user'

10. Create the user, and save the information from it

11. In env.py add the relevent credentials, the SECRET_KEY, MONGO_URI, and MONGO_DBNAME. Using os.environ.setdefault on the first two and os.environ.get on the last. Configure within app.py

12. Go to heroku

13. Sign in or create a user.

14. Create an app, preferably with a similar name to that of the website and choose a region closest to you

15. Go to 'deploy' section of heroku and then connect with the gitpod repository using 'deployment method' and adding the github account name and repository name

16. Choose a branch to deploy (in this case the master) and click 'deploy branch'

17. Select for it to do automatic deploys

18. Create a procfile, and add "web: python app.py". It is very important that the procfile is not given a file type

19. Use the terminal and install and then deploy to the heroku master branch

# Further Testing

## Technical Tests

* During the design and testing process, every function and possible operation was tested multiple times (including in various orders in order to ensure that no possible operations could cause errors within the system). This was paramount as sometimes it can happen that a certain combination to break the site, necessating being thorough with this process.

* Various tests were carried out with a large variety of devices, to ensure compatability to the highest level possible. Two computers, and three mobile phones were used to test this website and throughly test its usability.

* Multiple browsers were also used during the testing process. Google Chrome, Safari, Samsung Internet and firefox were tested.

* Placement of buttons and options were examined thoroughly, to ensure they all work and do not cause any issues with navigating the files.

* Database testing was carried out enormously, specifically the send and retrieve function to ensure it works without errors. Every function was tested in every possible user scenario, and order that a function could be done and at various speeds. For example, adding and removing from the database within a very short period of time, but all worked without error and the sites user experience has no delays with the backend.

* Responsiveness was tested heavily with development tools, as to ensure that not a single screen size has any issues with displaying the site. This was paramount to ensure that nothing would be missed, as it could be if only testing on devices with specific screen sizes

## Bugs Fixed
1. There was originally a bug in which the string created by the submission form would not generate correctly and removed too little of the string leaving undesirable characters (specifically a ' } ') from the end of the {space} string that was removed. This was fixed simply by increasing the removal by 1 and then applying this to other parts of the string removal.

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


