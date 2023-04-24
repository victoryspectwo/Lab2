import statistics


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_mm():
    print("Enter some numbers separated by commas (e.g. 33, 34, 35.)")

def user_input():
    listnum = input("Enter numbers: ")
    listonums = listnum.split(",")
    float_list = [float(i) for i in listonums]
    print(float_list)
    return float_list #

display_mm()
float_l1st = user_input()
print(float_l1st)
def avg_temp(): #can use variables from main code boy but not from inside the function
    average = sum(float_l1st)/len(float_l1st)
    print("Average of the list =", round(average, 3))
    return average


avg_temp()

def min_max(float_l1st):
    highest = max(float_l1st)
    lowest = min(float_l1st)
    print("The highest temperature is " + str(highest) + " deg C and the lowest temperature is " + str(lowest) + " deg C")
    return highest, lowest

min_max(float_l1st)

#come back and add median temp later

def median(float_l1st):
    median_val = statistics.median(float_l1st)
    print("the median temperature is " + str(median_val))
    return median_val

median(float_l1st)





if __name__ == "__main__":
    main()








