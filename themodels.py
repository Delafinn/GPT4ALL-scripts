from gpt4all import GPT4All

# uncomment for use as a function and indent code below.
# def model_lister():

models = GPT4All.list_models()
filenames = [model['filename'] for model in models]

for filename in filenames:
    print(filename)
