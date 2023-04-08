import random as r

def generate_population(size):
    population = []
    genes = [0, 1]	
    for i in range(size):
        chromosome = []
        for i in range(n):
            chromosome.append(r.choice(genes))
            population.append(chromosome)
    return population

    
def fitness(l):
    weight_sum=0
    value_sum=0
    for i in range(n):
        weight_sum+= l[i]*w[i]
        value_sum+= l[i]*v[i]
        
    if weight_sum>k:
        return 0
    else:
        return value_sum

def selection(p):
    fitness_values = []
    for chromosome in p:
        fitness_values.append(fitness(chromosome))
	
    fitness_values = [float(i)/sum(fitness_values) for i in fitness_values]

    selected=r.choices(p, weights=fitness_values, k=2)	
    parent1 = selected[0]
    parent2 = selected[1]
	
    return parent1, parent2
    

def crossover(parent1,parent2):
    point=r.randint(0,n-1)
    child1=parent1[0:point]+parent2[point:]
    child2=parent2[0:point]+parent1[point:]
    return child1,child2


def mutate(l):
    point=r.randint(0,n-1)
    if l[point]==0:
        l[point]=1
    else:
        l[point]=0

    return l    

def solution(p):
    fitness_values = []
    for chromosome in p:
        fitness_values.append(fitness(chromosome))

    max_value = max(fitness_values)
    max_index = fitness_values.index(max_value)
    return p[max_index]
    
    

k=int(input("Enter Knapsack's capactiy "))
n=int(input("Enter Number of items "))
w=list()
v=list()

print("Enter the weights")
for i in range(n):
    x=int(input())
    w.append(x)


print("Enter the values")
for i in range(n):
    x=int(input())
    v.append(x)



x=int(input("Number of Generations to run: "))
uc=0.8
um=0.2
    

population=generate_population(10)

for i in range(x):
    parent1,parent2=selection(population)
    if r.uniform(0,1)<uc:
        child1,child2=crossover(parent1,parent2)
    else:
        child1,child2=parent1,parent2
    
    if r.uniform(0,1)<um:
        child1=mutate(child1)
        child2=mutate(child2)
        
    population=[child1,child2] + population[2:]


ans=solution(population)

print("The solution is: ")
print(ans)
print("The Total values is:",fitness(ans))

    
    


    

