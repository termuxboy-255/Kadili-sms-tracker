# kadilisms.py

import time
import json

# Functio to simulate SMS tracking
def simulate_sms():
    messages = [
        {"sender": "12345", "content": "Your OTP code is 67890", "time": time.ctime()},
        {"sender": "67890", "content": "New promotional offer from Kadili SMS!", "time": time.ctime()},
    ]
    
    print("SMS Tracker Simulation:\n")
    for msg in messages:
        print(f"From: {msg['sender']}\nMessage: {msg['content']}\nTime: {msg['time']}\n")
        store_data(msg)

# Function to store simulated data
def store_data(message):
    data = {"sms_logs": []}
    try:
        with open("sms_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        pass

    data["sms_logs"].append(message)

    with open("sms_data.json", "w") as file:
        json.dump(data, file)

# Running the SMS tracker simulation
simulate_sms()
