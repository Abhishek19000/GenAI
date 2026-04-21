from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

model=init_chat_model("groq:openai/gpt-oss-120b")

response=model.invoke("What is the capital of France?")

print(response.content)

