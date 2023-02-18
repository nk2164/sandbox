# insertion sort algorithm in python

size = int(input("Enter the size of the list: "))
list = []
for i in range(size):
    list.append(int(input("Enter the element: ")))
for i in range(1, size):
    temp = list[i]
    j = i - 1
    while j >= 0 and temp < list[j]:
        list[j+1] = list[j]
        j = j - 1
    list[j+1] = temp
print("Sorted list is: ", list)
