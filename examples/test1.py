# 修正版 test1.py
import os
from pathlib import Path
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

# LangChainの新しい推奨モジュールを使用
from langchain_openai import ChatOpenAI
from crewai_tools import WebsiteSearchTool  # crewai[tools] に含まれる
from typing import Optional

# .envファイルの読み込み
env_path = Path("C:/work/002.workspace/.env")
load_dotenv(dotenv_path=env_path)

# OpenAIチャットモデルの初期化
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo"
)

search_tool = WebsiteSearchTool()

# リサーチャーエージェント
researcher = Agent(
    role="リサーチャー",
    goal="特定のトピックに関する情報を収集し、分析する",
    backstory="あなたは情報収集のスペシャリストです。効率的に関連情報を見つけ出し、整理する能力に長けています。",
    verbose=True,
    llm=llm,
    tools=[search_tool]
)

# ライターエージェント
writer = Agent(
    role="ライター",
    goal="収集された情報を元に、わかりやすいレポートを作成する",
    backstory="あなたは複雑な情報を整理して、読みやすく魅力的なコンテンツに変換するのが得意です。",
    verbose=True,
    llm=llm
)

# タスク定義
research_task = Task(
    description="AIマルチエージェントシステムの最新動向について調査せよ",
    agent=researcher,
    expected_output="AIマルチエージェントシステムの最新トレンド、主要プラットフォーム、応用事例のリスト"
)

writing_task = Task(
    description="調査結果をもとに、1000字程度のレポートを **日本語で** 作成せよ",
    agent=writer,
    expected_output="AIマルチエージェントシステムに関する包括的な概要レポート",
    context=[research_task]
)

# Crew定義
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

# 実行
result = crew.kickoff()

print("最終レポート:")
print(result)
