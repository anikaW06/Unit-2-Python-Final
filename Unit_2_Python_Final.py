#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:30:02 2020

@author: anikaweling
"""

import tweepy
import os
import time


Example_question = 0
EQ1_USA = 0
EQ2_Canada = 0
EQ3_Mexico = 0

q1 = 0
q1_Delhi=0
q1_London=0
q1_LA = 0

q2 = 0
q2_Earthquake=0
q2_Hurricane=0
q2_Flood=0

q3 = 0
q3_Monolith=0
q3_Hornets=0
q3_Locusts=0

q4 = 0
q4_Warren=0
q4_Bloomberg=0
q4_Cruz=0

points = 0

class Right:
  def Correct():
   print("CORRECT!")
   print("points =", points + 1)
   time.sleep(2)

class Wrong:
  def Incorrect():
    print("Sorry that is incorrect")
    print("points =", points)
    time.sleep(2)

#Please fill in the following with your information
consumer_key='' 
consumer_secret=''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

os.system('clear')
name = str(input("Write Your Name: "))

print("Welcome, " + name,", to  According to Twitter")
print("This new trivia game will ask you questions based on demographics") 
print("from Twitter - With each question, this code will scan Twitter ")
print("and tally the usage of specific hashtags through 2020")
print("Answer the multiple choice questions by typing the options number")
print("There are 4 questions, try and score as high as you can")
print("Keep in mind this code is scanning all of Twitter, give it a second to work")
print("Click enter if you are ready")
start = (input(""))
os.system('clear')


#Example Question option 1
for tweet in tweepy.Cursor(api.search,q="#TravelUSA",count=100,
                           lang="en",
                           since="2020-01-01").items():
    EQ1_USA += 1
print("One second just scanning Twitter")     

#Example Question option 2
for tweet in tweepy.Cursor(api.search,q="#TravelCanada",count=100,
                           lang="en",
                           since="2020-01-01").items():
    EQ2_Canada += 1
print("Almost there")

 #Example Question option 3
for tweet in tweepy.Cursor(api.search,q="#TravelMexico",count=100,
                           lang="en",
                           since="2020-01-01").items():
    EQ3_Mexico += 1  
    
    
if EQ1_USA > EQ2_Canada:
    if EQ1_USA > EQ3_Mexico:
        Example_question = 1

if EQ2_Canada > EQ1_USA:
    if EQ2_Canada > EQ3_Mexico:
        Example_question = 2

if EQ3_Mexico > EQ1_USA:
    if EQ3_Mexico > EQ2_Canada:
        Example_question = 3

#Practice Question
os.system('clear')
print("Lets start with a practice question:")
print("According to Twitter, which of the following North American countries is the most sought after travel destination?")
print("1. USA")
print("2. Canada")
print("3. Mexico")
EXquestion = int(input("Your answer:"))


if EXquestion == Example_question:
    print("CORRECT!")
    print("Now let's start the real game")
    time.sleep(2)
else:
  print("Sorry that is incorrect")
  print("Doesn't matter, now let's start the real game")
  time.sleep(2)
  
# Question 1 option 1
for tweet in tweepy.Cursor(api.search,q="#DelhiPhotography",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q1_Delhi += 1
print("Scanning")
     
# Question 1 option 2
for tweet in tweepy.Cursor(api.search,q="#LondonPhotography",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q1_London += 1
    
 # Question 1 option 3
for tweet in tweepy.Cursor(api.search,q="#LAPhotography",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q1_LA += 1  


    
if q1_Delhi> q1_London:
    if q1_Delhi > q1_LA:
        q1= 1
    
if q1_London> q1_Delhi :
    if q1_London> q1_LA:
        q1= 2

if q1_LA > q1_Delhi:
    if q1_LA> q1_London:
        q1= 3

 
#Question 1
os.system('clear')
print("Question 1: According to Twitter, which of the following cities has the largest photography community in 2020")
print("1. Delhi")
print("2. London")
print("3. LA")
question1 = int(input("Your answer:"))

if question1 == q1:
  Question1 = Right
  Question1.Correct()
  points += 1

else:
  Question1 = Wrong
  Question1.Incorrect()

#Question 2 Options:

#Question 2 option 1
os.system('clear')

for tweet in tweepy.Cursor(api.search,q="#Earthquakes",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q2_Earthquake += 1

print("This might take a minute") #Time filler
     
# Question 2 option 2
for tweet in tweepy.Cursor(api.search,q="#Hurricanes",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q2_Hurricane += 1

print("So... How's your day been?") #Time filler

 # Question 2 option 3
for tweet in tweepy.Cursor(api.search,q="#Floods",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q2_Flood += 1  

    
if q2_Earthquake> q2_Hurricane:
    if q2_Earthquake> q2_Flood:
        q2= 1
    
if q2_Hurricane> q2_Earthquake:
    if q2_Hurricane> q2_Flood:
        q2= 2

if q2_Flood> q2_Earthquake:
    if q2_Flood> q2_Hurricane:
        q2= 3


#Question 2
os.system('clear')
print("Question 2: According to Twitter, which of the following, was the most popular ")
print("Natural Disaster of 2020?")
print("1. Earthquakes")
print("2. Hurricanes")
print("3. Floods")
question2 = int(input("Your answer:"))

if question2 == q2:
  Question2 = Right
  Question2.Correct()
  points += 1

else:
  Question2 = Wrong
  Question2.Incorrect()
  
  #Question 3 Options:

#Question 3 option 1
os.system('clear')

for tweet in tweepy.Cursor(api.search,q="#monolith",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q3_Monolith += 1

print("Anything you want to say while we wait??") #Time filler
     
# Question 3 option 2
for tweet in tweepy.Cursor(api.search,q="#hornets",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q3_Hornets += 1

print("Hang on, just one more minute") #Time filler

 # Question 3 option 3
for tweet in tweepy.Cursor(api.search,q="#locusts",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q3_Locusts += 1  

    
if q3_Monolith > q3_Hornets:
    if q3_Monolith > q3_Locusts:
        q3= 1
    
if q3_Hornets> q3_Monolith :
    if q3_Hornets > q3_Locusts:
        q3= 2

if q3_Locusts> q3_Monolith:
    if q3_Locusts> q3_Hornets:
        q3= 3


#Question 3
os.system('clear')
print("Question 3: According to Twitter, which of the following 2020 phenomenons ")
print("was the biggest or most infamous?")
print("1. The Mysterious, Disappearing Monolith")
print("2. Murder Hornets")
print("3. Locusts")
question3 = int(input("Your answer: "))

if question3 == q3:
  Question3 = Right
  Question3.Correct()
  points += 1

else:
  Question3 = Wrong
  Question3.Incorrect()
  
   
  #Question 3 Options:

#Question 4 option 1
os.system('clear')

for tweet in tweepy.Cursor(api.search,q="#Warren2020",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q4_Warren += 1

print("So, that 2020 was a pretty crazy year right?") #Time filler
     
# Question 4 option 2
for tweet in tweepy.Cursor(api.search,q="#Bloomberg2020",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q4_Bloomberg += 1

 # Question 4 option 3
for tweet in tweepy.Cursor(api.search,q="#Cruz2020",count=100,
                           lang="en",
                           since="2020-01-01").items():
    q4_Cruz += 1  

    
if q4_Warren > q4_Bloomberg:
    if q4_Warren > q4_Cruz:
        q4= 1
    
if q4_Bloomberg> q4_Warren :
    if q4_Bloomberg > q4_Cruz:
        q4= 2

if q4_Cruz> q4_Warren:
    if q4_Cruz> q4_Bloomberg:
        q4= 3


#Question 4
os.system('clear')
print("Final Question: According to Twitter, which of the following presdential candidates ")
print("had the heighest chance of winning?")
print("1. Elizabeth Warren")
print("2. Micheal Bloomberg")
print("3. Ted Cruz")
question4 = int(input("Your answer: "))

if question4 == q4:
  Question4 = Right
  Question4.Correct()
  points += 1

else:
  Question4 = Wrong
  Question4.Incorrect()

os.system('clear')
print("And thats it!")
print("Congratulations, you got", points, "out of 4!")
