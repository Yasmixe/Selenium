from crewai import Task
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool,
)

from langchain_community.llms import Ollama
import os
from textwrap import dedent


class aidatagatheringTask:
    def newtask(self, agent):
        return Task(
            description="collect legal document, user agreements and policy documents",
            agent=agent,
            async_execution=True,
            expected_output="""a list of all documents, and detailed legal document, user agreements and policy documents""",
        )
