# Genetic-Algorithm-Knapsack
Implementation of Genetic Algorithm to solve the 0-1 Knapsack Problem.

# Problem
The Knapsack problem is a well-known optimization problem in computer science. It involves finding the maximum value of items that can be packed into a knapsack with a limited weight capacity.
E.g. :    
  
Input: N = 3, W = 4   
profit[] = {1, 2, 3}   
weight[] = {4, 5, 1}  
Output: 3   

# Input  

K (knapsack’s capacity)   
n (no. of Item)   
W1, W2, W3, .... Wn (Each Weight in a new Line)  
V1, V2, V3, …...Vn (Each Value in a new line)   

# Output  

P (total possible maximum value)   
[1, 0, 0, … n] (i th item considered or not)

# The Code
## Encoding
The solution is encodes as a binary string consisting of 0's and 1's. A 1 at ith postition represents that the ith item is considered. Conversely a 0 represents its absence.
This makes up the genotype of any individual in the population.

## Generate Random Population
https://github.com/shrinha/Genetic-Algorithm-Knapsack/blob/7048b5bc2cfda8fd283b6989ed85e12d926fd2d0/Genetic%20Algorithm_Knapsack.py#L3-L11

## Fitness Function
The function calculates how good an indiviual is by calculating the value of that solution. However, if weight exceeds the capacity of the knapsack, its fitness is set to 0 as 
the solution becomes infeasible.
https://github.com/shrinha/Genetic-Algorithm-Knapsack/blob/7048b5bc2cfda8fd283b6989ed85e12d926fd2d0/Genetic%20Algorithm_Knapsack.py#L14-L24

## Selection
Calculates the fitness of entire population, normalises it and then selects two parents from it with the probability proportional to their fitness value. 
https://github.com/shrinha/Genetic-Algorithm-Knapsack/blob/7048b5bc2cfda8fd283b6989ed85e12d926fd2d0/Genetic%20Algorithm_Knapsack.py#L26-L37

## Crossover 
Generates children from the parent by selecting a random index of the binary string and crossing strings
https://github.com/shrinha/Genetic-Algorithm-Knapsack/blob/7048b5bc2cfda8fd283b6989ed85e12d926fd2d0/Genetic%20Algorithm_Knapsack.py#L26-L37

## Mutation
Mutates the string by flipping a random bit in the binary string
https://github.com/shrinha/Genetic-Algorithm-Knapsack/blob/7048b5bc2cfda8fd283b6989ed85e12d926fd2d0/Genetic%20Algorithm_Knapsack.py#L47-L52

## Subsequent Generations
The entire process turns for given number of generations. Each Generation consists of Selection of parents, Crossover with probability uc, and mmutation with probability um.
The children are then added to the population pool. Once this process finishes, the best individual is selected from the final population.
https://github.com/shrinha/Genetic-Algorithm-Knapsack/blob/7048b5bc2cfda8fd283b6989ed85e12d926fd2d0/Genetic%20Algorithm_Knapsack.py#L92-L103 

