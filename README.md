# GenerateColor

数学的理論に基づく色生成アルゴリズムを提供する TypeScript のライブラリです。黄金比、等間隔分割、フィボナッチ数列、カラーホイール理論に基づいて美しい色の組み合わせを生成できます。

## デモ

実際の動作を確認したい場合は、[デモページ](https://www.johnkiyo.com/GenerateColor/)をご覧ください。

## 実装されているアルゴリズム

### 1. 黄金比 (Golden Ratio)

自然界の美しい比率である黄金比を使用して色相を決定します。Johannes Itten の色彩理論に基づき、調和の取れた色の組み合わせを生成します。

### 2. 等間隔分割 (Equidistant)

色相を等間隔に分割することで色を生成します。最もシンプルで確実に色が分散されるため、データ可視化や UI デザインに適しています。

### 3. フィボナッチ数列 (Fibonacci)

フィボナッチ数列の逆数を使用して色相を決定します。黄金比に似ているが、より数学的に興味深い分布を生成します。

### 4. カラーホイール (Color Wheel)

Johannes Itten のカラーホイール理論に基づいて色を生成します。補色・三色配色など、視覚的調和を数学的に体系化した理論を実装しています。

## 使用方法

### 基本的な使用例

```typescript
import {
  Color,
  GoldenRatioColorGenerator,
  EquidistantColorGenerator,
  FibonacciColorGenerator,
  ColorWheelColorGenerator,
} from 'generate-color';

// 黄金比アルゴリズムを使用
const goldenColor = new Color(new GoldenRatioColorGenerator());
const colors = goldenColor.generate(5);
console.log(colors); // ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']

// 等間隔アルゴリズムを使用
const equidistantColor = new Color(new EquidistantColorGenerator());
const colors = equidistantColor.generate(6);
console.log(colors); // ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff']
```

### パラメータの調整

```typescript
// 彩度と明度を調整
const colors = goldenColor.generate(3, 0.9, 0.5);

// 色相の開始位置を調整
const colors = equidistantColor.generate(3, 0.8, 0.6, 90);
```

## API リファレンス

### Color クラス

```typescript
class Color {
  constructor(colorGenerator: ColorGenerator);
  generate(n: number, saturation?: number, lightness?: number, offset?: number): string[];
}
```

### ColorGenerator インターフェース

```typescript
interface ColorGenerator {
  generateColors(n: number, saturation?: number, lightness?: number, offset?: number): string[];
}
```

### 実装クラス

```typescript
class GoldenRatioColorGenerator implements ColorGenerator
class EquidistantColorGenerator implements ColorGenerator
class FibonacciColorGenerator implements ColorGenerator
class ColorWheelColorGenerator implements ColorGenerator
```

### パラメータ

- `n`: 生成する色の数（1 以上の整数）
- `saturation`: 彩度（0.0-1.0 の範囲、デフォルト: 0.8）
- `lightness`: 明度（0.0-1.0 の範囲、デフォルト: 0.6）
- `offset`: 色相の開始オフセット（0-360 度、デフォルト: 0）

### 戻り値

hex 形式の色文字列の配列（例: `["#ff0000", "#00ff00", "#0000ff"]`）

## その他の言語

Python 版の実装については [README_Python.md](README_Python.md) をご覧ください。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 開発環境

開発環境のセットアップと使用方法については、[README_dev.md](README_dev.md)をご覧ください。

このプロジェクトでは、GitHub Actionsを使用して以下の自動チェックを実行しています：

- **TypeScript**: ESLint + Prettier
- **Python**: Black + isort + flake8 (PEP8準拠)

プルリクエストを作成すると、自動的にコード品質チェックが実行されます。

## コントリビューション

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/xxxx-feature`)
3. 変更をコミット (`git commit -m 'Add xxxx feature'`)
4. ブランチにプッシュ (`git push origin feature/xxxx-feature`)
5. プルリクエストを作成

**注意**: プルリクエストを作成する前に、ローカルでコード品質チェックを実行することをお勧めします。

## 参考文献

- Johannes Itten "The Art of Color" (1961) - 黄金比の色彩応用とカラーホイール理論
- Cynthia Brewer "Color in Information Display" (1999) - データ可視化の色選択理論
- "Fibonacci Numbers in Nature and Art" - Journal of Mathematics and the Arts (2000s) - 数学的パターンを色彩美学に応用した研究
