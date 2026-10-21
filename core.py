from transformers import pipeline
from langchain_core.prompts import ChatPromptTemplate

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

chatbot = pipeline(
    "text-generation",
    model=MODEL_NAME,
)

movie_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "Analyze movie descriptions accurately and concisely. "
                "Use only details stated or clearly supported by the "
                "paragraph. Do not add outside facts. Write 'Not stated' "
                "when information is missing. Label interpretations as "
                "inferences."
            ),
        ),
        (
            "human",
            """Analyze this movie paragraph.

Use these headings:
Title:
Release year:
Director:
Main cast:
Genre:
Setting and premise:
Key themes:
Tone and style:
Notable strengths:
Reception details:
Quick summary:
Key insights:

Paragraph:
{paragraph}""",
        ),
    ]
)