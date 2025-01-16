# Lagrange Interpolator
Implementation of Lagrange interpolation to find a polynomial that passes
through a given set of points (x,y)

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

1. Run `python lagrange-interpolator.py -p x0 y0 x1 y1 ...`
2. The polynomial will be printed in its expanded form.

### Example

```bash
python lagrange-interpolator.py -p 1 2 3 4 5 6

# Output: x + 1
```
