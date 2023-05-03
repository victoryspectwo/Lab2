def calculate_bmi (height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    # adding str() to add as string to string instead of string to int
    bmi = weight/(height**2)
    print (round(bmi, 3))
    if bmi < 18.5:
        print("Underweight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
        return 0
    elif bmi > 25.0:
        print("Over Weight")
        return 1

print ('Enter your height: ')
height = float(input())
print("Enter your weight: ")
weight = float(input())
result = calculate_bmi(height, weight)
print(result)


