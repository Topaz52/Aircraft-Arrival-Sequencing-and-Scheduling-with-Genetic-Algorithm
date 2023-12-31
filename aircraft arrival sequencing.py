# -*- coding: utf-8 -*-
"""Aircraft Arrival Sequencing and Scheduling with Genetic Algorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_cGsUBnXosencag5aS7CPtXn77C0cd5e

Aircraft Arrival Sequencing and Scheduling with Genetic Algorithm

Step 1: Import necessary libraries
First, we need to import the necessary libraries. We will use numpy for numerical operations and random for generating random numbers.

Step 2: Define the problem
Let's assume we have a set of aircraft with different arrival times and required landing times. We want to find the optimal sequence of aircraft landings that minimizes the total deviation from the target landing times.

Step 3: Initialize the population
We will create an initial population of possible solutions (sequences of aircraft landings). Each individual in the population is a permutation of the aircraft indices.

Step 4: Define the fitness function
The fitness function calculates the total deviation from the target landing times for a given sequence of aircraft landings.

Step 5: Selection
We will use tournament selection to choose parents for crossover. In tournament selection, a random subset of individuals is chosen, and the best individual from this subset is selected as a parent.

Step 6: Crossover
We will use ordered crossover to create offspring from two parent individuals. Ordered crossover preserves the relative order of genes in the offspring.

Step 7: Mutation
We will use swap mutation to introduce small changes in the offspring. Swap mutation randomly selects two positions in the sequence and swaps their values.

Step 8: Main loop
Now, we will run the Genetic Algorithm for a fixed number of generations. In each generation, we will perform selection, crossover, and mutation to create a new population.

Step 9: Find the best solution
Finally, we will find the best solution in the final population and print the results.
"""

# Step 1
import numpy as np
import random

# Step 2 Define the problem
aircraft_arrival_times = [10, 20, 30, 40, 50]
target_landing_times = [25, 22, 57, 42, 52]

# Step 3 Initialize the population
def generate_individual(aircraft_arrival_times):
    return random.sample(range(len(aircraft_arrival_times)), len(aircraft_arrival_times))

def generate_population(size, aircraft_arrival_times):
    return [generate_individual(aircraft_arrival_times) for _ in range(size)]

population_size = 100
population = generate_population(population_size, aircraft_arrival_times)

# Step 4 Define the fitness function
def fitness(individual, aircraft_arrival_times, target_landing_times):
    total_deviation = 0
    for i, aircraft_index in enumerate(individual):
        total_deviation += abs(target_landing_times[aircraft_index] - aircraft_arrival_times[i])
    return total_deviation

# Step 5 Selection
def tournament_selection(population, aircraft_arrival_times, target_landing_times, tournament_size):
    selected_indices = random.sample(range(len(population)), tournament_size)
    best_index = min(selected_indices, key=lambda i: fitness(population[i], aircraft_arrival_times, target_landing_times))
    return population[best_index]

# step 6 Crossover
def ordered_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    available_genes = [gene for gene in parent2 if gene not in child[start:end]]
    for i in range(size):
        if child[i] is None:
            child[i] = available_genes.pop(0)
    return child

# Step 7 Mutation
def swap_mutation(individual):
    size = len(individual)
    i, j = random.sample(range(size), 2)
    individual[i], individual[j] = individual[j], individual[i]

# Step 8 Main loop
generations = 1000
mutation_rate = 0.2
tournament_size = 10

for _ in range(generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1 = tournament_selection(population, aircraft_arrival_times, target_landing_times, tournament_size)
        parent2 = tournament_selection(population, aircraft_arrival_times, target_landing_times, tournament_size)
        child = ordered_crossover(parent1, parent2)
        if random.random() < mutation_rate:
            swap_mutation(child)
        new_population.append(child)
    new_population.append(population[population.index(min(population, key=lambda ind: fitness(ind, aircraft_arrival_times, target_landing_times)))])
    population = new_population
    print(population)

# Step 9 Find the best solution
best_individual = min(population, key=lambda ind: fitness(ind, aircraft_arrival_times, target_landing_times))
best_fitness = fitness(best_individual, aircraft_arrival_times, target_landing_times)

print("Best individual:", best_individual)
print("Best fitness:", best_fitness)