# Java-to-Python & Agentic AI Sandbox

An engineering workspace dedicated to mastering idiomatic Python, high-performance microservices, and production-grade Agentic AI. This project serves as a focused sandbox to map 10+ years of Java/Spring Boot enterprise engineering patterns directly into lightweight, composable Python solutions.

---

## 🗺️ 16-Week Roadmap Strategy

The repository follows a structured, hands-on progression scaling from foundational automation to autonomous AI agents:

### Phase 1: Core Engine & Testing (Weeks 1–4)
* **Topics:** Idiomatic syntax, advanced collections, exceptions, file I/O, OOP, type hints, and `pytest`.
* **Milestones:** CLI log-file analyzers, JSON task managers, and utility libraries.

### Phase 2: Microservices & Async Architecture (Weeks 5–8)
* **Topics:** FastAPI frameworks, Pydantic data validation, SQLAlchemy, PostgreSQL integration, and `async/await` runtime loops.
* **Milestones:** Dockerized CRUD services and high-throughput asynchronous workers.

### Phase 3: RAG & Agentic Workflow Systems (Weeks 9–16)
* **Topics:** LLM tool-calling, semantic embeddings, vector storage, agent memory patterns, and guardrails.
* **Milestones:** "Ask My Documents" vector workflows and a multi-step **Developer Incident Assistant** integrated with Kafka and log environments.

---

## 🔄 Core Mindset Shifts (Java 🔄 Python)

* **Composition over Hierarchy:** Swapping deep class hierarchies and interface boilerplate for small, highly composable functions.
* **Streamlined Data DTOs:** Replacing verbose boilerplate with `dataclass` structures and **Pydantic** models.
* **Lightweight Isolation:** Using local `.venv` environments instead of complex global scopes to mimic isolated Gradle/Maven dependencies.
* **Testing Workflows:** Shifting from JUnit paradigms over to native, expression-driven **pytest** suites.

---

## 🛠️ Project Workspace Layout

* `.venv/` - Project-isolated runtime and dependency binaries (Excluded from source control).
* `.gitignore` - Standard filters for caching systems, compiled code, and environment configurations.
* `README.md` - Technical architecture blueprints, roadmap details, and startup workflows.
* `analyzer.py` - Core scripting framework executing current analysis and stream parsing.

---

## 🚀 Getting Started & Execution

### 1. Initialize & Verify Runtime
Ensure you are using Python 3.12+ inside your shell workspace:
```bash
python3 --version
```

### 2. Spin Up Environment
Activate the isolated project scope to bind local tools and script pointers:
```bash
source .venv/bin/activate
```
*Note: Your prompt will display `(.venv)` upon successful activation.*

### 3. Run the Processing Engine
Execute the active script using the context-bound interpreter:
```bash
python3 analyzer.py
```

### 4. Tear Down Session
Safely exit the isolated environment when your engineering session concludes:
```bash
deactivate
```
