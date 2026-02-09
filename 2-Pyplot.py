# Trems
# 1. Data Point: in data set there is single pair of data onr for x-axis and one for y-axis
# 2. X-axis/Y-axis (x-axix: putinput data like time, days or months, y-axis: put output data like sales , emp, profit etc)
# note: don't forget to label four axis
# 3. Figure: a canvas or place/window where the figure is live
# 4. Axes: Graph box
# 5. Plot: an actual line bar, or anything you draw
# 6. Marker: a signal or dot we use son tat the data point is visible
# 7. Line style: line(maintain connection between data points) style(types of line)
# 8. Color: color of line, bar, marker
# 9. Legend: a small box that point out what line,color represent in the graph
# 10. Label: used while explaining what out x, y axis are doing
# 11. Title: to give headline of graph
# 12. Grid: add vertical or horizontal lines at the background of graph
# 14. Function: block of code  that do specific task
# 15. Method: a function that belongd to an object 
# 16. Parameters: information given to method/function
# 17. Keyword Arguments(kwargs): value you pass with varible(name = value)
# 18. Object-Oriented API: later pages
# 19. DPI: Dots per inch(resolution/clarity od te image/graph)
# 20. Backend: to darw and save  learn later
import matplotlib.pyplot as plt

x= ['Mon', 'Tues', 'Web', 'Thur', 'Fri']# x-axis
y = [10, 15, 7, 20, 12]

plt.plot(x, y)
plt.title("Weekly Bakery Sales")
plt.xlabel("Days of the week")
plt.ylabel("No of sales in a day")
plt.show()

# matplotlib Object oriented API
# this works as state machine - means it track the function used
# -for large project or mare than one plot
# -More flexible than pyplot