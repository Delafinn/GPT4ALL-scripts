
from gpt4all import GPT4All
import pyttsx3


while True:

    userprompt = input('Enter your prompt here: ')

    gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy")
    messages = [{"role": "assistant", "content": f"{userprompt}"}]
    results= gptj.chat_completion(messages)


    content = results['choices'][0]['message']['content']

    engine = pyttsx3.init()
    engine.say(content)
    engine.runAndWait()
