import numpy as np
import matplotlib.pyplot as plt
import itertools
import seaborn as sns
from collections import Counter

# Example Inputs (replace with input() when running locally)
current_gpa = 3.579
current_units = 24
new_units = 5

min_gpas = [4.0, 3.3, 3.3, 3.7, 3.0]
max_gpas = [4.0, 3.7, 4.0, 4.0, 4.0]

# Generate combinations with 5 steps per unit
steps_per_unit = 5
gpa_ranges = [np.linspace(min_gpas[i], max_gpas[i], steps_per_unit) for i in range(new_units)]
combinations = list(itertools.product(*gpa_ranges))

# Calculate final GPA for each combination
final_gpas = []
for combo in combinations:
    new_gpa_total = sum(combo)
    total_gpa = ((current_gpa * current_units) + new_gpa_total) / (current_units + new_units)
    final_gpas.append(total_gpa)

# Round final GPA outcomes before counting
rounded_gpas = [round(gpa, 2) for gpa in final_gpas]

# Count frequencies
gpa_counter = Counter(rounded_gpas)
total_outcomes = len(rounded_gpas)

# Print likelihood of each GPA
sorted_gpas = sorted(gpa_counter.items())
print("Final GPA | Likelihood (%)")
print("--------------------------")
for gpa, count in sorted_gpas:
    likelihood = (count / total_outcomes) * 100
    print(f"{gpa:.2f}     | {likelihood:6.2f}")

# Plot 1: Histogram of final GPA outcomes
plt.figure(figsize=(10, 6))
sns.histplot(final_gpas, bins=50, kde=True, color='skyblue', edgecolor='black')
plt.axvline(current_gpa, color='red', linestyle='--', linewidth=2, label=f'Current GPA = {current_gpa}')
plt.xlabel('Final GPA')
plt.ylabel('Frequency')
plt.title('Distribution of Possible Final GPA Outcomes')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: Boxplot per unit to show GPA ranges
plt.figure(figsize=(10, 6))
sns.boxplot(data=[np.linspace(min_gpas[i], max_gpas[i], steps_per_unit) for i in range(new_units)])
plt.xticks(ticks=np.arange(new_units), labels=[f'Unit {i+1}' for i in range(new_units)])
plt.ylabel('GPA Range')
plt.title('Range of GPA Outcomes per New Unit')
plt.grid(True)
plt.show()

# Plot 3: Line plot of min, mean, max final GPA
min_combo = [min_gpas[i] for i in range(new_units)]
max_combo = [max_gpas[i] for i in range(new_units)]
avg_combo = [(min_gpas[i] + max_gpas[i]) / 2 for i in range(new_units)]

def calc_final(c):
    return ((current_gpa * current_units) + sum(c)) / (current_units + new_units)

min_gpa = calc_final(min_combo)
avg_gpa = calc_final(avg_combo)
max_gpa = calc_final(max_combo)

plt.figure(figsize=(10, 6))
plt.plot(['Min', 'Avg', 'Max'], [min_gpa, avg_gpa, max_gpa], marker='o', linewidth=2, label='Projected Final GPA')
plt.axhline(current_gpa, color='red', linestyle='--', linewidth=2, label=f'Current GPA = {current_gpa}')
plt.ylabel('GPA')
plt.title('Final GPA Range Summary Based on Best/Worst/Average Case')
plt.legend()
plt.grid(True)
plt.show()
