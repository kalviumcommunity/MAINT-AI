# MAINT-AI

## AI-Powered Maintenance Intelligence

MAINT-AI is an AI-powered, source-referenced maintenance troubleshooting assistant designed to help manufacturing technicians quickly find reliable information from approved maintenance documentation.

> **Important:** MAINT-AI is a decision-support system. It assists technicians but does not directly control machinery or perform maintenance actions.

---

## 1. Problem Statement

Manufacturing firms maintain equipment manuals, maintenance logs, troubleshooting guides, and safety procedures, but floor technicians may not be able to quickly access the relevant information during machine failures.

The required information is often spread across lengthy documents and different records. Technicians have to manually search through these sources to identify possible causes, find troubleshooting steps, and verify safety procedures.

This increases troubleshooting time, machine downtime, and operational costs.

MAINT-AI addresses this problem by retrieving relevant maintenance information and generating useful troubleshooting guidance based on approved documentation.

---

## 2. Product Vision

To help manufacturing technicians quickly find reliable maintenance information and troubleshoot equipment problems using AI-powered, source-grounded assistance.

---

## 3. Target Users

### Primary Users

* Floor Technicians
* Maintenance Engineers

### Secondary Users

* Maintenance Managers
* Maintenance Supervisors

### Administrative Users

* Authorized users responsible for maintaining the documentation and knowledge base

---

## 4. Business Value

MAINT-AI aims to:

* Reduce the time technicians spend searching through manuals and maintenance documents.
* Provide faster access to relevant troubleshooting information.
* Provide source-referenced AI responses.
* Make maintenance documentation easier to access.
* Provide relevant safety information during troubleshooting.
* Maintain a searchable history of previous troubleshooting queries.
* Help technicians make faster and more informed maintenance decisions.

---

## 5. Objectives

* Centralize equipment-related maintenance documentation.
* Allow technicians to submit equipment problems and error codes.
* Retrieve relevant information from approved maintenance documents.
* Generate AI-assisted troubleshooting recommendations.
* Provide source references for AI-generated responses.
* Display relevant safety instructions.
* Allow users to view previous troubleshooting queries.
* Allow authorized users to upload and manage maintenance documents.
* Provide a simple dashboard for accessing the system.

---

## 6. Product Scope

### 6.1 In Scope

* User login
* Technician dashboard
* Equipment/problem query submission
* AI-powered troubleshooting
* RAG-based document retrieval
* Equipment manuals and maintenance documents
* Source references
* Safety instructions
* Query history
* Document upload and management
* Basic system settings
* Feedback on AI responses

### 6.2 Out of Scope for the Initial Version

* Real-time IoT/sensor integration
* Predictive maintenance
* Automatic machine control
* PLC/SCADA integration
* Automatic repair execution
* Spare-parts ordering
* Advanced enterprise analytics
* LLM fine-tuning
* Voice-based interaction

> These may be considered as future enhancements.

---

## 7. Core User Flow

```text
Login
  ↓
Dashboard
  ↓
New Query
  ↓
Enter Equipment + Problem/Error Code
  ↓
MAINT-AI retrieves relevant documentation
  ↓
LLM generates troubleshooting response
  ↓
Troubleshooting Result
  ↓
View Sources / Safety Information
  ↓
Technician verifies and acts according to approved procedures
```

---

## 8. Functional Requirements

### 8.1 Login

The system shall allow authorized users to:

* Log in using their credentials.
* Access the MAINT-AI dashboard after successful login.
* Log out of the system.

### 8.2 Dashboard

The dashboard shall provide:

* Quick access to create a new troubleshooting query.
* Recent troubleshooting queries.
* Basic query statistics.
* Number of available knowledge-base documents.
* Recent activity.

> The dashboard will focus on quick access to troubleshooting rather than advanced analytics.

### 8.3 New Query

Technicians shall be able to:

* Select or enter equipment information.
* Enter an equipment ID.
* Enter an error code if available.
* Describe the machine problem or symptoms.
* Provide additional information when required.
* Submit the query to MAINT-AI.

**Example:**

```text
Equipment: M-204

Problem:
Motor is overheating after approximately 30 minutes of operation.
```

### 8.4 AI Troubleshooting

After receiving a query, MAINT-AI shall:

* Understand the technician's problem.
* Use the provided equipment context.
* Retrieve relevant information from the knowledge base.
* Provide the retrieved information as context to the LLM.
* Generate possible causes.
* Provide recommended troubleshooting steps.
* Display relevant safety instructions.
* Provide supporting source references.

> The system should clearly indicate when sufficient information cannot be found.

**Example response structure:**

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

Follow the applicable equipment safety and lockout/tagout procedure before inspection.

Sources:

Motor Maintenance Manual — Section 4.2 — Page 18
```

---

## 9. RAG Requirements

MAINT-AI will use **Retrieval-Augmented Generation (RAG)** to provide the LLM with relevant maintenance information.

### 9.1 Document Processing

The system shall:

* Accept maintenance documents.
* Extract text from documents.
* Split documents into smaller chunks.
* Generate embeddings for document chunks.
* Store the embeddings and document information in the database.

### 9.2 Retrieval

When a technician submits a query:

```text
Technician Query
      ↓
Query Embedding
      ↓
Vector Similarity Search
      ↓
Relevant Document Chunks
      ↓
LLM Context
```

Relevant equipment/document metadata may be used to improve retrieval.

### 9.3 Generation

The LLM shall generate a response using:

* Technician query
* Equipment information
* Retrieved documentation
* Relevant maintenance context

The generated response should contain:

* Possible causes
* Troubleshooting steps
* Safety information where applicable
* Source references

---

## 10. Document Management

Authorized users shall be able to:

* Upload maintenance documents.
* View available documents.
* View document details.
* Categorize documents.
* Associate documents with equipment.
* Replace or remove outdated documents where required.
* View document processing/indexing status.

> Supported documents for the initial version will primarily be PDF-based technical documentation.

---

## 11. Source References

MAINT-AI shall provide the source of information used in the generated response.

Source information may include:

* Document name
* Document type
* Section
* Page number
* Equipment association

> Users should be able to open the relevant source document from the troubleshooting result. This allows technicians to verify the information before taking action.

---

## 12. Safety Requirements

MAINT-AI shall:

* Display relevant safety instructions when available.
* Use approved safety documentation as part of the knowledge base.
* Provide safety information alongside troubleshooting guidance.
* Clearly communicate when supporting safety information is unavailable.
* Avoid presenting unsupported maintenance procedures as verified instructions.

> MAINT-AI will not make autonomous safety decisions or directly control equipment.

---

## 13. Query History

The system shall maintain a history of previous troubleshooting queries.

Users shall be able to view:

* Previous query
* Equipment
* Date/time
* Response
* Status

> Users should be able to reopen a previous troubleshooting result and view its associated sources.

---

## 14. Feedback

Users shall be able to provide simple feedback on AI responses.

The initial version will support:

* Helpful / Not Helpful
* Optional feedback comment

> Feedback will be used to evaluate the usefulness of MAINT-AI responses.

---

## 15. System Settings

The initial settings screen will provide basic configuration options such as:

* User/account information
* System preferences
* Knowledge-base configuration
* AI configuration information

> Sensitive API credentials must not be exposed in the frontend. Advanced administrative configuration is outside the initial implementation scope.

---

## 16. AI Safety and Reliability

> **MAINT-AI should not be treated as an unrestricted chatbot.**

### Grounded Responses

AI responses should be based on retrieved maintenance documentation whenever relevant information is available.

### Source References

Responses should provide supporting document references.

### Insufficient Evidence

If relevant information cannot be found, the system should clearly state that sufficient verified information is unavailable rather than confidently inventing a procedure.

### Human Decision Making

The technician or authorized maintenance personnel remain responsible for the final operational decision.

---

## 17. LLM Requirements

The LLM should receive relevant context along with the technician's problem.

Relevant context may include:

* Equipment ID
* Equipment model
* Error code
* Symptoms
* Operating conditions
* Maintenance history
* Retrieved maintenance documentation

The LLM should:

* Understand the reported problem.
* Identify possible causes.
* Generate useful troubleshooting steps.
* Use the retrieved context.
* Communicate uncertainty when evidence is insufficient.
* Provide clear and actionable responses.

> The exact OpenAI model will be finalized based on evaluation of response quality, context understanding, latency, cost, and suitability for the project.

---

## 18. Technology Stack

### AI / RAG

| Component           | Technology               |
| ------------------- | ------------------------ |
| LLM                 | OpenAI API               |
| Embeddings          | BAAI BGE-M3              |
| RAG Framework       | LangChain                |
| Vector Search       | pgvector                 |
| Document Processing | PyMuPDF                  |
| Text Chunking       | LangChain Text Splitters |

### Application

| Component            | Technology |
| -------------------- | ---------- |
| Programming Language | Python     |
| Frontend             | Streamlit  |

### Data

| Component           | Technology |
| ------------------- | ---------- |
| Database            | PostgreSQL |
| Database Management | pgAdmin    |

### Development

| Component       | Technology             |
| --------------- | ---------------------- |
| Version Control | Git + GitHub           |
| Environment     | Python `venv` + `.env` |

---

## 19. System Architecture

### Document Ingestion Pipeline

```text
Approved Maintenance Documents
          ↓
       PyMuPDF
          ↓
    Text Extraction
          ↓
     Text Chunking
          ↓
        BGE-M3
          ↓
PostgreSQL + pgvector
```

### Query and Generation Pipeline

```text
Technician Query
       ↓
     BGE-M3
       ↓
Similarity Search
       ↓
Relevant Document Chunks
       ↓
    LangChain
       ↓
   OpenAI API
       ↓
Troubleshooting Response
       ↓
Sources + Safety Information
```

---

## 20. Mock UX

The initial MAINT-AI interface will contain the following screens:

* Login
* Dashboard
* New Query
* Troubleshooting Results
* Source References
* Document Viewer
* Query History
* Document Management
* System Settings

### Primary User Flow

```text
Login
  ↓
Dashboard
  ↓
New Query
  ↓
Troubleshooting Results
  ↓
Sources / Document Viewer
```

---

## 21. Success Metrics

The initial project will evaluate MAINT-AI using simulated maintenance scenarios.

### Proposed Targets

| Metric                                      | Target |
| ------------------------------------------- | -----: |
| Reduction in manual document search time    |  ≥ 40% |
| Reduction in simulated troubleshooting time |  ≥ 30% |
| Source-referenced responses                 |  ≥ 95% |
| Positive user feedback                      |  ≥ 80% |

Technical evaluation will also consider:

* Retrieval relevance
* Response relevance
* Source-reference correctness
* Response faithfulness
* Response latency

> Real-world machine downtime reduction cannot be directly validated within the college simulation and would require deployment in an actual manufacturing environment.

---

## 22. Research Basis

The architecture of MAINT-AI is based on research in dense retrieval, embeddings, Retrieval-Augmented Generation, and LLM-based industrial fault diagnosis.

### RAG Research

* Dense semantic retrieval
* Query and document embeddings
* Top-K retrieval
* Retrieval-Augmented Generation
* External knowledge bases
* Grounded generation
* Source attribution
* Retrieval quality
* Dense vs keyword retrieval

### LLM Research

* LLMs for industrial machine fault diagnosis
* Structured fault diagnosis
* Importance of equipment context
* LLM model selection
* Accuracy and evaluation
* Generalization
* Adaptability
* Latency and cost

The combined research supports the following principle:

> **Retrieve relevant evidence first, then use the LLM to interpret the evidence and generate a structured troubleshooting response.**

---

## 23. Future Enhancements

Future versions may include:

* Hybrid semantic + keyword retrieval
* Retrieval reranking
* Advanced RAG evaluation
* LLM fine-tuning
* Real-time sensor integration
* Predictive maintenance
* Voice-based interaction
* Multilingual support
* Integration with existing enterprise maintenance systems
* Advanced maintenance analytics

---

## 24. Conclusion

**MAINT-AI** is an AI-powered maintenance decision-support system designed to help manufacturing technicians troubleshoot equipment failures faster.

The system combines maintenance documentation, semantic retrieval, RAG, and an LLM to provide source-grounded troubleshooting guidance.

Instead of relying only on the LLM's general knowledge, MAINT-AI retrieves relevant organizational documentation and provides it as context for generating the response.

### Core Workflow

```text
RETRIEVE → UNDERSTAND → RECOMMEND → VERIFY
```

MAINT-AI assists technicians by providing relevant information, troubleshooting guidance, safety instructions, and source references while keeping the final operational decision with authorized maintenance personnel.
