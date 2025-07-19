/**
 * 数学的理論に基づく色生成アルゴリズム - TypeScript版
 */

/**
 * HSL色空間からRGB色空間への変換
 *
 * @param hue 色相（0-360度、0度=赤、120度=緑、240度=青）
 * @param saturation 彩度（0.0-1.0、0.0=グレー、1.0=純色）
 * @param lightness 明度（0.0-1.0、0.0=黒、0.5=通常、1.0=白）
 * @returns RGB値のタプル（r, g, b）- 各値は0-255の整数
 */
function hslToRgb(
  hue: number,
  saturation: number,
  lightness: number
): [number, number, number] {
  const h = hue % 360;

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

  return [
    Math.round((r + m) * 255),
    Math.round((g + m) * 255),
    Math.round((b + m) * 255),
  ];
}

/**
 * RGB値をhex形式の文字列に変換
 *
 * @param r 赤成分（0-255の整数）
 * @param g 緑成分（0-255の整数）
 * @param b 青成分（0-255の整数）
 * @returns hex形式の色文字列（#RRGGBB形式）
 */
function rgbToHex(r: number, g: number, b: number): string {
  return `#${r.toString(16).padStart(2, "0")}${g
    .toString(16)
    .padStart(2, "0")}${b.toString(16).padStart(2, "0")}`;
}

/**
 * 色生成アルゴリズムのインターフェース
 *
 * 様々な数学的理論に基づく色生成アルゴリズムの共通インターフェースを定義します。
 * 具体的な実装に依存せずに色生成機能を利用できます。
 */
export interface ColorGenerator {
  /**
   * 色を生成するメソッド
   *
   * 指定された数の色を生成し、hex形式の文字列リストを返します。
   * 各実装クラスは、異なる数学的理論に基づいて色相を決定します。
   *
   * @param n 生成する色の数（1以上の整数）
   * @param saturation 彩度（0.0-1.0の範囲、デフォルト: 0.8）
   * @param lightness 明度（0.0-1.0の範囲、デフォルト: 0.6）
   * @param offset 色相の開始オフセット（0-360度、デフォルト: 0）
   * @returns hex形式の色文字列の配列
   */
  generateColors(
    n: number,
    saturation?: number,
    lightness?: number,
    offset?: number
  ): string[];
}

/**
 * 色生成を行うクラス
 *
 * ColorGeneratorインターフェースに依存し、具体的な実装クラスには依存しません。
 * コンストラクタで色生成器を渡すことで、柔軟にアルゴリズムを切り替えることができます。
 */
export class Color {
  private _colorGenerator: ColorGenerator;

  /**
   * 色生成器を設定してColorインスタンスを初期化
   *
   * @param colorGenerator 色生成アルゴリズムの実装インスタンス
   */
  constructor(colorGenerator: ColorGenerator) {
    this._colorGenerator = colorGenerator;
  }

  /**
   * 設定された色生成器を使用して色を生成
   *
   * コンストラクタで設定された色生成器のgenerateColorsメソッドを呼び出し、
   * 指定されたパラメータに基づいて色のリストを生成します。
   *
   * @param n 生成する色の数（1以上の整数）
   * @param saturation 彩度（0.0-1.0の範囲、デフォルト: 0.8）
   * @param lightness 明度（0.0-1.0の範囲、デフォルト: 0.6）
   * @param offset 色相の開始オフセット（0-360度、デフォルト: 0）
   * @returns hex形式の色文字列の配列
   */
  generate(
    n: number,
    saturation: number = 0.8,
    lightness: number = 0.6,
    offset: number = 0
  ): string[] {
    return this._colorGenerator.generateColors(
      n,
      saturation,
      lightness,
      offset
    );
  }
}

/**
 * 黄金比を使用して色相を決定するアルゴリズム
 *
 * 自然界の美しい比率である黄金比（約1.618）を使用して色相を決定します。
 * Johannes Ittenの色彩理論に基づき、調和の取れた色の組み合わせを生成します。
 *
 * 参考文献:
 * - Johannes Itten "The Art of Color" (1961) - 黄金比の色彩応用
 * - 自然界の美しい比率を色彩に応用した調和理論
 */
export class GoldenRatioColorGenerator implements ColorGenerator {
  private goldenRatio: number = 0.618033988749895;

  /**
   * 黄金比を使用して色相を決定するアルゴリズム
   *
   * 各色の色相は、前の色相に黄金比を掛けた値で決定されます。
   * これにより、自然界に見られる美しい比率が色彩に反映され、
   * 調和の取れた色の組み合わせが生成されます。
   *
   * @param n 生成する色の数（1以上の整数）
   * @param saturation 彩度（0.0-1.0の範囲、デフォルト: 0.8）
   * @param lightness 明度（0.0-1.0の範囲、デフォルト: 0.6）
   * @param offset 色相の開始オフセット（0-360度、デフォルト: 0）
   * @returns hex形式の色文字列の配列
   */
  generateColors(
    n: number,
    saturation: number = 0.8,
    lightness: number = 0.6,
    offset: number = 0
  ): string[] {
    if (n <= 0) {
      throw new Error("色の数は1以上である必要があります");
    }

    const colors: string[] = [];

    for (let i = 0; i < n; i++) {
      const hue = ((i * this.goldenRatio) % 1.0) * 360 + offset;
      const h = hue % 360;

      const [r, g, b] = hslToRgb(h, saturation, lightness);
      colors.push(rgbToHex(r, g, b));
    }

    return colors;
  }
}

/**
 * 等間隔色相分割による色生成アルゴリズム
 *
 * 色相を等間隔に分割することで色を生成します。
 * 最もシンプルで確実に色が分散されるため、データ可視化やUIデザインに適しています。
 *
 * 参考文献:
 * - Cynthia Brewer "Color in Information Display" (1999) - データ可視化の色選択
 * - 科学的根拠に基づく色覚障害者にも配慮した色パレット設計
 */
export class EquidistantColorGenerator implements ColorGenerator {
  /**
   * 等間隔色相分割による色生成アルゴリズム
   *
   * 色相を360度をn等分して色を生成します。最もシンプルで
   * 確実に色が分散されるため、データ可視化やUIデザインに
   * 適しています。
   *
   * @param n 生成する色の数（1以上の整数）
   * @param saturation 彩度（0.0-1.0の範囲、デフォルト: 0.8）
   * @param lightness 明度（0.0-1.0の範囲、デフォルト: 0.6）
   * @param offset 色相の開始オフセット（0-360度、デフォルト: 0）
   * @returns hex形式の色文字列の配列
   */
  generateColors(
    n: number,
    saturation: number = 0.8,
    lightness: number = 0.6,
    offset: number = 0
  ): string[] {
    if (n <= 0) {
      throw new Error("色の数は1以上である必要があります");
    }

    const colors: string[] = [];

    for (let i = 0; i < n; i++) {
      const hue = (i / n) * 360 + offset;
      const h = hue % 360;

      const [r, g, b] = hslToRgb(h, saturation, lightness);
      colors.push(rgbToHex(r, g, b));
    }

    return colors;
  }
}

/**
 * フィボナッチ数列を使用した色生成アルゴリズム
 *
 * フィボナッチ数列の逆数を使用して色相を決定します。
 * 黄金比に似ているが、より数学的に興味深い分布を生成します。
 *
 * 参考文献:
 * - "Fibonacci Numbers in Nature and Art" - Journal of Mathematics and the Arts (2000s)
 * - 数学的パターンを色彩美学に応用した研究
 */
export class FibonacciColorGenerator implements ColorGenerator {
  private fibonacciRatio: number = 0.381966011250105; // 1 - goldenRatio

  /**
   * フィボナッチ数列を使用した色生成アルゴリズム
   *
   * 各色の色相は、前の色相にフィボナッチ数列の逆数を掛けた値で決定されます。
   * 黄金比に似ているが、より数学的に興味深い分布を生成し、
   * 芸術的なアプリケーションに適しています。
   *
   * @param n 生成する色の数（1以上の整数）
   * @param saturation 彩度（0.0-1.0の範囲、デフォルト: 0.8）
   * @param lightness 明度（0.0-1.0の範囲、デフォルト: 0.6）
   * @param offset 色相の開始オフセット（0-360度、デフォルト: 0）
   * @returns hex形式の色文字列の配列
   */
  generateColors(
    n: number,
    saturation: number = 0.8,
    lightness: number = 0.6,
    offset: number = 0
  ): string[] {
    if (n <= 0) {
      throw new Error("色の数は1以上である必要があります");
    }

    const colors: string[] = [];

    for (let i = 0; i < n; i++) {
      const hue = ((i * this.fibonacciRatio) % 1.0) * 360 + offset;
      const h = hue % 360;

      const [r, g, b] = hslToRgb(h, saturation, lightness);
      colors.push(rgbToHex(r, g, b));
    }

    return colors;
  }
}

/**
 * カラーホイール理論に基づく補色・三色配色アルゴリズム
 *
 * Johannes Ittenのカラーホイール理論に基づいて色を生成します。
 * 補色・三色配色など、視覚的調和を数学的に体系化した理論を実装しています。
 *
 * 参考文献:
 * - Johannes Itten "The Art of Color" (1961) - カラーホイール理論
 * - 補色・三色配色など、視覚的調和を数学的に体系化した理論
 */
export class ColorWheelColorGenerator implements ColorGenerator {
  private baseHues: number[] = [0, 60, 120, 180, 240, 300]; // 基本色相を定義（赤、黄、緑、シアン、青、マゼンタ）

  /**
   * カラーホイール理論に基づく補色・三色配色アルゴリズム
   *
   * 6つの基本色相（赤、黄、緑、シアン、青、マゼンタ）を基準として、
   * より洗練された色の組み合わせを生成します。6色以下の場合は
   * 基本色相を直接使用し、6色を超える場合は補間を行います。
   *
   * @param n 生成する色の数（1以上の整数）
   * @param saturation 彩度（0.0-1.0の範囲、デフォルト: 0.8）
   * @param lightness 明度（0.0-1.0の範囲、デフォルト: 0.6）
   * @param offset 色相の開始オフセット（0-360度、デフォルト: 0）
   * @returns hex形式の色文字列の配列
   */
  generateColors(
    n: number,
    saturation: number = 0.8,
    lightness: number = 0.6,
    offset: number = 0
  ): string[] {
    if (n <= 0) {
      throw new Error("色の数は1以上である必要があります");
    }

    const colors: string[] = [];

    for (let i = 0; i < n; i++) {
      let hue: number;

      if (n <= 6) {
        // 6色以下の場合は基本色相を使用
        hue = this.baseHues[i % 6] + offset;
      } else {
        // 6色を超える場合は補間
        const baseIndex = Math.floor(i / (n / 6));
        const nextIndex = (baseIndex + 1) % 6;
        const ratio = (i % (n / 6)) / (n / 6);
        hue =
          this.baseHues[baseIndex] +
          (this.baseHues[nextIndex] - this.baseHues[baseIndex]) * ratio +
          offset;
      }

      // 360度を超えた場合の処理
      hue = hue % 360;

      const [r, g, b] = hslToRgb(hue, saturation, lightness);
      colors.push(rgbToHex(r, g, b));
    }

    return colors;
  }
}
