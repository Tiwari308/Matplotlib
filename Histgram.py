import matplotlib.pyplot as plt

scores = [45,67,89,56,78,58,69,25,45,71,52,86,99,58,56,25,78,45,79,83]

plt.hist(scores, bins=5, color='purple', edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title('Score Distribution of Stuents')
plt.show()