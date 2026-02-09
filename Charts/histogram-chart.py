# to find out are the data compact together or how much apart are they

import matplotlib.pyplot as plt

# plt.hist(data, bins = number_of_bins, color = "color name", edgecolor = "black")
scores = [45, 67, 89, 56, 78, 88, 92, 60, 74, 81, 59, 75, 66, 82, 90, 85, 70, 73, 68, 77]
plt.hist(scores, bins=5, color='purple', edgecolor= "black")
plt.xlabel("Score Range")
plt.ylabel("No of students")
plt.title("Score Distribution of students")
plt.show()