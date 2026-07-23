# Tuple

# b = ("khan", 3, 87, "matloob")
# print(b[0])

# a = "kha", 5, 8
# print(type(a))

# c = "matloob",
# print(type(c))
# print(b[3:])

# devil = ["Trump", "Netenyahu", "Macron", "Modi", "Epestein"]

# for i in devil:
#     print(i)

# i = 0
# while i< len(devil):
#     print(devil[i])
#     i +=1

# print(devil[::2])
# print(devil[::-1])

# Tuple convert to List

# A = ("samsung", "vivo", "iPhone", "honors")
# print(A)
# print("type of before", type(A))

# A = list(A)
# A.append("Redmi")
# print(A)
# print("After covert", type(A))
# A = tuple(A)
# print(A)
# print("final covert", type(A))
# import json
# data = {"name": "Mohammad", "age": 23, "marks": 87}
# print(data)
# print(type(data))
# student_data = json.dumps(data)
# print(student_data)
# print(type(student_data))
# data = """{"name": "Mohammad", "age": 23, "marks": 87}"""
# student_data = json.loads(data)
# print(student_data["age"])

# data = {"name": "Mohammad", "age": 23, "marks": 87}
# stData = json.dumps(data, indent=4, separators=(",", "="))
# print(stData)

# data = {"name": "Mohammad", "age": 23, "marks": 87}
# f = open("demo.json", "w")
# sData = json.dumps(data, indent=4, sort_keys=True)
# print(f.write(sData))

# for x in data.values():
#     print(x)
# for x in data.keys():
#     print(x)
# for x, y in data.items():
#     print(x,"=",y)

# student = {"name": "Matloob Khan", "Class": "7th", "makrs": 97, "roll_number": 4}
# xStudent = student.setdefault("roll_number", 25)
# print(xStudent)

# empployee ={1:{"name": "john", "age": 23},
#             2:{"name":"Saim", "age": 35},
#             3:{"name":"Kim", "age":45}}

# print(empployee[2].keys())
# print(empployee[2].values())

# a = {"a": 12, "c": 23, "d": 54, "e": 15, "f": 7 }
# a = sorted(a.values())
# print(a)
# a = sorted(a.keys())
# print(a)

ab = 12
d = ab
print(d)

c = d + ab
print(c)
