# GenerateColor - 開発環境ガイド

このドキュメントは、GenerateColorプロジェクトの開発環境のセットアップと使用方法について説明します。

## 必要な環境

- Node.js 18以上
- Python 3.11以上
- npm または yarn

## セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/yourusername/GenerateColor.git
cd GenerateColor
```

### 2. Node.js依存関係のインストール

```bash
npm install
```

### 3. Python依存関係のインストール

```bash
pip install -r requirements-dev.txt
```

## 開発ツール

### TypeScript開発

#### ESLint

コード品質チェックとコーディング規約の強制を行います。

```bash
# コードチェック
npm run lint

# 自動修正
npm run lint:fix
```

#### Prettier

コードフォーマットを統一します。

```bash
# フォーマット実行
npm run format

# フォーマットチェック
npm run format:check
```

### Python開発

#### Black

Pythonコードの自動フォーマッターです。

```bash
# フォーマット実行
black src/ tests/

# フォーマットチェック
black --check src/ tests/
```

#### isort

インポート文を自動的に整理します。

```bash
# インポート整理
isort src/ tests/

# インポートチェック
isort --check-only src/ tests/
```

#### flake8

PEP8準拠のコードスタイルチェックを行います。

```bash
# PEP8チェック
flake8 src/ tests/
```

## 開発ワークフロー

### 1. 機能開発

```bash
# 新しいブランチを作成
git checkout -b feature/your-feature-name

# 開発作業
# ...

# コード品質チェック
npm run lint
npm run format:check
black --check src/ tests/
isort --check-only src/ tests/
flake8 src/ tests/

# コミット
git add .
git commit -m "Add your feature description"
```

### 2. プルリクエスト作成前のチェック

```bash
# すべてのチェックを実行
npm run lint && npm run format:check && \
black --check src/ tests/ && \
isort --check-only src/ tests/ && \
flake8 src/ tests/
```

## CI/CD

### GitHub Actions

このプロジェクトでは、以下のGitHub Actionsワークフローが設定されています：

- **`.github/workflows/lint-and-format.yml`**: コード品質チェック

#### 実行タイミング

- `main`ブランチと`develop`ブランチへのプッシュ
- プルリクエスト作成時

#### チェック内容

- **TypeScript**: ESLint + Prettier
- **Python**: Black + isort + flake8 (PEP8準拠)

### ローカルでのCI実行

GitHub Actionsと同じチェックをローカルで実行できます：

```bash
# すべてのチェックを実行
npm run lint && npm run format:check && \
black --check src/ tests/ && \
isort --check-only src/ tests/ && \
flake8 src/ tests/
```

## 設定ファイル

### TypeScript設定

- **`.eslintrc.json`**: ESLint設定
- **`.prettierrc`**: Prettier設定
- **`tsconfig.json`**: TypeScript設定

### Python設定

- **`pyproject.toml`**: Black、isort、flake8の設定
- **`requirements-dev.txt`**: 開発用Python依存関係

## トラブルシューティング

### ESLintエラーが発生する場合

```bash
# 自動修正を試す
npm run lint:fix

# 手動で修正が必要な場合は、エラーメッセージを確認
npm run lint
```

### Prettierエラーが発生する場合

```bash
# 自動フォーマット
npm run format
```

### Blackエラーが発生する場合

```bash
# 自動フォーマット
black src/ tests/
```

### isortエラーが発生する場合

```bash
# 自動整理
isort src/ tests/
```

### flake8エラーが発生する場合

```bash
# エラーの詳細を確認
flake8 src/ tests/ --show-source
```

## ベストプラクティス

1. **コミット前にチェック**: プッシュする前に必ずローカルでチェックを実行
2. **小さなコミット**: 機能ごとに小さなコミットを作成
3. **明確なコミットメッセージ**: 何を変更したかが分かるメッセージを記述
4. **ブランチ戦略**: 機能開発は`feature/`ブランチで行う

## 貢献ガイドライン

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/xxxx-feature`)
3. 変更をコミット (`git commit -m 'Add xxxx feature'`)
4. ブランチにプッシュ (`git push origin feature/xxxx-feature`)
5. プルリクエストを作成

**重要**: プルリクエストを作成する前に、必ずローカルでコード品質チェックを実行してください。
