#!/usr/bin/env python
"""
A hackathon-quality script to look up github projects by name and record some metadata about them.
There's a lot wrong with this script in terms of maintainability and quality but it works.
"""
import requests
import json
import time
import unicodedata


query_url = 'https://api.github.com/search/repositories?q={}&sort=stars&order=desc'
empty = {'stargazers_count': 0, 'url': '', 'description': ''}


def get_repo_data(name):
    r = requests.get(query_url.format(name))
    try:
        items = r.json()['items']
        for i in items:
            if i['name'].lower() == name.lower():
                return i
        return empty
    except Exception:
        print('COULD NOT GET REPO DATA')
        return empty


def format_data(data):
    return {
        'stars': data['stargazers_count'],
        'url': data['url'].encode('ascii', 'replace').decode("utf-8") if data['url'] else '',
        'description': data['description'].encode('ascii', 'replace').decode("utf-8") if data['description'] else ''
    }


if __name__ == '__main__':
    with open('base_elements.json') as f:
        elements = json.load(f)

    for e in elements[23:]:
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
