# GenerateColor

A library that provides color generation algorithms based on mathematical theories. It offers both TypeScript and Python versions, generating beautiful color combinations based on the golden ratio, equidistant division, Fibonacci sequence, and color wheel theory.

English | [日本語](README.md)

## Demo

To see the actual implementation in action, please visit the [demo page](https://www.johnkiyo.com/GenerateColor/).

## Implemented Algorithms

### 1. Golden Ratio

Uses the beautiful ratio found in nature to determine hue. The golden ratio has a value of approximately 1.618 and is a harmonious ratio commonly found in nature.

### 2. Equidistant Division

Generates colors by dividing the hue spectrum equally. The simplest and most reliable method for color distribution, suitable for data visualization and UI design.

### 3. Fibonacci Sequence

Uses the reciprocal of the Fibonacci sequence to determine hue. Similar to the golden ratio but generates a more mathematically interesting distribution.

### 4. Color Wheel

Generates colors based on Johannes Itten's color wheel theory. Implements mathematically systematized theories of visual harmony including complementary and triadic color schemes.

### 5. Alternating Color Generation 🆕

Generates colors by dividing the cold color range (200°-300°) into n parts. Even indices use cold colors, odd indices use their complementary colors (warm colors), creating a unified color combination.

## Usage

### TypeScript Version

#### TypeScript Basic Usage

```typescript
import {
  Color,
  GoldenRatioColorGenerator,
  EquidistantColorGenerator,
  FibonacciColorGenerator,
  ColorWheelColorGenerator,
  AlternatingColorGenerator,
} from 'generate-color';

// Using Golden Ratio algorithm
const goldenColor = new Color(new GoldenRatioColorGenerator());
const colors = goldenColor.generate(5);
console.log(colors); // ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']

// Using Equidistant algorithm
const equidistantColor = new Color(new EquidistantColorGenerator());
const colors = equidistantColor.generate(6);
console.log(colors); // ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff']

// Using Alternating Color Generation algorithm
const alternatingColor = new Color(new AlternatingColorGenerator());
const alternatingColors = alternatingColor.generate(10);
console.log(alternatingColors); // Flexible color combinations with cold color range divided into n parts
```

#### TypeScript Parameter Adjustment

```typescript
// Adjust saturation and lightness
const colors = goldenColor.generate(3, 0.9, 0.5);

// Adjust hue starting position
const colors = equidistantColor.generate(3, 0.8, 0.6, 90);
```

### Python Version

#### Python Basic Usage

```python
from src.color_generators import (
    Color,
    GoldenRatioColorGenerator,
    EquidistantColorGenerator
)

# Using Golden Ratio algorithm
golden_color = Color(GoldenRatioColorGenerator())
colors = golden_color.generate(5)
print(colors)  # ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']

# Using Equidistant algorithm
equidistant_color = Color(EquidistantColorGenerator())
colors = equidistant_color.generate(6)
print(colors)  # ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff']
```

#### Python Parameter Adjustment

```python
# Adjust saturation and lightness
colors = golden_color.generate(3, saturation=0.9, lightness=0.5)

# Adjust hue starting position
colors = equidistant_color.generate(3, offset=90)
```

#### Direct Instantiation

```python
from src.color_generators import GoldenRatioColorGenerator

generator = GoldenRatioColorGenerator()
colors = generator.generate_colors(8, saturation=0.9, lightness=0.5)
```

## API Reference

### TypeScript API

#### TypeScript Color Class

```typescript
class Color {
  constructor(colorGenerator: ColorGenerator);
  generate(n: number, saturation?: number, lightness?: number, offset?: number): string[];
}
```

#### TypeScript ColorGenerator Interface

```typescript
interface ColorGenerator {
  generateColors(n: number, saturation?: number, lightness?: number, offset?: number): string[];
}
```

#### Implementation Classes

```typescript
class GoldenRatioColorGenerator implements ColorGenerator
class EquidistantColorGenerator implements ColorGenerator
class FibonacciColorGenerator implements ColorGenerator
class ColorWheelColorGenerator implements ColorGenerator
class AlternatingColorGenerator implements ColorGenerator
```

### Python API

#### Python Color Class

```python
class Color:
    def __init__(self, color_generator: ColorGenerator)
    def generate(self, n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0) -> List[str]
```

#### Python ColorGenerator Abstract Class

```python
class ColorGenerator(ABC):
    @abstractmethod
    def generate_colors(self, n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0) -> List[str]
```

### Common Parameters

- `n`: Number of colors to generate (integer >= 1)
- `saturation`: Saturation (0.0-1.0 range, default: 0.8)
- `lightness`: Lightness (0.0-1.0 range, default: 0.6)
- `offset`: Hue starting offset (0-360 degrees, default: 0)

### Return Value

Array/list of hex color strings (e.g., `["#ff0000", "#00ff00", "#0000ff"]`)

## Development Environment

This project uses GitHub Actions to run the following automated checks:

- **TypeScript**: ESLint + Prettier
- **Python**: Black + isort + flake8 (PEP8 compliant)

When you create a pull request, code quality checks are automatically executed.

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/xxxx-feature`)
3. Commit your changes (`git commit -m 'Add xxxx feature'`)
4. Push to the branch (`git push origin feature/xxxx-feature`)
5. Create a Pull Request

**Note**: We recommend running code quality checks locally before creating a pull request.

## License

This project is published under the MIT License. See the [LICENSE](LICENSE) file for details.

## References

- "Introduction, Explanation & Calculation," Golden Ratio Colors.[https://goldenratiocolors.com/introduction-explanation-calculation-golden-ratio-colours/](https://goldenratiocolors.com/introduction-explanation-calculation-golden-ratio-colours/)
- J. Chao, I. Osugi, and M. Suzuki, "On Definitions and Construction of Uniform Color Space," in Conference on Colour in Graphics, Imaging, and Vision, vol. 2, no. 1, 2004, p. 55. doi: 10.2352/CGIV.2004.2.1.art00012.
- J. Itten, The Art of Color. [https://www.blinkist.com/en/books/the-art-of-color-en](https://www.blinkist.com/en/books/the-art-of-color-en)
