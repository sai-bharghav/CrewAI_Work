# 🚀 CrewAI Tech Stack Story Generator

A multi-agent AI system built using **CrewAI**, designed to research and generate compelling, technically accurate tech-stack stories on any given topic.

This project demonstrates how to orchestrate AI agents sequentially to:
1. 🔎 Research academic & technical sources (e.g., arXiv)
2. ✍️ Transform structured research into engaging engineering narratives

---

## 🧠 Architecture Overview

This system uses a **sequential multi-agent workflow**:

Researcher Agent → Writer Agent → Final Article Output

### 🔬 Researcher Agent
- Searches and analyzes research papers and technical sources
- Extracts architecture, tools, trade-offs, and implementation insights
- Produces structured research output

### ✍️ Writer Agent
- Consumes research findings
- Crafts a compelling, technically deep article
- Explains system design, tech stack choices, and real-world considerations

---

## 🏗️ Tech Stack

- **Python 3.12**
- **CrewAI**
- **OpenAI GPT-4o**
- **uv (Python package manager)**
- **dotenv** for environment management

---


## 📂 Project Structure
CrewAI_Work/  

│  

├── agents.py # Agent definitions  

├── tasks.py # Task definitions  

├── tools.py # Custom tools (e.g., arXiv tool)  

├── main.py # Crew execution entry point  

│  

├── pyproject.toml # uv dependency management  

├── uv.lock  

├── .env # API keys (not committed)  

└── README.md  


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sai-bharghav/CrewAI_Work.git
cd CrewAI_Work
```

### 2️⃣ Create Virtual Environment (Python 3.12)

```bash
uv venv --python 3.12
```

#### Activate(Windows)

```bash
.venv\Scripts\activate
```


#### Activate(Mac/Linux)

```bash
source .venv/bin/activate
```


### 3️⃣ Install Dependencies

```bash
uv add crewai crewai_tools python-dotenv
```


### 4️⃣ Configure Environment Variables

```bash
OPENAI_API_KEY=your_api_key_here
```

### 5️⃣ Run the Project

```bash
python crew.py
```

