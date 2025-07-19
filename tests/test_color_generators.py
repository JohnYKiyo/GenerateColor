"""
色生成アルゴリズムのテストファイル - シンプルな抽象クラス設計対応版
"""

import unittest

from src.color_generators import (  # 抽象クラスと実装クラス; Colorクラス; ユーティリティ関数
    Color,
    ColorGenerator,
    ColorWheelColorGenerator,
    EquidistantColorGenerator,
    FibonacciColorGenerator,
    GoldenRatioColorGenerator,
    hsl_to_rgb,
    rgb_to_hex,
)


class TestColorGenerators(unittest.TestCase):

    def test_hsl_to_rgb(self):
        """HSLからRGBへの変換テスト"""
        # 赤色 (0度)
        r, g, b = hsl_to_rgb(0, 1.0, 0.5)
        self.assertEqual(r, 255)
        self.assertEqual(g, 0)
        self.assertEqual(b, 0)

        # 緑色 (120度)
        r, g, b = hsl_to_rgb(120, 1.0, 0.5)
        self.assertEqual(r, 0)
        self.assertEqual(g, 255)
        self.assertEqual(b, 0)

        # 青色 (240度)
        r, g, b = hsl_to_rgb(240, 1.0, 0.5)
        self.assertEqual(r, 0)
        self.assertEqual(g, 0)
        self.assertEqual(b, 255)

        # グレー (彩度0)
        r, g, b = hsl_to_rgb(0, 0.0, 0.5)
        self.assertEqual(r, 128)
        self.assertEqual(g, 128)
        self.assertEqual(b, 128)

    def test_rgb_to_hex(self):
        """RGBからhexへの変換テスト"""
        self.assertEqual(rgb_to_hex(255, 0, 0), "#ff0000")
        self.assertEqual(rgb_to_hex(0, 255, 0), "#00ff00")
        self.assertEqual(rgb_to_hex(0, 0, 255), "#0000ff")
        self.assertEqual(rgb_to_hex(128, 128, 128), "#808080")
        self.assertEqual(rgb_to_hex(0, 0, 0), "#000000")
        self.assertEqual(rgb_to_hex(255, 255, 255), "#ffffff")

    def test_golden_ratio_generator(self):
        """GoldenRatioColorGeneratorのテスト"""
        generator = GoldenRatioColorGenerator()

        # 5色生成されることを確認
        colors = generator.generate_colors(5)
        self.assertEqual(len(colors), 5)

        # すべてhex形式であることを確認
        for color in colors:
            self.assertTrue(color.startswith("#"))
            self.assertEqual(len(color), 7)  # #RRGGBB

        # 異なる色が生成されることを確認
        self.assertEqual(len(set(colors)), 5)

        # ColorGeneratorのインスタンスであることを確認
        self.assertIsInstance(generator, ColorGenerator)

    def test_equidistant_generator(self):
        """EquidistantColorGeneratorのテスト"""
        generator = EquidistantColorGenerator()

        # 6色生成されることを確認
        colors = generator.generate_colors(6)
        self.assertEqual(len(colors), 6)

        # すべてhex形式であることを確認
        for color in colors:
            self.assertTrue(color.startswith("#"))
            self.assertEqual(len(color), 7)

        # 異なる色が生成されることを確認
        self.assertEqual(len(set(colors)), 6)

        # ColorGeneratorのインスタンスであることを確認
        self.assertIsInstance(generator, ColorGenerator)

    def test_fibonacci_generator(self):
        """FibonacciColorGeneratorのテスト"""
        generator = FibonacciColorGenerator()

        # 8色生成されることを確認
        colors = generator.generate_colors(8)
        self.assertEqual(len(colors), 8)

        # すべてhex形式であることを確認
        for color in colors:
            self.assertTrue(color.startswith("#"))
            self.assertEqual(len(color), 7)

        # 異なる色が生成されることを確認
        self.assertEqual(len(set(colors)), 8)

        # ColorGeneratorのインスタンスであることを確認
        self.assertIsInstance(generator, ColorGenerator)

    def test_color_wheel_generator(self):
        """ColorWheelColorGeneratorのテスト"""
        generator = ColorWheelColorGenerator()

        # 6色生成されることを確認
        colors = generator.generate_colors(6)
        self.assertEqual(len(colors), 6)

        # すべてhex形式であることを確認
        for color in colors:
            self.assertTrue(color.startswith("#"))
            self.assertEqual(len(color), 7)

        # 異なる色が生成されることを確認
        self.assertEqual(len(set(colors)), 6)

        # ColorGeneratorのインスタンスであることを確認
        self.assertIsInstance(generator, ColorGenerator)

    def test_parameter_validation(self):
        """パラメータ検証テスト"""
        # 色の数が0以下の場合
        with self.assertRaises(ValueError):
            GoldenRatioColorGenerator().generate_colors(0)

        # 彩度が範囲外の場合
        colors = GoldenRatioColorGenerator().generate_colors(3, saturation=1.5)  # 範囲外だが動作する
        self.assertEqual(len(colors), 3)

        # 明度が範囲外の場合
        colors = GoldenRatioColorGenerator().generate_colors(3, lightness=1.5)  # 範囲外だが動作する
        self.assertEqual(len(colors), 3)

    def test_offset_parameter(self):
        """オフセットパラメータテスト"""
        generator = GoldenRatioColorGenerator()

        # オフセットなし
        colors1 = generator.generate_colors(5, offset=0)

        # オフセットあり
        colors2 = generator.generate_colors(5, offset=180)

        # 異なる色が生成されることを確認
        self.assertNotEqual(colors1, colors2)

    def test_saturation_and_lightness(self):
        """彩度と明度のテスト"""
        generator = GoldenRatioColorGenerator()

        # 高彩度、高明度
        colors_bright = generator.generate_colors(3, saturation=1.0, lightness=0.8)

        # 低彩度、低明度
        colors_dark = generator.generate_colors(3, saturation=0.3, lightness=0.2)

        # 異なる色が生成されることを確認
        self.assertNotEqual(colors_bright, colors_dark)


class TestColorClass(unittest.TestCase):
    """Colorクラスのテスト - 依存性逆転の原則を体現"""

    def test_color_initialization(self):
        """Colorクラスの初期化テスト"""
        golden_generator = GoldenRatioColorGenerator()
        color = Color(golden_generator)

        # 正しく初期化されることを確認
        self.assertIsInstance(color, Color)

    def test_color_generate(self):
        """Colorクラスのgenerateメソッドテスト"""
        golden_generator = GoldenRatioColorGenerator()
        color = Color(golden_generator)

        # 色を生成
        colors = color.generate(5)

        # 正しく生成されることを確認
        self.assertEqual(len(colors), 5)
        for color_hex in colors:
            self.assertTrue(color_hex.startswith("#"))
            self.assertEqual(len(color_hex), 7)

    def test_color_with_different_generators(self):
        """異なる生成器を使用したColorクラスのテスト"""
        generators = [
            GoldenRatioColorGenerator(),
            EquidistantColorGenerator(),
            FibonacciColorGenerator(),
            ColorWheelColorGenerator(),
        ]

        results = []
        for generator in generators:
            color = Color(generator)
            colors = color.generate(5)
            results.append(colors)
            self.assertEqual(len(colors), 5)

        # すべて異なる結果であることを確認
        for i in range(len(results)):
            for j in range(i + 1, len(results)):
                self.assertNotEqual(results[i], results[j])

    def test_color_parameters(self):
        """Colorクラスのパラメータテスト"""
        golden_generator = GoldenRatioColorGenerator()
        color = Color(golden_generator)

        # デフォルトパラメータ
        colors1 = color.generate(3)

        # カスタムパラメータ
        colors2 = color.generate(3, saturation=0.9, lightness=0.5, offset=90)

        # 異なる結果であることを確認
        self.assertNotEqual(colors1, colors2)

    def test_dependency_inversion_principle(self):
        """依存性逆転の原則のテスト"""
        # 抽象クラスに依存し、具象クラスに依存しない
        color_generators = [
            GoldenRatioColorGenerator(),
            EquidistantColorGenerator(),
            FibonacciColorGenerator(),
            ColorWheelColorGenerator(),
        ]

        # すべて同じインターフェースで動作することを確認
        for generator in color_generators:
            color = Color(generator)
            colors = color.generate(3)
            self.assertEqual(len(colors), 3)
            self.assertIsInstance(colors, list)
            for color_hex in colors:
                self.assertIsInstance(color_hex, str)
                self.assertTrue(color_hex.startswith("#"))


class TestColorConsistency(unittest.TestCase):
    """色の一貫性テスト"""

    def test_same_parameters_same_colors(self):
        """同じパラメータで同じ色が生成されることを確認"""
        generator = GoldenRatioColorGenerator()
        colors1 = generator.generate_colors(10, 0.8, 0.6, 0)
        colors2 = generator.generate_colors(10, 0.8, 0.6, 0)
        self.assertEqual(colors1, colors2)

    def test_different_algorithms_different_colors(self):
        """異なるアルゴリズムで異なる色が生成されることを確認"""
        golden = GoldenRatioColorGenerator().generate_colors(10)
        equidistant = EquidistantColorGenerator().generate_colors(10)
        fibonacci = FibonacciColorGenerator().generate_colors(10)
        color_wheel = ColorWheelColorGenerator().generate_colors(10)

        # すべて異なることを確認
        self.assertNotEqual(golden, equidistant)
        self.assertNotEqual(golden, fibonacci)
        self.assertNotEqual(golden, color_wheel)
        self.assertNotEqual(equidistant, fibonacci)
        self.assertNotEqual(equidistant, color_wheel)
        self.assertNotEqual(fibonacci, color_wheel)


class TestFlexibility(unittest.TestCase):
    """柔軟性のテスト"""

    def test_instance_injection(self):
        """インスタンス注入による柔軟性テスト"""
        # 異なるアルゴリズムのインスタンスを注入
        generators = [
            GoldenRatioColorGenerator(),
            EquidistantColorGenerator(),
            FibonacciColorGenerator(),
            ColorWheelColorGenerator(),
        ]

        # 同じインターフェースで異なる結果
        results = []
        for generator in generators:
            colors = generator.generate_colors(5)
            results.append(colors)
            self.assertEqual(len(colors), 5)

        # すべて異なる結果であることを確認
        for i in range(len(results)):
            for j in range(i + 1, len(results)):
                self.assertNotEqual(results[i], results[j])

    def test_custom_algorithm(self):
        """カスタムアルゴリズムの実装テスト"""

        class CustomColorGenerator(ColorGenerator):
            def generate_colors(self, n, saturation=0.8, lightness=0.6, offset=0):
                if n <= 0:
                    raise ValueError("色の数は1以上である必要があります")

                colors = []
                for i in range(n):
                    hue = (i * 0.3) % 360 + offset  # カスタム計算
                    hue = hue % 360
                    r, g, b = hsl_to_rgb(hue, saturation, lightness)
                    colors.append(rgb_to_hex(r, g, b))
                return colors

        # カスタム生成器を使用
        custom_generator = CustomColorGenerator()
        colors = custom_generator.generate_colors(5)

        # 正常に動作することを確認
        self.assertEqual(len(colors), 5)
        self.assertIsInstance(custom_generator, ColorGenerator)

        # 他の生成器と異なる結果
        golden_colors = GoldenRatioColorGenerator().generate_colors(5)
        self.assertNotEqual(colors, golden_colors)

        # Colorクラスでも使用可能
        custom_color = Color(custom_generator)
        custom_colors = custom_color.generate(5)
        self.assertEqual(len(custom_colors), 5)


if __name__ == "__main__":
    # テストの実行
    unittest.main(verbosity=2)

    # 簡単なデモ
    print("\n" + "=" * 50)
    print("色生成アルゴリズム デモ")
    print("=" * 50)

    # シンプルな使用例
    print("\n=== シンプルな使用例 ===")
    generators = {
        "黄金比": GoldenRatioColorGenerator(),
        "等間隔": EquidistantColorGenerator(),
        "フィボナッチ": FibonacciColorGenerator(),
        "カラーホイール": ColorWheelColorGenerator(),
    }

    for name, generator in generators.items():
        colors = generator.generate_colors(5)
        print(f"{name}: {colors}")

    # 依存性逆転の原則を体現した使用例
    print("\n=== 依存性逆転の原則を体現した使用例 ===")
    golden_color = Color(GoldenRatioColorGenerator())
    equidistant_color = Color(EquidistantColorGenerator())

    print(f"Colorクラス（黄金比）: {golden_color.generate(3)}")
    print(f"Colorクラス（等間隔）: {equidistant_color.generate(3)}")
