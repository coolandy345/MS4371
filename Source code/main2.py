import time
source = [0,2,3,1,4,5] * 1000000
lookup_table = [11,22,33,44,55,66]
result = []
start = time.time()
for element in source:
    transformed_value = lookup_table[element]
    result.append(transformed_value)
end = time.time()
print(result[:5]) # [11,33,44,22,55]
print(end - start) # ~2.5 seconds