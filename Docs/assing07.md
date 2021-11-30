## Exception Handling & Pickling

NSoldano, 11/27/2021

### Introduction

This week’s module focuses on understanding exception handling and pickling in Python. The website Medium.com has a plethora of resources related to programming in Python. Two useful articles I found on exception handling in Python are https://pub.towardsai.net/python-examples-to-make-algorithm-more-robust-with-exception-handling-6bff7a127786 and https://medium.com/technofunnel/exception-handling-in-python-fc71497e0d18. The first article has a useful code example of exception handling that I decided to use for my script assignment. As for Pickling the following article makes use of some good examples, https://python.plainenglish.io/pickling-python-objects-for-future-use-95a2ce45f443. 

### Exception Handling

Programmers require exception handling for three main reasons. 
1.	Error Handling: In the case of errors during runtime, exception handling can handle the scenario of Failures and avoid termination of the program. 
2.	Code Separation: Error Handling can help us segregate the code that is required for error handling from the main logic. The error related code can be placed inside the except block which is segregating it from the regular code that contains the application logic.
3.	Grouping Error Type and Error Differentiation: It can help to segregate different kinds of errors that are encountered during the execution. It can have multiple except blocks, each handling a specific kind of error. 

![image](https://user-images.githubusercontent.com/45339790/143969067-cd22438d-9e9f-421d-85a2-0f630932e06c.png)

![image](https://user-images.githubusercontent.com/45339790/143969098-3c64e807-9908-4339-b2f1-f8697be55597.png)

![image](https://user-images.githubusercontent.com/45339790/143969106-a29674ea-baec-4478-8892-05aded5d652e.png)

![image](https://user-images.githubusercontent.com/45339790/143969122-c194751c-8433-47da-a8f1-558bb4c38177.png)


### Pickling

Pickling lets users save a python object in a hard disc space so that it can be used to in another program. An example of this is in Machine Learning, a predictive model can be trained on data and then saved as a pickle file. A user can then load the pickle file later and make predictions on another data set. Pickling is done for three reasons:
1.	Storing data for later use
2.	User’s object needs to be transferred to another user /across a network
3.	User needs to store some object into a database to be retrieved by some other system

![image](https://user-images.githubusercontent.com/45339790/143969205-d1cd343a-726b-4c14-beda-fedb1ea979af.png)

![image](https://user-images.githubusercontent.com/45339790/143969231-65f2a9f0-2171-4078-83db-257d249457d5.png)

## Summary

In Python programming there are error and exceptions. Errors are problems that cannot be handled by the program, but exceptions can. Examples of errors are Syntax Error, Out of Memory Error and Recursion Error. Exceptions are errors that are detected when the program is running and can be handled.  
Pickling as mentioned previously is for data persistence, transferring to another user or network, and storing objects in a database. It is not to be used for compression, encryption,  and outside of the Python Programming language. 
