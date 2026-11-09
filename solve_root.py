import numpy as np
m = 9.109e-31 #mass of an electron in kg
h_cut = 1.0546e-34 #reduced planck constant in J.s

a = 1e-10 #in meters
V_0 = 4e-17 #potential energy in J

z_0 = np.sqrt(2*m*V_0)*a/h_cut

#z = np.sqrt(2*m*(E+V_0))*a/h_cut

y_tanz = []
y_cotz = []
y_zterm = []

#with open("z_functions.txt", "w") as f:
for z in np.arange(0,10, 0.1):
        #f.write(f"{z} {np.tan(z)} {1/np.tan(z)} {np.sqrt((z_0/z)**2-1)}\n")
    y_tanz.append(np.tan(z))
    y_cotz.append(1/np.tan(z))
    y_zterm.append(np.sqrt((z_0/z)**2-1))

z_sym = np.array(y_zterm) - np.array(y_tanz)
z_antisym = np.array(y_zterm) - np.array(y_cotz)
import matplotlib.pyplot as plt
"""
fig, ax = plt.subplots()
ax.plot(y_tanz, label='tan(z)')
ax.plot(y_zterm, label='z term')
ax.set_ylim(0,10)
ax.legend()
plt.savefig("z_function with tanz.pdf")
plt.show()

fig, ax = plt.subplots()
ax.plot(y_cotz, label='cot(z)')
ax.plot(y_zterm, label='z term')
ax.set_ylim(0,10)
ax.legend()
plt.savefig("z_function with cotz.pdf")
plt.show()
"""
fig, ax = plt.subplots()
ax.plot(z_sym, label='z term')
ax.set_ylim(-10,10)
ax.legend()
plt.savefig("z_equation_symmetric.pdf")
plt.show()

fig, ax = plt.subplots()
ax.plot(z_antisym, label='z term')
ax.set_ylim(-10,10)
ax.legend()
plt.savefig("z_equation_antisymmetric.pdf")
plt.show()

#the symmetric and antisymmetric cases both have vertical/nearly-vertical lines, where the bisection method may fail
