from gpt4all import GPT4All


def model_lister():

    models = gpt4all.GPT4All.list_models()
    filenames = [model['filename'] for model in models]

    for filename in filenames:
        return(filename)
