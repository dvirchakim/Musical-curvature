"""
Curvature Calculation Example
==============================

This example demonstrates how to calculate and interpret
curvature values for different chord progressions.

We'll compare three progressions with different characteristics.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from twodimcurvcalc import TwoDimCurvCalc
import matplotlib.pyplot as plt
import numpy as np

print("=" * 70)
print("CURVATURE CALCULATION EXAMPLE")
print("=" * 70)

# Define three different progressions
progressions = {
    'Simple Diatonic (I-IV-V-I)': {
        'x': [0, 5, 7, 0],
        'y': [0, 0, 0, 0],
        'description': 'A basic, predictable progression'
    },
    'Chromatic Movement': {
        'x': [0, 1, 2, 3, 4, 5],
        'y': [0, 1, 0, 1, 0, 1],
        'description': 'Stepwise chromatic motion'
    },
    'Complex Jazz (ii-V-I-vi)': {
        'x': [2, 7, 0, 9],
        'y': [3, 4, 4, 3],
        'description': 'Common jazz turnaround'
    }
}

# Calculate curvature for each progression
results = {}
for name, prog in progressions.items():
    curvature = TwoDimCurvCalc(prog['x'], prog['y'])
    results[name] = curvature
    
    print(f"\n{name}")
    print("-" * 70)
    print(f"Description: {prog['description']}")
    print(f"Coordinates X: {prog['x']}")
    print(f"Coordinates Y: {prog['y']}")
    print(f"Total Curvature: {curvature:.2f}°")

# Visualize the progressions side by side
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Comparing Chord Progression Curvatures', fontsize=16, fontweight='bold')

for idx, (name, prog) in enumerate(progressions.items()):
    ax = axes[idx]
    x, y = prog['x'], prog['y']
    
    # Plot the progression
    ax.plot(x, y, 'b-', linewidth=2, marker='o', markersize=8, 
            markerfacecolor='red', markeredgecolor='darkred', markeredgewidth=2)
    
    # Add starting point indicator
    ax.plot(x[0], y[0], 'g*', markersize=15, label='Start')
    
    # Add ending point indicator
    ax.plot(x[-1], y[-1], 'r*', markersize=15, label='End')
    
    # Labels and title
    ax.set_xlabel('X Coordinate', fontsize=10)
    ax.set_ylabel('Y Coordinate', fontsize=10)
    ax.set_title(f'{name}\nCurvature: {results[name]:.1f}°', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_aspect('equal', adjustable='box')

plt.tight_layout()

# Create a bar chart comparing curvatures
fig2, ax2 = plt.subplots(figsize=(10, 6))
names = list(results.keys())
values = list(results.values())
colors = ['green', 'orange', 'purple']

bars = ax2.bar(range(len(names)), values, color=colors, alpha=0.7, edgecolor='black', linewidth=2)

# Add value labels on bars
for i, (bar, value) in enumerate(zip(bars, values)):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.1f}°',
            ha='center', va='bottom', fontsize=12, fontweight='bold')

ax2.set_ylabel('Total Curvature (degrees)', fontsize=12)
ax2.set_title('Curvature Comparison Across Progressions', fontsize=14, fontweight='bold')
ax2.set_xticks(range(len(names)))
ax2.set_xticklabels(names, rotation=15, ha='right')
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()

# Print interpretation guide
print("\n" + "=" * 70)
print("INTERPRETATION GUIDE")
print("=" * 70)
print("\nCurvature Ranges:")
print("  0-90°:     Very smooth, predictable progressions")
print("  90-180°:   Moderate complexity, some surprises")
print("  180-360°:  Complex, winding progressions")
print("  360°+:     Highly chromatic, experimental")

print("\nObservations:")
if results['Simple Diatonic (I-IV-V-I)'] < results['Chromatic Movement']:
    print("  ✓ As expected, chromatic movement has higher curvature")
if results['Simple Diatonic (I-IV-V-I)'] < results['Complex Jazz (ii-V-I-vi)']:
    print("  ✓ Jazz progressions show more harmonic complexity")

print("\nKey Insight:")
print("  Higher curvature generally indicates more unexpected")
print("  harmonic changes and greater musical complexity.")
print("=" * 70)

plt.show()
