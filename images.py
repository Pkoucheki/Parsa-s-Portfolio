#Images
#Tutorial on how to open images using python
#2/23

#Initialize
import webbrowser

#Functions
#Main
url = ["https://bestfriends.org/sites/default/files/styles/image_small/public/image/Puppy-Adoption_2.jpg-546769.jpg?itok=CxCSLVsf", #Puppy
       "https://www.lpzoo.org/wp-content/uploads/2023/01/parrot-tall-750x1203.png", #Monkey
       "https://i.guim.co.uk/img/media/1d3a1b588915aaae8d2ceefae6294414d7181077/0_100_5758_3455/master/5758.jpg?width=620&dpr=1&s=none&crop=none", #Sloth
       "https://media.newyorker.com/photos/59095bb86552fa0be682d9d0/master/w_1920,c_limit/Monkey-Selfie.jpg" #Monkey
       ]

descriptions = ["Getting a dog offers significant mental and physical health benefits, including reduced stress, lower blood pressure, and increased, consistent physical activity.",
                "Parrots are intelligent, highly affectionate, and long-lived companions that offer unique, interactive companionship, often suitable for apartment living without requiring large outdoor spaces.",
                "Sloths are wild, solitary animals with specialized needs, including a highly specific diet, high temperatures, and high humidity, making them unsuitable for domestic life.",
                "Monkeys are wild animals with complex needs, requiring 20–40 year commitments, specialized diets, large, secure enclosures, and expensive veterinary care, often becoming dangerous and aggressive when they reach maturity."
                ]

def pet_finder():
    question = input("Welcome to Pet-Finder. Are you looking for a domestic or wild animal?: ").lower()
    if question == "wild":
        question2 = input("Are you interested in a lazy animal?: ").lower()
        if question2 == "yes":
            print("The pet we have selected for you is a sloth!")
            webbrowser.open(url[2])
        elif question2 == "no":
            print("The pet we have selected for you is a monkey!")
            webbrowser.open(url[3])
        else:
            print("pick one of the options")
    elif question == "domestic":
        question3 = input("Are you interested in an intelligent or a caring animal: ").lower()
        if question3 == "intelligent":
            print("The pet we have selected for you is a parrot!")
            webbrowser.open(url[1])
        elif question3 == "caring":
            print("The pet we have selected for you is a dog!")
            webbrowser.open(url[0])
        else:
            print("pick one of the options")
    else:
        print("pick one of the options")

pet_finder()

#Sources of Information

#Picture of Puppy
#Website Name: bestfriends
#Author Name: none
#URL: https://bestfriends.org/pet-care-resources/what-expect-new-puppy
#Article Title: What to Expect With a New Puppy
#Date: None

#Picture of Parrot
#Website Name: Lincoln Park Zoo
#Author Name: none
#URL: https://www.lpzoo.org/animals/puerto-rican-parrot/
#Article Title: Puerto Rican Parrot
#Date: none

#Picture of Sloth
#Website Name: The Guardian
#Author Name: Patrick Greenfield
#URL: https://www.theguardian.com/environment/2020/jun/02/why-cant-we-leave-them-alone-the-troubling-truth-about-selfies-with-sloths-aoe
#Article Title: Why can't we leave them alone? The troubling truth about selfies with sloths
#Date: June 2, 2020

#Picture of Monkey
#Website Name: The New Yorker
#Author Name: Jay Caspian Kang
#URL: https://www.newyorker.com/news/daily-comment/monkey-see-monkey-click
#Article Title: Wikipedia Defends the Monkey Selfie
#Date: August 8, 2014
