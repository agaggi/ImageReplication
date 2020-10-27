# Image Replication via Genetic Algorithm

## Program Requirements

- Python version 3.7+
- PIL

To install PIL (Python Imaging Library):

```bash
# Linux
pip3 install PIL

# Windows
pip install PIL
```

## Execution Instructions

The `main.py` file is the file specified to be run; attempting to run any other file will result in no output. The program should be run following this format:

```bash
# Linux
python3 main.py [image] [population size] [reproduction method] [crossover rate]

# Windows
py .\main.py [image] [population size] [reproduction method] [crossover rate]
```

### Arguements

1. Image - The following images are available:

    - `d.jpg` - An apple
    - `mona.jpg` - Mona Lisa
    - `chester.jpg` - My cat
        - This image is complex / detailed so it will be harder to get "good" results.
    - `black.jpg` - A pure black image

- Note that if you add your own image it **must** be in **.jpg** format, as that is how the results are saved / compared.
    
2. Population Size:

    - **<= 100** is recommended as the program will take a considerable amount of time if a greater population size is entered.
    - If the reproductive method you chose is `sexual`, your population size **must be at least** 2.

3. Reproductive Method:

| Arguement      | Reproduction Method    
| :------------: | :------------------: 
| `sexual`       | Sexual Reproduction   
| `asexual`      | Asexual Reproduction

4. Crossover Rate (sexual reproduction only):

    - A floating point value from **0** to **1**.

## Analysis

This program takes in an image, the number of images per generation, a reproductive method (i.e. *asexual* or *sexual*), as well as crossover rate if needed. Throughout the testing, each parameter was found to have a considerable impact on the functionality of the program. For example, when a population size of **2** is entered, over the course of the program, minor improvements will be made and the evolution process will be slow; it was very common for the fitness value to increase again.

- Fitness values in this program represent the pure difference between the target image and an image within a population. **Lower is better**.

- Note: 256 triangles were used throughout this program.

It should also be noted that images with less complexity (i.e. images of a solid color) run much faster. When running the **black.jpg** file, the fitness values decrease dramatically at first and then plateau at around a fitness value of **250000** (see how the image was ran below). Other images would also plateau around a particular fitness value. This could have likely been alleviated by adding more members to the population or more triangles; however, it would have taken much more time.

Two reproduction methods were used within this program: asexual and sexual. Of the two, asexual produced far better results than sexual reproduction. This was likely due to the fact that the best image was always chosen, not two parents, and the inherited triangles had the chance to be mutated. When running the program with a crossover rate of 100%, the results were not favorable; clusters of triangles of the same color would appear and would not reproduce properly. This was likely why crossover rate was a requirement for this program.

## Sample Images

For examples of how this program ran, see the `sample images` folder.

| Image         | Population Size | Reproduction Method    | Mutation Rate  
| :-----------: | :-------------: | :--------------------: | :-----------: 
| `d.jpg`       | 100             | Asexual                | 5% 
| `mona.jpg`    | 50              | Asexual                | 5% 
| `chester.jpg` | 100             | Asexual                | 5% 
| `black.jpg`   | 50              | Sexual (70% crossover) | 5%

## Citations

1. [Genetic Programming: Evolution of Mona Lisa](https://rogerjohansson.blog/2008/12/07/genetic-programming-evolution-of-mona-lisa/)
    - Author: Roger Johansson
    - Date Retreived: 10/16/20
    - This website served as inspiration for the project. No code was used from this source as there was none provided.

2. [Python - multi-triangle fitting image example based on genetic algorithm](https://www.cnblogs.com/yu-long/p/11974213.html)
    - Author: Yulong
    - Date Retreived: 10/16/20
    - This website explained and provided sample code for a project quite similar to this one. The mutation functions within my program were influenced by the author's implementation.
