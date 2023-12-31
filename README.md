# End-to-End Chatbot with Scalable Design, Database Creation, and BI Visualization

## Overview

SQL user info --> invoke curl request --> have rasa chat --> send metrics through kinesis to aws --> ETL??? --> dashboard 

This project will imploy an end-to-end pipeline for chatbot using Rasa. The goal is to demonstrate the integration of SQL, Rasa, Python, AWS, and BI tools. 

The skills touched on will include 
* database creation and population
* SQL
* advanced Python OOP including factory methods and heavy automation
* data migration via AWS Kinesis
* cloud warehousing in AWS
* BI analytics
* and more...


### LLM
While GPT-4 is the current hottest topic, other LLMs such as BERT are still capable of a wide variety of chatbot needs. While GPT has a superior embedding size, BERT has a free API that we can utilize. Therefore, we will use Hugging Face's Bert as the weights for this model.


## Getting Started
### DataBase Creation
We will be using the database music which holders a users table populated with names, ages, and music preferences. The tables can be populated by running the database_creation/ project located in the root folder. This project currently does not have a requirements doc. 

### Rasa SetUp


Create an enviornment for this project and download Rasa. For this project I'm using rasa version 2.0.2 . 

In an isolated folder, run 

>> rasa init

to instatiate the rasa files. At this point you can test the basic Rasa functions by running

>> rasa shell

and having a short conversation. Once you see that Rasa is up and running, we can add on to the basic framework to create our project. 


We can envoke Rasa's api using the command 
>> rasa run --enable-api

Then we can interface with the rasa shell using curl commands. This allows us to send extra parameters that we will use to customize aspects of the conversation. The flexibility of the curl requests paired with our custom action server will give us the freedom to pull user args from a database and use them within the framework.



### Data
Since the purpose of this project is to show the integration between frameworks, I will not spend time on data collection and will use the given data from rasa init command. This data can be found in ./data/nlu.yml





// for rasa framework help
https://jaguhiremath62.medium.com/building-an-end-to-end-conversational-assistant-with-rasa-407bf1feb866


// for factory methods help
https://realpython.com/factory-method-python/#introducing-factory-method
