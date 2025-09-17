import numpy as np 

a = np.array([.6,.5,.6,.5,.5,.6,.5,.5,.5,.6,.5,.4,.4,.6])
b = np.array([6.6,6.7,6.6,6.9,7,6.9,6.9,7.5,6.6,6.9,6.9,6.8,6.4,7])

print(len(a))
print(len(b))
fac = 7.5
result = (a* b* fac).astype(int)

total=result.sum()


print("Result", result)
print("Total", total)   