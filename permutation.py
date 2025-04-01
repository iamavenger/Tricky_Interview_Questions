def permutation(arr, chosen = [], all = []) -> list:
    if len(arr) == 0:
        all.append(chosen)

    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i+1:]
        permutation(new_arr, chosen + [arr[i]])
    return all

