# in this program we will run the whole project 
# and test the optimization algorithm
# Author: Stephen Kerr


# import input_values
import input_values
# import calculate_k
import calculate_k
# import calculate_reaction_rate
import calculate_reaction_rate
# import optimization
import optimization


def main():
    # get input values from the user
    temperature = input_values.get_temperature()
    concentration_a = input_values.concentration()
    volume_a = input_values.get_volume()
    concentration_b = input_values.concentration()
    volume_b = input_values.get_volume()
    # calculate the rate constant k
    k = calculate_k.calculate_k(temperature)
    # calculate the reaction rate
    rate = calculate_reaction_rate.calculate_reaction_rate(k, concentration_a, volume_a, concentration_b, volume_b)
    # print the reaction rate
    print("The reaction rate is: ", rate)
    # run the optimization algorithm to find the optimal values of k, [A], and [B]
    optimal_values = optimization.optimize_reaction_rate(k, concentration_a, volume_a, concentration_b, volume_b)
    # print the optimal values of k, [A], and [B]
    print("The optimal values are:")
    print("k:", optimal_values[0])
    print("[A]:", optimal_values[1])
    print("[B]:", optimal_values[2])

if __name__ == "__main__":
    main()
# this program runs the whole project and tests the optimization algorithm