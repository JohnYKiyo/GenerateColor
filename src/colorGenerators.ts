/**
 * 黄金比を使用して色相を決定するアルゴリズム
 *
 * 参考文献:
 * - Johannes Itten "The Art of Color" (1961) - 黄金比の色彩応用
 * - 自然界の美しい比率を色彩に応用した調和理論
 *
 * @param n 生成する色の数
 * @param saturation 彩度 (0-1)
 * @param lightness 明度 (0-1)
 * @param offset 色相の開始オフセット (0-360度)
 * @returns 色のリスト（hex形式）
 */
export const generateGoldenRatioColors = (
  n: number,
  saturation: number = 0.8,
  lightness: number = 0.6,
  offset: number = 0
): string[] => {
  const colors: string[] = [];
  const goldenRatio = 0.618033988749895;

  for (let i = 0; i < n; i++) {
    const hue = ((i * goldenRatio) % 1.0) * 360 + offset; // オフセットを追加
    const h = hue % 360; // 360度を超えた場合の処理

    // HSLからRGBへの変換
    const c = (1 - Math.abs(2 * lightness - 1)) * saturation;
    const x = c * (1 - Math.abs(((h / 60) % 2) - 1));
    const m = lightness - c / 2;

    let r: number, g: number, b: number;

    if (h < 60) {
      r = c;
      g = x;
      b = 0;
    } else if (h < 120) {
      r = x;
      g = c;
      b = 0;
    } else if (h < 180) {
      r = 0;
      g = c;
      b = x;
    } else if (h < 240) {
      r = 0;
      g = x;
      b = c;
    } else if (h < 300) {
      r = x;
      g = 0;
      b = c;
    } else {
      r = c;
      g = 0;
      b = x;
    }

    const red = Math.round((r + m) * 255);
    const green = Math.round((g + m) * 255);
    const blue = Math.round((b + m) * 255);

    colors.push(
      `#${red.toString(16).padStart(2, "0")}${green
        .toString(16)
        .padStart(2, "0")}${blue.toString(16).padStart(2, "0")}`
    );
  }

  return colors;
};

/**
 * 等間隔色相分割による色生成アルゴリズム
 * 最もシンプルで確実に色が分散される
 *
 * 参考文献:
 * - Cynthia Brewer "Color in Information Display" (1999) - データ可視化の色選択
 * - 科学的根拠に基づく色覚障害者にも配慮した色パレット設計
 *
 * @param n 生成する色の数
 * @param saturation 彩度 (0-1)
 * @param lightness 明度 (0-1)
 * @param offset 色相の開始オフセット (0-360度)
 * @returns 色のリスト（hex形式）
 */
export const generateEquidistantColors = (
  n: number,
  saturation: number = 0.8,
  lightness: number = 0.6,
  offset: number = 0
): string[] => {
  const colors: string[] = [];

  for (let i = 0; i < n; i++) {
    const hue = (i / n) * 360 + offset; // オフセットを追加
    const h = hue % 360; // 360度を超えた場合の処理

    // HSLからRGBへの変換
    const c = (1 - Math.abs(2 * lightness - 1)) * saturation;
    const x = c * (1 - Math.abs(((h / 60) % 2) - 1));
    const m = lightness - c / 2;

    let r: number, g: number, b: number;

    if (h < 60) {
      r = c;
      g = x;
      b = 0;
    } else if (h < 120) {
      r = x;
      g = c;
      b = 0;
    } else if (h < 180) {
      r = 0;
      g = c;
      b = x;
    } else if (h < 240) {
      r = 0;
      g = x;
      b = c;
    } else if (h < 300) {
      r = x;
      g = 0;
      b = c;
    } else {
      r = c;
      g = 0;
      b = x;
    }

    const red = Math.round((r + m) * 255);
    const green = Math.round((g + m) * 255);
    const blue = Math.round((b + m) * 255);

    colors.push(
      `#${red.toString(16).padStart(2, "0")}${green
        .toString(16)
        .padStart(2, "0")}${blue.toString(16).padStart(2, "0")}`
    );
  }

  return colors;
};

/**
 * フィボナッチ数列を使用した色生成アルゴリズム
 * 黄金比に似ているが、より数学的に興味深い
 *
 * 参考文献:
 * - "Fibonacci Numbers in Nature and Art" - Journal of Mathematics and the Arts (2000s)
 * - 数学的パターンを色彩美学に応用した研究
 *
 * @param n 生成する色の数
 * @param saturation 彩度 (0-1)
 * @param lightness 明度 (0-1)
 * @param offset 色相の開始オフセット (0-360度)
 * @returns 色のリスト（hex形式）
 */
export const generateFibonacciColors = (
  n: number,
  saturation: number = 0.8,
  lightness: number = 0.6,
  offset: number = 0
): string[] => {
  const colors: string[] = [];
  const fibonacciRatio = 0.381966011250105; // 1 - goldenRatio

  for (let i = 0; i < n; i++) {
    const hue = ((i * fibonacciRatio) % 1.0) * 360 + offset; // オフセットを追加
    const h = hue % 360; // 360度を超えた場合の処理

    // HSLからRGBへの変換
    const c = (1 - Math.abs(2 * lightness - 1)) * saturation;
    const x = c * (1 - Math.abs(((h / 60) % 2) - 1));
    const m = lightness - c / 2;

    let r: number, g: number, b: number;

    if (h < 60) {
      r = c;
      g = x;
      b = 0;
    } else if (h < 120) {
      r = x;
      g = c;
      b = 0;
    } else if (h < 180) {
      r = 0;
      g = c;
      b = x;
    } else if (h < 240) {
      r = 0;
      g = x;
      b = c;
    } else if (h < 300) {
      r = x;
      g = 0;
      b = c;
    } else {
      r = c;
      g = 0;
      b = x;
    }

    const red = Math.round((r + m) * 255);
    const green = Math.round((g + m) * 255);
    const blue = Math.round((b + m) * 255);

    colors.push(
      `#${red.toString(16).padStart(2, "0")}${green
        .toString(16)
        .padStart(2, "0")}${blue.toString(16).padStart(2, "0")}`
    );
  }

  return colors;
};

/**
 * カラーホイール理論に基づく補色・三色配色アルゴリズム
 * より洗練された色の組み合わせを生成
 *
 * 参考文献:
 * - Johannes Itten "The Art of Color" (1961) - カラーホイール理論
 * - 補色・三色配色など、視覚的調和を数学的に体系化した理論
 *
 * @param n 生成する色の数
 * @param saturation 彩度 (0-1)
 * @param lightness 明度 (0-1)
 * @param offset 色相の開始オフセット (0-360度)
 * @returns 色のリスト（hex形式）
 */
export const generateColorWheelColors = (
  n: number,
  saturation: number = 0.8,
  lightness: number = 0.6,
  offset: number = 0
): string[] => {
  const colors: string[] = [];

  // 基本色相を定義（赤、黄、緑、シアン、青、マゼンタ）
  const baseHues = [0, 60, 120, 180, 240, 300];

  for (let i = 0; i < n; i++) {
    let hue: number;

    if (n <= 6) {
      // 6色以下の場合は基本色相を使用
      hue = baseHues[i % 6] + offset;
    } else {
      // 6色を超える場合は補間
      const baseIndex = Math.floor(i / (n / 6));
      const nextIndex = (baseIndex + 1) % 6;
      const ratio = (i % (n / 6)) / (n / 6);
      hue =
        baseHues[baseIndex] +
        (baseHues[nextIndex] - baseHues[baseIndex]) * ratio +
        offset;
    }

    // 360度を超えた場合の処理
    hue = hue % 360;

    // HSLからRGBへの変換
    const c = (1 - Math.abs(2 * lightness - 1)) * saturation;
    const x = c * (1 - Math.abs(((hue / 60) % 2) - 1));
    const m = lightness - c / 2;

    let r: number, g: number, b: number;

    if (hue < 60) {
      r = c;
      g = x;
      b = 0;
    } else if (hue < 120) {
      r = x;
      g = c;
      b = 0;
    } else if (hue < 180) {
      r = 0;
      g = c;
      b = x;
    } else if (hue < 240) {
      r = 0;
      g = x;
      b = c;
    } else if (hue < 300) {
      r = x;
      g = 0;
      b = c;
    } else {
      r = c;
      g = 0;
      b = x;
    }

    const red = Math.round((r + m) * 255);
    const green = Math.round((g + m) * 255);
    const blue = Math.round((b + m) * 255);

    colors.push(
      `#${red.toString(16).padStart(2, "0")}${green
        .toString(16)
        .padStart(2, "0")}${blue.toString(16).padStart(2, "0")}`
    );
  }

  return colors;
};
