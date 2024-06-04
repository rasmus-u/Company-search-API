import requests as re
import pandas as pd

API_KEY = ''
SEARCH_ENGINE_ID = ''
FILE_NAME = 'companies.xlsx'
RESULTS_TO_RETURN = 3

params = {
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID
}
url = 'https://www.googleapis.com/customsearch/v1'

df = pd.read_excel(FILE_NAME)

def add_search_results(row):
    search_q = str(row['Companies']) + ' company'
    params['q'] = search_q

    r = re.get(url=url, params=params)

    if r.ok:
        search_results = r.json()['items']
        links = [item['link'] for item in search_results[:RESULTS_TO_RETURN]]
        return links
    else:
        return [None] * RESULTS_TO_RETURN

result_columns = list(map(lambda x: 'Result{}'.format(x), range(1, RESULTS_TO_RETURN + 1)))

df[result_columns] = df.apply(lambda row: add_search_results(row), axis=1, result_type='expand')

df.to_excel('results.xlsx')
