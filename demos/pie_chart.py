import matplotlib.pyplot as plt

from data import pie_data

plt.pie(*list(pie_data.values())[:-1])
plt.show()
