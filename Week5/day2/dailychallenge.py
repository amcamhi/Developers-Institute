import random


class Gene():
    def __init__(self):
        self.value = random.choice([True, False])  # True = 1, False = 0

    def mutate(self):
        self.value = not self.value

    def __repr__(self):
        return "1" if self.value else "0"


class Chromosome():
    def __init__(self):
        self.value = [Gene() for i in range(10)]

    def mutate(self):
        for gene in self.value:
            if random.choice([True, False]):
                gene.mutate()

    def __repr__(self):
        return str(self.value)


class DNA():
    def __init__(self):
        self.value = [Chromosome() for i in range(10)]

    def mutate(self):
        for chromosome in self.value:
            if random.choice([True, False]):
                chromosome.mutate()

    def __repr__(self):
        return str(self.value)


class Organism():
    def __init__(self, dna, probability_to_mutate):
        self.dna = dna
        self.probability_to_mutate = probability_to_mutate

    def mutate(self):
        if random.random() <= self.probability_to_mutate:
            self.dna.mutate()

    def __repr__(self):
        return str(self.dna)


class Evolution():
    def __init__(self, num_of_organisms):
        self.population = [Organism(DNA(), 0.8)
                           for i in range(num_of_organisms)]
        self.generations = 0

    def is_complete(self):
        for organism in self.population:

    def big_bang(self):
        for organism in self.population:
            organism.mutate()
