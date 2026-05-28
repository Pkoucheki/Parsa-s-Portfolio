#Dog Breed (CREATE TASK)
#The purpose of my program is to help users choose a dog breed that meets their needs

#Init
import pandas as pd
import random
import webbrowser

data = pd.read_csv("Dogs.csv")

id = data['id'].tolist()
Name = data['Name'].tolist()
Breed_Group = data['Breed Group'].tolist()
BredFor = data['BredFor'].tolist()
Minimum_Life_Span = data['Minimum Life Span'].tolist()
Maximum_Life_Span = data['Maximum Life Span'].tolist()
Minimum_Height = data['Minimum Height'].tolist()
Maximum_Height = data['Maximum Height'].tolist()
Minimum_Weight = data['Minimum Weight'].tolist()
Maximum_Weight = data['Maximum Weight'].tolist()
Temperament = data['Temperament'].tolist()
Image = data['Image'].tolist()
tiny = []
small = []
medium = []
large = []
filter = []

def getDogSize(size):
    for i in range(len(id)):
        if Maximum_Weight[i] <= 10:
            tiny.append(Name[i])
        elif Minimum_Weight[i] >= 11 and Maximum_Weight[i] <= 25:
            small.append(Name[i])
        elif Minimum_Weight[i] >= 26 and Maximum_Weight[i] <= 60:
            medium.append(Name[i])
        elif Minimum_Weight[i] >= 60:
            large.append(Name[i])
    if size == "tiny":
        number = random.randint(0,2)
        print(f"The perfect dog for you would be {tiny[number]}")
        print(f"If you dont like our recomendation here are some more tiny dogs: {tiny}")
    if size == "small":
        number = random.randint(0,8)
        print(f"The perfect dog for you would be {small[number]}")
        print(f"If you dont like our recomendation here are some more small dogs: {small}")
    if size == "medium":
        number = random.randint(0,18)
        print(f"The perfect dog for you would be {medium[number]}")
        print(f"If you dont like our recomendation here are some more medium dogs: {medium}")
    if size == "large":
        number = random.randint(0,26)
        print(f"The perfect dog for you would be {large[number]}")
        print(f"If you dont like our recomendation here are some more large dogs: {large}")
    else:
        print("Pick one of the options")

#getDogSize("large")

def breedinfo(breed):
    for i in range(len(id)):
        if breed == Name[i]:
            print(f"You're interested in {breed}! Some info on them: {Temperament[i]}")
            webbrowser.open(Image[i])
    if breed != Name[i]:
        print("We don't have any info on that breed")

#breedinfo("Affenpinscher")

def dogfinder(purpose):
    for i in range(len(id)):
        if purpose in BredFor[i]:
            filter.append(Name[i])
    if filter == []:
        print("We found no matches")
    print(f"here are some dogs that fit the trait you're looking for: {filter}")


#INTERFACE
def dogsite():
    while True:
        question = input("Welcome to DogSite! What are you looking to do today? (dogsize, breedinfo, dogfinder, or exit): ").lower()
        if question == "dogsize":
            size = input("What size dog are you looking for? (tiny, small, medium, or large): ")
            getDogSize(size)
            continue
        elif question == "breedinfo":
            breed = input("Please enter the breed you are looking for information about: ")
            breedinfo(breed)
            continue
        elif question == "dogfinder":
            purpose = input("What traits are you looking for in a dog?: ")
            dogfinder(purpose)
            continue
        elif question == "exit":
            print("Thank you for using DogSite")
            break
        else:
            print("Please enter a valid answer")
            continue

dogsite()

#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en

#Weight ranges:
#tiny = 10 and under
#small = 25 -11
#medium = 60 - 26
#large = over 60
