# import numpy as np
# import re
import pathlib as pl
from pathlib import Path
from PIL import Image

# from PIL import Image


def solveA(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    space = input_data.splitlines()
    beams = set()
    beams.add(space[0].index('S'))
    splitting = 0
    for line in space[1:]:
        new_beams = set()
        for b in beams:
            if line[b] == '^':
                # assuming a) no adjacent splitters and b) no splitting of the edge
                new_beams.add(b-1)
                new_beams.add(b+1)
                splitting += 1
            else:
                new_beams.add(b)
        beams = new_beams
        
    output = splitting
        
    print("Answer Part 1:")
    print(output)


def make_christmas_tree(tree):
    # Create an image of the Christmas tree
    # Coloring: Green for the tree (0 within) black for the background (0 outside) and depending on the number of beams if even or odd we take red or yellow lights.
    height = len(tree)
    width = len(tree[0])
    
    # Create image with RGB mode, scale up for better visibility
    scale = 10  # Make each pixel 10x10 for better visibility
    img = Image.new('RGB', (width * scale, height * scale))
    
    # Create pixel data
    for y in range(height):
        for x in range(width):
            value = tree[y][x]
            if value == 0:
                color = (0, 100, 0)  # Dark green for tree body (0 values)
            elif value % 2 == 0:
                color = (255, 0, 0)  # Red lights for even beam counts
            else:
                color = (255, 255, 0)  # Yellow lights for odd beam counts
            
            # Fill the scaled pixel area
            for dy in range(scale):
                for dx in range(scale):
                    img.putpixel((x * scale + dx, y * scale + dy), color)
    
    # Save and show the image ( in folder of the script)
    img.save(Path(__file__).parent / f'christmas_tree_{hash(tuple(tree))}.png')
    print(f"Christmas tree saved as 'christmas_tree_{hash(tuple(tree))}.png'")
    
    try:
        img.show()  # This will open the image in default viewer
    except Exception as e:
        print(f"Could not open image automatically: {e}")
        print("You can manually open 'christmas_tree.png' to view the tree!")



def solveB(file_name):
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    space = input_data.splitlines()
    beams = [0]* len(space[0])
    beams[space[0].index('S')] = 1
    tree = [tuple(beams.copy())]
    for line in space[1:]:
        for index, char  in enumerate(line):
            if char == '^':
                beams[index-1] += beams[index]
                beams[index+1] += beams[index]
                beams[index] = 0
        tree.append(tuple(beams.copy()))
        
    output = sum(beams)


    print("Answer Part 2:")
    print(output)
    
    make_christmas_tree(tree)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
    solveB('test.txt')
