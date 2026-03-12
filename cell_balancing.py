import random

# Number of cells in battery pack
num_cells = 6

# Generate random voltages between 3.6V and 4.2V
cells = [round(random.uniform(3.6, 4.2), 3) for _ in range(num_cells)]

print("Initial Cell Voltages:")
for i, v in enumerate(cells):
    print(f"Cell {i+1}: {v} V")

# Target voltage (minimum cell voltage)
target_voltage = min(cells)

print("\nTarget Voltage for Balancing:", target_voltage)

# Passive balancing simulation
balanced_cells = []

for voltage in cells:
    if voltage > target_voltage:
        # discharge higher voltage cells
        voltage = target_voltage
    balanced_cells.append(voltage)

print("\nBalanced Cell Voltages:")
for i, v in enumerate(balanced_cells):
    print(f"Cell {i+1}: {v} V")

print("\nCell balancing completed.")
