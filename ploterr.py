import matplotlib.pyplot as plt
import numpy as np

fi = open("error.1",'r')
fi.readline()
ne = np.zeros(3)
ue = np.zeros(3)
ve = np.zeros(3)
pe = np.zeros(3)
i=0
for line in fi:
    line_str= line.split()
    ne[i] = int(line_str[0])
    ue[i] = float(line_str[1])
    ve[i] = float(line_str[2])
    pe[i] = float(line_str[3])
    i+=1
dx = np.sqrt(1.0/ne)
plt.figure(1)
plt.plot(dx,ue,label="error")
plt.plot(dx,5.0e6*dx**6,label=r"$O(x^6)$")
plt.legend(loc="best")
plt.xlabel(r"$dx$")
plt.xscale("log")
plt.yscale("log")
plt.title(r'$\| u-\tilde{u}\| ^2_{L^2}$')

plt.figure(2)
plt.plot(dx,ve,label="error")
plt.plot(dx,5.0e6*dx**6,label=r"$O(x^6)$")
plt.xlabel(r"$dx$")
plt.xscale("log")
plt.yscale("log")
plt.legend(loc="best")
plt.title(r'$\| v-\tilde{v} \| ^2_{L^2}$')

plt.figure(3)
plt.plot(dx,pe,label="error")
plt.xlabel(r"$dx$")
plt.xscale("log")
plt.yscale("log")
plt.title(r'$\| p-\tilde{p} \| ^2_{L^2}$')

plt.show()

