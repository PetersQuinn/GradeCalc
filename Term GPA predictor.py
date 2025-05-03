import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import itertools

# Inputs
new_units = 5
min_gpas = [4.0, 3.3, 3.3, 3.7, 3.0]
max_gpas = [4.0, 3.7, 4.0, 4.0, 4.0]

benchmarks = {
    "2024 Fall": 3.733,
    "2024 Spring": 3.6,
    "2023 Fall": 3.72,
    "2023 Spring": 3.4,
    "2022 Fall": 3.325
}

# Generate combinations
steps_per_unit = 5
gpa_ranges = [np.linspace(min_gpas[i], max_gpas[i], steps_per_unit) for i in range(new_units)]
combinations = list(itertools.product(*gpa_ranges))

# Round all term GPA outcomes
term_gpas = [round(sum(combo) / new_units, 2) for combo in combinations]

# Count frequencies
gpa_counter = Counter(term_gpas)
total_outcomes = len(term_gpas)

# Print likelihood table
sorted_gpas = sorted(gpa_counter.items())
gpa_vals = [gpa for gpa, _ in sorted_gpas]
prob_vals = [(count / total_outcomes) * 100 for _, count in sorted_gpas]
print("Term GPA | Likelihood (%)")
print("--------------------------")
for gpa, count in sorted_gpas:
    likelihood = (count / total_outcomes) * 100
    print(f"{gpa:.2f}    | {likelihood:6.2f}")

# Plot histogram with rounded bin edges
plt.figure(figsize=(10, 6))
sorted_keys = sorted(gpa_counter.keys())
bin_edges = [g - 0.005 for g in sorted_keys] + [sorted_keys[-1] + 0.005]
sns.histplot(term_gpas, bins=bin_edges, kde=False, color='lightgreen', edgecolor='black')

# Add benchmark lines
min_plot, max_plot = min(term_gpas), max(term_gpas)
for label, value in benchmarks.items():
    if min_plot <= value <= max_plot:
        plt.axvline(value, linestyle='--', linewidth=2, label=f'{label}: {value}', alpha=0.8)

plt.xlabel('Term GPA')
plt.ylabel('Frequency')
plt.title('Distribution and Likelihood of Term GPA Outcomes')
plt.legend()
plt.grid(True)
plt.show()

# Plot line chart of probabilities
plt.figure(figsize=(10, 6))
sns.lineplot(x=gpa_vals, y=prob_vals, marker='o', linewidth=2)
for label, value in benchmarks.items():
    if min_plot <= value <= max_plot:
        plt.axvline(value, linestyle='--', linewidth=2, label=f'{label}: {value}', alpha=0.8)
plt.xlabel('Term GPA')
plt.ylabel('Probability (%)')
plt.title('Probability of Each Term GPA Outcome')
plt.legend()
plt.grid(True)
plt.show()