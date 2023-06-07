import datetime
import os
from collections import defaultdict
import pandas
from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_wines(wines_from_excel):
    wines_list = defaultdict(list)
    for item in wines_from_excel:
        category = item['Категория']
        wines_list[category].append(item)
    wines = dict(wines_list)
    return wines


def get_delta():
    start_year = 1920
    now = datetime.datetime.now()
    numeric = now.year - start_year
    return numeric


def get_correct_year(numeric):
    numeric = str(numeric)[-2:]
    if numeric in ('11', '12', '13', '14', '111', '913'):
        return 'лет'
    elif numeric[-1] == '1':
        return 'год'
    elif numeric[-1] in ('2', '3', '4'):
        return 'года'
    else:
        return 'лет'


def main():
    load_dotenv()
    path_to_file = os.getenv('FILE')
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    wines_from_excel = pandas.read_excel(path_to_file, keep_default_na=False).to_dict(orient='records')

    rendered_page = template.render(
        wines=get_wines(wines_from_excel),
        years=get_delta(),
        correct_year=get_correct_year(get_delta()),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
