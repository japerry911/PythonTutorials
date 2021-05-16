file = open("sandbox2.csv", "r")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(",")
    name = person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree = person_data[3]

    print(f"{name.title()} is {age}, studying {degree.title()} at "
          f"{university.title()}.")


from csv import reader

file = open("sandbox2.csv", "r")

csv_reader = reader(file)
for line in csv_reader:
    print(line)

file.close()


