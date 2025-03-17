import os
import json
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")

def get_current_weather(location, unit="fahrenheit"):
	if "tokyo" in location.lower():
		return json.dumps(
			{
				"location": "Tokyo",
				"temperature": 10,
				"unit": unit
			},
		)
	elif "san francisco" in location.lower():
		return json.dumps(
			{
				"location": "San Francisco",
				"temperature": 72,
				"unit": unit
			},
		)
	elif "paris" in location.lower():
		return json.dumps(
			{
				"location": "Paris",
				"temperature": 22,
				"unit": unit
			},
		)
	else:
		return json.dumps(
			{
				"location": "location",
				"temperature": "unknown",
			},
		)
	

tools = [
	{
		"type": "function",
		"function": {
			"name": "get_current_weather",
			"description": "Get the current weather in a given location",
			"parameters": {
				"type": "object",
				"properties": {
					"location": {
						"type": "string",
						"description": "The city and state, e.g. San Francisco, CA",
					},
					"unit": {
						"type": "string",
						"enum": ["celsius", "fahrenheit"],
					},
				},
				"required": ["location"],
			}
		}
	}
]


client = OpenAI(api_key=os.environ["OPEN_API_KEY"])

messages = [
	{
		"role": "user",
		"content": "東京の天気はどうですか？"
	}
]

response = client.chat.completions.create(
	model="gpt-4o",
	messages=messages,
	tools=tools,
)

print(response.to_json(indent=2))