import pygame, sys, time, random
from pygame.locals import *
from GAengine import GAEngine

simulator_speed = 10

# add colors as needed...
red_color = pygame.Color(255, 0, 0)
green_color = pygame.Color(0, 255, 0)
blue_color = pygame.Color(0, 0, 255)
black_color = pygame.Color(0, 0, 0)
white_color = pygame.Color(255, 255, 255)

pygame.init()
fps_clock = pygame.time.Clock()

play_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Assignment 4 - DTE2501')

# initialize engine - you can experiment with different values for the population and food
ga = GAEngine()
ga.make_initial_population(100)
ga.add_food(1)

running = True
import time

start = time.time()
foods_eaten = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                running = False

    # make your calls to GAEngine here...
    

    ga.assign_fitness()
    # ca 60 % of population to do crossover
    no_of_crossover = int(0.6 * len(ga.get_population()))
    ga.do_crossover(no_of_crossover)
    
    # Hihg number of mutations keeps the "flock" moving faster
    no_of_mutation = 20
    for i in range(no_of_mutation):
        index = random.randint(0, len(ga.get_population())-1)
        ga.get_population()[index].mutate()
    
    
    

    play_surface.fill(white_color)
    for pp in ga.get_population():
        pygame.draw.rect(play_surface, black_color, Rect(pp.x_pos - 1, pp.y_pos - 1, 22, 22))
        pygame.draw.rect(play_surface, green_color, Rect(pp.x_pos, pp.y_pos, 20, 20))
    for food in ga.get_foods():
        food_size = food.get_amount() / 100 * 40
        pygame.draw.rect(play_surface, red_color, Rect(food.x_pos - food_size / 2, food.y_pos - food_size / 2, food_size, food_size))
        
        # Eating the food
        for pp in ga.get_population():
            dist = pp.get_distance_to(food)
            if dist < 20:
                food.reduce_amount()
                food_size = food.get_amount() / 100 * 40
                pygame.draw.rect(play_surface, red_color, Rect(food.x_pos - food_size / 2, food.y_pos - food_size / 2, food_size, food_size))
            #If food is eaten, reposition the food
            if food.get_amount() == 0:
                foods_eaten += 1
                food.reposition()
                food_size = food.get_amount() / 100 * 40
                pygame.draw.rect(play_surface, red_color, Rect(food.x_pos - food_size / 2, food.y_pos - food_size / 2, food_size, food_size))
            
        
    
        pygame.display.flip()

    fps_clock.tick(simulator_speed)

end = time.time()
duration = end - start

print("Foods eaten {} in {} time".format(foods_eaten, duration))
