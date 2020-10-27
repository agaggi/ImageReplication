import random
from PIL import Image, ImageDraw

'''Module contains methods that assist in the reproduction / creation process.'''

def color_gen():

    '''Generates random primary color values and transparency which are used as a triangles color.'''

    # Primary colors & how transparent a triangle will be
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a = random.randint(95, 115)

    return r, g, b, a


def coord_gen():

    '''Generates random coordinates which serves as a triangles size.'''

    # Triangle coordinates
    x1 = random.randint(0, 255)
    y1 = random.randint(0, 255)
    x2 = random.randint(0, 255)
    y2 = random.randint(0, 255)
    x3 = random.randint(0, 255)
    y3 = random.randint(0, 255)

    return (x1, y1), (x2, y2), (x3, y3)


def init_draw(children):

    '''Draws the initial population with their respective triangles.'''

    new_children = []

    for child in children:

        triangles = []
        new_image = ImageDraw.Draw(child, 'RGBA')

        # Value within range represents number of triangles there will be
        for j in range(256):

            r, g, b, a = color_gen()
            coord1, coord2, coord3 = coord_gen()

            new_image.polygon([coord1, coord2, coord3], fill=(r, g, b, a))
            triangles.append([[coord1, coord2, coord3], [r, g, b, a]])

        new_children.append([child, triangles])

    return new_children


def mutate_coords(coords, mutation_rate):

    '''Mutates coordinates if the mutation rate is greater than the random value.'''

    if mutation_rate > random.random():

        new_x1 = max(0, min(255, coords[0][0] + random.randint(-20, 20)))
        new_y1 = max(0, min(255, coords[0][1] + random.randint(-20, 20)))
        new_x2 = max(0, min(255, coords[1][0] + random.randint(-20, 20)))
        new_y2 = max(0, min(255, coords[1][1] + random.randint(-20, 20)))
        new_x3 = max(0, min(255, coords[2][0] + random.randint(-20, 20)))
        new_y3 = max(0, min(255, coords[2][1] + random.randint(-20, 20)))

        return (new_x1, new_y1), (new_x2, new_y2), (new_x3, new_y3)
    
    else:

        return coords


def mutate_color(colors, mutation_rate):

    '''Mutates color and transparency if the mutation rate is greater than the random value.'''
    
    if mutation_rate > random.random():

        new_r = max(0, min(colors[0] + random.randint(-10, 10), 255))
        new_g = max(0, min(colors[1] + random.randint(-10, 10), 255))
        new_b = max(0, min(colors[2] + random.randint(-10, 10), 255))
        new_a = max(95, min(colors[3] + random.randint(-5, 5), 115))

        return new_r, new_g, new_b, new_a
    
    else:

        return colors