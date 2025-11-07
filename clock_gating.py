# -----------------------------------------------
# Project: Low Power Clock Gating Simulation
# Author: Dhanusha M
# Tool: Python (VS Code)
# -----------------------------------------------

import random
import matplotlib.pyplot as plt

# Number of clock cycles for simulation
cycles = 20

# Random enable pattern (1 = active, 0 = idle)
enable_pattern = [random.choice([0, 1]) for _ in range(cycles)]

# Lists to hold clock signals
clock_without_gating = []
clock_with_gating = []

# Generate clock signals for both cases
for i in range(cycles):
    # Base clock (no gating)
    clock_without_gating.append(1 if i % 2 == 0 else 0)

    # Gated clock (only toggles when enable = 1)
    if enable_pattern[i] == 1:
        clock_with_gating.append(1 if i % 2 == 0 else 0)
    else:
        clock_with_gating.append(0)

# Calculate number of toggles (switching activity)
toggles_without = sum([abs(clock_without_gating[i] - clock_without_gating[i-1]) for i in range(1, cycles)])
toggles_with = sum([abs(clock_with_gating[i] - clock_with_gating[i-1]) for i in range(1, cycles)])

# Calculate power saved
power_saved = ((toggles_without - toggles_with) / toggles_without) * 100

# Print results
print("Clock without gating toggled:", toggles_without, "times")
print("Clock with gating toggled:", toggles_with, "times")
print(f"Power saved: {power_saved:.2f}%")

# -----------------------------------------------
# Visualization Section
# -----------------------------------------------

# 1. Bar chart comparison
plt.figure(figsize=(8, 4))
plt.bar(["Without Gating", "With Gating"], [toggles_without, toggles_with], color=["red", "green"])
plt.title("Low Power Clock Gating Simulation")
plt.ylabel("Clock Toggles (Power Consumption)")
plt.text(0, toggles_without + 0.5, str(toggles_without), ha='center', fontsize=10)
plt.text(1, toggles_with + 0.5, str(toggles_with), ha='center', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 2. Waveform plots (Timing Diagrams)
plt.figure(figsize=(10, 5))

plt.subplot(3, 1, 1)
plt.step(range(cycles), enable_pattern, where='mid', color='blue')
plt.title("Enable Signal (Random Activity)")
plt.ylabel("Enable")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.step(range(cycles), clock_without_gating, where='mid', color='red')
plt.title("Clock Signal Without Gating")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.step(range(cycles), clock_with_gating, where='mid', color='green')
plt.title("Clock Signal With Gating (Low Power Mode)")
plt.xlabel("Clock Cycles")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
