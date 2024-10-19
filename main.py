print("Hello")
input("> ")

name = input()

int(1,2,3,4)
float(0.3,9.5)
str("string")
bool(True, False)

students = ["Yasha", "Sasha"]
students.append("Dima")
students.remove("Dima")

students = {"Yasha": 
					["0506666666", "068777777"], 
			"Sasha": 
					["0506666666", "068777777"]
			}

if name == "Yasha":
	print("Ok")
elif name != "Sasha":
	print("Ok")
else:
	print("No")
#####################################
students = ["Yasha", "Sasha"]

if "Dima" not in students or "Grisha" in student:
	print("True")
else:
	print("Error")


marshutka = 0

while marshutka<=5:
	marshutka = marshutka + 1
	print(marshutka)

for i in range(1,6):
	print(i)