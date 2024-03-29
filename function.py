import math


def print_lyrics():
    print('Я дровосек, и со мной все в порядке.')
    print('Я работал весь день, и теперь я в достатке.')


# print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()


# repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)


# print_twice('Spam')
# print_twice(365)
# print_twice(math.pi)
# print_twice('Nurlan ' * 3)
# print_twice(math.cos(math.pi))

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


line1 = "Тили-тили"
line2 = " трали-вали"


# print(cat_twice(line1, line2))

# Находим площадь круга
def area(radius):
    a = math.pi * radius ** 2
    return a

# print(a)
print(round(area(6778)))
