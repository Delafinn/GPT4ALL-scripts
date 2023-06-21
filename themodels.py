from gpt4all import GPT4All


# def model_lister():

models = GPT4All.list_models()
filenames = [model['filename'] for model in models]

descriptions = [model['description'] for model in models]


for counter, (filename, description) in enumerate(zip(filenames, descriptions), 1):
    print(f"{counter}. {filename} - {description}")
