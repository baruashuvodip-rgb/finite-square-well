import numpy as np
import bisection_solve_FSW as bisection

m = 9.109e-31 #mass of an electron in kg
h_cut = 1.0546e-34 #reduced planck constant in J.s

a = 1e-10 #in meters
V_0 = 4e-17 #potential energy in J

z_0 = np.sqrt(2*m*V_0)*a/h_cut
print(z_0)

#z = np.sqrt(2*m*(E+V_0))*a/h_cut

def symmetric(z):
    return np.sqrt((z_0/z)**2-1)-np.tan(z)


def antisymmetric(z):
    return np.sqrt((z_0/z)**2-1)+1/np.tan(z)

z_values = np.linspace(1e-6,z_0-1e-6,100000)
sym = symmetric(z_values)
anti_sym = antisymmetric(z_values)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(z_values, sym, label="symmetric states")
ax.set_ylim(-8,8)
ax.legend()
plt.savefig("z_equation_symmetric.pdf")
plt.show()

fig, ax = plt.subplots()
ax.plot(z_values, anti_sym, label='antisymmetric states')
ax.set_ylim(-8,8)
ax.legend()
plt.savefig("z_equation_antisymmetric.pdf")
plt.show()

pairs = bisection.find_sign_change(symmetric, 0.00001, 0.000001, z_0)
print(pairs)
roots_sym = bisection.bisection(symmetric,pairs,1e-6, max_iter = 100)
pairs = bisection.find_sign_change(antisymmetric, 0.00001, 0.000001, z_0)
print(pairs)
roots_antisym = bisection.bisection(antisymmetric,pairs,1e-6, max_iter = 100)

print(roots_sym)
print(roots_antisym)

number_of_zeroes = len(roots_sym) + len(roots_antisym)

def energy(z):
    return (h_cut**2 * np.asarray(z)**2)/(2*m*a**2) - V_0

energy_states_antisym = energy(roots_antisym)
energy_states_sym = energy(roots_sym)

e = 1.60218e-19

print("Symmetric energies (eV):", energy_states_sym/e)
print("Antisymmetric energies (eV):", energy_states_antisym/e)

def energy_predict(n):
    return (n**2*h_cut**2*np.pi**2)/(8*m*a**2) - V_0

energy_states_predicted = []

for i in range(1, number_of_zeroes+1):
    energy_states_predicted.append(energy_predict(i)/e)

print(energy_states_predicted)

# the values are not very close. they are mostly of the same order of magnitude, but the values calculated using the roots of the 
# transcendental equation increase slower than the values calulated from the infinite square well approximation
'''y_tanz = []
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
import matplotlib.pyplot as plt'''
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
'''
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
'''

#the symmetric and antisymmetric cases both have vertical/nearly-vertical lines, where the bisection method may fail
#these are values where the function is undefined. we will skip these by setting a limit on the bisection loop

