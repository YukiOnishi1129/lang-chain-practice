import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=os.environ["OPEN_API_KEY"])

response = client.chat.completions.create(
	model="gpt-4o-mini",
	messages= [
		{
			"role": "system",
			"content": "You are a helpful assistant."
		},
		{
			"role": "user",
			"content": "こんにちは！私はジョンと言います。"
		}
	]
)

print(response.to_json(indent=2))