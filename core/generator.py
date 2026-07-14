"""
generator.py

Uses Gemini to generate answers from retrieved context.
"""
import time

from google import genai

from core.config import GEMINI_API_KEY, GENERATION_MODEL
from core.logger import logger


class Generator:

    def __init__(self):

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, query: str, retrieved_chunks: list):

        if not retrieved_chunks:
            return "I couldn't find any relevant information in the uploaded documents."

        context = ""

        for chunk in retrieved_chunks:

            context += f"""
    Document: {chunk['source']}
    Page: {chunk['page']}

    {chunk['text']}

    ==================================================
    """

        prompt = f"""
    You are an intelligent document assistant.

    Use ONLY the provided context.

    Rules:

    1. Answer only from the documents.
    2. If information is missing, say:
    "I couldn't find this information in the uploaded documents."
    3. Do not make up facts.
    4. If multiple documents contain relevant information, combine them.

    Context:

    {context}

    User Question:

    {query}

    Answer:
    """

        logger.info("Generating response using Gemini...")

        for attempt in range(3):

            try:

                response = self.client.models.generate_content(
                    model=GENERATION_MODEL,
                    contents=prompt,
                )

                return response.text

            except Exception as e:

                logger.warning(
                    f"Gemini attempt {attempt + 1} failed: {e}"
                )

                if attempt < 2:
                    time.sleep(2)
                else:
                    raise