# Lab in the Loop
Interesting concept from Nvidia around lab in the loop I want to explore it and document it here with research / references and maybe a simulated example

## Best Fit Project: Simulated Lab in the Loop

### Project - Optimise a Virtual Chemical Reaction
- Simulation of a lab optimising the yield by tuning experimental parameters presure, temperature, etc. 
- Objective: Use a feedback loop to optimize experimental parameters (like temperature T, concentrations [A],[B]) to maximize the reaction rate r.
    #### The loop will be
    1. choose parameter to optimise
    2. simulate the reaction
    3. evaluate the result (yield, cost)
    4. update parameters using optimization (bayesian optimization)
    5. repeat 

#### Tools used:
- Python (Libaries in requirements.txt), 
- GitHub,

#### Reaction Model 
Simple chemical reaction
$A + B -> C$

The rate of tis reaction is governed by **Rate Law**: 

$r = k .[A]^m .[B]^n$

Where:
- r = reaction rate
- [A],[B] = concentration of reactants
- m,n = reaction orders
- k = rate constant ($A.e^Ea/RT$) (Arrhenius Equation)

#### **Constants**
- Activation Energy Ea = 50000 J/mol
- Gas constant R = 8.314 J/mol K
- Pre-exponential factor A = 1 x10^7

#### **Variable to Optimise**
- Temperature T [300, 800] Kelvin
- Concentrations [A], [B] mol/L

#### **Reaction Orders**
- m = 1, n = 1 (simple case)

#### Loop Plan
1. Choose Values for T, [A], and [B]
2. Compute k using Arrhenius equation
3. Compute reaction rate r = k.[A].[B]
4. Use an optimization strategy to update parameters and try again.

