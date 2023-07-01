arr = [1, 2, 3, 4]
sol = [1, 1, 1, 1]
sol2 = [1, 1, 1, 1]
pre = 1
post = 1
for i, n in enumerate(arr):
    sol[len(arr) - i - 1] *= post
    post *= arr[len(arr) - i - 1]

for i, n in enumerate(arr):
    sol2[i] *= pre
    pre *= n

print(sol)
print(sol2)