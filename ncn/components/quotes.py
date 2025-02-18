import json
import random

path_to_json = r"../database/quotes.json"


def get_json_data(path_):
    with open(path_, 'r') as json_object:
        json_data = json.load(json_object)
    return json_data


def add_quote_to_json(quote: str, author: str, path=path_to_json):
    data = get_json_data(path)
    data.append([quote, author])
    json_data = json.dumps(data)
    with open(path, "w") as quotes:
        quotes.write(json_data)
    print('complete')


def random_quote(path=path_to_json):
    try:
        quotes = get_json_data(path)
        return random.choice(quotes)

    except FileNotFoundError as fnfe:
        print(fnfe)
        return


if __name__ == '__main__':
    path_to_json = "../database/quotes.json"

    # for i in q:
    #     add_quote_to_json(quote=i[0], author=i[1], path=path_to_json)

    print(random_quote(path=path_to_json))
