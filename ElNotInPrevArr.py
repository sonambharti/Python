#print element which is not in list B.

A = [42, 48, 65, 45, 55, 87]
B = [ 65, 55, 87]

res = []

for el in A:
    if el not in B:
        res.append(el)
        
print(res)
