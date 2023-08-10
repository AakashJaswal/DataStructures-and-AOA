arr = [1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1, 1, 2, 2, 0, 0, 0]

l, m, h = 0, 0, len(arr) - 1

while m <= h:
    match arr[m]:
        case 0:
            arr[m], arr[l] = arr[l], arr[m]
            m += 1
            l += 1
        case 1:
            m += 1
        case 2:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1

print(arr)

# 0 -> low - 1 low -> mid - 1 mid -> high high + 1 -> n - 1
#   0               1         Unsorted              2
