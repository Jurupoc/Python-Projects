def merge(array):
    if len(array) == 1:
        return 0
    start = 0
    mid = len(array) // 2
    end = len(array)
    inv = 0
    inv1 = 0
    inv2 = 0
    left = array[start:mid]
    right = array[mid:end]
    top_left, top_right = 0, 0
    inv1 += merge(left)
    inv2 += merge(right)

    for x in range(start, end):
        if top_left >= len(left):
            array[x] = right[top_right]
            top_right = top_right + 1

        elif top_right >= len(right):
            array[x] = left[top_left]
            top_left = top_left + 1

        elif left[top_left] <= right[top_right]:
            array[x] = left[top_left]
            top_left = top_left + 1

        else:
            array[x] = right[top_right]
            top_right = top_right + 1
            inv += (len(left) - top_left)

    return inv + inv1 + inv2


N = int(input())
pregos = [int(x) for x in input().split()]

print(merge(pregos))