import matplotlib.pyplot as plt

file = open("frames.dat", "r")
file_content = file.read().split("\n")
figures = []
x = []
y = []
new_y = []

for i in range(len(file_content) - 1):
    row = file_content[i].split()
    row = [float(j) for j in row]
    if i % 2 == 0:
        x.append(row)
    else:
        y.append(row)

for arr in y:
    arr = arr[0:1844]
    new_y.append(arr)

for i in range(len(new_y)):
    title = "Frame " + str(i)
    fig = plt.figure()
    plt.plot(x[i], new_y[i])
    plt.grid()
    plt.title(title)
    plt.ylim(-9, 12)
    plt.xlim(0, 15.7)
    plt.yticks(range(-8, 12))
    plt.xticks(range(0, 16))
    figures.append(fig)


i = 0
for fig in figures:
    name = str(i) + ".png"
    fig.savefig(name)
    i += 1
