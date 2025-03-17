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
			"content": '人物一覧を次のJSON形式で出力してください。\n{"people": ["aaa", "bbb]}'
		},
		{
			"role": "user",
			"content": "昔々あるところにお祖父さんとお婆さんがいました。"
		},
	],
	response_format={"type":"json_object"}
)

print(response.choices[0].message.content)