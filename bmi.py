def calculate_bmi (height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    # adding str() to add as string to string instead of string to int
    bmi = weight/(height**2)
    print (round(bmi, 3))
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
    elif bmi > 25.0:
        print("Over Weight")
calculate_bmi(weight=57, height=1.73)

