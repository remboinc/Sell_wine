import datetime
import os
from collections import defaultdict
import pandas
from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def group_wines_by_category(wines_from_excel):
    wines_by_category = defaultdict(list)
    for card in wines_from_excel:
        category = card['Категория']
        wines_by_category[category].append(card)
    wines = dict(wines_by_category)
    return wines


def calculate_year_delta():
    start_year = 1920
    now = datetime.datetime.now()
    year_delta = now.year - start_year
    return year_delta


def get_correct_year(year_delta):
    year_delta = str(year_delta)[-2:]
    if year_delta in ('11', '12', '13', '14', '111', '913'):
        return 'лет'
    elif year_delta[-1] == '1':
        return 'год'
    elif year_delta[-1] in ('2', '3', '4'):
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
        wines=group_wines_by_category(wines_from_excel),
        years=calculate_year_delta(),
        correct_year=get_correct_year(calculate_year_delta()),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
