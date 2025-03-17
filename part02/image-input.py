import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")

image_url = "https://raw.githubusercontent.com/yoshidashingo/langchain-book/main/assets/cover.jpg"

client = OpenAI(api_key=os.environ["OPEN_API_KEY"])

response = client.chat.completions.create(
	model="gpt-4o-mini",
	messages= [
		{
			"role": "user",
			"content":[
				{
				"type":"text",
				"text":"画像を説明してください。"
				},
				{
					"type": "image_url",
					"image_url": {"url": image_url}
				},
			]
		},
	],
)

print(response.choices[0].message.content)