#!/usr/bin/env python3
import datetime
import json
import os
import random


def gradient(start_color, end_color, steps, text):
    def hex_to_rgb(hex_color):
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    rgb_range = [(end_rgb[i] - start_rgb[i]) / (steps - 1) for i in range(3)]

    result = []
    for step in range(steps):
        current_rgb = [int(start_rgb[i] + rgb_range[i] * step) for i in range(3)]
        color_code = f"\033[38;2;{current_rgb[0]};{current_rgb[1]};{current_rgb[2]}m"
        result.append(color_code + text[step])

    return "".join(result) + "\033[0m"


def get_colors_from_wal():
    wal_colors_path = os.path.expanduser("~/.cache/wal/colors.json")

    with open(wal_colors_path, "r") as file:
        data = json.load(file)

    color1 = data["colors"]["color1"]
    color5 = data["colors"]["color5"]

    return color1, color5


def get_hour():
    return datetime.datetime.now().hour


def waifu_greetings():
    hour = get_hour()

    greetings = {
        "morning": [
            "Good morning, darling~",
            "Rise and shine, love~",
            "Morning cutie~ Ready to start your day?",
            "Time to wake up, my sweet cinnamon roll~",
            "Good morning, sleepyhead~ Did you dream of me?",
            "Morning sunshine~ Let's conquer the day together!",
            "Rise and shine, darling~ You’ve got this!",
            "Good morning, love~ It’s a beautiful day because you're in it!",
            "Wake up, sleepy bear~ Let’s start a fun day together!",
            "Yay~ It's morning, and I'm so happy to see you, darling~",
        ],
        "noon": [
            "Good noon, dear~",
            "Time for lunch, honey~",
            "Midday, don’t forget to stay hydrated~",
            "Lunch break~ Let’s eat something yummy together, sweetie~",
            "It’s noon, darling~ Recharge your energy with a snack!",
            "Hello, cutie~ The afternoon is calling you to be awesome!",
            "Hey love, did you have your lunch yet? Don’t skip it, okay~",
            "Half the day is done, love! Keep going~",
            "Noon vibes, darling~ You’re doing amazing!",
            "Midday magic time~ Don't forget to take a breather!",
        ],
        "afternoon": [
            "Afternoon, cutie~",
            "Hope you’re enjoying your afternoon, sweetie~",
            "Good afternoon, darling~ Keep going!",
            "Afternoon vibes~ The day’s still young, darling~",
            "The sun’s high in the sky, just like your potential~ Keep shining!",
            "Hey, sweetie~ It’s afternoon, and you’re doing great~",
            "Keep up the good work, darling~ You’re slaying the day!",
            "Ahh~ The afternoon breeze is as wonderful as you, love~",
            "Good afternoon, cutie pie~ Let’s finish the day strong!",
            "Hello, darling~ Afternoon time, stay fab~",
        ],
        "evening": [
            "Good evening, darling~",
            "Time to unwind, love~",
            "Evening, cutie~ Don’t forget to relax!",
            "The sun is setting, but you’re still shining, darling~",
            "Ah, evening already~ Time to chill and enjoy the peaceful vibes, love~",
            "Evening has come, my dear~ How about some cozy time?",
            "Good evening, honey~ You’ve worked hard today~",
            "Hello, darling~ The night is approaching, but you’re still amazing!",
            "Evening’s here~ Let’s enjoy the rest of the day together, sweetie~",
            "Ah~ Evening, darling~ You deserve a break!",
        ],
        "night": [
            "Night, love~",
            "It’s getting late, sweetie~",
            "Time to sleep soon, darling~ Sweet dreams~",
            "Ah, night has fallen, darling~ Let's get ready for bed~",
            "Good night, my love~ May your dreams be sweet and restful~",
            "The stars are out, but none shine brighter than you, darling~",
            "Ah~ It’s nighttime, love~ Time to snuggle in~",
            "Night night, cutie~ I’ll be here when you wake up~",
            "Sleep tight, darling~ Dream of happy things~",
            "It’s night, love~ Time for peaceful dreams and sweet rest~",
        ],
        "late_night": [
            "Why are you still awake, darling~?",
            "It’s so late, hun~ Time for bed~",
            "Ahh, it’s past bedtime! Get some rest, cutie~",
            "Late night, darling~ You need your beauty sleep~",
            "Why are you still up, love? Go to bed, I’ll be here tomorrow~",
            "Cutie, it’s super late! Time to head to dreamland~",
            "It’s waaaay too late, love~ Don’t stay up too long~",
            "Ahhh~ You’re a night owl, huh? Even so, bed’s calling you~",
            "The night is quiet, but you should be resting, darling~",
            "Darling~ It’s late, get some rest, okay? I’ll be waiting when you wake up~",
        ],
    }

    if 5 <= hour < 12:
        greeting = random.choice(greetings["morning"])
    elif 12 <= hour < 15:
        greeting = random.choice(greetings["noon"])
    elif 15 <= hour < 18:
        greeting = random.choice(greetings["afternoon"])
    elif 18 <= hour < 21:
        greeting = random.choice(greetings["evening"])
    elif 21 <= hour < 23:
        greeting = random.choice(greetings["night"])
    else:
        greeting = random.choice(greetings["late_night"])

    start_color, end_color = get_colors_from_wal()

    colored_greeting = gradient(
        start_color.lstrip("#"), end_color.lstrip("#"), len(greeting), greeting
    )
    print(colored_greeting)


if __name__ == "__main__":
    waifu_greetings()
