# savefig('finename.extension', dpi = value, bbox_inches = 'tight')
# finename.extension - plot.png,graph.pdf
# dpi value - dot per inch (resolution od an image)
# bbox_inches = to crop wide spaces in the canvas
import matplotlib.pyplot as plt
x= [1,2,3,4]
y = [10, 20, 15, 25]

# craete plot
plt.plot(x,y, color = "blue", marker= "o")
plt.title("Simple Line plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.savefig('Line_plot.png', dpi = 300, bbox_inches = "tight")
# make sure you use savefig before plt.show()
plt.show()