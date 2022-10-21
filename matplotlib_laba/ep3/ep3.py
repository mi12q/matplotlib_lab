import csv
import matplotlib.pyplot as plt
import numpy as np

data = []
teachers = {}
groups = {}
figures = []

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        new_row = row[0].split(";")
        data.append(new_row)
    for row in data:
        if row[0] not in teachers:
            teachers[row[0]] = [int(row[2])]
        else:
            teachers[row[0]].append(int(row[2]))
        if row[1] not in groups:
            groups[row[1]] = [int(row[2])]
        else:
            groups[row[1]].append(int(row[2]))

groups = dict(sorted(groups.items(), key=lambda t: t[0]))
teacher_stats = {}
groups_stats = {}
grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rev_grades = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for key in teachers:
    statistics = []
    for grade in grades:
        statistics.append(teachers[key].count(grade))
    teacher_stats[key] = statistics

for key in groups:
    statistics = []
    for grade in grades:
        statistics.append(groups[key].count(grade))
    groups_stats[key] = statistics


all_grades_t = []
all_grades_g = []
for i in range(10):
    grade_t = []
    grade_g = []
    for key in teacher_stats:
        grade_t.append(teacher_stats[key][i])
    for key in groups_stats:
        grade_g.append(groups_stats[key][i])
    all_grades_t.append(np.array(grade_t))
    all_grades_g.append(np.array(grade_g))

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'skyblue', 'orange', 'darkgreen']
bar_numbers1 = range(len(teachers))


x = list(teachers.keys())
fig1 = plt.figure()
suma = all_grades_t[0]
plt.bar(x, all_grades_t[0], color=colors[0])
for i in range(1, 10):
    plt.bar(x, all_grades_t[i], bottom=suma, color=colors[i])
    suma += all_grades_t[i]

plt.title("Marks per prep")
plt.ylim(0, 18)
plt.yticks(range(0, 20, 5))
plt.legend(rev_grades)
figures.append(fig1)


x = list(groups.keys())
fig2 = plt.figure()
suma = all_grades_g[0]
plt.bar(x, all_grades_g[0], color=colors[0])
for i in range(1, 10):
    plt.bar(x, all_grades_g[i], bottom=suma, color=colors[i])
    suma += all_grades_g[i]

plt.title("Marks per group")
plt.ylim(0, 19)
plt.yticks(range(0, 20, 5))
plt.legend(rev_grades)
figures.append(fig2)


figures[0].savefig("preps.png")
figures[1].savefig("groups.png")
