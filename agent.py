from crewai import Agent
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool,
)

import OpenAI from "openai";
import os
from textwrap import dedent


class AiDataGather:

    def __init__(self):
        self.llm = Ollama(model=os.environ["MODEL"])

    def data_gather(self):
        search_tool = SerperDevTool()
        web_rag_tool = WebsiteSearchTool()
        return Agent(
            role="Data Engineer",
            goal=dedent(
                """\ gather legal document, user agreements and policy documents."""
            ),
            backstory=dedent(
                """\ as a Data Engineer, you gather significat legal document online"""
            ),
            tools=[search_tool, web_rag_tool],
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
        )
