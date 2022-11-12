class Zoo:
    total_count = 0
    __animals = total_count

    def __init__(self, name_of_the_zoo):
        self.name_of_the_zoo = name_of_the_zoo

        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name) :
        self.species = species
        self.name = name

        if self.species == 'mammal':
            self.mammals.append(name)
        elif self.species == 'fish':
            self.fishes.append(name)
        elif self.species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        this_list = []
        if species == "mammal":
            this_list = self.mammals
            species = "Mammals"
        elif species == "fish":
            this_list = self.fishes
            species = "Fishes"
        elif species == "bird":
            this_list = self.birds
            species = "Birds"
        return f"{species} in {self.name_of_the_zoo}: {', '.join(this_list)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
num_of_animals = int(input())
animal = Zoo(zoo_name)

for i in range(num_of_animals):
    species, name = input().split()
    animal.add_animal(species, name)

what_species = input()
print(animal.get_info(what_species))
