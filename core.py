from typing import List, Optional

from pydantic import BaseModel
from transformers import pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser


model = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
)


class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Extract movie information using only facts stated in the paragraph. "
        "Do not guess. Use null for missing optional values and empty lists "
        "when no list items are stated.\n{format_instructions}",
    ),
    ("human", "{paragraph}"),
])

paragraph = input("Give your paragraph: ")

final_prompt = prompt.invoke({
    "paragraph": paragraph,
    "format_instructions": parser.get_format_instructions(),
})

messages = [
    {
        "role": {"system": "system", "human": "user"}.get(message.type, "assistant"),
        "content": str(message.content),
    }
    for message in final_prompt.to_messages()
]

result = model(messages, do_sample=False)
generated = result[0]["generated_text"]
response_text = generated[-1]["content"] if isinstance(generated, list) else generated

movie_data = parser.parse(response_text)
print(movie_data)