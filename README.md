# Agentic Jobs Recommender

An AI-powered job recommendation system that intelligently analyzes your CV and searches for matching job opportunities using a multi-agent architecture built with CrewAI.

## Overview

Agentic Jobs Recommender automates the job search process by:
- Extracting detailed information from CV documents using RAG (Retrieval-Augmented Generation)
- Intelligently searching the web for relevant job opportunities that match your profile
- Generating curated job recommendations with detailed match explanations

The system uses two specialized AI agents that work together:
1. **CV Scanner Agent**: Analyzes your CV and extracts your professional profile
2. **Job Search Agent**: Searches for matching job opportunities based on your profile

## Features

- **RAG-Based CV Analysis**: Uses ChromaDB vector embeddings for semantic understanding of your CV
- **Automated Web Search**: Leverages SerperDev API to find relevant job listings across multiple platforms
- **Multi-Agent Collaboration**: CrewAI orchestrates agents working in sequence to deliver optimal results
- **Training Capability**: Improve agent performance through iterative training
- **Task Replay**: Debug and replay specific tasks for development and testing
- **Structured Output**: Results delivered in clean Markdown format

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    MAIN ENTRY POINT                     │
│                      (main.py)                          │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              CREW ORCHESTRATION                         │
│                 (crew.py)                               │
│  - Process: Sequential                                  │
│  - 2 Agents, 2 Tasks                                    │
└─────────┬───────────────────────────────┬───────────────┘
          │                               │
          ▼                               ▼
┌──────────────────────┐      ┌───────────────────────────┐
│   CV SCANNER AGENT   │      │  JOB SEARCH AGENT         │
│                      │      │                           │
│ Role: CV Analyst     │      │ Role: Career Research     │
│ Tool: PDFSearchTool  │      │ Tool: SerperDevTool       │
│                      │      │       (Web Search)        │
└──────────┬───────────┘      └───────────┬───────────────┘
           │                              │
           ▼                              ▼
    ┌──────────────┐              ┌──────────────┐
    │CV Analysis   │              │Job Search    │
    │Task          │──────────────▶│Task          │
    └──────────────┘              └──────┬───────┘
                                         │
                                         ▼
                                  ┌──────────────┐
                                  │recommended_  │
                                  │jobs.md       │
                                  └──────────────┘
```

## Prerequisites

- Python >=3.10, <3.14
- UV package manager (recommended) or pip
- OpenAI API key
- SerperDev API key (for web search)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Agentic-Jobs-Recommender/ai_cv_jobs_recommender
   ```

2. **Install UV package manager** (if not already installed):
   ```bash
   pip install uv
   ```

3. **Install dependencies:**
   ```bash
   crewai install
   # or
   uv sync
   ```

4. **Set up environment variables:**
   Create a `.env` file in the `ai_cv_jobs_recommender` directory:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

## Usage

### Run Job Recommendation

```bash
# Using the installed script
ai_cv_jobs_recommender

# Or directly
python src/ai_cv_jobs_recommender/main.py
```

The system will:
1. Analyze the CV PDF located in the project directory
2. Extract your professional profile (skills, experience, education)
3. Search for matching job opportunities
4. Generate recommendations in `recommended_jobs.md`

### Train Agents

Improve agent performance through iterative training:

```bash
# Train with n iterations
python src/ai_cv_jobs_recommender/main.py train <n_iterations>
```

### Replay Tasks

Replay a specific task execution for debugging:

```bash
python src/ai_cv_jobs_recommender/main.py replay <task_id>
```

### Test Crew

Test the crew execution and return results:

```bash
python src/ai_cv_jobs_recommender/main.py test
```

## Configuration

### Agent Configuration

Agents are defined in `src/ai_cv_jobs_recommender/config/agents.yaml`:
- **CV Scanner Agent**: Analyzes CV documents using PDFSearchTool with RAG
- **Job Search Agent**: Searches for jobs using SerperDevTool

### Task Configuration

Tasks are defined in `src/ai_cv_jobs_recommender/config/tasks.yaml`:
- **CV Analysis Task**: Extracts professional profile from CV
- **Job Search Task**: Finds matching job opportunities

### User Preferences

Customize search parameters in `knowledge/user_preference.txt` to specify:
- Target job titles
- Preferred locations
- Required skills
- Other search criteria

## Project Structure

```
Agentic-Jobs-Recommender/
├── ai_cv_jobs_recommender/          # Main application directory
│   ├── src/                         # Source code
│   │   └── ai_cv_jobs_recommender/
│   │       ├── config/              # Agent and task configurations
│   │       │   ├── agents.yaml      # Agent definitions
│   │       │   └── tasks.yaml       # Task definitions
│   │       ├── tools/               # Custom tool implementations
│   │       ├── main.py              # Entry point
│   │       └── crew.py              # Crew orchestration
│   ├── db/                          # ChromaDB vector database
│   ├── knowledge/                   # Knowledge base
│   │   └── user_preference.txt      # User preferences
│   ├── pyproject.toml               # Project configuration
│   ├── recommended_jobs.md          # Output: Job recommendations
│   └── CV_Kartikeya_Chitranshi.pdf  # Sample CV (replace with yours)
└── README.md                        # This file
```

## Technologies Used

- **CrewAI** (v0.177.0+): Multi-agent AI orchestration framework
- **ChromaDB** (v0.5.23): Vector database for document embeddings
- **OpenAI API**: LLM backend for agent intelligence
- **SerperDev**: Web search API integration
- **PDFSearchTool**: RAG-based CV document analysis
- **Pydantic**: Data validation
- **UV**: Modern Python package manager

## Output

The system generates a `recommended_jobs.md` file containing:
- Curated list of job opportunities (8-12 recommendations)
- Direct links to job postings
- Match explanations for each recommendation
- Coverage across multiple job platforms (LinkedIn, Glassdoor, Indeed, etc.)

## Development

### Custom Tools

Add custom tools in `src/ai_cv_jobs_recommender/tools/`:
- Use `custom_tool.py` as a template
- Import and register tools in `crew.py`

### Modifying Agents

Edit `config/agents.yaml` to:
- Change agent roles and goals
- Add new agents
- Modify agent backstories

### Modifying Tasks

Edit `config/tasks.yaml` to:
- Change task descriptions
- Modify expected outputs
- Add new tasks

## Author

**Kartikeya Chitranshi**
- Email: kartikeya4524@gmail.com

## License

This project is licensed under the terms specified in the LICENSE file (if available).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure `.env` file contains valid API keys
2. **Package Installation**: Use `uv sync` or `crewai install` to resolve dependency issues
3. **Python Version**: Verify you're using Python 3.10-3.13
4. **ChromaDB Issues**: Delete `db/` directory and restart to rebuild vector database

## Acknowledgments

Built with [CrewAI](https://www.crewai.com/) - a framework for orchestrating role-playing, autonomous AI agents.
