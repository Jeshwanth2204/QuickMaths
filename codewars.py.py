def better_than_average(*class_points, your_points):
    average = sum(class_points)/len(*class_points)
    if average < your_points:
        return True
    else:
        return False

class_points = 80, 70, 90, 85, 75
your_points = 88
result = better_than_average(*class_points, your_points)
print(result)  # Output: True
