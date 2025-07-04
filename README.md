# CrewAI Learning Repository

このリポジトリは、[CrewAI](https://docs.crewai.com/) を活用したAIエージェント開発の学習・検証を目的としたプロジェクトです。

## 📚 概要

CrewAIは、複数のAIエージェントが連携・分業してタスクを処理するためのフレームワークです。  
本リポジトリでは、以下の目的でCrewAIを活用したサンプルや実験的コードを管理します。

- CrewAIの基本構造（Agent / Task / Crew / Process）の理解
- シンプルなタスクの自動化や分業処理の実装
- OpenAIなど外部LLMとの連携
- 学習記録やTipsの蓄積

## 🧹 使用技術

- Python 3.10+
- [CrewAI](https://github.com/joaomdmoura/crewai)
- LangChain / OpenAI / その他必要なライブラリ（プロジェクトに応じて）

## 📁 ディレクトリ構成（予定）

```
├── agents/           # エージェント定義
├── tasks/            # タスク定義
├── crews/            # Crew構成（エージェントとタスクの組み合わせ）
├── examples/         # 実行例・実験コード
└── README.md         # このファイル
```

## 環境変数について
環境変数は 以下のファイルで設定します。  
 `C:/work/002.workspace/.env` 

 例：  

 ```python
 # .envファイルの読み込み
env_path = Path("C:/work/002.workspace/.env")
load_dotenv(dotenv_path=env_path)

openai.api_key = os.getenv("OPENAI_API_KEY")

 ```


## 🚀 セットアップ手順

1. Python仮想環境の作成（推奨）:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
    ```

2. 依存関係のインストール:
    ```bash
    pip install -r requirements.txt
    ```

3. 環境変数の設定:
    `.env.example` をコピーして `.env` を作成し、APIキーなどを記入します。

## 🛠 実行方法（例）

```bash
python examples/crew_sample.py
```

## 🔖 参考リンク

- [CrewAI 公式ドキュメント](https://docs.crewai.com/)
- [CrewAI GitHubリポジトリ](https://github.com/joaomdmoura/crewai)
- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)

## イントロダクション資料

日本語でまとめたCrewAI紹介文書を `crewai_intro_ja.md` として用意しています。
サンプルコードの概要や実行方法を簡潔に説明していますので、併せてご覧ください。

## 📌 補足

このリポジトリは個人またはチームの学習目的で使用しており、商用利用や本番運用は想定していません。
