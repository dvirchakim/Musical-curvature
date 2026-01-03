"""
Basic Visualization Example
============================

This example demonstrates the fundamental concepts of visualizing
chord progressions in 3D space.

We'll create a simple I-IV-V-I progression and visualize it.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a new figure
fig = plt.figure('Basic Chord Progression - I-IV-V-I', figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define a simple I-IV-V-I progression
# These coordinates represent: C major - F major - G major - C major
# Mapping: [root position, third quality, seventh presence]

x = [0, 5, 7, 0]   # Root positions (C=0, F=5, G=7)
y = [4, 4, 4, 4]   # All major thirds (4 semitones)
z = [0, 0, 0, 0]   # No seventh chords (triads only)

# Plot the chord positions as points
ax.scatter(x, y, z, c='red', s=100, marker='o', label='Chords')

# Connect the chords with lines to show the progression
ax.plot(x, y, z, color='blue', linewidth=2, label='Progression Path')

# Add labels for each chord
chord_names = ['C (I)', 'F (IV)', 'G (V)', 'C (I)']
for i, name in enumerate(chord_names):
    ax.text(x[i], y[i], z[i] + 0.5, name, fontsize=10, fontweight='bold')

# Set axis labels
ax.set_xlabel('Root Position', fontsize=12)
ax.set_ylabel('Third Quality', fontsize=12)
ax.set_zlabel('Seventh Extension', fontsize=12)

# Set title
ax.set_title('Basic I-IV-V-I Progression in 3D Space', fontsize=14, fontweight='bold')

# Add legend
ax.legend()

# Set viewing angle for better perspective
ax.view_init(elev=20, azim=45)

# Add grid for better depth perception
ax.grid(True, alpha=0.3)

print("=" * 60)
print("BASIC VISUALIZATION EXAMPLE")
print("=" * 60)
print("\nChord Progression: I-IV-V-I (C-F-G-C)")
print("\nCoordinate Mapping:")
for i, name in enumerate(chord_names):
    print(f"  {name}: ({x[i]}, {y[i]}, {z[i]})")

print("\nVisualization Tips:")
print("  - Red dots represent individual chords")
print("  - Blue line shows the progression path")
print("  - Rotate the plot by clicking and dragging")
print("  - Zoom with scroll wheel")
print("\nNotice how this progression forms a closed loop,")
print("returning to the starting chord (tonic).")
print("=" * 60)

# Show the plot
plt.show()
