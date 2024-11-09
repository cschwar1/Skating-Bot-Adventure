# Skating Bot Adventure Developer Guide

This guide provides information for developers who want to contribute to the Skating Bot Adventure game.

## Setting Up the Development Environment

1. Clone the repository:
   ```
   git clone https://github.com/your-username/skating-bot-adventure.git
   cd skating-bot-adventure
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Project Structure

- `src/`: Contains the main source code
  - `main.py`: Entry point of the application
  - `game/`: Game logic and objects
  - `utils/`: Utility functions and classes
  - `assets/`: Game assets (images, sounds)
- `tests/`: Unit tests
- `docs/`: Documentation files

## Coding Standards

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Write docstrings for all functions, classes, and modules
- Keep functions small and focused on a single task

## Adding New Features

1. Create a new branch for your feature
2. Implement the feature in the appropriate module
3. Add unit tests for the new feature
4. Update the README.md if necessary
5. Submit a pull request

## Testing

Run unit tests using:
```
python -m unittest discover tests
```

Add new tests in the `tests/` directory, following the existing test structure.

## Asset Management

- Place new images in `src/assets/images/`
- Place new sound files in `src/assets/sounds/`
- Update `src/utils/assets.py` when adding new assets

## Educational Content

To add new educational content:

1. Open `src/utils/education.py`
2. Add new math problems, spelling challenges, or fun facts to the appropriate lists
3. If adding a new type of educational content, update the `EducationManager` class accordingly

## Releasing New Versions

1. Update the version number in `src/utils/constants.py`
2. Update the CHANGELOG.md file with the changes
3. Create a new release on GitHub with a tag matching the version number

## Getting Help

If you have any questions or need assistance, please open an issue on the GitHub repository or contact the maintainers directly.

Thank you for contributing to Skating Bot Adventure!