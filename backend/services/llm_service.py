import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_troubleshooting_answer(query, context):

    prompt = f"""
You are MaintAI, an AI assistant for industrial maintenance technicians.

Answer the technician's question using ONLY the maintenance information
provided in the context below.

If the answer is not available in the context, clearly say:
"I could not find enough information in the maintenance documents."

Do not invent technical specifications, procedures, causes, or safety instructions.

Technician Question:
{query}

Maintenance Document Context:
{context}

Give the response in this structure:

Possible Cause:
- Explain the most likely cause based on the documents.

Recommended Actions:
1. Action one
2. Action two
3. Action three

Safety Warning:
- Mention any relevant safety precaution from the documents.

Confidence:
- High / Medium / Low

Keep the answer clear and practical for a maintenance technician.
"""

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt
    )

    return response.text