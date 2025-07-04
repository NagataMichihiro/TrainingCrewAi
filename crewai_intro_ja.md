# CrewAIの概要とサンプルコードの紹介

CrewAIは、複数のAIエージェントを連携させてタスクを分担・実行させるフレームワークです。  
一般的な言語モデル単体では扱いにくい複雑な処理を、役割を分けたエージェントで協調させることにより効率的に解決できます。  

以下では、CrewAIの基本的な仕組みと、実際に動作するサンプルスクリプト `examples/test1.py` を紹介します。  

## CrewAIの基本要素

- **Agent**: 役割や目標、使用ツールを定義します。  
- **Task**: Agentが取り組む具体的な作業内容を記述します。  
- **Crew**: 複数のAgentとTaskをまとめて実行するユニットです。  

## サンプル `test1.py` について

このリポジトリでは、以下のページを参考にしたサンプルコード `test1.py` を用意しています。  
<https://arpable.com/artificial-intelligence/crewai-multi-agent-framework/>  

元のサンプルはそのままでは動作しなかったため、次のような変更を加えました。  

1. **LangChainのモジュール更新**: `langchain_openai.ChatOpenAI` を使用して最新の構成に対応しました。  
2. **検索ツールの追加**: `WebsiteSearchTool` を利用し、Web検索を行えるようにしました。  
3. **環境変数の読み込み**: `.env` ファイルを指定してAPIキーを取得するよう修正しました。  

実行すると、リサーチャーAgentが情報収集を担当し、その結果をもとにライターAgentが日本語レポートを生成します。  

```bash
python examples/test1.py
```

上記コマンドを実行すると、コンソールに最終的なレポートが表示されます。  
興味のある方は内容をカスタマイズしてみてください。  

