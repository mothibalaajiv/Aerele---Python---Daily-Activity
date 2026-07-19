file = open("numbers.txt" ,"r")
numbers = [int(line.strip()) for line in file]
file.close()
print(numbers)