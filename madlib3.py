name = input("Name: ")
hours = input("Hours: ")
vehicle = input("Vehicle: ")
adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
verb1 = input("Verb: ")
animal = input("Animal: ")
adj3 = input("Adjective: ")
verb2 = input("Verb: ")
adj4 = input("Adjective: ")
noun = input("Noun: ")
Friend_name = input("Friend's Name: ")
verb3 = input("Verb: ")
verb4 = input("Verb: ")
place = input("Place: ")
verb5 = input("Verb: ")

madlib = f""" Last month, I went to Disney World with {name}. We\n
traveled for {hours} by {vehicle}. Finally, we 
arrived and it was very {adj1}. There were\n
{adj2} people {verb1} everywhere. There\n
were also people dressed up in {animal} costumes.\n

I wish it had been more {adj3}, but we {verb2} anyway.\n
We also went on a(n) {adj4} ride \n
called Magic {noun}. {Friend_name} nearly fell off a ride and had to be\n 
{verb3}. Later, we went to the hotel and \n
{verb4}. Next year, I want to go to {place},\n 
where we can {verb5}.
"""

print(madlib)
