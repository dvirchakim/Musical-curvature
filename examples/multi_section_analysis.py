"""
Multi-Section Analysis Example
================================

This example demonstrates how to analyze different sections
of a song (verse, chorus, bridge) and compare their geometric
properties.

We'll use a simplified version of a typical pop song structure.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from twodimcurvcalc import TwoDimCurvCalc
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

print("=" * 70)
print("MULTI-SECTION ANALYSIS EXAMPLE")
print("=" * 70)
print("\nAnalyzing a typical pop song structure:")
print("  - Verse: Stable, lower energy")
print("  - Chorus: Dynamic, higher energy")
print("  - Bridge: Contrasting, exploratory")
print("=" * 70)

# Define sections of a hypothetical song
sections = {
    'Verse': {
        'x': [0, 5, 7, 0],
        'y': [4, 4, 4, 4],
        'z': [0, 0, 0, 0],
        'color': 'blue',
        'description': 'Simple, repetitive progression'
    },
    'Chorus': {
        'x': [0, 9, 5, 7, 0],
        'y': [4, 3, 4, 4, 4],
        'z': [0, 7, 0, 0, 0],
        'color': 'red',
        'description': 'More dynamic with minor chord'
    },
    'Bridge': {
        'x': [2, 4, 7, 11, 0],
        'y': [3, 4, 4, 4, 4],
        'z': [7, 0, 7, 0, 0],
        'color': 'green',
        'description': 'Contrasting, exploratory'
    }
}

# Calculate curvature for each section
print("\nCurvature Analysis:")
print("-" * 70)
for name, section in sections.items():
    curv = TwoDimCurvCalc(section['x'], section['y'])
    section['curvature'] = curv
    print(f"{name:10s}: {curv:6.2f}° - {section['description']}")

# Create 3D visualization with all sections
fig = plt.figure('Multi-Section 3D Analysis', figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot each section
for name, section in sections.items():
    x, y, z = section['x'], section['y'], section['z']
    color = section['color']
    
    # Plot points
    ax.scatter(x, y, z, c=color, s=100, marker='o', 
              edgecolors='black', linewidth=2, label=f'{name}')
    
    # Plot lines
    ax.plot(x, y, z, color=color, linewidth=2, alpha=0.7)
    
    # Mark start of each section
    ax.scatter([x[0]], [y[0]], [z[0]], c=color, s=200, 
              marker='*', edgecolors='black', linewidth=2)

# Styling
ax.set_xlabel('Root Position', fontsize=12, fontweight='bold')
ax.set_ylabel('Third Quality', fontsize=12, fontweight='bold')
ax.set_zlabel('Seventh Extension', fontsize=12, fontweight='bold')
ax.set_title('Song Structure: Verse, Chorus, and Bridge in 3D Space', 
            fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='upper left')
ax.view_init(elev=25, azim=45)
ax.grid(True, alpha=0.3)

# Create 2D comparison plots
fig2, axes = plt.subplots(2, 2, figsize=(14, 10))
fig2.suptitle('Section-by-Section Comparison', fontsize=16, fontweight='bold')

# Plot each section in 2D
for idx, (name, section) in enumerate(sections.items()):
    row, col = idx // 2, idx % 2
    ax2 = axes[row, col]
    
    x, y = section['x'], section['y']
    color = section['color']
    
    ax2.plot(x, y, color=color, linewidth=3, marker='o', 
            markersize=10, markerfacecolor=color, 
            markeredgecolor='black', markeredgewidth=2)
    
    # Mark start and end
    ax2.plot(x[0], y[0], 'g*', markersize=20, label='Start')
    ax2.plot(x[-1], y[-1], 'r*', markersize=20, label='End')
    
    ax2.set_xlabel('X Coordinate', fontsize=10)
    ax2.set_ylabel('Y Coordinate', fontsize=10)
    ax2.set_title(f'{name}\nCurvature: {section["curvature"]:.1f}°', 
                 fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=9)
    ax2.set_aspect('equal', adjustable='box')

# Curvature comparison bar chart
ax3 = axes[1, 1]
names = list(sections.keys())
curvatures = [sections[name]['curvature'] for name in names]
colors_list = [sections[name]['color'] for name in names]

bars = ax3.bar(names, curvatures, color=colors_list, alpha=0.7, 
              edgecolor='black', linewidth=2)

for bar, curv in zip(bars, curvatures):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'{curv:.1f}°', ha='center', va='bottom', 
            fontsize=11, fontweight='bold')

ax3.set_ylabel('Curvature (degrees)', fontsize=11)
ax3.set_title('Curvature Comparison', fontsize=12, fontweight='bold')
ax3.grid(axis='y', alpha=0.3)

plt.tight_layout()

# Analysis summary
print("\n" + "=" * 70)
print("ANALYSIS SUMMARY")
print("=" * 70)

verse_curv = sections['Verse']['curvature']
chorus_curv = sections['Chorus']['curvature']
bridge_curv = sections['Bridge']['curvature']

print(f"\nVerse Curvature:   {verse_curv:.2f}°")
print(f"Chorus Curvature:  {chorus_curv:.2f}°")
print(f"Bridge Curvature:  {bridge_curv:.2f}°")

print("\nObservations:")
if chorus_curv > verse_curv:
    print(f"  ✓ Chorus is {chorus_curv - verse_curv:.1f}° more complex than verse")
    print("    → Typical of pop songs: chorus has more harmonic movement")

if bridge_curv > verse_curv:
    print(f"  ✓ Bridge is {bridge_curv - verse_curv:.1f}° more complex than verse")
    print("    → Bridge provides contrast and exploration")

most_complex = max(sections.items(), key=lambda x: x[1]['curvature'])
print(f"\n  Most Complex Section: {most_complex[0]} ({most_complex[1]['curvature']:.1f}°)")

least_complex = min(sections.items(), key=lambda x: x[1]['curvature'])
print(f"  Least Complex Section: {least_complex[0]} ({least_complex[1]['curvature']:.1f}°)")

print("\nMusical Interpretation:")
print("  - Lower curvature → More stable, predictable")
print("  - Higher curvature → More dynamic, surprising")
print("  - Contrast between sections → More interesting song structure")

print("\n" + "=" * 70)
print("TIP: Try modifying the coordinates to see how changes")
print("     in chord progressions affect the geometric properties!")
print("=" * 70)

plt.show()
