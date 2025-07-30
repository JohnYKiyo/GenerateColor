"""
数学的理論に基づく色生成アルゴリズム - Python版

参考文献:

- "Introduction, Explanation & Calculation," Golden Ratio Colors.[https://goldenratiocolors.com/introduction-explanation-calculation-golden-ratio-colours/](https://goldenratiocolors.com/introduction-explanation-calculation-golden-ratio-colours/)
- J. Chao, I. Osugi, and M. Suzuki, "On Definitions and Construction of Uniform Color Space," in Conference on Colour in Graphics, Imaging, and Vision, vol. 2, no. 1, 2004, p. 55. doi: 10.2352/CGIV.2004.2.1.art00012.
- J. Itten, The Art of Color. [https://www.blinkist.com/en/books/the-art-of-color-en](https://www.blinkist.com/en/books/the-art-of-color-en)
"""

from abc import ABC, abstractmethod
from typing import List, Tuple


class ColorGenerator(ABC):
    """
    色生成アルゴリズムの抽象基底クラス

    様々な数学的理論に基づく色生成アルゴリズムの共通インターフェースを定義します。

    Attributes:
        なし（抽象クラスのため）

    Methods:
        generate_colors: 色を生成する抽象メソッド
    """

    @abstractmethod
    def generate_colors(self, n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0) -> List[str]:
        """
        色を生成する抽象メソッド

        指定された数の色を生成し、hex形式の文字列リストを返します。
        各実装クラスは、異なる数学的理論に基づいて色相を決定します。

        Args:
            n: 生成する色の数（1以上の整数）
            saturation: 彩度（0.0-1.0の範囲、デフォルト: 0.8）
            lightness: 明度（0.0-1.0の範囲、デフォルト: 0.6）
            offset: 色相の開始オフセット（0-360度、デフォルト: 0）

        Returns:
            hex形式の色文字列のリスト（例: ["#ff0000", "#00ff00", "#0000ff"]）

        Raises:
            ValueError: 色の数が0以下の場合
            TypeError: パラメータの型が不正な場合

        Example:
            >>> generator = GoldenRatioColorGenerator()
            >>> colors = generator.generate_colors(5)
            >>> print(colors)
            ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']
        """
        pass


class Color:
    """
    色生成を行うクラス

    抽象クラスColorGeneratorに依存し、具体的な実装クラスには依存しません。
    コンストラクタで色生成器を渡すことで、柔軟にアルゴリズムを切り替えることができます。

    Attributes:
        _color_generator (ColorGenerator): 設定された色生成器のインスタンス

    Methods:
        generate: 色を生成するメソッド

    Example:
        >>> golden_color = Color(GoldenRatioColorGenerator())
        >>> colors = golden_color.generate(5)
        >>> print(colors)
        ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']
    """

    def __init__(self, color_generator: ColorGenerator):
        """
        色生成器を設定してColorインスタンスを初期化

        Args:
            color_generator: 色生成アルゴリズムの実装インスタンス

        Raises:
            TypeError: color_generatorがColorGeneratorのインスタンスでない場合

        Example:
            >>> generator = GoldenRatioColorGenerator()
            >>> color = Color(generator)
        """
        if not isinstance(color_generator, ColorGenerator):
            raise TypeError("color_generatorはColorGeneratorのインスタンスである必要があります")
        self._color_generator = color_generator

    def generate(self, n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0) -> List[str]:
        """
        設定された色生成器を使用して色を生成

        コンストラクタで設定された色生成器のgenerate_colorsメソッドを呼び出し、
        指定されたパラメータに基づいて色のリストを生成します。

        Args:
            n: 生成する色の数（1以上の整数）
            saturation: 彩度（0.0-1.0の範囲、デフォルト: 0.8）
            lightness: 明度（0.0-1.0の範囲、デフォルト: 0.6）
            offset: 色相の開始オフセット（0-360度、デフォルト: 0）

        Returns:
            hex形式の色文字列のリスト

        Raises:
            ValueError: 色の数が0以下の場合
            TypeError: パラメータの型が不正な場合

        Example:
            >>> golden_color = Color(GoldenRatioColorGenerator())
            >>> colors = golden_color.generate(3, saturation=0.9, lightness=0.5)
            >>> print(colors)
            ['#ff0000', '#00ff00', '#0000ff']
        """
        return self._color_generator.generate_colors(n, saturation, lightness, offset)


def hsl_to_rgb(hue: float, saturation: float, lightness: float) -> Tuple[int, int, int]:
    """
    HSL色空間からRGB色空間への変換

    HSL（Hue, Saturation, Lightness）色空間の値をRGB色空間の値に変換します。
    この関数は、色生成アルゴリズムで使用される内部的な変換関数です。

    Args:
        hue: 色相（0-360度、0度=赤、120度=緑、240度=青）
        saturation: 彩度（0.0-1.0、0.0=グレー、1.0=純色）
        lightness: 明度（0.0-1.0、0.0=黒、0.5=通常、1.0=白）

    Returns:
        RGB値のタプル（r, g, b）- 各値は0-255の整数

    Example:
        >>> r, g, b = hsl_to_rgb(0, 1.0, 0.5)
        >>> print(f"RGB: ({r}, {g}, {b})")
        RGB: (255, 0, 0)
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

    RGB色空間の値を、Web標準のhex形式（#RRGGBB）の文字列に変換します。
    この関数は、色生成アルゴリズムの最終出力形式として使用されます。

    Args:
        r: 赤成分（0-255の整数）
        g: 緑成分（0-255の整数）
        b: 青成分（0-255の整数）

    Returns:
        hex形式の色文字列（#RRGGBB形式）

    Example:
        >>> hex_color = rgb_to_hex(255, 0, 0)
        >>> print(hex_color)
        #ff0000
    """
    return f"#{r:02x}{g:02x}{b:02x}"


class GoldenRatioColorGenerator(ColorGenerator):
    """
    黄金比を使用して色相を決定するアルゴリズム

    自然界の美しい比率である黄金比（約1.618）を使用して色相を決定します。

    Attributes:
        golden_ratio (float): 黄金比の値（約0.618）

    Methods:
        generate_colors: 黄金比に基づく色生成

    References:
        - "Introduction, Explanation & Calculation," Golden Ratio Colors.

    Example:
        >>> generator = GoldenRatioColorGenerator()
        >>> colors = generator.generate_colors(5)
        >>> print(colors)
        ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']
    """

    def __init__(self):
        """黄金比の値を初期化"""
        self.golden_ratio = 0.618033988749895

    def generate_colors(self, n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0) -> List[str]:
        """
        黄金比を使用して色相を決定するアルゴリズム

        各色の色相は、前の色相に黄金比を掛けた値で決定されます。
        これにより、自然界に見られる美しい比率が色彩に反映され、
        調和の取れた色の組み合わせが生成されます。

        Args:
            n: 生成する色の数（1以上の整数）
            saturation: 彩度（0.0-1.0の範囲、デフォルト: 0.8）
            lightness: 明度（0.0-1.0の範囲、デフォルト: 0.6）
            offset: 色相の開始オフセット（0-360度、デフォルト: 0）

        Returns:
            hex形式の色文字列のリスト

        Raises:
            ValueError: 色の数が0以下の場合

        Example:
            >>> generator = GoldenRatioColorGenerator()
            >>> colors = generator.generate_colors(5, saturation=0.9)
            >>> print(colors)
            ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']
        """
        if n <= 0:
            raise ValueError("色の数は1以上である必要があります")

        colors = []

        for i in range(n):
            hue = ((i * self.golden_ratio) % 1.0) * 360 + offset
            hue = hue % 360

            r, g, b = hsl_to_rgb(hue, saturation, lightness)
            colors.append(rgb_to_hex(r, g, b))

        return colors


class EquidistantColorGenerator(ColorGenerator):
    """
    等間隔色相分割による色生成アルゴリズム

    色相を等間隔に分割することで色を生成します。
    最もシンプルで確実に色が分散されるアルゴリズムで、
    データ可視化やUIデザインに適しています。

    Attributes:
        なし（パラメータのみで動作）

    Methods:
        generate_colors: 等間隔色相分割による色生成

    References:
        - J. Chao, I. Osugi, and M. Suzuki, "On Definitions and Construction of Uniform Color Space," in Conference on Colour in Graphics, Imaging, and Vision, vol. 2, no. 1, 2004, p. 55. doi: 10.2352/CGIV.2004.2.1.art00012.

    Example:
        >>> generator = EquidistantColorGenerator()
        >>> colors = generator.generate_colors(6)
        >>> print(colors)
        ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff']
    """

    def generate_colors(self, n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0) -> List[str]:
        """
        等間隔色相分割による色生成アルゴリズム

        色相を360度をn等分して色を生成します。最もシンプルで
        確実に色が分散されるため、データ可視化やUIデザインに
        適しています。

        Args:
            n: 生成する色の数（1以上の整数）
            saturation: 彩度（0.0-1.0の範囲、デフォルト: 0.8）
            lightness: 明度（0.0-1.0の範囲、デフォルト: 0.6）
            offset: 色相の開始オフセット（0-360度、デフォルト: 0）

        Returns:
            hex形式の色文字列のリスト

        Raises:
            ValueError: 色の数が0以下の場合

        Example:
            >>> generator = EquidistantColorGenerator()
            >>> colors = generator.generate_colors(6, offset=30)
            >>> print(colors)
            ['#ff8000', '#ffff80', '#80ff00', '#80ffff', '#0080ff', '#ff80ff']
        """
        if n <= 0:
            raise ValueError("色の数は1以上である必要があります")

        colors = []

        for i in range(n):
            hue = (i / n) * 360 + offset
            hue = hue % 360

            r, g, b = hsl_to_rgb(hue, saturation, lightness)
            colors.append(rgb_to_hex(r, g, b))

        return colors


class FibonacciColorGenerator(ColorGenerator):
    """
    フィボナッチ数列を使用した色生成アルゴリズム

    フィボナッチ数列の逆数を使用して色相を決定します。
    黄金比に似ているが、より数学的に興味深い分布を生成します。

    Attributes:
        fibonacci_ratio (float): フィボナッチ数列の逆数（約0.382）

    Methods:
        generate_colors: フィボナッチ数列に基づく色生成

    Example:
        >>> generator = FibonacciColorGenerator()
        >>> colors = generator.generate_colors(8)
        >>> print(colors)
        ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff', '#ff8000', '#8000ff']
    """

    def __init__(self):
        """フィボナッチ数列の逆数を初期化"""
        self.fibonacci_ratio = 0.381966011250105  # 1 - goldenRatio

    def generate_colors(self, n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0) -> List[str]:
        """
        フィボナッチ数列を使用した色生成アルゴリズム

        各色の色相は、前の色相にフィボナッチ数列の逆数を掛けた値で決定されます。
        黄金比に似ているが、より数学的に興味深い分布を生成し、
        芸術的なアプリケーションに適しています。

        Args:
            n: 生成する色の数（1以上の整数）
            saturation: 彩度（0.0-1.0の範囲、デフォルト: 0.8）
            lightness: 明度（0.0-1.0の範囲、デフォルト: 0.6）
            offset: 色相の開始オフセット（0-360度、デフォルト: 0）

        Returns:
            hex形式の色文字列のリスト

        Raises:
            ValueError: 色の数が0以下の場合

        Example:
            >>> generator = FibonacciColorGenerator()
            >>> colors = generator.generate_colors(8, lightness=0.7)
            >>> print(colors)
            ['#ff6666', '#66ff66', '#6666ff', '#ffff66', '#ff66ff', '#66ffff', '#ffb366', '#b366ff']
        """
        if n <= 0:
            raise ValueError("色の数は1以上である必要があります")

        colors = []

        for i in range(n):
            hue = ((i * self.fibonacci_ratio) % 1.0) * 360 + offset
            hue = hue % 360

            r, g, b = hsl_to_rgb(hue, saturation, lightness)
            colors.append(rgb_to_hex(r, g, b))

        return colors


class ColorWheelColorGenerator(ColorGenerator):
    """
    カラーホイール理論に基づく補色・三色配色アルゴリズム

    Johannes Ittenのカラーホイール理論に基づいて色を生成します。
    補色・三色配色など、視覚的調和を数学的に体系化した理論を実装しています。

    Attributes:
        base_hues (List[float]): 基本色相のリスト（赤、黄、緑、シアン、青、マゼンタ）

    Methods:
        generate_colors: カラーホイール理論に基づく色生成

    References:
        - J. Itten, The Art of Color.

    Example:
        >>> generator = ColorWheelColorGenerator()
        >>> colors = generator.generate_colors(6)
        >>> print(colors)
        ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff']
    """

    def __init__(self):
        """基本色相を定義"""
        # 基本色相を定義（赤、黄、緑、シアン、青、マゼンタ）
        self.base_hues = [0, 60, 120, 180, 240, 300]

    def generate_colors(self, n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0) -> List[str]:
        """
        カラーホイール理論に基づく補色・三色配色アルゴリズム

        6つの基本色相（赤、黄、緑、シアン、青、マゼンタ）を基準として、
        より洗練された色の組み合わせを生成します。6色以下の場合は
        基本色相を直接使用し、6色を超える場合は補間を行います。

        Args:
            n: 生成する色の数（1以上の整数）
            saturation: 彩度（0.0-1.0の範囲、デフォルト: 0.8）
            lightness: 明度（0.0-1.0の範囲、デフォルト: 0.6）
            offset: 色相の開始オフセット（0-360度、デフォルト: 0）

        Returns:
            hex形式の色文字列のリスト

        Raises:
            ValueError: 色の数が0以下の場合

        Example:
            >>> generator = ColorWheelColorGenerator()
            >>> colors = generator.generate_colors(6, saturation=0.9)
            >>> print(colors)
            ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff']
        """
        if n <= 0:
            raise ValueError("色の数は1以上である必要があります")

        colors = []

        for i in range(n):
            if n <= 6:
                # 6色以下の場合は基本色相を使用
                hue = self.base_hues[i % 6] + offset
            else:
                # 6色を超える場合は補間
                base_index = int(i / (n / 6))
                next_index = (base_index + 1) % 6
                ratio = (i % (n / 6)) / (n / 6)
                hue = (
                    self.base_hues[base_index]
                    + (self.base_hues[next_index] - self.base_hues[base_index]) * ratio
                    + offset
                )

            # 360度を超えた場合の処理
            hue = hue % 360

            r, g, b = hsl_to_rgb(hue, saturation, lightness)
            colors.append(rgb_to_hex(r, g, b))

        return colors


class AlternatingColorGenerator(ColorGenerator):
    """
    交互色生成アルゴリズム

    寒色系の範囲（base_hueからend_hue）をn分割して色を生成します。
    偶数番目は寒色系、奇数番目はその補色（暖色系）を使用し、
    統一感のある色の組み合わせを生成します。

    Attributes:
        base_hue (float): 基本色相（寒色系の開始）
        end_hue (float): 終了色相（寒色系の終了）

    Methods:
        generate_colors: 交互色生成アルゴリズム

    Example:
        >>> generator = AlternatingColorGenerator()
        >>> colors = generator.generate_colors(10)
        >>> print(colors)
        ['#00b3b3', '#ff4d00', '#00ccb3', '#ff3300', '#00e6b3', '#ff1a00', '#00ffb3', '#ff0000', '#1affb3', '#e60000']
    """

    def __init__(self):
        """基本色相と終了色相を初期化"""
        self.base_hue = 200  # 基本色相（寒色系の開始）
        self.end_hue = 300  # 終了色相（寒色系の終了）

    def generate_colors(self, n: int, saturation: float = 0.8, lightness: float = 0.6, offset: float = 0) -> List[str]:
        """
        交互色生成アルゴリズム

        寒色系の範囲（base_hueからend_hue）をn分割して色を生成します。
        偶数番目は寒色系、奇数番目はその補色（暖色系）を使用し、
        統一感のある色の組み合わせを生成します。

        Args:
            n: 生成する色の数（1以上の整数）
            saturation: 彩度（0.0-1.0の範囲、デフォルト: 0.8）
            lightness: 明度（0.0-1.0の範囲、デフォルト: 0.6）
            offset: 色相の開始オフセット（0-360度、デフォルト: 0）

        Returns:
            hex形式の色文字列のリスト

        Raises:
            ValueError: 色の数が0以下の場合

        Example:
            >>> generator = AlternatingColorGenerator()
            >>> colors = generator.generate_colors(10, saturation=0.9)
            >>> print(colors)
            ['#00b3b3', '#ff4d00', '#00ccb3', '#ff3300', '#00e6b3', '#ff1a00', '#00ffb3', '#ff0000', '#1affb3', '#e60000']
        """
        if n <= 0:
            raise ValueError("色の数は1以上である必要があります")

        colors = []

        for i in range(n):
            is_even = i % 2 == 0

            if is_even:
                # 偶数番目：寒色系の範囲をn/2分割
                cold_index = i // 2
                hue_step = (self.end_hue - self.base_hue) / max(1, (n // 2) - 1)
                hue = self.base_hue + (cold_index * hue_step) + offset
            else:
                # 奇数番目：寒色系の補色（暖色系）
                cold_index = (i - 1) // 2
                hue_step = (self.end_hue - self.base_hue) / max(1, (n // 2) - 1)
                cold_hue = self.base_hue + (cold_index * hue_step)
                hue = (cold_hue + 180 + offset) % 360

            # 色の数が多い場合は彩度と明度を少しずつ変化させる
            saturation_variation = min(0.1, n / 100)  # 最大0.1の変化
            lightness_variation = min(0.1, n / 100)  # 最大0.1の変化

            adjusted_saturation = max(0.3, min(1.0, saturation + (i * 0.02 - 0.01 * n) * saturation_variation))
            adjusted_lightness = max(0.3, min(0.8, lightness + (i * 0.015 - 0.0075 * n) * lightness_variation))

            r, g, b = hsl_to_rgb(hue, adjusted_saturation, adjusted_lightness)
            colors.append(rgb_to_hex(r, g, b))

        return colors


# 使用例
if __name__ == "__main__":
    # シンプルな使用例
    print("=== シンプルな使用例 ===")

    # 抽象クラスを使用した柔軟な設計
    generators = {
        "黄金比": GoldenRatioColorGenerator(),
        "等間隔": EquidistantColorGenerator(),
        "フィボナッチ": FibonacciColorGenerator(),
        "カラーホイール": ColorWheelColorGenerator(),
        "交互色生成": AlternatingColorGenerator(),
    }

    for name, generator in generators.items():
        colors = generator.generate_colors(5)
        print(f"{name}: {colors}")

    print("\n=== 依存性逆転の原則を体現した使用例 ===")

    # Colorクラスを使用した依存性逆転の例
    golden_color = Color(GoldenRatioColorGenerator())
    equidistant_color = Color(EquidistantColorGenerator())
    fibonacci_color = Color(FibonacciColorGenerator())
    color_wheel_color = Color(ColorWheelColorGenerator())
    alternating_color = Color(AlternatingColorGenerator())

    # 同じインターフェースで異なるアルゴリズムを使用
    print(f"黄金比色: {golden_color.generate(5)}")
    print(f"等間隔色: {equidistant_color.generate(5)}")
    print(f"フィボナッチ色: {fibonacci_color.generate(5)}")
    print(f"カラーホイール色: {color_wheel_color.generate(5)}")
    print(f"交互色生成: {alternating_color.generate(5)}")

    # パラメータを変更して使用
    print(f"\n高彩度黄金比色: {golden_color.generate(3, saturation=0.9, lightness=0.5)}")
    print(f"オフセット等間隔色: {equidistant_color.generate(3, offset=90)}")
    print(f"交互色生成（10色）: {alternating_color.generate(10)}")
