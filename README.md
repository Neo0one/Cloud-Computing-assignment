# Cloud-Computing-assignment

Assignment 1:

Author: Yangruibo Ding (yd2447); Zhihao Liu (zl2696)

The URL of the web app: http://www.robinchatbot.com.s3-website.us-east-2.amazonaws.com/

IMPORTANT: 
1. Please click "Log in" button to show the chat interface. This button is reserved for functional extension.

2. Please do not press "Enter" in our web app, if you want to send the message, please click the "send!" button by mouse. There is still a small bug about frontend waiting to be fixed, and we will improve our frontend interface in next assignment.

3. The NLP function of our app is still very naive, so please be sure to use the following 3 sentences as input so that you can get a logical response. If you type something else, the robot will tell you: "I am sorry......".

Input:

Hello, my name is Robin.

I am good. What is your name?

It's a cool name, I think.

Note for the respected person who will grade this assignment: We finish some parts of this assignment by using aws console, so some steps of this assignment cannot be shown in code format. If you have any trouble to run this code, please contact me: yd2447@columbia.edu. Or you can go to the url at the top to view our web app. Thank you so much!

How to run code step by step:

1. S3: Our frontend code files are all included in the directory named "chatbot_frontend". Just create a new bucket and upload the files under this directory.

2. API Gateway: Create new API by importing the Swagger file directly. The address of Swagger file: https://github.com/001000001/aics-columbia-s2018/blob/master/aics-swagger.yaml

3. Lambda: The code of backend is in "chatbot.py". Create a lambda function and choose "Python 3.6", and then copy the code of "chatbot.py" and paste it into lambda console.

