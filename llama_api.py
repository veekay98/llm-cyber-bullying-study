

from llamaapi import LlamaAPI
import json

# Replace 'Your_API_Token' with your actual API token
llama = LlamaAPI('xxxxxxx')

"""## Run a simple message

This is an example on how to call Llama API
"""

# API Request JSON Cell
api_request_json = {
  "model": "llama3-70b",
  "messages": [
    {"role": "system", "content": "You are a llama assistant that talks like a llama, starting every word with 'll'."},
    {"role": "user", "content": "Hi, happy llama day!"},
  ]
}

# Make your request and handle the response
response = llama.run(api_request_json)
print(json.dumps(response.json(), indent=2))

# print(response)
# print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)

# """## Run Functions
#
# This is an example on how to run Llama Functions without streaming (\*Credits to Harrison Chase 🦜🔗 for this amazing example)
# """
#
# api_request_json = {
#   "messages": [
#     {"role": "user", "content": "Extract the desired information from the following passage.:\n\nHi!"},
#   ],
#   "functions": [
#         {'name': 'information_extraction',
#          'description': 'Extracts the relevant information from the passage.',
#          'parameters': {
#              'type': 'object',
#              'properties': {
#                  'sentiment': {
#                     'title': 'sentiment',
#                     'type': 'string',
#                     'description': 'the sentiment encountered in the passage'
#                     },
#                  'aggressiveness': {
#                     'title': 'aggressiveness',
#                     'type': 'integer',
#                     'description': 'a 0-10 score of how aggressive the passage is'
#                     },
#                  'language': {
#                     'title': 'language',
#                     'type': 'string',
#                     'description': 'the language of the passage'
#                     }
#              },
#              'required': ['sentiment', 'aggressiveness', 'language']
#          }
#       }
#     ],
#   "stream": False,
#   "function_call": {"name": "information_extraction"},
# }
#
# # Make your request and handle the response
# response = llama.run(api_request_json)
# print(json.dumps(response.json(), indent=2))
#
# """## Use OpenAI client
#
# """
#
# !pip install openai -q
#
# from openai import OpenAI
#
# client = OpenAI(
#     # This is the default and can be omitted
#     api_key="<your_api_token>",
#     base_url="https://api.llama-api.com"
# )
#
# functions = [
#         {'name': 'information_extraction',
#          'description': 'Extracts the relevant information from the passage.',
#          'parameters': {
#              'type': 'object',
#              'properties': {
#                  'sentiment': {'title': 'sentiment', 'type': 'string', 'description': 'the sentiment encountered in the passage'},
#                  'aggressiveness': {'title': 'aggressiveness', 'type': 'integer', 'description': 'a 0-10 score of how aggressive the passage is'},
#                  'language': {'title': 'language', 'type': 'string', 'description': 'the language of the passage'},
#              }, 'required': []
#          }
#         }
#     ]
#
#
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the weather like in Boston?",
#         }
#     ],
#     functions = functions,
#     model="llama3-70b",
#     stream=False
# )
#
# print(chat_completion)
#
# """## Streaming
#
# """
#
# from openai import OpenAI
#
# client = OpenAI(
#     # This is the default and can be omitted
#     api_key="<your_api_token>",
#     base_url="https://api.llama-api.com"
# )
#
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "How to use AI functions?",
#         }
#     ],
#     functions = None,
#     model="llama3-70b",
#     stream=True
# )
#
# for chunk in chat_completion:
#     print(chunk.choices[0].delta.content or "", end="")
