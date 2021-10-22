import random
from Utils import Chromosome, Food

class GAEngine:
    
    def __init__(self):
        self.population = []
        self.food = []
        self.generations = 0

    def make_initial_population(self, population_size):       
        for i in range(population_size):
            self.population.append(Chromosome(random.randint(0, 790), random.randint(0, 590)))

    def add_food(self, no_of_food):     
        for i in range(no_of_food):
            self.food.append(Food(random.randint(0, 790), random.randint(0, 590)))

    # selection code goes here...
    def do_crossover(self, no_of_offspring):
        population_size = len(self.population)
        # Here we combine elitism selection with roulette wheel
        # We carry ca 40 % of the most fit over to the next generation.
        # Then we use roulette wheel because we want diversity too.
        # We want diversity because the foods are repositioned to different places.
        
        # Get the top ca 40 % fittest.
        rate_to_keep = 0.4
        keep_nr = int(population_size * rate_to_keep)
        self.population = sorted(self.population, key=lambda x: x.fitness)
        new_generation = self.population[-keep_nr:]
        
        # new_generation = list()

        # Then we make offsprings based on random choices with weights.
        # We raise the exponent fitness to 2 to make the differences more
        # Since we are using "roulette wheel" in selection, we want to increase the chance of
        # the most fit to be selected.
        fitness_values = [x.fitness**2 for x in self.population]
        for i in range(no_of_offspring):
            parent1, parent2 = random.choices(self.population, weights=fitness_values, k=2)
            offspring = parent1.crossover(parent2)
            new_generation.append(offspring)
        
        self.population = new_generation
        return
    
    
    # fitness calculation goes here...
    def assign_fitness(self):
        # Fitness is 987 substracted by distance to closest food
        # We want the chromosomes close to some food to survive, not close to all foods on average.
        nr_of_foods = len(self.food)
        for ch in self.population:
            distances = list()
            distances = [ch.get_distance_to(f) for f in self.food]
            # Max distance is ca 986, but we use 987 to avoid negative values.
            # Higher the distance, less the fitness score.
            ch.fitness = (987 - min(distances))
        return

    def get_population(self):
        return self.population

    def get_foods(self):
        return self.food