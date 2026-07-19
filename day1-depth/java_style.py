numbers = []

file = open("numbers.txt", "r")

while True:
    line = file.readline()

    if line == "":
        break

    line = line.strip()
    number = int(line)
    numbers.append(number)

file.close()

print(numbers)