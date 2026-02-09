# used for comparision of cateory side by side of eachother
#plt.bar(x, height, color= "color name", width = value, label = "label name")
import matplotlib.pyplot as plt
product = ["A", "B", "C", "D"]
sales = (1000, 1500, 800, 1200)

plt.barh(product, sales, color = 'orange',label= "Sales 2026")
# to give the data horizontal plt.hbar()
plt.xlabel("Products")
plt.ylabel("No. of Sales")
plt.title("No. of sales on Each Products")
plt.legend(loc="upper left")
plt.show()