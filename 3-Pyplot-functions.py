# to convert numbers into graphpicture we need pyplot functions
# to draw graph, data-comapre, trends\
# plt.plot() to draw line graph
# plt.ploy(x, y, color= "color name", linestyle = "line style", linewidt=value, marker = "marker symbol", label = "label")
# plt.xlable('text')
# plt.legend(loc = "Upper left/ lower right", fontsize= 12)
# plt.grid(color="gray", linestyle=":", linewidth=1)
# xlim()/ylim() - to limit x and y axis
import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [1000, 1500, 1200, 1800]
plt.plot(months, sales, color= "blue", linestyle = "--", linewidth = 2, marker = 'o', label= "2025 sales data")
plt.xlabel("Month")
plt.ylabel("Sales per month")
plt.title("Monthly Sales data Report")
plt.legend(loc= "lower right", fontsize= 8)
plt.grid(color="gray", linestyle=":", linewidth=1)
plt.xlim(1,4)
plt.ylim(0,2000)
plt.xticks([1,2,3,4], ['M1', 'M2', 'M3', 'M4'])
plt.show()