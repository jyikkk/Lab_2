
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input().split(",")
    n = len(x)
    i = int(0)
    for i in range (0, n):
        x[i] = int(x[i])
        i += 1
    return x

def calc_average_temp(nl):
    x = nl
    n = len(x)
    i = int(0)
    y = float(0)
    for i in range (0, n):
        y += x[i] 
        i += 1
    y = float(y/n)
    return y

def max_temperature(nl):
    x = nl
    n = len(x)
    i = int(0)
    max = int(0)
    for i in range (0, n):
        if x[i] > max:
            max = x[i]
    return max

def min_temperature(nl):
    x = nl
    n = len(x)
    i = int(0)
    min = x[0]
    for i in range (0, n):
        if x[i] < min:
            min = x[i]
    return min

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("You provided: " + str(num_list))
    average = calc_average_temp(num_list)
    print("The average is: " + str(average))
    max = max_temperature(num_list)
    print("From the list, the largest number is: "+ str(max))
    min = min_temperature(num_list)
    print("and the lowest is: "+ str(min))
    

if __name__ == "__main__":
    main()