import matplotlib.pyplot as plt


grades = {
    "riyazi": 16,
    "naram afzar": 14,
    "System Amel": 12,
    "sakhteman dadeh": 17,
    "Database": 18,
    "Algorithm": 15
}


names = list(grades.keys())
scores = list(grades.values())


plt.figure(figsize=(10, 6))
plt.bar(names, scores, color='skyblue', edgecolor='black')


plt.title("Student Grades", fontsize=16)
plt.xlabel("Students", fontsize=14)
plt.ylabel("Grades", fontsize=14)
plt.ylim(0, 20)


for i, score in enumerate(scores):
    plt.text(i, score + 1, str(score), ha='center', fontsize=12)


plt.tight_layout()
plt.show()
