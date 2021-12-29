def selection_sort(lst):
    
    for i in range(len(lst)):
        min = i
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                min = j
        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp


def main():
    lst = [5,3,6,1,7,3]
    print(lst)
    selection_sort(lst)
    print(lst)

if __name__ == "__main__":
    main()
