from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, tool
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import PDFSearchTool, SerperDevTool
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AiCvJobsRecommender():
    """AiCvJobsRecommender crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    tools: List
    path_to_file = './CV_Kartikeya_Chitranshi.pdf'
    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def cv_scanner(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_scanner'], # type: ignore[index]
            tools=[self.cv_rag_tool()],
            verbose=True
        )

    @agent
    def job_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['job_search_agent'], # type: ignore[index]
            tools=[self.web_search_tool()],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def cv_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['cv_analysis_task'], # type: ignore[index]
        )

    @task
    def job_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_search_task'], # type: ignore[index]
            output_file='recommended_jobs.md'
        )
    
    @tool
    def cv_rag_tool(self):
        rag_tool = PDFSearchTool(
            pdf=self.path_to_file
        )
        
        return rag_tool
    
    @tool
    def web_search_tool(self):
        return SerperDevTool()
        
    @crew
    def crew(self) -> Crew:
        """Creates the AiCvJobsRecommender crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
