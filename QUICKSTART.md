# Quick Start Guide

Get up and running with Musical Curvature analysis in 5 minutes!

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/dvirchakim/Musical-curvature.git
cd Musical-curvature

# 2. Install dependencies
pip install -r requirements.txt
```

## Your First Visualization

```bash
# Run a simple example
python examples/basic_visualization.py
```

You should see a 3D plot showing a I-IV-V-I chord progression!

## Try a Real Song

```bash
# Visualize "Imagine" by John Lennon
python imagine.py
```

This will show three separate plots for verse, chorus, and bridge.

## Calculate Curvature

```python
# Create a new file: my_analysis.py
from twodimcurvcalc import TwoDimCurvCalc

# Define your chord progression
x = [0, 5, 7, 0]  # I-IV-V-I
y = [4, 4, 4, 4]  # All major chords

# Calculate
curvature = TwoDimCurvCalc(x, y)
print(f"Curvature: {curvature}°")
```

Run it:
```bash
python my_analysis.py
```

## Next Steps

1. **Learn the theory**: Read [`THEORY.md`](THEORY.md)
2. **Explore examples**: Check out the [`examples/`](examples/) directory
3. **Analyze your favorite songs**: Use existing files as templates
4. **Read the full guide**: See [`USAGE_GUIDE.md`](USAGE_GUIDE.md)

## Common Commands

```bash
# Run all examples
python examples/basic_visualization.py
python examples/curvature_calculation.py
python examples/multi_section_analysis.py

# Analyze specific songs
python "Yellow submarine.py"
python "hotel california.py"
python africa.py
```

## Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'matplotlib'`
```bash
pip install matplotlib numpy
```

**Problem**: Plot doesn't appear
- Make sure you have a display/GUI environment
- On remote servers, you may need X11 forwarding

**Problem**: Deprecated warning about `projection='3d'`
- This is just a warning, the code still works
- We'll update to the newer syntax in future versions

## Quick Reference

### Coordinate System
- **X-axis**: Root note position
- **Y-axis**: Third quality (major/minor)
- **Z-axis**: Seventh extensions

### Curvature Ranges
- **0-90°**: Simple, predictable
- **90-180°**: Moderate complexity
- **180-360°**: Complex progressions
- **360°+**: Highly chromatic

## Get Help

- 📖 Read the [full documentation](README.md)
- 💬 Open an [issue](https://github.com/dvirchakim/Musical-curvature/issues)
- 🤝 Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

---

Happy analyzing! 🎵📐
