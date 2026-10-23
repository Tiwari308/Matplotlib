import matplotlib.pyplot as plt

plt.scatter([1,2,3], [50,55,60], color='blue', label='Class A')
plt.scatter([1,2,3], [40,50,52], color='orange', label='Class B')

plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Relationship between Stud time and Exam score')
plt.legend()
plt.grid(True)
plt.show()