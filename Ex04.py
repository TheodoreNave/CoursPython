import datetime
import random
import json

class Animal:

	def __init__(self, my_type, my_sex, my_birthdate=None):
		self.my_type = my_type
		self.my_sex = my_sex
		self.my_birthdate = my_birthdate

		if my_birthdate == None :
			global current_farms_date
			self.my_birthdate = current_farms_date


	def __str__(self):
		return "Animal : " + str(self.my_type) + " " + str(self.my_sex) + " " + str(self.my_birthdate)


	def want_reproduce(self):

		global future_farms_date

		if (self.my_sex == "Female") and ((future_farms_date - self.my_birthdate).days > 365) and ((future_farms_date - self.my_birthdate).days % 365 < 30):

			return True

		else :
			return False

class Farm:

	"""This class reprensent a farm with its attributes.

    Attributes:
        farm_name (str)
		animal_list (list)
		current_date (datetime)
	"""

	def __init__(self, farm_name=None):

		"""Instanciation of the class

		Arguments:
			farm_name (str) : optionnal
		"""

		self.farm_name = farm_name
		self.animal_list = []
		self.current_date = datetime.datetime.now()


	def __str__(self):
		return_string = "Farm : " + str(self.farm_name) + "\n"

		for current_animal in self.animal_list:

			return_string += current_animal.__str__() + "\n"

		return return_string


	def add_animal(self, my_type, my_sex, my_age=None):
		self.animal_list.append(Animal(my_type, my_sex, my_age))
		print("\t\t=>Farm.add_animal(" + str(my_type) + ", " + str(my_sex) + ", " + str(my_age) + ")")



	def pass_time(self, time_delta_to_advance):

		"""Advance time of the farm by time_delta_to_advance.
		Handle reproduction and retirement of animals.
		"""

		global future_farms_date

		for current_animal in self.animal_list:


			if(current_animal.want_reproduce() == True):

				print("\t\tAnimal " + str(current_animal.my_type) + "  wants to reproduce (" + str(current_animal.my_sex)
						+ " " + str((future_farms_date - current_animal.my_birthdate).days) + " days)")

				# We look for a male in the farm

				for searched_animal in self.animal_list:
					if (searched_animal.my_type == current_animal.my_type) and (searched_animal.my_sex == "Male") :

						print("\t\tPerfect match ! A baby was born !")

						self.add_animal(current_animal.my_type, random.choice(["Male", "Female"]), my_age=None)

						break


			if((future_farms_date - current_animal.my_birthdate).days > 3*365):
				self.animal_list.remove(current_animal)
				print("\t\tGoodby animal !!")



    def farm_factory(farm_name, animal_description):
    	my_current_farm = Farm(farm_name)

    	# for each animal in animal_description add it to the farm
    	for animal in animal_description:
            datetime = datetime.strptime(animal['birthdate'], '%b %d %Y')
            my_current_farm.add_animal(animal['type'], animal['sex'], datetime)

            return my_current_farm

    if __name__ == "__main__":

    	# Load JSON file into a variable
    	with open ('farm.json') as json_file:
    		data = json.load(json_file)
    		for p in data['animal list']:

    	with open ('farm.json', 'w') as outfile:
    		json.dump(data, outfile)

    	json.dumps(data, indent=4)

    	# Create farms list
    	farm_list = ["farmville", "farmcity", "farmland"]

    	# For each farm in JSON file, create it and add it to the farm list

    	for .....

    		farm_list.append(farm_factory(..., ...))


    	# The rest is the same as before.

    	# We print the list of farms (and animals)
    	for current_farm in farm_list:
    		print(current_farm)


    	# We start travelling to the future
    	print("\nWe start the time...:\n")

    	time_iteration = 0

    	while time_iteration < 100:

    		# Advance time of 28 days = 4 weeks
    		future_farms_date = current_farms_date + datetime.timedelta(days = 28)

    		print("\n\tAdvancing to : " + str(future_farms_date))

    		time_iteration += 1

    		for current_farm in farm_list:
    			current_farm.pass_time(datetime.timedelta(weeks = 4))


    		current_farms_date = future_farms_date

    	# We print the list of farms (and animals)
    	for current_farm in farm_list:
    		print(current_farm)
