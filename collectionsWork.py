myTuples = [(2, 'b', 'world'), (3, 'c', '.'), (1, 'a', 'hello')]

result = sorted(myTuples, key=lambda x : x[1])
print(result)