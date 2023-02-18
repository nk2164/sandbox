# selection sort in python
size = int(input("Enter the size of the list: "))
list = []
for i in range(size):
    list.append(int(input("Enter the element: ")))  
for i in range(size):
    min = i
    for j in range(i+1, size):
        if list[min] > list[j]:
            min = j
    list[i], list[min] = list[min], list[i]
print("Sorted list is: ", list)

