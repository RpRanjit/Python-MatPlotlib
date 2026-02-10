import matplotlib.pyplot as plt

x= [1,2,3,4]
y = [10,20, 30, 40]

# more professional method
# fig, ax = plt.subplots(nrows, ncols, figsize = (width, height))
fig, ax = plt.subplots(1,2, figsize = (10,5))
ax[0].plot(x,y, color= "red")
ax[0].set_title('Line Plot')

ax[1].bar(x,y, color = "green")
ax[1].set_title('Bar chart')

fig.suptitle('Comparision of Line and Bar Charts')

plt.tight_layout()
plt.show()
