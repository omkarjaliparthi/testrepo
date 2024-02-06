import matplotlib.pyplot as plt

responses = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
frequencies = [8, 12, 6, 24, 20]

total_responses = sum(frequencies)
percentages = [(count / total_responses) * 100 for count in frequencies]

plt.figure(figsize=(8, 6))
plt.bar(responses, percentages, color='skyblue')
plt.xlabel('Responses')
plt.ylabel('Percentage of Total Responses')
plt.title('Response Frequencies and Percentages')
plt.ylim(0, 100)

# Add percentage labels to the bars
for i, percentage in enumerate(percentages):
    plt.text(i, percentage + 1, f'{percentage:.1f}%', ha='center')

plt.show()
