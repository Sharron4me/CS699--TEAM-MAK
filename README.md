Mess Food Review Web App
========================
 
##Problem Statement or Motivation:##
The idea is to create a Mess Food Review application to provide
mess food review, for the betterment of food quality.
The motivation behind this topic is to create a common portal, so
that communication can be established between Mess sta and
hostel students.
Good food quality is a prerequisite to healthy life style and better
learning, Hence this portal is a to providing a say to the students
in what they are being served.


##Sell your product/service :##
This web app makes hostel mess administration easy and effective.

##List of features##
* rate, upvote, downvote a dish
* provide reviews with images
* register complaint
* start campaign to add a particular dish,etc

##Technology Stack##
*Python
* Django Framework
* Jquery Framework
* JavaScript
* Ajax
* Bootstrap
* HTML
* CSS

##List of deliverables## 
- [x]Provide a way to choose to review anonymously
- [x] Functionality for management to enter food wastage
- [x] Generate food waste report

##Hardware/Software Requirements##
*Python latest
*Django latest


##How to operate##
*In \mess_review\mess_review\settings.py Add Host Email Id and password
*In \mess_review\ execute command: python .\manage.py runserver
*The terminal output gives the url to home page

####Admin####
open url\adminlog\
Enter AdminId Password to login
Click on Add Dish to add new dishes
Click on View Dish to view\edit\delete dishes
Click on All Complaints to view all Complaints
Click on All Campaigns to view\accept\reject Campaigns 
Click on Home to verify new users

####User####
open url To register click on Register
Enter Name LDAP id and password and click on register
Once Registered verification link is sent on LDAP email , click on link to verify.
User can only login only when Admin verify new registered user
open url To login as user
Click on Home to view all dishes and click on dishes card to view\add reviews of the dish
Click on My Complaints to view user raised Complaints
Click on New Complaints to raise New Complaint
Click on Campaigns to view\upvote\downvote Campaigns 
Click on New Campaign to start new Campaign

##Primary stakeholders of the product/service built##
Kiran C Ranebennur
Mohammad Ummair
Aastik 

##Team details along with the contribution##
21q050017 :Kiran C Ranebennur
Front end
Django Setup
Student registration using LDAP, send email to LDAP@iitb.ac.in for confirmation
Admin dashboard to load all students and provide action to verify students 
Student login 
Documentation using Sphinx

213050004 :Mohammad Ummair
Table for admin to view all available dishes
Add ,delete, Edit dish feature for admin
Add daily food wastage 
Generate wastage report for given interval of time
Show all dish to students on home page
Show a detailed page of dish

213050012 :Aastik
Add campaign feature for students, upvote/downvote other campaigns
Admin dashboard to accept reject campaigns
Add and view review for dishes for students(reviews can be anonymous)
Raise complaint for students and admin dashboard to view them
Admin and student navbar integration


##Path to Code Documentation (index.html)##
\mess_review\docs\_build\html\New folder\docs\_build\html\index.html



