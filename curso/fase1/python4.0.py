from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['Joan', ' Peter', 'John', 'Lety']

camisetas = [['green', 'blue',],
         ['masculine', 'female', 'unknown'],
         ['short', 'medium', 'tall'],
         ['algodão', 'poliester']               
         ]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))

print_iter(product(*camisetas))