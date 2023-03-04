
#area of a right angled triangle


'''
area = (base * hight)/2
'''

# base = 10,
# height = 15

# area = (10 * 5) /2

# print(area)

# print("Area " +  str(area)) #concatinate -> combine stings

# print(f'Area {area}')

from math import sqrt
import random

# base = int( input("Enter base: ") )
# height = int( input("Enter height: "))


# hypotenues = sqrt((base*base) + (height*height))
# perimeter = base + height + hypotenues
# area = (base * height) /2

# print("Hypotenues: " + str(hypotenues))
# # print(f'{hypotenues:.2f}'
# print("Perimeter: " + str(perimeter))
# print("Area: " + str(area))


# def right_triangle():
#     base = int( input("Enter base: ") )
#     height = int( input("Enter height: "))

#     hypotenues = sqrt((base*base) + (height*height))
#     perimeter = base + height + hypotenues
#     area = (base * height) /2

#     print("Hypotenues: " + str(hypotenues))
#     # print(f'{hypotenues:.2f}'
#     print("Perimeter: " + str(perimeter))
#     print("Area: " + str(area))

# right_triangle()


def random_right_triangles():

    list_numbers = []

    times = int( input("Number of triangles: "))
    range_ = int( input("Triangles range: "))

    for t in range(times):
        for count in range(5):
            list_numbers.append(random.choice( [ num for num in range(range_) ] ))

        print("\n==========Triangle " + str(t+1) + '===========\n')
        base = random.choice(list_numbers)
        height = random.choice(list_numbers)

        hypotenues = sqrt((base*base) + (height*height))
        perimeter = base + height + hypotenues
        area = (base * height) /2

        print('Base: ' + str(base))
        print('Height: ' + str(height))
        print("\nHypotenues: " + str(hypotenues))
        print("Perimeter: " + str(perimeter))
        print("Area: " + str(area))



'''
ASSIGNMENT: 
    CIRCLE
        main.py -> function random_cirles()
            input = > number of circles
            input = > range how big the diameter and radius can be
            
            print(radius)
            print(diameter)
            print(circumfrence)
            print(area)

        circle.py -> call random_circles()

        run circle.py 
'''