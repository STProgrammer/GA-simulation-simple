import math, random

# base class for simulator
class GAPoint:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    # find the distance to another object
    def get_distance_to(self, other):
        return math.sqrt(math.pow(self.x_pos - other.x_pos, 2) + math.pow(self.y_pos - other.y_pos, 2))


class Chromosome(GAPoint):
    # x_pos and y_pos are the features of our chromosome
    def __init__(self, x_pos, y_pos):
        self.fitness = 0
        super().__init__(x_pos, y_pos)

    # encode X-Y position into low-level representation
    # we convert them to list of binary numbers representing the value
    # for easier manipulation
    def encode_position(self):
        self.x_pos = list(bin(self.x_pos))
        self.y_pos = list(bin(self.y_pos))
        return
    
    # decode X-Y position from low-level representation
    def decode_position(self):
        self.x_pos = int("".join(self.x_pos), 2)
        self.y_pos = int("".join(self.y_pos), 2)
        return

    # produce a new offspring from 2 parents
    def crossover(self, other):
        # Taking the mean causes all chromosomes to be flocked at a centrum (since each
        # offspring in the center of the parents).  So when the food is placed
        # at the edge, it takes long time for chromosomes to eat that food. 
        # Thus I use random values that's a between parent values +/- 30, so it's not always at the center.
        # The reason I add +/- 30 is to not always position offspring betwen parents. It is to
        # Make more variation, so foods on corner get eaten faster.I didn't use 
        # binary operations because the variation of position could be too much
        x_pos = random.randint(min(self.x_pos, other.x_pos)-30, max(self.x_pos, other.x_pos)+30)
        y_pos = random.randint(min(self.y_pos, other.y_pos)-30, max(self.y_pos, other.y_pos)+30)
        
        # Since we have +/- 30 we need to make sure it's not off the pane
        x_pos = 0 if x_pos < 0 else x_pos
        x_pos = 800 if x_pos > 800 else x_pos
        y_pos = 0 if y_pos < 0 else y_pos
        y_pos = 600 if y_pos > 600 else y_pos
        
        offspring = Chromosome(x_pos, y_pos)
        return offspring

    # mutate the individual
    def mutate(self):
        # I tried both "random bit flipping" and uniform random that has same 
        # limits as the stage size. In my experience "uniform random" is 
        # performing better than ranodm bit flipping, that is because
        # the variation is bigger with uniform random than bit flipping. 
        # (That may be because different integers have different sizes, 
        # flipping one bit on them may not make a very big difference).
        # Higher variance causes the chromosomes be more spread out and 
        # to move faster to the food source. Since the position of food 
        # varies a lot, I want variance in the population with mutation. 
        # And this gives more variance than just flipping a bit. Uniform 
        # random is how foods a randomly positioned, so the chromosomes 
        # moves faster with uniform random.
        self.x_pos = random.randint(0, 800)
        self.y_pos = random.randint(0, 600)
        
        # THE BIT FLIP METHOD, FLIPPING RANDOM BIT
        # self.encode_position()
        # # Get random index of binary string (excluding 'b0')
        # x_i = random.randint(2, len(self.x_pos)-1)
        # y_i = random.randint(2, len(self.y_pos)-1)
        # # flip random bit in the string
        # self.x_pos[x_i] = '0' if self.x_pos[x_i] == '1' else '1'
        # self.y_pos[y_i] = '0' if self.y_pos[y_i] == '1' else '1'
        # self.decode_position()
        return


class Food(GAPoint):
    def __init__(self, x_pos, y_pos):
        self.amount = 100
        super().__init__(x_pos, y_pos)

    def reduce_amount(self):
        self.amount -= 1

    def get_amount(self):
        return self.amount

    # respawn food when depleted
    def reposition(self):
        self.amount = 100
        self.x_pos = random.randint(10, 790)
        self.y_pos = random.randint(10, 590)