import openai
import gradio
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('SECRET_KEY')
model = os.environ.get('MODEL')
server_port = int(os.environ.get('GRADIO_SERVER_PORT'))
content = os.environ.get('CONTENT')

openai.api_key = api_key

messages = [{"role": "system", "content": content}]


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Software Development")

demo.launch(share=True, server_port=server_port)
