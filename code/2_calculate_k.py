# In this program we will calculate the value of k using the input values
# and the formula k = k = rate constant (A.eEa/RT) (Arrhenius Equation)

# import the math module
import math

def calculate_k(temperature):
    # calculate the value of k using the Arrhenius equation
    # k = A.eEa/RT
    # where A is the pre-exponential factor, Ea is the activation energy,
    # R is the universal gas constant, and T is the temperature in Kelvin
    # convert the temperature from Celsius to Kelvin
    temperature = temperature + 273.15
    # define the universal gas constant unit J/(mol.K)
    R = 8.314
    # define the pre-exponential factor unit mol/(L.s)
    A = 1.0e7
    # define the activation energy unit J/mol
    Ea = 50000
    # calculate the value of k
    k = A * math.exp(-Ea / (R * temperature))
    return k

if __name__ == "__main__":
    # get the temperature from the user
    temperature = float(input("Enter the temperature in degrees Celsius: "))
    # calculate the value of k
    k = calculate_k(temperature)
    # print the value of k
    print("The value of k is: ", k)