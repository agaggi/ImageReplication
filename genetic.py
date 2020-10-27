import os, glob
import gc
import random

import triangle as t
from PIL import Image, ImageDraw

class GeneticAlgorithm:

    '''Class contains methods that are used for recreating an image with triangles.'''

    def __init__(self, image, population, mode):

        self.generation = 0
        self.parents = []

        self.population = population
        self.image = Image.open(image).resize((256, 256))       # Resize image to 256x256
        self.mode = mode.lower()


    def get_fitness(self, children):

        '''Takes in a list of children and compares each child to the original image.

        `children`: A list of children in the form of [image, triangles within image]
        
        A list of children is passed in and run through a for-loop for n number of times;
        n being how ever many children are in the list. For every child, each pixel is
        compared to the respective pixel in the original image, and the difference is
        calculated. After all pixels have been compared, the total difference is stored
        in a new list, along with the image and its triangles. After all iterations, the
        new list is returned.
        '''

        # For every image in the list, go through its pixel values and compare to original
        for child in children:

            difference = 0

            for i in range(256):

                for j in range(256):

                    r, g, b = child[0].getpixel((i, j))
                    r2, g2, b2 = self.image.getpixel((i, j))
                    
                    difference += abs(r2 - r) + abs(g2 - g) + abs(b2 - b)
            
            # List format: [image, triangles within image, difference]
            # difference will be used to sort the images to get the best
            child.append(difference)

        return children

    
    def keyFunc(self, child):

        '''A function to be used when sorting the children by least difference.
        
        `child`: [image, triangles within image, difference]
        '''

        return child[2]


    def selection(self, children):

        '''Selects the best image(s) to be used in reproduction.

        `children`: [image, triangles within image]
        
        The fitness function is used in order to obtain the list of children with their
        differences from the original image. The list is then sorted by `difference` by
        using `keyFunc`, which sorts by the first element in a child. In this case, it
        is `difference`. Then, depending on the reproduction method, the best image(s)
        and its triangles are selected to be the parent(s).
        '''

        # Sorting the list of children by difference using a key function
        children_list = self.get_fitness(children)
        children_list.sort(reverse=False, key=self.keyFunc)
        
        # Parent list format: [image, triangles within image]
        if self.mode == 'sexual':

            self.parents = [[children_list[0][0], children_list[0][1]],
                            [children_list[1][0], children_list[1][1]]]
        
        elif self.mode == 'asexual':

            self.parents = [[children_list[0][0], children_list[0][1]]]
        
        else:

            exit('\n-- Invalid reproductive method entered. --\n')

        # Every 100 generations, the best image of that generation is outputted
        if self.generation % 100 == 0:

            self.parents[0][0].save(os.path.join('images/', f'{self.generation}.jpg'))
            print(f'Fitness after {self.generation} generations: {children_list[0][2]}')

        # If the difference is 0 we are done
        if children_list[0][2] == 0:

            return True

        del(children_list)
        gc.collect()
        
        return False
  

    def crossover(self):

        '''Takes a random number of triangles from parent 1 and parent 2 and creates `n`
        amount of children.
        
            parent1_inherit = random.randint(1, len(parent1))
            parent2_inherit = len(parent1) - parent1_inherit
        
        After it has been decided how many triangles of each parent will be draw on a new
        blank image, there will be a chance for coordinates and color to mutate 
        respectively. Then the new triangles are appended with the child image to a new
        list that is returned.
        '''

        offspring = [(Image.new('RGB', size=(256, 256))) for _ in range(self.population)]

        mutation_rate = 0.05
        new_gen = []

        parent1, parent2 = self.parents[0][1], self.parents[1][1]
        
        for child in offspring:

            triangles = []
            new_image = ImageDraw.Draw(child, 'RGBA')

            parent1_inherit = random.randint(1, len(parent1))
            parent2_inherit = len(parent1) - parent1_inherit
            
            for j in range(parent1_inherit):

                coord1, coord2, coord3 = t.mutate_coords(parent1[j][0], mutation_rate)
                r, g, b, a = t.mutate_color(parent1[j][1], mutation_rate)

                new_image.polygon([coord1, coord2, coord3], fill=(r, g, b, a))
                triangles.append([[coord1, coord2, coord3], [r, g, b, a]])

            for j in range(parent2_inherit):

                coord1, coord2, coord3 = t.mutate_coords(parent2[j][0], mutation_rate)
                r, g, b, a = t.mutate_color(parent2[j][1], mutation_rate)

                new_image.polygon([coord1, coord2, coord3], fill=(r, g, b, a))
                triangles.append([[coord1, coord2, coord3], [r, g, b, a]])
            
            new_gen.append([child, triangles])

        self.generation += 1
        
        del(self.parents[:])
        del(triangles)
        del(offspring)
        del(parent1)
        del(parent2)

        gc.collect()
        
        return new_gen


    def asexual(self):

        '''The best parent of each generation reproduces, creating `n` new children.
        
        New images are created and inherit triangles from the parent, but there will be a
        chance for coordinates and color to mutate respectively. Then the new triangles
        are appended with the child image to a new list that is returned.
        '''

        offspring = [(Image.new('RGB', size=(256, 256))) for _ in range(self.population)]

        mutation_rate = 0.05
        new_gen = []

        parent = self.parents[0][1]

        for child in offspring:

            triangles = []
            new_image = ImageDraw.Draw(child, 'RGBA')

            for i in range(len(parent)):

                coord1, coord2, coord3 = t.mutate_coords(parent[i][0], mutation_rate)
                r, g, b, a = t.mutate_color(parent[i][1], mutation_rate)

                new_image.polygon([coord1, coord2, coord3], fill=(r, g, b, a))
                triangles.append([[coord1, coord2, coord3], [r, g, b, a]])
            
            new_gen.append([child, triangles])
        
        self.generation += 1

        del(self.parents[:])
        del(triangles)
        del(offspring)
        del(parent)

        gc.collect()
        
        return new_gen