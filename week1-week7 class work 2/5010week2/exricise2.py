def functionBMI(weight,height):
    height_in_centimers = height /100
    BMi = weight / height_in_centimers ** 2

    return BMi

weight = float(input("Enter the weight"))
height = float(input("Enter the height"))

print(functionBMI(weight,height))





