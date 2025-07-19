"""
色生成アルゴリズムのテストファイル
"""

import unittest

from src.color_generators import (
    generate_color_wheel_colors,
    generate_colors_by_algorithm,
    generate_equidistant_colors,
    generate_fibonacci_colors,
    generate_golden_ratio_colors,
    get_all_algorithms,
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

    def test_generate_golden_ratio_colors(self):
        """黄金比色生成テスト"""
        colors = generate_golden_ratio_colors(5)

        # 5色生成されることを確認
        self.assertEqual(len(colors), 5)

        # すべてhex形式であることを確認
        for color in colors:
            self.assertTrue(color.startswith("#"))
            self.assertEqual(len(color), 7)  # #RRGGBB

        # 異なる色が生成されることを確認
        self.assertEqual(len(set(colors)), 5)

    def test_generate_equidistant_colors(self):
        """等間隔色生成テスト"""
        colors = generate_equidistant_colors(6)

        # 6色生成されることを確認
        self.assertEqual(len(colors), 6)

        # すべてhex形式であることを確認
        for color in colors:
            self.assertTrue(color.startswith("#"))
            self.assertEqual(len(color), 7)

        # 異なる色が生成されることを確認
        self.assertEqual(len(set(colors)), 6)

    def test_generate_fibonacci_colors(self):
        """フィボナッチ色生成テスト"""
        colors = generate_fibonacci_colors(8)

        # 8色生成されることを確認
        self.assertEqual(len(colors), 8)

        # すべてhex形式であることを確認
        for color in colors:
            self.assertTrue(color.startswith("#"))
            self.assertEqual(len(color), 7)

        # 異なる色が生成されることを確認
        self.assertEqual(len(set(colors)), 8)

    def test_generate_color_wheel_colors(self):
        """カラーホイール色生成テスト"""
        colors = generate_color_wheel_colors(6)

        # 6色生成されることを確認
        self.assertEqual(len(colors), 6)

        # すべてhex形式であることを確認
        for color in colors:
            self.assertTrue(color.startswith("#"))
            self.assertEqual(len(color), 7)

        # 異なる色が生成されることを確認
        self.assertEqual(len(set(colors)), 6)

    def test_get_all_algorithms(self):
        """アルゴリズム一覧取得テスト"""
        algorithms = get_all_algorithms()

        # 4つのアルゴリズムが含まれていることを確認
        self.assertEqual(len(algorithms), 4)
        self.assertIn("golden_ratio", algorithms)
        self.assertIn("equidistant", algorithms)
        self.assertIn("fibonacci", algorithms)
        self.assertIn("color_wheel", algorithms)

        # すべて関数であることを確認
        for func in algorithms.values():
            self.assertTrue(callable(func))

    def test_generate_colors_by_algorithm(self):
        """アルゴリズム名指定での色生成テスト"""
        # 有効なアルゴリズム名
        colors = generate_colors_by_algorithm("golden_ratio", 3)
        self.assertEqual(len(colors), 3)

        colors = generate_colors_by_algorithm("equidistant", 4)
        self.assertEqual(len(colors), 4)

        # 無効なアルゴリズム名
        with self.assertRaises(ValueError):
            generate_colors_by_algorithm("invalid_algorithm", 3)

    def test_parameter_validation(self):
        """パラメータ検証テスト"""
        # 色の数が0以下の場合
        with self.assertRaises(ValueError):
            generate_golden_ratio_colors(0)

        # 彩度が範囲外の場合
        colors = generate_golden_ratio_colors(3, saturation=1.5)  # 範囲外だが動作する
        self.assertEqual(len(colors), 3)

        # 明度が範囲外の場合
        colors = generate_golden_ratio_colors(3, lightness=1.5)  # 範囲外だが動作する
        self.assertEqual(len(colors), 3)

    def test_offset_parameter(self):
        """オフセットパラメータテスト"""
        # オフセットなし
        colors1 = generate_golden_ratio_colors(5, offset=0)

        # オフセットあり
        colors2 = generate_golden_ratio_colors(5, offset=180)

        # 異なる色が生成されることを確認
        self.assertNotEqual(colors1, colors2)

    def test_saturation_and_lightness(self):
        """彩度と明度のテスト"""
        # 高彩度、高明度
        colors_bright = generate_golden_ratio_colors(3, saturation=1.0, lightness=0.8)

        # 低彩度、低明度
        colors_dark = generate_golden_ratio_colors(3, saturation=0.3, lightness=0.2)

        # 異なる色が生成されることを確認
        self.assertNotEqual(colors_bright, colors_dark)


class TestColorConsistency(unittest.TestCase):
    """色の一貫性テスト"""

    def test_same_parameters_same_colors(self):
        """同じパラメータで同じ色が生成されることを確認"""
        colors1 = generate_golden_ratio_colors(10, 0.8, 0.6, 0)
        colors2 = generate_golden_ratio_colors(10, 0.8, 0.6, 0)
        self.assertEqual(colors1, colors2)

    def test_different_algorithms_different_colors(self):
        """異なるアルゴリズムで異なる色が生成されることを確認"""
        golden = generate_golden_ratio_colors(10)
        equidistant = generate_equidistant_colors(10)
        fibonacci = generate_fibonacci_colors(10)
        color_wheel = generate_color_wheel_colors(10)

        # すべて異なることを確認
        self.assertNotEqual(golden, equidistant)
        self.assertNotEqual(golden, fibonacci)
        self.assertNotEqual(golden, color_wheel)
        self.assertNotEqual(equidistant, fibonacci)
        self.assertNotEqual(equidistant, color_wheel)
        self.assertNotEqual(fibonacci, color_wheel)


if __name__ == "__main__":
    # テストの実行
    unittest.main(verbosity=2)

    # 簡単なデモ
    print("\n" + "=" * 50)
    print("色生成アルゴリズム デモ")
    print("=" * 50)

    from src.color_generators import (
        generate_equidistant_colors,
        generate_golden_ratio_colors,
    )

    print("\n黄金比色 5色:")
    colors = generate_golden_ratio_colors(5)
    for i, color in enumerate(colors, 1):
        print(f"  {i}: {color}")

    print("\n等間隔色 5色:")
    colors = generate_equidistant_colors(5)
    for i, color in enumerate(colors, 1):
        print(f"  {i}: {color}")
