# Contributing to Musical Curvature

Thank you for your interest in contributing to the Musical Curvature project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:
1. Check if the issue already exists in the Issues section
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (Python version, OS, etc.)

### Adding New Song Analyses

We welcome analyses of new songs! To contribute:

1. **Fork the repository**
2. **Create a new branch**: `git checkout -b add-song-name`
3. **Create your analysis file**: `song_name.py`
4. **Follow the standard format**:

```python
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Song: [Song Name]
# Artist: [Artist Name]
# Section: [Verse/Chorus/Bridge]

fig = plt.figure('[Song Name] - [Section]')
ax = fig.gca(projection='3d')

# Chord progression coordinates
x, y, z = [...], [...], [...]

ax.scatter(x, y, z, c='r', s=50)
ax.plot(x, y, z, color='blue')

ax.set_xlabel('Root')
ax.set_ylabel('Third')
ax.set_zlabel('Seventh')
ax.set_title('[Song Name] - [Section]')

plt.show()
```

5. **Document your chord mapping**: Create a text file with the chord progression
6. **Test your code**: Ensure it runs without errors
7. **Commit and push**: 
   ```bash
   git add song_name.py
   git commit -m "Add analysis for [Song Name] by [Artist]"
   git push origin add-song-name
   ```
8. **Create a Pull Request**

### Improving the Curvature Algorithm

If you have improvements to the curvature calculation:

1. Document the mathematical basis
2. Provide test cases showing improvements
3. Maintain backward compatibility or provide migration guide
4. Update `THEORY.md` with new methodology

### Code Style Guidelines

- Use descriptive variable names
- Add comments for complex calculations
- Follow PEP 8 style guide for Python
- Keep functions focused and modular

### Documentation

When adding features:
- Update relevant `.md` files
- Add examples to `USAGE_GUIDE.md`
- Include docstrings in functions
- Update README if needed

## Research Contributions

### Theoretical Contributions

If you have insights about the mathematical framework:
- Write a detailed explanation
- Provide references to relevant literature
- Include examples demonstrating the concept
- Submit as an issue or discussion first

### Empirical Studies

If you've conducted analysis on multiple songs:
- Share your methodology
- Provide data and code
- Include visualizations
- Discuss findings and implications

## Pull Request Process

1. **Update documentation** for any changes
2. **Add tests** if applicable
3. **Ensure all tests pass**
4. **Update CHANGELOG** (if exists)
5. **Request review** from maintainers

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Credit others' work appropriately
- Focus on the research and learning

## Questions?

- Open a Discussion for general questions
- Use Issues for specific problems
- Tag maintainers for urgent matters

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for helping advance the intersection of mathematics and music!
