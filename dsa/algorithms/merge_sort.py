def merge(l1, l2):
    l3 = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1

    while i < len(l1):
        l3.append(l1[i])
        i += 1

    while j < len(l2):
        l3.append(l2[j])
        j += 1

    return l3

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def main():
    l = [5,3,7,6,2,1,9]
    print(merge_sort(l))

if __name__ == "__main__":
    main()
