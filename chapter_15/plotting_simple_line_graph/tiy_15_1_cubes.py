# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-01-29
# --------------------------------------------------------------------------- #
import matplotlib.pyplot as plt

x_values = range(-5000, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c='Red')

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([-150, 150, -1100000, 1100000])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)
# plt.savefig('squares.png', bbox_inches='tight')
plt.show()
