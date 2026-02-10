# plt.scatter(x,y, color= "color name", marker = "marker style", label = "label name")
# Used to find the coorelation between two variables (eg advertising budget with sales)
import matplotlib.pyplot as plt

hours_study = [1,2,3,4,5,6,7,8]
exam_score = [50, 55, 60, 65, 70, 75, 80, 85]

# scatter plot

plt.scatter(hours_study, exam_score, color = "red", marker = "o", label = "Student Data")

plt.xlabel("Houes Studied")
plt.ylabel("Exam Score")
plt.title("Relationship Between Study time and Exam Score")
plt.legend()
plt.grid()
plt.show()

# for more tan one group
plt.scatter([1,2,3,4,5,6,7,8,9], [50, 55, 60, 65, 70, 75, 80, 85, 90], color = "red", marker = "o", label = "Group 1")
plt.scatter([1,2,3,4,5,6,7,8,9], [42, 45, 53, 55, 58, 60, 63, 65, 70], color = "blue", marker = "o", label = "Group 2")


plt.xlabel("Houer Studied")
plt.ylabel("Exam Score")
plt.title("Comparision between Two Groups")
plt.legend()
plt.grid()
plt.show()

