def mystery_doors(num_students):
    doors = []
    for n in range(num_students):
        doors.append(False)
    for stu in range(num_students):
        for d in range(stu, num_students, stu+1):
            doors[d] = not doors[d]
    return doors.count(True)

# def mystery_doors2(num_students:int)->int:
#     return (int(num_students**0.5))

# Check that it works:
print(mystery_doors(5))