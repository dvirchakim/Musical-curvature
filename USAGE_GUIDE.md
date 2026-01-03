# Usage Guide: Musical Curvature Analysis

## Table of Contents
1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Visualizing Songs](#visualizing-songs)
4. [Calculating Curvature](#calculating-curvature)
5. [Creating Your Own Analysis](#creating-your-own-analysis)
6. [Interpreting Results](#interpreting-results)
7. [Advanced Techniques](#advanced-techniques)

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Install Dependencies

```bash
# Clone the repository
git clone https://github.com/dvirchakim/Musical-curvature.git
cd Musical-curvature

# Install required packages
pip install -r requirements.txt
```

Or install manually:
```bash
pip install numpy matplotlib
```

## Basic Usage

### Running a Song Visualization

Each song has its own Python file that generates 3D visualizations:

```bash
# Visualize "Imagine" by John Lennon
python imagine.py

# Visualize "Yellow Submarine" by The Beatles
python "Yellow submarine.py"

# Visualize "Hotel California" by Eagles
python "hotel california.py"
```

### What You'll See

The visualization shows:
- **Red dots**: Individual chord positions in 3D space
- **Colored lines**: The path connecting chords (the progression)
- **Multiple figures**: Different sections (verse, chorus, bridge) if applicable

### Interactive Controls

Once the plot opens:
- **Rotate**: Click and drag to rotate the 3D view
- **Zoom**: Scroll wheel to zoom in/out
- **Pan**: Right-click and drag to pan
- **Reset**: Home button to reset view

## Visualizing Songs

### Understanding the Code Structure

Here's a breakdown of a typical song file (`imagine.py`):

```python
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Create a figure for the verse
fig = plt.figure('imagine verse-FullchorDot')
ax = fig.gca(projection='3d')

# Define chord coordinates [X, Y, Z]
x, y, z = [3, 3, 8], [7, 7, 0], [10, 2, 4]

# Plot the chords and progression
ax.scatter(x, y, z, c='r', s=10)  # Chords as red dots
ax.plot(x, y, z, color='r')        # Progression as red line

plt.show()
```

### Coordinate Interpretation

Each list represents one dimension:
```python
x = [3, 3, 8]  # X-coordinates of 3 chords
y = [7, 7, 0]  # Y-coordinates of 3 chords
z = [10, 2, 4] # Z-coordinates of 3 chords
```

This means:
- Chord 1: (3, 7, 10)
- Chord 2: (3, 7, 2)
- Chord 3: (8, 0, 4)

## Calculating Curvature

### Using the 2D Curvature Calculator

The `twodimcurvcalc.py` module calculates the total curvature of a chord progression:

```python
from twodimcurvcalc import TwoDimCurvCalc

# Define a simple progression (2D projection)
x = [1, 4, 4, 1]  # X coordinates
y = [4, 4, 0, 0]  # Y coordinates

# Calculate curvature
curvature = TwoDimCurvCalc(x, y)
print(f"Total curvature: {curvature}°")
```

### Understanding the Output

The output is in degrees and represents:
- **0°**: Perfectly straight (no harmonic change)
- **Low values (< 90°)**: Smooth, predictable progressions
- **Medium values (90-270°)**: Moderate harmonic complexity
- **High values (> 270°)**: Complex, winding progressions

### Example Calculations

```python
# Simple I-IV-V-I progression (low curvature)
x1 = [0, 5, 7, 0]
y1 = [0, 0, 0, 0]
print(f"I-IV-V-I: {TwoDimCurvCalc(x1, y1)}°")

# Chromatic progression (high curvature)
x2 = [0, 1, 2, 3, 4, 5]
y2 = [0, 1, 0, 1, 0, 1]
print(f"Chromatic: {TwoDimCurvCalc(x2, y2)}°")
```

## Creating Your Own Analysis

### Step 1: Identify the Chord Progression

First, determine the chords in your song:
```
Example: "Wonderwall" by Oasis
Verse: Em7 - G - Dsus4 - A7sus4
```

### Step 2: Map Chords to Coordinates

Use the mapping system (see THEORY.md for details):
```python
# Example mapping (simplified)
Em7:     [0, 3, 10]
G:       [7, 4, 0]
Dsus4:   [2, 5, 7]
A7sus4:  [9, 4, 10]
```

### Step 3: Create the Visualization

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure('Wonderwall - Verse')
ax = fig.gca(projection='3d')

# Chord coordinates
x = [0, 7, 2, 9]
y = [3, 4, 5, 4]
z = [10, 0, 7, 10]

# Plot
ax.scatter(x, y, z, c='r', s=50)
ax.plot(x, y, z, color='blue', linewidth=2)

# Labels
ax.set_xlabel('Root')
ax.set_ylabel('Third')
ax.set_zlabel('Seventh')
ax.set_title('Wonderwall - Verse Progression')

plt.show()
```

### Step 4: Calculate Curvature

```python
from twodimcurvcalc import TwoDimCurvCalc

# Use X and Y coordinates for 2D curvature
curvature = TwoDimCurvCalc(x, y)
print(f"Wonderwall verse curvature: {curvature}°")
```

## Interpreting Results

### Visual Patterns

#### Circular/Closed Patterns
- Indicates cyclic progressions
- Common in verse-chorus structures
- Example: 12-bar blues

#### Linear Patterns
- Indicates directional progressions
- Often found in bridges
- Suggests modulation or development

#### Spiral Patterns
- Indicates repeated progressions with variation
- Common in extended jams
- Shows gradual harmonic evolution

### Curvature Values

| Range | Interpretation | Musical Characteristics |
|-------|---------------|------------------------|
| 0-90° | Very smooth | Diatonic, predictable |
| 90-180° | Moderate | Some unexpected changes |
| 180-360° | Complex | Chromatic, surprising |
| 360°+ | Very complex | Highly chromatic, experimental |

### Comparing Songs

```python
# Compare two songs
songs = {
    'Imagine': 245.3,
    'Yellow Submarine': 189.7,
    'Hotel California': 312.5
}

for song, curv in songs.items():
    print(f"{song}: {curv}°")
```

## Advanced Techniques

### Multiple Sections Analysis

Compare different sections of the same song:

```python
# Analyze verse vs chorus
verse_curv = TwoDimCurvCalc(verse_x, verse_y)
chorus_curv = TwoDimCurvCalc(chorus_x, chorus_y)

print(f"Verse curvature: {verse_curv}°")
print(f"Chorus curvature: {chorus_curv}°")
print(f"Difference: {abs(verse_curv - chorus_curv)}°")
```

### Customizing Visualizations

#### Change Colors by Section
```python
# Verse in blue, chorus in red
ax.plot(verse_x, verse_y, verse_z, color='blue', label='Verse')
ax.plot(chorus_x, chorus_y, chorus_z, color='red', label='Chorus')
ax.legend()
```

#### Adjust Point Sizes
```python
# Larger dots for emphasis chords
sizes = [100, 50, 50, 100]  # First and last chords larger
ax.scatter(x, y, z, c='r', s=sizes)
```

#### Add Annotations
```python
# Label specific chords
chord_names = ['C', 'Am', 'F', 'G']
for i, name in enumerate(chord_names):
    ax.text(x[i], y[i], z[i], name, fontsize=12)
```

### Exporting Results

#### Save Figures
```python
plt.savefig('my_song_analysis.png', dpi=300, bbox_inches='tight')
```

#### Export Data
```python
import csv

with open('curvature_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Song', 'Section', 'Curvature'])
    writer.writerow(['Imagine', 'Verse', verse_curv])
    writer.writerow(['Imagine', 'Chorus', chorus_curv])
```

### Batch Analysis

Analyze multiple songs at once:

```python
import os
import glob

songs = glob.glob('*.py')
results = {}

for song_file in songs:
    if song_file != 'twodimcurvcalc.py':
        # Extract coordinates and calculate
        # (Implementation depends on your data format)
        pass
```

## Troubleshooting

### Common Issues

**Issue**: Plot doesn't show
```python
# Solution: Make sure to call plt.show()
plt.show()
```

**Issue**: "projection='3d'" deprecated warning
```python
# Solution: Use newer syntax
ax = fig.add_subplot(111, projection='3d')
```

**Issue**: Curvature calculation returns NaN
```python
# Solution: Check for duplicate points
# Remove consecutive duplicates before calculation
```

## Tips and Best Practices

1. **Start Simple**: Begin with well-known songs to understand the patterns
2. **Compare Genres**: Analyze songs from different genres to see geometric differences
3. **Document Your Mappings**: Keep track of your chord-to-coordinate mappings
4. **Use Consistent Scales**: Keep axis scales consistent for fair comparisons
5. **Experiment**: Try different projections and visualizations

## Next Steps

- Read `THEORY.md` for mathematical background
- Explore the song files to see real examples
- Create your own analyses of favorite songs
- Contribute your findings to the repository

---

*Happy analyzing! Remember: every song has a unique geometric fingerprint.*
