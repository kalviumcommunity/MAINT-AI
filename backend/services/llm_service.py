import os

from dotenv import load_dotenv
from openai import OpenAI


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in .env")


client = OpenAI(
    api_key=OPENAI_API_KEY
)

MODEL_NAME = "gpt-5.6-luna"


# --------------------------------------------------
# GENERATE AI RESPONSE
# --------------------------------------------------

def generate_answer(query_text, context):
    """
    Generate a maintenance troubleshooting answer
    using retrieved RAG context.
    """

    if not query_text:
        return {
            "success": False,
            "message": "query_text is required"
        }

    if not context:
        context = (
            "No relevant maintenance documentation "
            "was found."
        )

    instructions = """
You are MAINT-AI, an industrial maintenance
troubleshooting assistant.

Your job is to help technicians diagnose and
resolve equipment problems.

Rules:

1. Use the provided maintenance documentation
   as the primary source.

2. Do not invent technical specifications,
   procedures, error codes, or measurements.

3. If the documentation does not contain enough
   information, clearly state that.

4. Give practical troubleshooting steps.

5. Mention relevant safety precautions.

6. Keep the answer clear and useful for a
   maintenance technician.

7. If multiple possible causes exist, list them
   in a logical order.
"""

    prompt = f"""
Technician question:

{query_text}


Relevant maintenance documentation:

{context}


Based only on the maintenance documentation above,
provide a practical troubleshooting answer.
"""

    try:

        response = client.responses.create(
            model=MODEL_NAME,
            instructions=instructions,
            input=prompt
        )

        answer = response.output_text

        return {
            "success": True,
            "answer": answer
        }

    except Exception as e:

        return {
            "success": False,
            "message": "Failed to generate AI response",
            "error": str(e)
        }