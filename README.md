# Final Project-COP3035
## Basic emailer with a gui to enter CSV of email list and a text file with the message to be sent. 
This project is using **Selenium** and **PyQt5**

*    To install Selenium make sure that you have all the files [needed](https://selenium-python.readthedocs.io/installation.html). From there run *pip install selenium*, extract the geckodriver (this project is based on using Firefox so Firefox is needed already as well as geckodriver specifically), add the geckodriver to the computers PATH.
*    To install PyQt5 run *python3 -m venv venv*. On **Windows** use *call venv/scripts/activate.bat*, on **Mac or Linux** use *source venv/bin/activate*. Lsatly run *pip install PyQt5==5.9.2*

## Basic Project Information
Our project is made to be used by professionals in the working world as a tool for solicitation. Although this method is widely hated of getting personalized spam emails, it is still a used and common method. We have created a simple GUI using PyQt5 to collect user input for the name that is wanted on the email, the email address, subject of the email, and message body. The message body and subject are the same through each run but the email and name can be manually input or read through a CSV loaded with the names and emails. The program will then run through the message body and look for a specific patter (---), when this pattern is encountered it is replaced with the name to be in the email. We then used Selenium to load gmail webpage and have Selenium to log in with the account username and password then create all the emails and send them out in a loop.

## Division of Work
Isaac - Worked on the web automation side, used Selenium to pull the website, login, and create and send the emails.
Jason - Responsible for creating the front end design using PyQt5 and collecting each value and assigning these to resonable variables that will be passed to the CSV function Nick wrote.
Nick - Responsible for creating the function that will read the CSV file and collect all the appropriate values and assign to the correct functions to be passed to the web automation function.

## Explanation of Project Components
Consisted of the main file being the PyQt5 creation file that then called the CSV parser after passing that function the CSV file name. The CSV parser then extracts the data of the CSV and other data and sets it to appropriate data types as well as slight validation. The parser then calls the final piece of the web automation to login to gmail and create each message through Selenium.

## Challenges Faced
Communication for three seperate files was the hardest part trying to make sure everyone was on the same page for how the project was to be completed and how it would work when all combined.
Some of the libraries gave issues on certain computers for installations since we were using 2 Windows computers and one Linux computer, some steps had to be altered.
