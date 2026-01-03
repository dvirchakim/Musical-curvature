# Project Overview: Musical Curvature

## What This Project Does

Musical Curvature is a research project that applies differential geometry to music theory. It transforms chord progressions into 3D curves and analyzes their geometric properties to understand musical structure.

### Core Concept

**Traditional Music Theory**: Analyzes chords through functional harmony, voice leading, and tonal relationships.

**Musical Curvature**: Maps chords to 3D coordinates and studies the geometry of the resulting curves.

## Key Innovation

By representing music as geometric curves, we can:
- **Visualize** harmonic relationships spatially
- **Quantify** musical complexity through curvature
- **Compare** songs using geometric metrics
- **Discover** patterns invisible in traditional notation

## Research Questions

1. Do songs that sound similar have similar geometric shapes?
2. Can we predict genre from curvature characteristics?
3. What geometric properties correlate with musical tension/resolution?
4. Are there universal geometric motifs in popular music?

## Technical Approach

### 1. Chord Mapping
Each chord is mapped to 3D coordinates based on:
- Root position (X-axis)
- Third quality - major/minor (Y-axis)  
- Seventh extensions (Z-axis)

### 2. Curve Construction
Consecutive chords form a parametric curve in 3D space:
```
γ(t) = (x(t), y(t), z(t))
```

### 3. Curvature Calculation
We calculate how much the curve "bends" using discrete differential geometry:
```
κ = Σ angular_changes_between_consecutive_vectors
```

### 4. Analysis & Visualization
- 3D plots show the geometric shape of progressions
- Curvature values quantify harmonic complexity
- Comparisons reveal patterns across songs

## Repository Components

### Core Algorithm
- **`twodimcurvcalc.py`**: Curvature calculation engine

### Song Analyses
- **27 song files**: Individual visualizations of popular songs
- **Multiple genres**: Rock, pop, folk, reggae, soul, jazz influences
- **Classic artists**: Beatles, Dylan, Eagles, Pink Floyd, etc.

### Documentation
- **`README.md`**: Project introduction and overview
- **`THEORY.md`**: Mathematical foundations
- **`USAGE_GUIDE.md`**: Detailed how-to guide
- **`QUICKSTART.md`**: Get started in 5 minutes
- **`CONTRIBUTING.md`**: Contribution guidelines
- **`SONG_LIST.md`**: Complete catalog of analyzed songs

### Examples
- **`examples/`**: Three educational examples
  - Basic visualization
  - Curvature calculation
  - Multi-section analysis

## Use Cases

### For Researchers
- Study harmonic patterns across large music corpora
- Test hypotheses about musical structure
- Develop new music theory frameworks

### For Musicians
- Understand chord progressions geometrically
- Analyze favorite songs in a new way
- Generate new progressions with desired properties

### For Educators
- Teach music theory through visualization
- Demonstrate abstract concepts concretely
- Engage students with interdisciplinary connections

### For Data Scientists
- Extract features for music information retrieval
- Build classification models
- Develop recommendation systems

## Current Findings

### Observations from Analyzed Songs

1. **Cyclic progressions** (returning to tonic) form closed curves
2. **Diatonic progressions** have lower curvature (smoother)
3. **Chromatic movements** increase curvature significantly
4. **Jazz progressions** tend to have higher curvature than pop
5. **Verse sections** often have lower curvature than choruses

### Patterns Identified

- **I-IV-V-I**: Forms a simple triangular path
- **ii-V-I**: Creates characteristic jazz geometry
- **Chromatic descents**: Produce spiral-like patterns
- **Modal interchange**: Causes sharp angular changes

## Future Directions

### Short Term
- Analyze more songs (target: 100+)
- Improve coordinate mapping system
- Add rhythm and duration weighting
- Create interactive web visualizations

### Medium Term
- Statistical analysis across genres
- Machine learning for pattern recognition
- Real-time analysis tools
- Composition assistance software

### Long Term
- 4D+ representations (adding time, dynamics)
- Cross-cultural music studies
- Integration with digital audio workstations
- Educational software development

## Technical Stack

- **Python 3.7+**: Core language
- **NumPy**: Numerical computations
- **Matplotlib**: 3D visualization
- **Differential Geometry**: Mathematical framework

## Academic Context

This work sits at the intersection of:
- **Mathematics**: Differential geometry, topology
- **Music Theory**: Harmony, form, analysis
- **Computer Science**: Visualization, algorithms
- **Cognitive Science**: Perception, pattern recognition

### Related Research
- Dmitri Tymoczko's *A Geometry of Music*
- Neo-Riemannian theory
- Tonnetz representations
- Music information retrieval

## Impact & Applications

### Music Theory
- New analytical tools
- Visual teaching aids
- Computational musicology

### Composition
- Algorithmic composition
- Progression generators
- Harmonic exploration tools

### Music Technology
- Genre classification
- Cover song detection
- Similarity search
- Recommendation engines

### Education
- Interactive learning tools
- Visualization software
- Interdisciplinary curriculum

## Getting Involved

### Ways to Contribute
1. **Analyze new songs**: Add to our database
2. **Improve algorithms**: Enhance calculations
3. **Create visualizations**: Build better tools
4. **Conduct research**: Test hypotheses
5. **Write documentation**: Help others learn

### Skills Needed
- Music theory knowledge
- Python programming
- Mathematical background (helpful)
- Data visualization skills
- Research experience

## Project Status

**Current Phase**: Active Research & Development

- ✅ Core algorithm implemented
- ✅ 27 songs analyzed
- ✅ Comprehensive documentation
- ✅ Example code provided
- 🔄 Expanding song database
- 🔄 Refining methodology
- 📋 Statistical analysis (planned)
- 📋 Machine learning integration (planned)

## Contact & Collaboration

This is an open research project. We welcome:
- Academic collaborations
- Student projects
- Industry partnerships
- Community contributions

See `CONTRIBUTING.md` for details on how to get involved.

## Citation

Based on research presented at Bridges 2022 Conference:
```
Musical Curvature: A Geometric Approach to Chord Progression Analysis
Bridges Conference Proceedings, 2022, pp. 461-468
```

## License

MIT License - Free for academic and commercial use

---

## Quick Links

- 📖 [README](README.md) - Start here
- 🚀 [Quick Start](QUICKSTART.md) - Get running in 5 minutes  
- 📚 [Theory](THEORY.md) - Mathematical background
- 📘 [Usage Guide](USAGE_GUIDE.md) - Detailed instructions
- 🎵 [Song List](SONG_LIST.md) - All analyzed songs
- 🤝 [Contributing](CONTRIBUTING.md) - Join the project

---

*"The geometry of music reveals patterns that traditional notation cannot show."*
