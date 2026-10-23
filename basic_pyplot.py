import matplotlib.pyplot as plt

x = ['Mon', 'tue', 'Wed', 'thur', 'Fri']
y = [10,15,7,20,12]

plt.plot(x,y)

plt.title("Bakery Slaes this Week")

plt.xlabel('Day of the week')
plt.ylabel('Sales Per Day')

plt.show()  