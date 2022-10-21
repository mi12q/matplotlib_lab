import os
import matplotlib.pyplot as plt

path = 'C:/Users/Milica/PycharmProjects/matplotlib_laba/ep1/dead_moroz'
os.chdir(path)
file_paths = []
figures = []

for file in os.listdir():
    if file.endswith('.dat'):
        file_path = f"{path}/{file}"
        file_paths.append(file_path)


def read_file(f_path):
    f = open(f_path, 'r')
    data = []
    x_data = []
    y_data = []
    file_content = f.read().split("\n")
    for i in range(1, int(file_content[0])+1):
        row = file_content[i].split()
        row = [float(j) for j in row]
        data.append(row)
    for i in range(len(data)):
        x_data.append(data[i][0])
        y_data.append(data[i][1])
    return x_data, y_data


for path in file_paths:
    plt.axis('scaled')
    x, y = read_file(path)
    fig = plt.figure()
    title = 'Number of points: ' + str(len(x))
    plt.scatter(x, y, marker='o', s=20)
    plt.title(title)
    figures.append(fig)

i = 1
for fig in figures:
    name = str(i) + ".png"
    fig.savefig(name)
    i += 1
