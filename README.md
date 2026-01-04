# Musical Curvature: A Geometric Approach to Chord Progression Analysis

[![Research Paper](https://img.shields.io/badge/Paper-Bridges%202022-blue)](https://archive.bridgesmathart.org/2022/bridges2022-461.pdf)
[![Python](https://img.shields.io/badge/Python-3.7+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

This repository contains research code and visualizations for analyzing musical chord progressions through geometric curvature. The project maps musical chords into 3D coordinate space and calculates their curvature, revealing hidden geometric patterns in popular songs.

<img width="1473" height="346" alt="image" src="https://github.com/user-attachments/assets/c7b67cea-9373-46b2-baf7-26d11e10d4d7" />

**Based on the research paper**: *"Musical Curvature: A Geometric Approach to Chord Progression Analysis"* presented at Bridges 2022 Conference on Mathematics, Art, Music, Architecture, Culture.

## What is Musical Curvature?

Musical curvature is a novel approach to understanding chord progressions by:

1. **Mapping chords to 3D space**: Each chord (major, minor, seventh) is represented as coordinates [X, Y, Z]
2. **Calculating geometric curvature**: The path traced by chord progressions forms a curve in 3D space
3. **Analyzing patterns**: Different songs create distinct geometric shapes that can be analyzed mathematically

### The Mathematical Framework

- **Chord Representation**: Triads and seventh chords are mapped to coordinates based on their intervallic structure
- **Curvature Calculation**: Using differential geometry principles to measure how the chord progression "bends" in space
- **Pattern Recognition**: Identifying recurring geometric motifs across different musical genres and compositions

## Repository Structure

```
Musical-curvature/
├── README.md                          # This file
├── twodimcurvcalc.py                 # 2D curvature calculation algorithm
├── [song_name].py                    # Individual song analyses (3D visualizations)
├── [SONG_NAME]                       # Chord progression data files
└── examples/                         # (to be added) Documented examples
```

## Featured Song Analyses

This repository includes geometric analyses of classic songs:

### Beatles
- **Imagine** - Verse, chorus, and bridge visualizations
- **Yellow Submarine** - Repetitive chord pattern analysis
- **Come Together** - Complex progression geometry
- **Get Back** - Blues-rock curvature patterns

### Classic Rock
- **Hotel California** (Eagles) - Iconic progression mapping
- **Knocking on Heaven's Door** (Bob Dylan) - Simple yet effective geometry
- **Paradise City** (Guns N' Roses) - Hard rock curvature

### Contemporary
- **Shape of You** (Ed Sheeran) - Modern pop geometry
- **I'm Yours** (Jason Mraz) - Reggae-influenced patterns

And many more...

## Quick Start

### Prerequisites

```bash
pip install numpy matplotlib
```

### Running a Visualization

```python
# Example: Visualize "Imagine" by John Lennon
python imagine.py
```

This will generate 3D plots showing:
- Red dots: Individual chord positions
- Colored lines: Chord progression paths
- Separate figures for verse, chorus, and bridge

### Calculating Curvature

```python
from twodimcurvcalc import TwoDimCurvCalc

# Define chord progression as coordinates
x = [1, 4, 4, 1]  # X coordinates
y = [4, 4, 0, 0]  # Y coordinates

# Calculate total curvature
curvature = TwoDimCurvCalc(x, y)
print(f"Total curvature: {curvature}°")
```

## Research Questions

This project explores:

1. **Do similar-sounding songs have similar geometric patterns?**
2. **Can genre be predicted from curvature characteristics?**
3. **What geometric properties correlate with musical "tension" and "resolution"?**
4. **Are there universal geometric motifs in popular music?**

## Mathematical Background

### Chord Mapping System

The coordinate system maps musical intervals to spatial dimensions:
- **X-axis**: Root note relationships
- **Y-axis**: Third intervals (major/minor quality)
- **Z-axis**: Seventh intervals and extensions

### Curvature Formula

The curvature κ at each point in the progression is calculated using:

```
κ = |dT/ds|
```

Where:
- T is the unit tangent vector
- s is arc length along the curve

For discrete chord progressions, we calculate angular changes between successive chord vectors.

## Contributing

We welcome contributions! Areas of interest:

- **New song analyses**: Add more songs with documented chord progressions
- **Improved algorithms**: Enhance curvature calculation methods
- **Visualization tools**: Create interactive 3D viewers
- **Statistical analysis**: Find correlations between geometric and musical properties
- **Machine learning**: Train models to recognize patterns

## Research Team

This is an ongoing research project exploring the intersection of mathematics, geometry, and music theory.

## Citation

If you use this work in your research, please cite:

```bibtex
@inproceedings{musical-curvature-2022,
  title={Musical Curvature: A Geometric Approach to Chord Progression Analysis},
  booktitle={Bridges 2022 Conference Proceedings},
  year={2022},
  pages={461-468}
}
```

## Future Directions

- **4D+ representations**: Incorporating rhythm and dynamics
- **Real-time analysis**: Live visualization of musical performances
- **Comparative studies**: Cross-cultural musical geometry
- **Composition tools**: Using geometric principles to generate new progressions

## License

MIT License - See LICENSE file for details

## Acknowledgments

Special thanks to the Bridges Conference community for fostering interdisciplinary research in mathematics and the arts.

---

*"Music is the pleasure the human mind experiences from counting without being aware that it is counting." - Gottfried Wilhelm Leibniz*
