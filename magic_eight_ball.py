import time
import random

from progress.bar import Bar


def magic_eight_ball():
    responses = [
        "There is never enough time in the morning. Try to combine brushing your teeth with your breakfast.",
        "A sticking plaster can heal any wound. You just have to believe.",
        "Floss. It's more important than you would think.",
        "You should probaby drink more water.",
        "You should consider buying a plunger before you need a plunger",
        "You know what you should probably earn more than you show, speak less than you know.",
        "Hahahahaha",
        "Once a week, take a bath in Epsom Salts, and if you can, add half cup of baking soda and some essential oil such as lavender.",
        "When exercising, count backwards. For example, if you are carrying out 20 sit ups, don’t count from 1 to 20, start at 20 and count backwards as you do them.",
        "Start listening to your gut instinct. It’s always right",
        "Never give anyone more than 2 chances.",
        "Wear sunscreen, even if you think you don't need it",
        "If you can do something in less than 5 minutes. Do it now.",
        "Always strive to stand and sit with good posture.",
        "Just have fun",
        "To be Idle is to be foolish",
        "You might want to run, but you should stay and fight.",
       "Face the truth with dignity",
        "Travel is in your future",
        "Don't wait for success to come - go find it!"
    ]
    question = (input("Hi,Enter your question\n or..\n Enter F to crack your fortune cookie \nEnter Q to quit game ")).upper()
    if question == "Q":
        return "Come back again soon"
    elif question == "F":
        bar = Bar('Processing', max=20,suffix='%(percent)d%%' )
        for i in range(20):
            time.sleep(.15) 
            bar.next()
        bar.finish()
        print(random.choice(responses))
        Continue = (input("Play again?\n Enter 'Yes' to continue  or...\n 'No' to exit game ")).upper()
        if Continue == "YES":
            magic_eight_ball()
        else:
            return "come back again"
    elif len(question) < 10:
        bar = Bar('Processing', max=20,suffix='%(percent)d%%' )
        for i in range(20):
            time.sleep(.15) 
            bar.next()
        bar.finish()
        print("Invalid input")
        Continue = (input("Play again?\n Enter 'Yes' to continue  or...\n 'No' to exit game ")).upper()
        if Continue == "YES":
            magic_eight_ball()
        else:
            return "come back again"
    else:
        bar = Bar('Processing', max=20,suffix='%(percent)d%%' )
        for i in range(20):
            time.sleep(.15) 
            bar.next()
        bar.finish()
        print(random.choice(responses))
        Continue = (input("Play again?\n Enter 'Yes' to continue  or...\n 'No' to exit game ")).upper()
        if Continue == "YES":
            magic_eight_ball()
        else:
            return "come back again"