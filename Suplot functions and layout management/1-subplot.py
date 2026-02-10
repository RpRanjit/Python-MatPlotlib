import matplotlib.pyplot as plt

x= [1,2,3,4]
y = [10,20, 30, 40]

# casual method

# plt.subplot(1,2,1) # 1row, 2 column, 1st subplot
# plt.plot(x,y)
# plt.title('line chart')

# plt.subplot(1,2,2) # 1row, 2column, 2nd subplot
# plt.bar(x,y)
# plt.title("Bar cahrt")

# plt.show()


# more professional method
# fig, ax = plt.subplots(nrows, ncols, figsize = (width, height))
fig, ax = plt.subplots(1,2, figsize = (10,5))
ax[0].plot(x,y)
ax[0].set_title('Line Plot')

ax[1].bar(x,y)
ax[1].set_title('Bar chart')
plt.tight_layout()
plt.show()
