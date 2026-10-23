import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.subplot(1,2,1)  #1 row, 2nd colum, 1 subplot
plt.plot(x,y)
plt.title('Line chart')

plt.subplot(1, 2, 2)
plt.bar(x,y)
plt.title('Bar chart')

plt.show()


