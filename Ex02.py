
class animals:

    def __init__(self, name, nb, aliment, nb_pattes, food):
        self.name = name
        self.nb = nb
        self.aliment = aliment
        self.nb_pattes = nb_pattes
        self.food = food

    def __str__(self):
        return "Cet animal est un(e) " + self.name + " il possède " + str(self.nb) + " Jambes, il est de type " + self.aliment + ", il a " + str(self.nb_pattes) + " pattes et mange environ " + str(self.food) + " grammes de nourriture"

class animaux_marin(animals):
    pass

pieuvre = animaux_marin('Pieuvre', 1, 'Carnivore', 0, 200)

class mammiferes(animals):
    pass

        humain = mammiferes('Humain', 2, 'Omnivore', 2, 600)
        lion = mammiferes('Lion', 2, 'Carnivore', 4, 3000)
        mouton = mammiferes('Mouton', 5, 'Vegetarien', 4, 500)
        lapin = mammiferes('Lapin', 7, 'Vegetarien', 4, 100)
        chien = mammiferes('Chien', 2,  'Omnivore', 4, 500)

class domestique(animals):
    pass

        poule = domestique('Poule', 8, 'Omnivore', 2, 2000)
        mouton = domestique('Mouton', 5, 'Vegetarien', 4, 500)
        lapin = domestique('Lapin', 7, 'Vegetarien', 4, 100)
        chien = domestique('Chien', 2, 'Omnivore', 4, 500)


if __name__=="__main__":

        autruche = animals('Autruche', 4, 'Omnivore', 2, 1000)
        serpent = animals('Serpent', 2, 'Carnivore', 0, 200)

        ma_ferme = {}
        ma_ferme["Dans ma ferme il y a :"] = animals()

    for
