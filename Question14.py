lth = []
for i in range(100):  #100 iterations --> O(N)
    if i%3 == 0 or i%5==0:  #checking if the required condition is satisfied
        lth.append(i)
print(lth)
