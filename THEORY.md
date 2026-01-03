# Mathematical Theory Behind Musical Curvature

## Introduction

This document explains the mathematical foundations of representing musical chord progressions as geometric curves in 3D space and calculating their curvature.

## Chord Representation System

### Basic Principle

Every chord in Western music can be decomposed into intervals from a root note. We map these intervals to coordinates in 3D space:

- **X-coordinate**: Represents the root note position
- **Y-coordinate**: Represents the third (major vs minor quality)
- **Z-coordinate**: Represents the seventh and other extensions

### Coordinate Mapping

#### Major Triads
A major triad consists of:
- Root (0 semitones)
- Major third (4 semitones)
- Perfect fifth (7 semitones)

#### Minor Triads
A minor triad consists of:
- Root (0 semitones)
- Minor third (3 semitones)
- Perfect fifth (7 semitones)

#### Seventh Chords
Seventh chords add an additional note:
- Dominant 7th: Major triad + minor seventh (10 semitones)
- Major 7th: Major triad + major seventh (11 semitones)
- Minor 7th: Minor triad + minor seventh (10 semitones)

### Example Mappings

From the code analysis:
```
C major:  [x, y, z] = [0, 4, 7]
C minor:  [x, y, z] = [0, 3, 7]
C7:       [x, y, z] = [0, 4, 10]
```

## Curvature Calculation

### 2D Curvature (Simplified Model)

The `twodimcurvcalc.py` implements a discrete curvature calculation for chord progressions projected onto a 2D plane.

#### Algorithm Steps

1. **Vector Construction**
   - For each consecutive pair of chords, create a vector:
   ```
   v_i = (x_{i+1} - x_i, y_{i+1} - y_i)
   ```

2. **Angle Calculation**
   - Calculate the angle between successive vectors using the dot product:
   ```
   cos(α) = (v_i · v_{i+1}) / (||v_i|| × ||v_{i+1}||)
   ```

3. **Total Curvature**
   - Sum all angular changes:
   ```
   κ_total = Σ α_i
   ```

### Mathematical Formulation

For a discrete curve defined by points P₀, P₁, ..., Pₙ:

```
Total Curvature = Σ(i=0 to n-2) arccos(|v_i · (-v_{i+1})| / (||v_i|| × ||v_{i+1}||))
```

Where:
- `v_i` is the vector from P_i to P_{i+1}
- `·` denotes dot product
- `|| ||` denotes vector magnitude

### Closing the Loop

For cyclic progressions (songs that return to the starting chord), we add:
```
α_closing = 180° - arccos((v_n · (-v_0)) / (||v_n|| × ||v_0||))
```

## 3D Visualization

### Parametric Curve Representation

A chord progression in 3D space forms a parametric curve:
```
γ(t) = (x(t), y(t), z(t))
```

Where t represents the position in the progression (discrete time steps).

### Curvature in 3D

For continuous curves, the curvature at any point is:
```
κ(t) = ||γ'(t) × γ''(t)|| / ||γ'(t)||³
```

For discrete points, we approximate using angular changes in 3D space.

## Geometric Interpretation

### What Does Curvature Mean Musically?

- **High Curvature**: Sharp changes in harmonic direction
  - Unexpected chord changes
  - Modulations
  - Chromatic movements

- **Low Curvature**: Smooth harmonic flow
  - Diatonic progressions
  - Common chord sequences (I-IV-V)
  - Predictable patterns

- **Zero Curvature**: Straight line
  - Repeated chords
  - Pedal points

### Closed vs Open Curves

- **Closed Curves**: Progressions that return to the starting chord
  - Verse-chorus patterns
  - 12-bar blues
  - Total curvature relates to the winding number

- **Open Curves**: Progressions that end on a different chord
  - Modulating sequences
  - Through-composed sections

## Advanced Concepts

### Torsion

While not implemented in the current code, torsion measures how much the curve twists out of its osculating plane:
```
τ = (γ' × γ'') · γ''' / ||γ' × γ''||²
```

This could represent:
- Voice leading complexity
- Harmonic tension beyond simple chord changes

### Frenet-Serret Frame

The moving frame along the curve consists of:
- **Tangent (T)**: Direction of chord progression
- **Normal (N)**: Direction of maximum curvature
- **Binormal (B)**: Perpendicular to both

These could represent different aspects of harmonic motion.

## Practical Applications

### Pattern Recognition

Songs with similar geometric properties may:
- Sound harmonically similar
- Belong to the same genre
- Use similar compositional techniques

### Composition Tool

By analyzing curvature patterns of successful songs, composers could:
- Generate new progressions with desired geometric properties
- Identify points of high/low harmonic tension
- Create variations that maintain geometric similarity

### Music Information Retrieval

Curvature features could be used for:
- Automatic genre classification
- Cover song detection
- Harmonic similarity search

## Limitations and Future Work

### Current Limitations

1. **Discrete Approximation**: We use discrete points rather than continuous curves
2. **2D Projection**: Most calculations use 2D projections of 3D data
3. **Fixed Mapping**: The chord-to-coordinate mapping is somewhat arbitrary
4. **No Rhythm**: Temporal aspects are not considered

### Future Enhancements

1. **Weighted Curvature**: Account for chord duration
2. **Dynamic Mapping**: Adapt coordinate system to key/mode
3. **Higher Dimensions**: Include rhythm, dynamics, timbre
4. **Statistical Analysis**: Large-scale corpus studies

## References

### Differential Geometry
- Do Carmo, M. P. (1976). *Differential Geometry of Curves and Surfaces*
- Pressley, A. (2010). *Elementary Differential Geometry*

### Music Theory
- Tymoczko, D. (2011). *A Geometry of Music*
- Cohn, R. (1996). "Maximally Smooth Cycles, Hexatonic Systems, and the Analysis of Late-Romantic Triadic Progressions"

### Computational Music Analysis
- Temperley, D. (2007). *Music and Probability*
- Müllensiefen, D., & Frieler, K. (2004). "Cognitive Adequacy in the Measurement of Melodic Similarity"

---

*This theoretical framework provides the mathematical foundation for understanding music through the lens of geometric curvature.*
