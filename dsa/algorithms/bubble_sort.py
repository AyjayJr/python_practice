def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list [j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


def main():
    l = [5,3,6,1,7,3]
    print(bubble_sort(l))

if __name__ == "__main__":
    main()
