# to figure out how much percentage does the part takes

import matplotlib.pyplot as plt
# plt.pie(value, labels = label_list, color = color_list, autopct = "%1.1f%")-%string starts from here- 1.1f means one digit before and one digit after the decimal
regions = ['North', 'South', 'East', 'West']
revenue = [3000, 2000, 1500, 1000]

plt.pie(revenue, labels= regions, autopct='%1.1f%%', colors=['gold', 'skyblue', 'lightgreen', 'coral'])
plt.title("Revenue Contribution By Region")
plt.show()
