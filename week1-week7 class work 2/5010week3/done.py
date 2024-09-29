def wavelength_to_color(wavelength):
    if 620 <= wavelength <= 750:
        return "Red"
    elif 590 <= wavelength < 620:
        return "Orange"
    elif 570 <= wavelength < 590:
        return "Yellow"
    elif 495 <= wavelength < 570:
        return "Green"
    elif 450 <= wavelength < 495:
        return "Blue"
    elif 380 <= wavelength < 450:
        return "Violet"
    else:
        return None

def main():
    print("Welcome to wavelength to colour converter")
    try:
        wavelength = int(input("Please enter an integer wavelength between 380 and 750: "))
        color = wavelength_to_color(wavelength)
        if color:
            print(f"Thank you, the wavelength that you entered in nanometres is {wavelength}")
            print(f"The colour for this wavelength is... {color}")
        else:
            print(f"The wavelength {wavelength} is outside of the visible spectrum.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
