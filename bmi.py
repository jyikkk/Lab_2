def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print ("Bmi = "+ str(bmi))
    if bmi < 18.5:
        print("You are underweighttttt")
        return(-1)
    if bmi > 18.5 and bmi < 25:
        print("You are normalll YAAHH")
        return(0)
    if bmi > 25:
        print("You are overweightttt NOOOO")
        return(1)

calculate_bmi(1.76, 58.5)