import random

def sense_environment():
    moisture = random.uniform(20, 80)  
    temperature = random.uniform(10, 40)  
    crop_health = random.uniform(0, 1)  
    market_demand = random.uniform(0, 1)  
    return moisture, temperature, crop_health, market_demand

def calculate_utility(moisture, temperature, crop_health, market_demand):
    return (moisture / 100) * 0.3 + (1 - abs(25 - temperature) / 40) * 0.2 + crop_health * 0.3 + market_demand * 0.2

def decide(utility, moisture, crop_health, market_demand):
    actions = []
    
    if moisture < 40:
        actions.append("Water the crops")
    else:
        actions.append("No watering needed")

    if crop_health < 0.4:
        actions.append("Apply fertilizers/pesticides")
    else:
        actions.append("Crop is healthy")

    if market_demand > 0.7 and crop_health > 0.6:
        actions.append("Harvest the crops")
    else:
        actions.append("Wait before harvesting")

    actions.append(f"Utility Score: {utility:.2f}")
    return actions

def smart_agriculture_agent():
    moisture, temperature, crop_health, market_demand = sense_environment()
    utility = calculate_utility(moisture, temperature, crop_health, market_demand)
    actions = decide(utility, moisture, crop_health, market_demand)

    print("\nAgriculture Report:")
    print(f"Moisture: {moisture:.2f}% | Temp: {temperature:.2f}°C | Health: {crop_health:.2f} | Demand: {market_demand:.2f}")
    for action in actions:
        print(f"- {action}")

for _ in range(5):
    smart_agriculture_agent()
