def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print ("Bmi = "+ str(bmi))
    if bmi < 18.5:
        print("you are underweighttttt")
    if bmi > 18.5 and bmi < 25:
        print("you are normalweightttt YAH")
    if bmi > 25:
        print("you are overweighttt ?????")

calculate_bmi(1.76, 58.5)

