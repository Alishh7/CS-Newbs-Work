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
