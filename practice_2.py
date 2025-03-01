weight = int(input('weight: '))
unit = input("(k)g or (l)bs: ")
if unit == "k":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))
elif unit == "l":
    converted = weight * 0.45
    print("weight in kilograms: " + str(converted))
