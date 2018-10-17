import json
import time

def lambda_handler(event, context):
    request = event["messages"][0]["unstructured"]["text"]
    if request == "Hello, my name is Robin.":
        response = "Chatbot: Hi, Robin, how are you?"
    elif request == "I am good. What is your name?":
        response = "Chatbot: Oh, my name is Chatbot."
    elif request == "It's a cool name, I think.":
        response = "Chatbot: Thank you so much."
    else:
        response = "Chatbot: I am sorry for not understanding you right now......"
    return {
    "messages":[
        {
            "type":"string",
            "unstructured":{
                "id":"123",
                "text":response,
                "timestamp":get_time()
            }
        }
    ]
}

def get_time():
    timestamp = int(round(time.time()*1000))
    time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp/1000))
    return time_str
