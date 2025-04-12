#!/bin/bash

# Update packages and install dependencies
pkg update -y
pkg upgrade -y
pkg install python git figlet -y

# Clone repository
git clone https://github.com/termuxboy-255/Kadili-sms-tracker

cd Kadili-sms-tracker

# Run the SMS tracker tool
python kadilisms.py
