from gpt4all import GPT4All


# def model_lister():

models = GPT4All.list_models()
filenames = [model['filename'] for model in models]

descriptions = [model['description'] for model in models]


for counter, (filename, description) in enumerate(zip(filenames, descriptions), 1):
    print(f"{counter}. {filename} - {description}")

#  Output below

#1. ggml-gpt4all-j-v1.3-groovy.bin - GPT-J 6B finetuned by Nomic AI on the latest GPT4All dataset.<br>- Licensed for commercial use.<br>- Fast responses.
# 2. GPT4All-13B-snoozy.ggmlv3.q4_0.bin - LLaMA 13B finetuned by Nomic AI on the latest GPT4All dataset.<br>- Cannot be used commercially.<br>- Slower responses but higher quality.
# 3. ggml-mpt-7b-chat.bin - MPT 7B chat model trained by Mosaic ML.<br>- Cannot be used commercially.<br>- Fast responses.
# 4. nous-hermes-13b.ggmlv3.q4_0.bin - LLaMa 13B finetuned on over 300,000 curated and uncensored instructions.<br>- Cannot be used commercially.<br>- Best finetuned LLaMA model.<br>- This model was fine-tuned by Nous Research, with Teknium and Karan4D leading the fine tuning process and dataset curation, Redmond AI sponsoring the compute, and several other contributors. The result is an enhanced Llama 13b model that rivals GPT-3.5-turbo in performance across a variety of tasks. This model stands out for its long responses, low hallucination rate, and absence of OpenAI censorship mechanisms.
# 5. ggml-vicuna-7b-1.1-q4_2.bin - LLaMA 7B finetuned by teams from UC Berkeley, CMU, Stanford, MBZUAI, and UC San Diego.<br>- Cannot be used commercially.
# 6. ggml-vicuna-13b-1.1-q4_2.bin - LLaMA 13B trained by teams from UC Berkeley, CMU, Stanford, MBZUAI, and UC San Diego.<br>- Cannot be used commercially.
# 7. ggml-wizardLM-7B.q4_2.bin - LLaMA 7B finetuned by Microsoft and Peking University.<br>- Cannot be used commercially.
# 8. ggml-stable-vicuna-13B.q4_2.bin - LLaMa 13B finetuned with RLHF by Stability AI.<br>- Cannot be used commercially.
# 9. ggml-mpt-7b-base.bin - MPT 7B pre-trained by Mosaic ML. Trained for text completion with no assistant finetuning.<br>- Licensed for commercial use.
# 10. ggml-nous-gpt4-vicuna-13b.bin - LLaMa 13B fine-tuned on ~180,000 instructions by Nous Research.<br>- Cannot be used commercially.
# 11. ggml-mpt-7b-instruct.bin - MPT 7B instruction finetuned by Mosaic ML.<br>- Licensed for commercial use.
# 12. wizardLM-13B-Uncensored.ggmlv3.q4_0.bin - LLaMa 13B finetuned on the uncensored assistant and instruction data.<br>- Cannot be used commercially.
# 13. ggml-replit-code-v1-3b.bin - Replit 3B code model trained on subset of the Stack.<br>- Licensed for commercial use.
