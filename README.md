# Lagrange Interpolator
Implementation of Lagrange interpolation to find a polynomial that passes
through a given set of points (x,y)

This is a really really early implementation of this method, so don't expect
much for now

## Requirements

- Python 3.10 or newer
- SymPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cadusouza1/lagrange-interpolator.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Provide the x and y coordinates of the points in the `lagrange-interpolator.py` file.
2. Run `python lagrange-interpolator.py`
3. The polynomial will be printed in its expanded form.

### Example

```python
x_coordinates = [1, 2, 3, 4]
y_coordinates = [2, 3, 4, 5]

# Output: x + 1
```
