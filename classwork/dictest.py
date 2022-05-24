#!/usr/bin/env python3
from pprint import pprint

cable = {
	"Real Name": "Nathan Summers",
	"Creators": ["Chris Claremont", "Rick Leonardi", "Louise Simonson", "Rob Liefeld"],
	"Team Affliations": ["X-Men", "X-Force", "Askani", "Six Pack", "The Twelve", "New Mutants", "The Underground"],
	"Aliases": ["Nathan Winters", "Nathan Dayspring", "Askani'son", "Soldier X", "Chosen One", "Traveler"],
	"Base of Operations": "Often in Flux", 
	"Powers": ["Telepathy", "Telekinesis", "Technopathy", "Enhanced Physical Attributes"]
}

# DrStrange={'Real Name':'Stephen Strange','Abilities':['Martial Arts','Energy Blasts','Sword Fighting'],'Aliases':['Sherlock','Sorcerer Supreme','Vincent Stephens'],'Universe':'Marvel','Education':['MD','Extensive Sorcery Training']}


# print(f"Dr Strange, aka {DrStrange['Real Name']}, aka {DrStrange['Aliases'][1]}, was a member of the {DrStrange['Universe']} universe. He is known for his {DrStrange['Abilities'][1]} and {DrStrange['Education'][1]}.")

cable["Partnerships"] = [
    'Domino',
    'Rachel Summers',
    'Deadpool',
    'Hope Summers']

pprint(cable)
print('\n')
print(cable.keys())

choice = input(">")

