import os
import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt



def create_file_list(path):
    return_list = []
    for filenames in os.walk(path):
        for file_list in filenames:
            for file_name in file_list:
                if file_name.endswith((".out")):
                    return_list.append(file_name)

    return return_list

points = []
files = create_file_list("./")
ips = map(lambda x: x.replace('.out', ''), files)
for ff in files:
    i = 0
    with open(ff) as f:
        lines = f.readlines()
        for line in lines:
            i = i + 1
            if line == "\n":
                # we pass the latency measurement
                break
            split = line.split(' ')
            target = ips.index(split[0])
            avg = sum(map(float, split[3:-1]))/len(split[3:-1])
            points.append([ips.index(ff.replace('.out', '')), target, avg])

x = map(lambda x: x[0], points)
y = map(lambda x: x[1], points)
z = np.asarray(map(lambda x: x[2], points))

xi,yi = np.meshgrid(x, y)
plt_z = np.zeros((yi.max()+1, xi.max()+1))
plt_z[y, x] = z
plt_y = np.arange(plt_z.shape[0])
plt_x = np.arange(plt_z.shape[1])
print(plt_z)
plt.subplot(2, 2, 1)
plt.pcolor(plt_x, plt_y, plt_z, cmap='RdBu', vmin=0, vmax=1000)
plt.title('Observed latencies')
# set the limits of the plot to the limits of the data
#plt.axis([xi.min(), xi.max(), yi.min(), yi.max()])
plt.colorbar()
plt.show()



