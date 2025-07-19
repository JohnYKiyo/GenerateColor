# 🎨 GenerateColor - 数学的理論に基づく色生成アルゴリズム

数学的理論に基づいて美しい色の組み合わせを生成する TypeScript ライブラリです。4 つの異なるアルゴリズムを実装し、それぞれが異なる用途やデザイン要件に適した色の組み合わせを提供します。

## 🌟 特徴

- **4 つの異なる色生成アルゴリズム**を実装
- **数学的理論**に基づく美しい色の組み合わせ
- **TypeScript**で型安全な実装
- **インタラクティブなデモページ**で実際の色を確認可能
- **学術的参考文献**に基づく実装

## 🚀 デモ

[デモページを見る](https://www.johnkiyo.com/GenerateColor/)

> **注意**: GitHub Pages の設定が必要です。リポジトリの Settings → Pages → Source で "GitHub Actions" を選択してください。

## 📚 実装されているアルゴリズム

### 1. 等間隔色相分割 (Equidistant Colors)

- **用途**: データ可視化、チャート、グラフ
- **特徴**: 最もシンプルで確実に色が分散される
- **参考文献**: Cynthia Brewer "Color in Information Display" (1999)

### 2. フィボナッチ数列 (Fibonacci Colors)

- **用途**: 芸術的アプリケーション、デザイン
- **特徴**: 数学的に興味深い分布
- **参考文献**: "Fibonacci Numbers in Nature and Art" - Journal of Mathematics and the Arts

### 3. カラーホイール理論 (Color Wheel Colors)

- **用途**: デザイン、アート作品
- **特徴**: 補色・三色配色理論に基づく調和の取れた配色
- **参考文献**: Johannes Itten "The Art of Color" (1961)

### 4. 黄金比 (Golden Ratio Colors)

- **用途**: 芸術作品、高級感のあるデザイン
- **特徴**: 自然界の美しい比率を色彩に応用
- **参考文献**: Johannes Itten "The Art of Color" (1961)

## 📦 インストール

```bash
npm install generate-color
```

## 🔧 使用方法

```typescript
import {
  generateGoldenRatioColors,
  generateEquidistantColors,
  generateFibonacciColors,
  generateColorWheelColors,
} from "generate-color";

// 黄金比を使用して10色生成
const goldenColors = generateGoldenRatioColors(10);

// 等間隔で20色生成（彩度0.9、明度0.7）
const equidistantColors = generateEquidistantColors(20, 0.9, 0.7);

// フィボナッチ数列で15色生成（オフセット30度）
const fibonacciColors = generateFibonacciColors(15, 0.8, 0.6, 30);

// カラーホイール理論で12色生成
const colorWheelColors = generateColorWheelColors(12);
```

## 🛠️ 開発

### セットアップ

```bash
git clone https://github.com/yourusername/GenerateColor.git
cd GenerateColor
npm install
```

### ビルド

```bash
npm run build
```

### 開発モード

```bash
npm run dev
```

## 📖 API リファレンス

### generateGoldenRatioColors(n, saturation?, lightness?, offset?)

黄金比を使用して色相を決定するアルゴリズム

**パラメータ:**

- `n` (number): 生成する色の数
- `saturation` (number, optional): 彩度 (0-1, デフォルト: 0.8)
- `lightness` (number, optional): 明度 (0-1, デフォルト: 0.6)
- `offset` (number, optional): 色相の開始オフセット (0-360 度, デフォルト: 0)

**戻り値:** `string[]` - 色のリスト（hex 形式）

### generateEquidistantColors(n, saturation?, lightness?, offset?)

等間隔色相分割による色生成アルゴリズム

**パラメータ:** 同上

### generateFibonacciColors(n, saturation?, lightness?, offset?)

フィボナッチ数列を使用した色生成アルゴリズム

**パラメータ:** 同上

### generateColorWheelColors(n, saturation?, lightness?, offset?)

カラーホイール理論に基づく補色・三色配色アルゴリズム

**パラメータ:** 同上

## 🎯 使用例

### データ可視化での使用

```typescript
// チャート用の色パレット生成
const chartColors = generateEquidistantColors(8, 0.8, 0.6);
```

### デザインシステムでの使用

```typescript
// ブランドカラーパレット生成
const brandColors = generateGoldenRatioColors(6, 0.9, 0.5);
```

### アート作品での使用

```typescript
// 芸術的な色の組み合わせ
const artisticColors = generateFibonacciColors(12, 0.7, 0.7);
```

## 📄 ライセンス

MIT License

## 🤝 コントリビューション

プルリクエストやイシューの報告を歓迎します！

## 📚 参考文献

- Johannes Itten "The Art of Color" (1961)
- Cynthia Brewer "Color in Information Display" (1999)
- "Fibonacci Numbers in Nature and Art" - Journal of Mathematics and the Arts (2000s)

## 🌟 スター

このプロジェクトが役に立ったら、スターを付けてください！
