def selection_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while temp < lst[j] and j > -1:
            lst[j+1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst


def main():
    lst = [5,4,6,2,2,9]
    print(lst)
    print(selection_sort(lst))

if __name__ == "__main__":
    main()
