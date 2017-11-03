#!/usr/bin/env python
import requests
import json
import time
import unicodedata


query_url = 'https://api.github.com/search/repositories?q={}&sort=stars&order=desc'


def get_repo_data(name):
    r = requests.get(query_url.format(name))
    try:
        data = r.json()['items'][0]
        return data
    except Exception:
        print('COULD NOT GET REPO DATA')
        return {'stargazers_count': 0, 'url': '', 'description': ''}


def format_data(data):
    return {
        'stars': data['stargazers_count'],
        'url': data['url'].encode('ascii', 'replace').decode("utf-8") if data['url'] else '',
        'description': data['description'].encode('ascii', 'replace').decode("utf-8") if data['description'] else ''
    }


if __name__ == '__main__':
    with open('base_elements.json') as f:
        elements = json.load(f)


    for e in elements[17:]:
        with open('github_element_data.json', 'r+') as d:
            output_data = json.load(d)
            
            data = get_repo_data(e['name'])
            formatted_data = format_data(data)
            merged_data = {**e, **formatted_data}
            output_data.append(merged_data)
            print('Got data: ' + str(merged_data) + '\n')
            time.sleep(7)

            d.seek(0)
            json.dump(output_data, d, ensure_ascii=False)
            d.truncate()