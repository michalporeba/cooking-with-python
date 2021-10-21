# cooking-with-python

From zero to hero in Python, step at a time. 

# Steps

## Step 01

Objective: Basic command line application in python

Create an application that stores recipes for a few (at least 3) dishes or cakes. At this stage each recipe will have a name, and a brief description. When the programme starts it should display a list of all known recipes by name after its number and ask which recipe would the user want to see the details off. Once the user povides the number the details should be displayed. 

Some extra things to consider:
* Some recipes should not have a description at all. Make sure the application still works well. 
* What is the user enters number not only the list? Or perhaps not a number at all? 
* Can you make the application ask the question multiple times? 

## Step 02 

Objective: Read recipes data from a simple text file

Extend the previous application so that the recipes data is read from a text file of some sort. Try making up a data format. 
Data is often stored in database, or 'serialised' to formats like BSON, JSON or CSV, but let's not use those just yet. A plain text file will do. 

## Step 03

Objective: Create a new recipe

At the moment, to add a new recipe we can edit the recipes files and restart the application. Most applications allows users to modify the data without the need to directly modify their data file. Let's change our cook book application so that we can new recipes at runtime. For now, without saving. 

Things to consider: 
* What will the user interface be? 
* What if we try to add a recipe for something already existing? How would we know that? 

Extra things to consider: 
* How about allowing updates too? 
* Can you update the file so we don't have to re-enter the data every time we start the application? 

## Step 04

Objective: Support multiple file types 

Let's make up another simple file format. For now, let's try to keep all the code in the same file for 'simplicity' (or rather to see how quickly things get out of hand). 

Things to consdier: 
* With multiple file formats it makes sense to expect multiple data files. How can we choose which one to open without changing the code? 

Extra things to consdier: 
* What if there is no data file? 
* If we wanted to offer the user choice of the recipes book to open, can we add a description rather than just showing the file names? 

## Step 05

Refactoring. By now the code is getting out of hand. It is time to do some refactoring