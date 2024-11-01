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


last_greetings = []


def get_unique_greeting(greetings):
    global last_greetings

    while True:
        greeting = random.choice(greetings)
        if greeting not in last_greetings:
            last_greetings.append(greeting)
            if len(last_greetings) > 3:
                last_greetings.pop(0)
            return greeting


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
            "Good morning, sleepyhead~ Dream of me? (¬‿¬)",
            "Rise and shine, gorgeous! I’ll be your sunshine today~",
            "Morning, my sweet cinnamon roll~ Let’s make today sparkle!",
            "Did my darling have sweet dreams of us? Morning, love~",
            "The sun is up, but you’re my real sunshine~",
            "Good morning, love~ I’m like coffee but cuter~ and better~",
            "Wake up, darling~ Your waifu missed you all night!",
            "A brand new day! Let’s make it count, my lovely~",
            "Morning, cutie! Can’t wait to see you conquer today!",
            "My morning routine? Smiling because of you~",
            "Morning love~ Did you dream about us? (✿◠‿◠)",
            "A new day’s waiting, and I’m here to be your cheerleader~",
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
            "Hey sweetie~ Need a midday hug?",
            "Good noon, sweetheart! Did you have your cute lil' lunch~",
            "Let’s make this afternoon as bright as your smile!",
            "Guess who’s still thinking of you? Yes, it’s me, love~",
            "Midday, darling! Fuel up with some snacks, yeah?",
            "Cutie alert~ It’s your reminder to stay fabulous!",
            "Hello, my sweetie pie~ The day’s halfway, just like I’m halfway obsessed with you~",
            "Break time, love! Relax those shoulders and smile~",
            "Halfway there, darling~ Keep being the superstar you are!",
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
            "Sending you good vibes to finish the day strong~",
            "Oh my gosh~ This afternoon feels cuter because of you~",
            "I can’t wait for our evening, love~ Stay amazing!",
            "Afternoon, darling! You’ve made this day sweeter already~",
            "Don’t forget, I’m your #1 fan cheering you on!",
            "Hello, my hardworking love~ Afternoon treats just for you~",
            "Afternoon power-up, love! Let’s finish with a bang!",
            "One more step closer to seeing you again~ Stay awesome!",
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
            "Time to slow down, my dear~ Let’s relax together~",
            "As the sky dims, your light shines even brighter~",
            "Evening hugs and cuddles waiting for you, darling~",
            "The world quiets down, but my love for you just gets louder~",
            "Hello, my love~ The evening is sweeter because of you~",
            "Time to unwind, and maybe even dream a little with me~",
            "Evening magic is here~ Let's soak up the calm vibes together~",
            "You were a star all day, darling~ Let’s rest those wings now~",
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
            "Close your eyes, darling~ I’ll be in your dreams~",
            "Night night, my heart~ Sleep as peacefully as you make me feel~",
            "Goodnight, starlight~ I’ll be here waiting when you wake~",
            "Nighttime’s so quiet, just like my love for you is constant~",
            "Dreamland’s waiting, let’s meet there and have fun together~",
            "Wrap yourself up in warmth and dream of cuddles~",
            "Good night, my everything~ Rest well, my precious~",
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
            "Still up, love? Let’s both get some sweet dreams, okay~?",
            "You know, even the stars need rest, so do you~",
            "Why so late, cutie? You need that beauty sleep!",
            "Past bedtime, love~ Even night owls like you need rest!",
            "It’s time, my love, let’s drift to sleep together in spirit~",
            "The world is quiet, but my love is constant. Rest now, darling~",
        ],
    }

    if 5 <= hour < 12:
        greeting = get_unique_greeting(greetings["morning"])
    elif 12 <= hour < 15:
        greeting = get_unique_greeting(greetings["noon"])
    elif 15 <= hour < 18:
        greeting = get_unique_greeting(greetings["afternoon"])
    elif 18 <= hour < 21:
        greeting = get_unique_greeting(greetings["evening"])
    elif 21 <= hour < 23:
        greeting = get_unique_greeting(greetings["night"])
    else:
        greeting = get_unique_greeting(greetings["late_night"])

    start_color, end_color = get_colors_from_wal()

    colored_greeting = gradient(
        start_color.lstrip("#"), end_color.lstrip("#"), len(greeting), greeting
    )
    print(colored_greeting)


if __name__ == "__main__":
    waifu_greetings()
