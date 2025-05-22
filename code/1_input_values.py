# in this program, we will define the input values for the project
# Define the input values
# Author: Stephen Kerr

# promopt the user for the input values
def get_temperature():
    # get the temperature from the user
    temperature = input("Enter the temperature in degrees Celsius: ")
    return temperature

def concentration():
    # get the concentration from the user
    concentration = input("Enter the concentration in mol/L: ")
    return concentration

def get_volume():
    # get the volume from the user
    volume = input("Enter the volume in L: ")
    return volume

if __name__ == "__main__":
    # get the input values from the user
    temperature = get_temperature()
    concentration_a = concentration()
    volume_a = get_volume()
    concentration_b = concentration()
    volume_b = get_volume()

    # print the input values
    print("Temperature: ", temperature)
    print("Concentration A: ", concentration_a)
    print("Volume A: ", volume_a)
    print("Concentration B: ", concentration_b)
    print("Volume B: ", volume_b)