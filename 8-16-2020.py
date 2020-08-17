#instruct the user and collect input
print("Hello, this program will find the lowest positive integer that does not exist in the array.")
print("You will enter an array of numbers with spaces inbetween each number    Ex. 3 4 -1 1")
array = input("Enter the array: ")

# seperate user input into an array and remove values from zero down
splitArray = array.split(' ')
splitArray = [i for i in splitArray if i != ' ']
splitArray = [int(i, base=10) for i in splitArray]
splitArray = [i for i in splitArray if i > 0]

# search for the lowest number not in the array
j = 0
counter = 0
while True:
    counter = 0
    j = j + 1
    for k in range(len(splitArray)):
        if splitArray[k] != j:
            counter = counter + 1
    if counter == len(splitArray):
        print(j)
        break
