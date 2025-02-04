import random

threshold = 28

def environment():
    temperature = random.uniform(0, 100)  
    return temperature

def sensetemperature():
    current_temp = environment()
    return current_temp

def decide(current_temp):
    if current_temp > threshold:
        action = "High"
    else:
        action = "Low"
    return action

def agent():
    current_temp = sensetemperature()  
    action = decide(current_temp)       
    print(f"Current temperature: {current_temp:.2f}°C")  
    print(f"Action: {action}")  

for i in range(10):
    agent()
