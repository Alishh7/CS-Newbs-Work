# Ammar
# Could save more lines of code if you put Pi in the sub program
input("Which shape volume? (cube, cuboid, cylinder, square_pyramid, sphere) ")
# Poor grammar lol
if input == ("cube"):
    def cube_volume(length):
        volume = length * length * length
        return volume
    answer1 = cube_volume(4)
    print (answer1)
# your good is a bit too long cut it down to make it look smaller








#perimiter
def circle_perimiter(diameter):
    pi = 3.142
    perimiter = pi * diameter
    return perimiter

answer = circle_perimiter(4)

print(answer)

#area
def circle_area(diameter):
    radius = (diameter / 2)
    pi = 3.142
    area = pi * radius * radius
    return area

answer = circle_area(4)

print(answer)

#cube volume
def cube_volume(length):
    volume = length * length * length
    return volume

answer1 = cube_volume(4)
print (answer1)

#cuboid volume
def cuboid_volume(length, width, height):
    volume = length * width * height
    return volume

answer2 = cuboid_volume(4, 4, 2)
print(answer2)

#cylinder volume
def cylinder_volume(height, radius):
    pi = 3.142
    volume = pi * radius * radius * height
    return volume

answer3 = cylinder_volume(10, 4)
print(answer3)

#square pyramid volume
def pyramid_volume(base, height):
    volume = base * base * height * (1/3)
    return volume

answer4 = pyramid_volume(4, 10)
print (answer4)

#sphere_volume
def sphere_volume(radius):
    pi = 3.142
    volume = radius * radius * radius * pi * (4/3)
    return volume

answer5 = sphere_volume(4)
print(answer5)
    
