f = open("data.txt", mode='w', encoding='utf-8')
f.write("Name: Munevver Neva\nSurname: Armagan\nGender: Female\nUsername: Muneva\nJob: Student\n")
f.close

f = open("data.txt", mode='r', encoding='utf-8')
d = {}
for i in f:
    liste = i.split(": ")
    d[liste[0]] = liste[1][0:-1]
print(d)
