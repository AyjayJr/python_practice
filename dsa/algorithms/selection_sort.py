def selection_sort(lst):
    
    for i in range(len(lst) - 1):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        if i != min:
            temp = lst[i]
            lst[i] = lst[min]
            lst[min] = temp
    return lst


def main():
    lst = [5,3,6,1,7,3]
    print(lst)
    print(selection_sort(lst))

if __name__ == "__main__":
    main()
