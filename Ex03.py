import json
import datetime
import random
import pprint

class Animal:

    def __init__(self, name, nb, aliment, nb_pattes, food):
        self.name = name
        self.nb = nb
        self.aliment = aliment
        self.nb_pattes = nb_pattes
        self.food = food

    def __str__(self):
        return "un animal qui est un(e) " + self.name + " il possède " + str(self.nb) + " Jambes, il est de type " + self.aliment + ", il a " + str(self.nb_pattes) + " pattes et mange environ " + str(self.food) + " grammes de nourriture"

    def __add__(self, animal, type, birth_year):

       parsed_json = (json.loads(json_data))
       print(json.dumps(parsed_json, indent=4, sort_keys=True))

with open('farm.json') as json_file:
    data = json.load(json_file)
    for p in data['animal list']:

        print('type : ' + p['type'])

if __name__ == '__main__':

    my_farm = ["farmville", "farmcity", "farmland"]

for x in range(len(my_farm)):
    print (my_farm[x])

#rand()
