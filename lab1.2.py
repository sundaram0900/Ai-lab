import random
import datetime

def get_user_tasks():
    tasks = ["Complete project report", "Buy groceries", "Call the doctor", "Attend meeting"]
    return random.sample(tasks, k=random.randint(1, len(tasks)))

def get_user_schedule():
    appointments = ["10:00 AM - Team Meeting", "3:00 PM - Dentist Appointment"]
    return random.choice(appointments) if random.random() > 0.5 else "No appointments today"

def provide_information():
    info = ["Weather: Sunny, 25°C", "Stock Market: Up 1.2%", "Reminder: Pay electricity bill"]
    return random.choice(info)

def decide(tasks, schedule, info):
    actions = [f"Today's Tasks: {', '.join(tasks)}"]
    actions.append(f"Schedule: {schedule}")
    actions.append(f"Info: {info}")
    return actions

def virtual_assistant():
    tasks = get_user_tasks()
    schedule = get_user_schedule()
    info = provide_information()
    actions = decide(tasks, schedule, info)

    print("\nVirtual Assistant Summary:")
    for action in actions:
        print(f"- {action}")

for _ in range(5):
    virtual_assistant()
