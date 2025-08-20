import numpy as np 

a = np.array([9.2,9,8.8,9.5,8.2,8.3,8,7.7,8.7,8.5,8.2,8.4])
b = np.array([1.4,1.3,1.2,1.7,.9,1.2,1.2,1.1,1.2,1.5,2.2,1.6,2.1])

print(len(a))
print(len(b))
fac = 7.5
result = (a* b* fac).astype(int)

total=result.sum()


print("Result", result)
print("Total", total)