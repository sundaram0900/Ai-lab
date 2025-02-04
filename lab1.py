import random

MOISTURE_THRESHOLD = 40  
PEST_THRESHOLD = 0.3    

def sense_environment():
    moisture = random.uniform(20, 60)  
    weather = random.choice(["Sunny", "Rainy"])  
    pests = random.random()  
    return moisture, weather, pests

def decide(moisture, weather, pests):
    if moisture < MOISTURE_THRESHOLD and weather != "Rainy":
        water = "Watering the crops"
    else:
        water = "Skipping watering"

    if pests > PEST_THRESHOLD:
        pesticide = "Applying pesticide"
    else:
        pesticide = "No pesticide needed"

    return water, pesticide

def agent():
    moisture, weather, pests = sense_environment()
    water_action, pesticide_action = decide(moisture, weather, pests)

    print(f"\nMoisture: {moisture:.2f}% | Weather: {weather} | Pest Level: {pests:.2f}")
    print(f"Action: {water_action} | {pesticide_action}")

for _ in range(10):
    agent()
