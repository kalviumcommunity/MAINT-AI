# MAINT-AI

## AI-Powered Maintenance Intelligence using RAG

MAINT-AI is an AI-powered, source-referenced maintenance troubleshooting assistant designed to help **manufacturing technicians and maintenance engineers** quickly find reliable information from approved maintenance documentation.

Instead of manually searching through equipment manuals, maintenance logs, troubleshooting guides, and safety procedures, technicians can enter an equipment problem, error code, or symptom and receive relevant troubleshooting guidance.

MAINT-AI uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant maintenance information from approved documents and provides the retrieved context to an LLM to generate a grounded troubleshooting response with source references and relevant safety information.

> **MAINT-AI is a decision-support system. It assists technicians but does not directly control machinery or perform maintenance actions.**

---

# Problem Statement

Manufacturing organizations maintain large amounts of technical information such as:

- Equipment manuals
- Maintenance logs
- Troubleshooting guides
- Safety procedures
- Technical documentation

However, this information is often distributed across lengthy documents and different records.

During a machine failure, technicians may need to manually search through several documents to:

- Identify possible causes.
- Find troubleshooting steps.
- Check equipment-specific information.
- Verify safety procedures.

This increases troubleshooting time, machine downtime, and operational costs.

MAINT-AI solves this problem by providing a centralized AI-powered interface that retrieves relevant maintenance information and presents source-grounded troubleshooting guidance.

---

# Solution

MAINT-AI allows technicians to:

1. Log in to the application.
2. Access the maintenance dashboard.
3. Select or enter equipment information.
4. Enter an error code or describe the machine problem.
5. Submit the troubleshooting query.
6. Retrieve relevant information from approved maintenance documents.
7. Generate an AI-assisted troubleshooting response.
8. View possible causes and recommended troubleshooting steps.
9. View relevant safety information.
10. Verify the response using source references.
11. Review previous troubleshooting queries.

The system is designed to provide assistance based on the organization's approved maintenance knowledge base rather than relying only on general LLM knowledge.

---

# How MAINT-AI Works

```text
                         Technician
                              |
                              v
                           Login
                              |
                              v
                      Streamlit Frontend
                              |
                              v
                         New Query
                              |
                              v
                       Flask Backend
                              |
                              v
                      Query Processing
                              |
                              v
                    BGE-M3 Query Embedding
                              |
                              v
                PostgreSQL + pgvector Search
                              |
                              v
                 Relevant Document Chunks
                              |
                              v
                         LangChain
                              |
                              v
                         OpenAI API
                              |
                              v
                Troubleshooting Response
                              |
             +----------------+----------------+
             |                |                |
             v                v                v
        Possible Causes   Troubleshooting   Safety
                              Steps          Information
             |
             v
                     Source References
````

---

# RAG Pipeline

MAINT-AI uses **Retrieval-Augmented Generation (RAG)** to ground AI-generated troubleshooting guidance in approved maintenance documentation.

## Document Processing

```text
Maintenance Document
        ↓
     PyMuPDF
        ↓
   Text Extraction
        ↓
    Text Chunking
        ↓
      BGE-M3
        ↓
 Generate Embeddings
        ↓
PostgreSQL + pgvector
```

The document ingestion process includes:

* Maintenance document upload
* PDF text extraction
* Text splitting
* Chunk creation
* Metadata association
* BGE-M3 embedding generation
* Vector storage in PostgreSQL using pgvector

---

## Question Answering

```text
Technician Query
       ↓
Equipment + Problem + Error Code
       ↓
BGE-M3 Query Embedding
       ↓
Vector Similarity Search
       ↓
Top-K Relevant Chunks
       ↓
Relevant Maintenance Context
       ↓
LangChain
       ↓
OpenAI API
       ↓
Structured Troubleshooting Response
       ↓
Sources + Safety Information
```

The retrieved documentation is provided to the LLM as context so that the generated response can be grounded in approved maintenance information.

---

# Grounded Troubleshooting

MAINT-AI is designed to avoid acting as an unrestricted chatbot.

The system should:

* Use retrieved maintenance documentation whenever relevant information is available.
* Provide supporting source references.
* Use equipment context when available.
* Communicate uncertainty when evidence is insufficient.
* Avoid confidently inventing unsupported maintenance procedures.
* Keep the final operational decision with authorized maintenance personnel.

If sufficient information cannot be found, the system should clearly communicate that verified information is unavailable.

Example:

```text
Insufficient verified information was found in the available
maintenance documentation for this issue.
Please verify the equipment manual or applicable maintenance procedure.
```

---

# Example

## Technician Query

```text
Equipment: M-204

Problem:
Motor is overheating after approximately 30 minutes of operation.
```

## MAINT-AI Response

```text
Possible Causes:

- Insufficient lubrication
- Cooling system issue
- Excessive motor load

Recommended Actions:

- Check the lubrication level.
- Inspect the cooling system.
- Verify motor load.

Safety:

Follow the applicable equipment safety and lockout/tagout
procedure before inspection.

Sources:

Motor Maintenance Manual
Section: 4.2
Page: 18
```

---

# Source References

MAINT-AI provides source information associated with retrieved maintenance content.

Source information may include:

```text
Document Name
Document Type
Section
Page Number
Equipment Association
Chunk ID
```

Example:

```text
Source:
Motor Maintenance Manual

Section:
4.2

Page:
18

Equipment:
M-204
```

The source-reference feature allows technicians to verify the information in the original documentation before taking action.

---

# Safety Information

Safety is an important part of the MAINT-AI workflow.

The system shall:

* Display relevant safety instructions when available.
* Use approved safety documentation as part of the knowledge base.
* Show safety information alongside troubleshooting guidance.
* Clearly indicate when safety information is unavailable.
* Avoid presenting unsupported procedures as verified instructions.

> MAINT-AI does not make autonomous safety decisions and does not directly control equipment.

---

# Authentication and Users

MAINT-AI is designed for authorized users with different responsibilities.

## Primary Users

* Floor Technicians
* Maintenance Engineers

## Secondary Users

* Maintenance Managers
* Maintenance Supervisors

## Administrative Users

Authorized users responsible for:

* Maintenance documentation
* Knowledge-base management
* Document administration

The application includes login functionality so authorized users can access the MAINT-AI system.

---

# Key Features

* User login
* Technician dashboard
* Equipment selection
* Equipment ID entry
* Error code input
* Problem and symptom description
* AI-powered troubleshooting
* RAG-based document retrieval
* BGE-M3 embeddings
* PostgreSQL + pgvector vector search
* OpenAI API integration
* Possible cause generation
* Recommended troubleshooting steps
* Safety information
* Source references
* Query history
* Document upload
* Document management
* Document viewer
* Feedback on AI responses
* Basic system settings
* Grounded-response handling
* Insufficient-evidence handling

---

# Document Management

Authorized users can manage maintenance documentation through the application.

The document management workflow supports:

```text
Upload Document
      ↓
Document Processing
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embedding Generation
      ↓
Vector Storage
      ↓
Knowledge Base
```

Users should be able to:

* Upload maintenance documents.
* View available documents.
* View document details.
* Categorize documents.
* Associate documents with equipment.
* Replace outdated documents.
* Remove outdated documents where required.
* View document processing/indexing status.

The initial implementation primarily supports **PDF-based technical documentation**.

---

# Query History

MAINT-AI maintains a history of previous troubleshooting queries.

Users can view information such as:

```text
Previous Query
Equipment
Date / Time
Response
Status
```

Users should also be able to reopen previous troubleshooting results and access their associated sources.

---

# Feedback

Users can provide simple feedback on AI responses.

The initial feedback system supports:

* Helpful
* Not Helpful
* Optional feedback comment

Feedback can be used to evaluate the usefulness and quality of MAINT-AI responses.

---

# Technology Stack

## AI / RAG

| Technology                   | Purpose                                       |
| ---------------------------- | --------------------------------------------- |
| **OpenAI API**               | LLM-based troubleshooting response generation |
| **BAAI BGE-M3**              | Document and query embeddings                 |
| **LangChain**                | RAG pipeline orchestration                    |
| **pgvector**                 | Vector similarity search                      |
| **PyMuPDF**                  | PDF text extraction                           |
| **LangChain Text Splitters** | Document chunking                             |

## Application

| Technology    | Purpose                       |
| ------------- | ----------------------------- |
| **Python**    | Main programming language     |
| **Streamlit** | Frontend application          |
| **Flask**     | Backend API/application layer |

## Database

| Technology     | Purpose                              |
| -------------- | ------------------------------------ |
| **PostgreSQL** | Application and maintenance data     |
| **pgvector**   | Vector storage and similarity search |
| **pgAdmin**    | Database management                  |

## Development

| Technology      | Purpose                           |
| --------------- | --------------------------------- |
| **Git**         | Version control                   |
| **GitHub**      | Repository and team collaboration |
| **Python venv** | Virtual environment               |
| **.env**        | Environment configuration         |

---

# Data Storage

## Application Data

PostgreSQL is used to store structured application and maintenance data.

The database includes entities such as:

```text
Users
Equipment
Documents
Document Chunks
Issues
Queries
Feedback
```

---

## Document Data

Maintenance documents are associated with equipment and stored with relevant metadata.

Example:

```text
Document
 ├── Document ID
 ├── Document Name
 ├── Document Type
 ├── Equipment
 ├── Uploaded By
 └── Upload Date
```

---

## Document Chunks

Document content is divided into smaller chunks for retrieval.

Example:

```text
Document
   ↓
Chunk
   ├── Chunk ID
   ├── Document ID
   ├── Chunk Text
   ├── Page Number
   └── Embedding
```

Embeddings are stored in PostgreSQL using the `pgvector` extension.

---

# Project Structure

```text
MAINT-AI/
│
├── backend/
│   ├── app.py
│   │
│   ├── controllers/
│   │   ├── auth_controller.py
│   │   ├── document_controller.py
│   │   ├── feedback_controller.py
│   │   └── query_controller.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── equipment.py
│   │   ├── document.py
│   │   ├── document_chunk.py
│   │   ├── issue.py
│   │   ├── query.py
│   │   └── feedback.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── documents.py
│   │   ├── feedback.py
│   │   ├── query.py
│   │   └── history.py
│   │
│   ├── services/
│   │   └── query_service.py
│   │
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   └── rag_pipeline.py
│   │
│   └── utils/
│       ├── database.py
│       └── config.py
│
├── frontend/
│   ├── app.py
│   │
│   ├── pages/
│   │   ├── dashboard.py
│   │   ├── new_query.py
│   │   ├── results.py
│   │   ├── history.py
│   │   ├── sources.py
│   │   ├── document_viewer.py
│   │   ├── documents.py
│   │   ├── feedback.py
│   │   └── settings.py
│   │
│   ├── components/
│   ├── services/
│   │   └── api.py
│   ├── utils/
│   └── styles/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Backend Architecture

The backend is implemented using Flask.

The Flask application provides modules for:

* Authentication
* Query processing
* Document management
* Feedback
* History
* Database integration
* RAG integration

The backend architecture follows:

```text
Streamlit Frontend
        ↓
Flask Backend
        ↓
Routes / Controllers
        ↓
Services
        ↓
RAG Pipeline
        ↓
PostgreSQL + pgvector
```

---

# API Modules

The Flask backend provides functionality for:

## Authentication

Handles:

* User authentication
* Login
* Logout
* User access

## Query

Handles:

* Maintenance troubleshooting queries
* Equipment context
* Problem descriptions
* Error codes
* RAG retrieval
* Troubleshooting response generation

## Documents

Handles:

* Document upload
* Document management
* Document metadata
* Knowledge-base documents

## Feedback

Handles:

* Helpful / Not Helpful feedback
* User comments

---

# Frontend and Backend Integration

The main application flow is:

```text
Technician
    ↓
Streamlit New Query
    ↓
Frontend Service
    ↓
Flask Backend
    ↓
Query Processing
    ↓
RAG Pipeline
    ↓
PostgreSQL + pgvector
    ↓
Retrieved Context
    ↓
LLM
    ↓
Troubleshooting Response
    ↓
Streamlit Results
```

The frontend is responsible for collecting technician input and presenting the response.

The backend is responsible for query processing, retrieval, database interaction, and AI/RAG processing.

---

# Setup

## 1. Clone the Repository

```bash
git clone https://github.com/kalviumcommunity/MAINT-AI.git
cd MAINT-AI
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

---

## 3. Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=your_postgresql_connection_string
OPENAI_API_KEY=your_openai_api_key
```

> Never commit `.env` or API credentials to GitHub.

---

# Database Setup

MAINT-AI uses:

```text
PostgreSQL
   +
pgvector
```

The database stores application data and document embeddings.

The `pgvector` extension must be enabled in PostgreSQL.

The system uses vector similarity search to retrieve relevant document chunks for technician queries.

---

# Running the Application

## Start Flask Backend

From the project root:

```bash
python backend/app.py
```

The Flask development server runs locally according to the configuration in `backend/app.py`.

---

## Start Streamlit Frontend

Open another terminal:

```bash
streamlit run frontend/app.py
```

The Streamlit application will then be available locally.

---

# User Flow

```text
Login
   ↓
Dashboard
   ↓
New Query
   ↓
Select Equipment
   ↓
Enter Error Code / Symptoms
   ↓
Describe Maintenance Problem
   ↓
Submit Query
   ↓
RAG Retrieval
   ↓
Relevant Document Chunks
   ↓
LLM Response
   ↓
Troubleshooting Result
   ↓
Sources + Safety Information
   ↓
Verify Against Approved Documentation
```

---

# Example User Flow

```text
Technician
    ↓
Select Equipment: M-204
    ↓
Enter Problem:
Motor is overheating after 30 minutes
    ↓
Submit Query
    ↓
Retrieve Relevant Maintenance Chunks
    ↓
Generate Troubleshooting Guidance
    ↓
Display:
    - Possible Causes
    - Recommended Actions
    - Safety
    - Sources
```

---

# AI Safety and Reliability

MAINT-AI follows several principles to improve reliability.

## Grounded Responses

Responses should use relevant retrieved maintenance documentation whenever available.

## Source References

Generated responses should provide supporting document references.

## Insufficient Evidence

When relevant information cannot be found, the system should clearly communicate that verified information is unavailable.

## Human Decision Making

Technicians and authorized maintenance personnel remain responsible for the final operational decision.

---

# Evaluation

MAINT-AI will initially be evaluated using simulated maintenance scenarios.

## Proposed Success Metrics

| Metric                                      | Target |
| ------------------------------------------- | -----: |
| Reduction in manual document search time    |  ≥ 40% |
| Reduction in simulated troubleshooting time |  ≥ 30% |
| Source-referenced responses                 |  ≥ 95% |
| Positive user feedback                      |  ≥ 80% |

---

# Technical Evaluation

The RAG and AI pipeline will also be evaluated using:

* Retrieval relevance
* Response relevance
* Source-reference correctness
* Response faithfulness
* Response latency
* Ability to communicate insufficient evidence

---

# Example Evaluation Scenario

| Maintenance Query      | Expected Information             |
| ---------------------- | -------------------------------- |
| Motor overheating      | Motor maintenance documentation  |
| Cooling system problem | Cooling-system procedure         |
| High vibration         | Equipment troubleshooting guide  |
| Lubrication issue      | Maintenance manual               |
| Unknown error code     | Relevant equipment documentation |

---

# Scope

## In Scope

* User login
* Technician dashboard
* Equipment/problem query submission
* AI-powered troubleshooting
* RAG-based document retrieval
* Maintenance documentation
* Source references
* Safety information
* Query history
* Document upload and management
* Basic system settings
* Feedback on AI responses

## Out of Scope

* Real-time IoT/sensor integration
* Predictive maintenance
* Automatic machine control
* PLC/SCADA integration
* Automatic repair execution
* Spare-parts ordering
* Advanced enterprise analytics
* LLM fine-tuning
* Voice-based interaction

---

# Research Basis

MAINT-AI is based on research in:

## RAG

* Dense semantic retrieval
* Query and document embeddings
* Top-K retrieval
* Retrieval-Augmented Generation
* External knowledge bases
* Grounded generation
* Source attribution
* Retrieval quality
* Dense vs keyword retrieval

## LLM-based Fault Diagnosis

* Industrial machine fault diagnosis
* Structured troubleshooting
* Equipment context
* Model selection
* Accuracy evaluation
* Generalization
* Adaptability
* Latency and cost

The core principle is:

```text
RETRIEVE
    ↓
UNDERSTAND
    ↓
RECOMMEND
    ↓
VERIFY
```

---

# Future Enhancements

Future versions of MAINT-AI may include:

* Hybrid semantic + keyword retrieval
* Retrieval reranking
* Advanced RAG evaluation
* LLM fine-tuning
* Real-time sensor integration
* Predictive maintenance
* Voice-based interaction
* Multilingual support
* Integration with enterprise maintenance systems
* Advanced maintenance analytics

---

# Mock UI/UX

The initial MAINT-AI interface includes the following screens:

```text
Login
   ↓
Dashboard
   ↓
New Query
   ↓
Troubleshooting Results
   ↓
Source References
   ↓
Document Viewer
```

Additional screens include:

* Query History
* Document Management
* System Settings
* Feedback

The interface is designed to provide a simple workflow for technicians who need to troubleshoot equipment quickly.

---

# Team Responsibilities

## Ajay Dharshan — Product / Documentation / Integration

* Product Requirements Document
* Product requirements
* Project documentation
* Mock UI/UX design
* System workflow definition
* Streamlit frontend integration
* Frontend-backend integration testing
* Application integration and debugging

## Vijayashree — AI / UI/UX

* LLM research
* Model evaluation
* UI/UX research and design
* Figma design

## Amulya — RAG / Database

* RAG research
* Retrieval architecture
* Embedding research
* Vector-search research
* PostgreSQL and pgvector
* RAG pipeline implementation
* Technical mockup

> Team members collaborate on implementation, testing, integration, and final presentation.

---

# Development Roadmap

## Phase 1 — Foundation

* GitHub repository setup
* Python environment
* Environment variables
* PostgreSQL setup
* pgvector setup
* Streamlit setup
* Flask setup

## Phase 2 — Database and Models

* User model
* Equipment model
* Document model
* Document chunk model
* Issue model
* Query model
* Feedback model
* Database connection

## Phase 3 — Document Processing

* PDF processing
* Text extraction
* Text chunking
* Metadata handling
* Embedding generation
* Vector storage

## Phase 4 — RAG Pipeline

* Query embedding
* Vector similarity search
* Top-K retrieval
* Context construction
* LangChain integration
* OpenAI integration
* Source references
* Safety context

## Phase 5 — Application Integration

* Streamlit dashboard
* New Query interface
* Results interface
* Source display
* Document management
* Query history
* Feedback
* Frontend-backend integration

## Phase 6 — Testing and Delivery

* End-to-end testing
* RAG evaluation
* Source-reference testing
* Error handling
* Documentation
* README completion
* Demo preparation
* Final presentation

---

# Project Status

**Under Development**

MAINT-AI is being developed as an AI-powered maintenance decision-support application using:

```text
Python
+
Streamlit
+
Flask
+
PostgreSQL
+
pgvector
+
BGE-M3
+
LangChain
+
OpenAI API
```

---

# Success Criteria

The MAINT-AI initial version will be considered successful when:

* Users can log in.
* Technicians can create maintenance queries.
* Equipment information can be submitted.
* Error codes and symptoms can be entered.
* Maintenance documents can be processed.
* Document chunks can be embedded.
* Embeddings can be stored in PostgreSQL with pgvector.
* Relevant document chunks can be retrieved.
* Retrieved context can be provided to the LLM.
* Troubleshooting responses can be generated.
* Responses provide source references.
* Relevant safety information can be displayed.
* The system can communicate when sufficient evidence is unavailable.
* Previous queries can be accessed.
* Users can provide feedback.
* The complete frontend and backend workflow can be demonstrated.

---

# Conclusion

**MAINT-AI** is an AI-powered maintenance intelligence system designed to help manufacturing technicians troubleshoot equipment problems faster.

The system combines:

* Maintenance documentation
* Semantic retrieval
* BGE-M3 embeddings
* PostgreSQL + pgvector
* LangChain
* OpenAI API
* Streamlit
* Flask

to provide source-grounded troubleshooting assistance.

Instead of relying only on general-purpose AI knowledge, MAINT-AI retrieves relevant organizational maintenance documentation and uses that information as context for generating the response.

The core workflow is:

```text
RETRIEVE → UNDERSTAND → RECOMMEND → VERIFY
```

MAINT-AI provides technicians with relevant maintenance information, possible causes, troubleshooting steps, safety information, and source references while keeping the final operational decision with authorized maintenance personnel.

````

