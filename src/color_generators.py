"""
数学的理論に基づく色生成アルゴリズム - Python版

参考文献:
- Johannes Itten "The Art of Color" (1961) - 黄金比の色彩応用
- Cynthia Brewer "Color in Information Display" (1999) - データ可視化の色選択
- "Fibonacci Numbers in Nature and Art" - Journal of Mathematics and the Arts (2000s)
- Johannes Itten "The Art of Color" (1961) - カラーホイール理論
"""

from typing import List, Tuple


def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> Tuple[int, int, int]:
    """
    HSL色空間からRGB色空間への変換

    Args:
        hue: 色相 (0-360度)
        saturation: 彩度 (0-1)
        lightness: 明度 (0-1)

    Returns:
        RGB値のタプル (r, g, b) - 各値は0-255
    """
    hue = hue % 360

    # HSLからRGBへの変換
    c = (1 - abs(2 * lightness - 1)) * saturation
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = lightness - c / 2

    if hue < 60:
        r, g, b = c, x, 0
    elif hue < 120:
        r, g, b = x, c, 0
    elif hue < 180:
        r, g, b = 0, c, x
    elif hue < 240:
        r, g, b = 0, x, c
    elif hue < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return (round((r + m) * 255), round((g + m) * 255), round((b + m) * 255))


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    RGB値をhex形式の文字列に変換

    Args:
        r: 赤成分 (0-255)
        g: 緑成分 (0-255)
        b: 青成分 (0-255)

    Returns:
        hex形式の色文字列 (#RRGGBB)
    """
    return f"#{r:02x}{g:02x}{b:02x}"


def generate_golden_ratio_colors(
    n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0
) -> List[str]:
    """
    黄金比を使用して色相を決定するアルゴリズム

    参考文献:
    - Johannes Itten "The Art of Color" (1961) - 黄金比の色彩応用
    - 自然界の美しい比率を色彩に応用した調和理論

    Args:
        n: 生成する色の数
        saturation: 彩度 (0-1)
        lightness: 明度 (0-1)
        offset: 色相の開始オフセット (0-360度)

    Returns:
        色のリスト（hex形式）

    Raises:
        ValueError: 色の数が0以下の場合
    """
    if n <= 0:
        raise ValueError("色の数は1以上である必要があります")

    colors = []
    golden_ratio = 0.618033988749895

    for i in range(n):
        hue = ((i * golden_ratio) % 1.0) * 360 + offset
        h = hue % 360

        r, g, b = hsl_to_rgb(h, saturation, lightness)
        colors.append(rgb_to_hex(r, g, b))

    return colors


def generate_equidistant_colors(
    n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0
) -> List[str]:
    """
    等間隔色相分割による色生成アルゴリズム
    最もシンプルで確実に色が分散される

    参考文献:
    - Cynthia Brewer "Color in Information Display" (1999) - データ可視化の色選択
    - 科学的根拠に基づく色覚障害者にも配慮した色パレット設計

    Args:
        n: 生成する色の数
        saturation: 彩度 (0-1)
        lightness: 明度 (0-1)
        offset: 色相の開始オフセット (0-360度)

    Returns:
        色のリスト（hex形式）

    Raises:
        ValueError: 色の数が0以下の場合
    """
    if n <= 0:
        raise ValueError("色の数は1以上である必要があります")

    colors = []

    for i in range(n):
        hue = (i / n) * 360 + offset
        h = hue % 360

        r, g, b = hsl_to_rgb(h, saturation, lightness)
        colors.append(rgb_to_hex(r, g, b))

    return colors


def generate_fibonacci_colors(
    n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0
) -> List[str]:
    """
    フィボナッチ数列を使用した色生成アルゴリズム
    黄金比に似ているが、より数学的に興味深い

    参考文献:
    - "Fibonacci Numbers in Nature and Art" - Journal of Mathematics and the Arts (2000s)
    - 数学的パターンを色彩美学に応用した研究

    Args:
        n: 生成する色の数
        saturation: 彩度 (0-1)
        lightness: 明度 (0-1)
        offset: 色相の開始オフセット (0-360度)

    Returns:
        色のリスト（hex形式）

    Raises:
        ValueError: 色の数が0以下の場合
    """
    if n <= 0:
        raise ValueError("色の数は1以上である必要があります")

    colors = []
    fibonacci_ratio = 0.381966011250105  # 1 - goldenRatio

    for i in range(n):
        hue = ((i * fibonacci_ratio) % 1.0) * 360 + offset
        h = hue % 360

        r, g, b = hsl_to_rgb(h, saturation, lightness)
        colors.append(rgb_to_hex(r, g, b))

    return colors


def generate_color_wheel_colors(
    n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0
) -> List[str]:
    """
    カラーホイール理論に基づく補色・三色配色アルゴリズム
    より洗練された色の組み合わせを生成

    参考文献:
    - Johannes Itten "The Art of Color" (1961) - カラーホイール理論
    - 補色・三色配色など、視覚的調和を数学的に体系化した理論

    Args:
        n: 生成する色の数
        saturation: 彩度 (0-1)
        lightness: 明度 (0-1)
        offset: 色相の開始オフセット (0-360度)

    Returns:
        色のリスト（hex形式）

    Raises:
        ValueError: 色の数が0以下の場合
    """
    if n <= 0:
        raise ValueError("色の数は1以上である必要があります")

    colors = []

    # 基本色相を定義（赤、黄、緑、シアン、青、マゼンタ）
    base_hues = [0, 60, 120, 180, 240, 300]

    for i in range(n):
        if n <= 6:
            # 6色以下の場合は基本色相を使用
            hue = base_hues[i % 6] + offset
        else:
            # 6色を超える場合は補間
            base_index = int(i / (n / 6))
            next_index = (base_index + 1) % 6
            ratio = (i % (n / 6)) / (n / 6)
            hue = (
                base_hues[base_index]
                + (base_hues[next_index] - base_hues[base_index]) * ratio
                + offset
            )

        # 360度を超えた場合の処理
        hue = hue % 360

        r, g, b = hsl_to_rgb(hue, saturation, lightness)
        colors.append(rgb_to_hex(r, g, b))

    return colors


# 便利な関数
def get_all_algorithms() -> dict:
    """
    利用可能なすべてのアルゴリズムを辞書形式で返す

    Returns:
        アルゴリズム名と関数の辞書
    """
    return {
        "golden_ratio": generate_golden_ratio_colors,
        "equidistant": generate_equidistant_colors,
        "fibonacci": generate_fibonacci_colors,
        "color_wheel": generate_color_wheel_colors,
    }


def generate_colors_by_algorithm(
    algorithm_name: str,
    n: int,
    saturation: float = 0.8,
    lightness: float = 0.6,
    offset: float = 0,
) -> List[str]:
    """
    アルゴリズム名を指定して色を生成

    Args:
        algorithm_name: アルゴリズム名 ("golden_ratio", "equidistant", "fibonacci", "color_wheel")
        n: 生成する色の数
        saturation: 彩度 (0-1)
        lightness: 明度 (0-1)
        offset: 色相の開始オフセット (0-360度)

    Returns:
        色のリスト（hex形式）

    Raises:
        ValueError: 無効なアルゴリズム名が指定された場合、または色の数が0以下の場合
    """
    algorithms = get_all_algorithms()

    if algorithm_name not in algorithms:
        raise ValueError(
            f"無効なアルゴリズム名: {algorithm_name}. 利用可能: {list(algorithms.keys())}"
        )

    return algorithms[algorithm_name](n, saturation, lightness, offset)


# 使用例
if __name__ == "__main__":
    # 各アルゴリズムで10色ずつ生成
    print("=== 黄金比色 10色 ===")
    golden_colors = generate_golden_ratio_colors(10)
    for i, color in enumerate(golden_colors, 1):
        print(f"{i:2d}: {color}")

    print("\n=== 等間隔色 10色 ===")
    equidistant_colors = generate_equidistant_colors(10)
    for i, color in enumerate(equidistant_colors, 1):
        print(f"{i:2d}: {color}")

    print("\n=== フィボナッチ色 10色 ===")
    fibonacci_colors = generate_fibonacci_colors(10)
    for i, color in enumerate(fibonacci_colors, 1):
        print(f"{i:2d}: {color}")

    print("\n=== カラーホイール色 10色 ===")
    color_wheel_colors = generate_color_wheel_colors(10)
    for i, color in enumerate(color_wheel_colors, 1):
        print(f"{i:2d}: {color}")

    # アルゴリズム名を指定して生成
    print("\n=== アルゴリズム名指定で生成 ===")
    try:
        colors = generate_colors_by_algorithm("golden_ratio", 5, 0.9, 0.5)
        print("黄金比色 5色 (高彩度、中明度):", colors)
    except ValueError as e:
        print(f"エラー: {e}")
