with open("input.txt", 'r') as f:
    text = f.read().split('\n')
    safeCount = 0
    for row in text:
        arr = list(map(int, row.split()))
        isIncreasing = arr[0] < arr[1]
        for j in range(len(arr) - 1):
            if ((arr[j + 1] > arr[j]) != isIncreasing):
                break
            if (abs(arr[j + 1] - arr[j]) > 3):
                break
            if arr[j + 1] == arr[j]:
                break

        else:
            safeCount += 1

    print(safeCount)