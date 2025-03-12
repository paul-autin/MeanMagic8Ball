import random
answer_list=['I literally hate you.', 
             'It is decidedly so.', 
             'Without a doubt.',
             'My dad is in jail.', 
             'Eat my ass.', 
             'As I see it, no. Ask a better question.',
             'Noooo, you look so ugly when you cry.',
             'Welcome to Weenie Hut Jr, where we serve up sadness on a silver platter.', 
             'Ugh.', 
             'All signs point to Lauderdale.',
             'Dude I am completely shitfaced.', 
             'Ask again after I sober up.', 
             'Better not tell you now - I smell like decimated cow fetus.',
             'Cannot predict now - still drunk.', 
             'Concentrate and ask again, pussy.',
             "I thought we'd made an agreement to not ask me political questions...", 
             "No no no, now I've got a question for you: how do my arms look in this tank top?", 
             "My sources say OJ was innocent.", 
             'Jesus Christ... Can I recommend a self-help book?',
             "I can't focus over the deafening sound of you being an idiot."]
while True:
    question=input("Ask the magic 8 ball a question (or type 'quit' to quit): ")
    if question=="quit":
        print("Stopping the Game.")
        break
    answer_string=random.choice(answer_list)
    print(answer_string)
