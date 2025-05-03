import numpy as np
import matplotlib.pyplot as plt
import itertools

# Inputs
current_gpa = float(input("Enter your current GPA: "))
current_units = int(input("Enter your current number of units: "))
new_units = int(input("Enter the number of new units you're adding (4 to 6): "))

assert 4 <= new_units <= 6, "This visualization is designed for 4 to 6 new units."

# Collect GPA ranges for each unit
min_gpas = []
max_gpas = []
for i in range(new_units):
    min_val = float(input(f"Minimum GPA for new unit {i+1}: "))
    max_val = float(input(f"Maximum GPA for new unit {i+1}: "))
    min_gpas.append(min_val)
    max_gpas.append(max_val)

# Generate combinations with 5 steps per unit (to control size)
steps_per_unit = 5
gpa_ranges = [np.linspace(min_gpas[i], max_gpas[i], steps_per_unit) for i in range(new_units)]
combinations = list(itertools.product(*gpa_ranges))

# Calculate final GPA for each combo
final_gpas = []
for combo in combinations:
    new_gpa_total = sum(combo)
    total_gpa = ((current_gpa * current_units) + new_gpa_total) / (current_units + new_units)
    final_gpas.append(total_gpa)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(final_gpas, bins=50, color='skyblue', edgecolor='black')
plt.xlabel('Final GPA')
plt.ylabel('Frequency')
plt.title('Distribution of Possible Final GPA Outcomes')
plt.grid(True)
plt.show()
