#Writing Prompts
#100 Days Of Code inspired

import random, time, sys

name = input("Welcome to the prompt generator! What shall I call you?\n ")

#Check input
def check_input(inspired):
    #inspired = input(f"Hi there {name.capitalize()}! it's good to see you. Are you feeling inspired today?\n Enter 'Y' for YES and 'N' for NO: ").upper()

    if inspired.isalpha() == True and inspired == "Y":
        type_writer("Great! I'm glad you are able to keep going. I may be of no use to you, but if you need me, you know where to find me")
        type_writer(f"Goodbye {name.capitalize()}!")


    elif inspired.isalpha() == True and inspired == "N":
        print("I can help with that. Here, this can get you started: ")
        prompt_generator()

    else:
        #inspired = None
        inspired = (input("\tPlease enter 'Y' or 'N': ")).upper()
        check_input(inspired)
        
#Ask if user wants a new prompt
def new_prompt():
    time.sleep(2)
    new_prompt= input(f"\nWould you like another prompt, {name.capitalize()}? Please enter 'Y' or 'N': ").upper()
    if new_prompt.isalpha() == True and new_prompt == "Y":
        text1 = "Sweet! Here is another: "
        type_writer(text1)
        prompt_generator()
    elif new_prompt.isalpha() == True and new_prompt == "N":
        text2 = "I understand. I shall take my leave then. Until next time!\n"
        text3 = f"Goodbye {name.capitalize()}!"

        type_writer(text2)
        time.sleep(0.5)
        type_writer(text3)

    else:
        #inspired = None
        new_prompt = (input("\tPlease enter 'Y' or 'N': ")).upper()
        new_prompt(new_prompt)
        
#Typewriter effect. Referenced https://trinket.io/python/73ba588f2b
def type_writer(input):
    time.sleep(1)
    for i in input:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1) #A pause

def prompt_generator():
    prompt_list = ['"If I could change anything, in all honesty with myself, what and why?"',
                '"Time will pass anyway"',
                '"A mistake done more than once is a decision"',
                '"What do you seek in friends?"',
                '"Are you happy?"',
                '"What act of kindness still goes with you?"',
                '"Are you doing what you are supposed to do?"',
                '"The only thing that is constant is change"',
                '"What is your purpose?"',
                '"What is stopping you?"',
                '"When was the last time you were vulnerable?"',
                '"What is something you are proud of and never had the opportunity to talk about?"',
                '"What have you been fighting?"',
                '"What do you want to tell that person, and you probably never will?"',
                '"How was your day?"',
                '"Nature does not hurry, yet everything is accomplished"',
                '"Do you have the patience to wait until your mud settles and the water is clear?"',
                '"Stop thinking, and end your problems"',
                '"Doing nothing is better than being busy doing nothing"',
                '"We make gods who look like us for a reason"',
                '"When I let go of what I am, I become what I might be"',
                '"If anything is worth doing, do it with all your heart"']
    prompt =  random.choice(prompt_list)
    #Print output using typewriter effect
    type_writer(prompt)
    #Ask if user wants a new prompt
    new_prompt()


#Running code order...
inspired = input(f"Hi there {name.capitalize()}! it's good to see you. Are you feeling inspired today?\n Enter 'Y' for YES and 'N' for NO: ").upper()
#inspired = opt.upper()
check_input(inspired)
