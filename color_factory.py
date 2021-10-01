import random

def getNonConsecutiveRepeatedColor(colors, compare_color, random_color):
    if compare_color == random_color:
        while compare_color == random_color:
            random_color = random.choice(colors)
    return random_color

def colorFactory(n: int):
    colors = ('R', 'B', 'G', 'Y')
    factory = []
    
    for i in range(n):
        random_color = random.choice(colors)
        
        if i > 0:
            random_color = getNonConsecutiveRepeatedColor(colors, factory[i - 1], random_color)
        
        if i > 4:
            for j in range(len(factory)):
                last_two = factory[i-2:i]
                next_pair = factory[j-2:j]
                if j > 1 and next_pair == last_two:
                    random_color = getNonConsecutiveRepeatedColor(colors, factory[j], random_color)
                        
        factory.append(random_color)
    
    return factory

# INPUT:
#     - Set of available colors: [ RED, BLUE, GREEN, YELLOW ]
#     - Integer length: the expected output length - 12

# OUTPUT: An in order collection of colors
#     - [ RED, YELLOW, GREEN, BLUE, YELLOW, .... RED] - of length 12

# RESTRICTIONS:
#     - No repeated adjacent colors: [ RED, RED ]
#     - No repeated patterns of three: [ RED, GREEN, YELLOW, .... RED, GREEN, YELLOW ]

print(colorFactory(12))