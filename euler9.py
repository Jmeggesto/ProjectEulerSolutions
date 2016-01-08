pythagorean_triples = []
for x in range(1, 1001):
    y = x+1
    z = y+1
    while z <= 1000:
        while z * z < x * x + y * y:
            z = z + 1
        
        if z * z == x * x + y * y and z <= 1001:

            pythagorean_triples.append((x, y, z))

            
        
        y = y + 1
    

special_triple = [tup for tup in pythagorean_triples if sum(tup) == 1000][0]
product = reduce(lambda x, y: x*y, special_triple)
print(product)
