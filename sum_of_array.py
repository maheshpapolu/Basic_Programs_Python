def sum_of_arr(list_data):
    result = 0
    for i in list_data:
        result += i
    return result


if __name__ == '__main__':
    arr_sum = [12, 32, 34, 56, 64]
    n = len(arr_sum)
    ans = sum(arr_sum)
    answer = sum_of_arr(arr_sum)
    print("sum of the array is ", answer)
