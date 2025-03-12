#This is a prototype for a Mean Magic 8 Ball - as of now, the potential responses of the 8 Ball
#are limited to 15. Will be adding more soon. The idea is to bind potential answers
#to corresponding numbers as opposed to having the answers themselves be randomly selected.

#Before you say anything about how this code would be cleaner if I had the answers themselves randomnly
#selected from an answer bank, I'm new to Python and wanted to play around with "if/else/elif" statements
#for this. My GitHub will host two versions of the game, one of which will use the more popular (and cleaner)
#"choice()" function.

#Players should fill out the "Name" field before running the script. There's literally a single nice answer in this program,
#so hats off to you if you manage to get an answer that isn't rude on your first try.

import random

name = "user"
#Change to your first name, or leave as is.

answer = ""

random_number = random.randint(1,15)
#print(random_number)

if random_number == 1:
    answer = "Back off, I need space"
elif random_number == 2:
    answer = "You're such a little fat girl"
elif random_number == 3:
    answer = "Leave me alone; I'm expressing myself"
elif random_number == 4:
    answer = "Global warming gives me the ick"
elif random_number == 4:
    answer = "Try again later"
elif random_number == 5:
    answer = "Fine, whatever"
elif random_number == 6:
    answer = "Okay, I can see that working out"
elif random_number == 7:
    answer = "I would love that for you... NOT!"
elif random_number == 8:
    answer = "You should ask me in about 4 hours, I'll be sober by then"
elif random_number == 9:
    answer = "*Free Bird plays in the background while I ram my Dodge Durango into a family of four*"
elif random_number == 10:
    answer = "Maybe instead of playing with another man's Python script, you should go touch grass"
elif random_number == 11:
    answer = "Dude I'm WAYYY too drunk for this rn"
elif random_number == 12:
    answer = "Okay, I'll help you out if you can get my ankle monitor off"
elif random_number == 13:
    answer = "I hate that question almost as much as I hate you"
elif random_number == 14:
    answer = "It turns out that there aren't any hot singles in your area"
elif random_number == 15:
    answer = "Nooooo, you're so ugly when you cry..."

while True:
    question=input("Ask the 8 Ball a question (press enter to quit): ")
    if question=="":
        print("Stopping the game")
        break
    else:
        print(name + " asks: " + question)
        print("Mean Magic 8 Ball's answer: " + answer)
