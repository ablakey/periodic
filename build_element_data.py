#!/usr/bin/env python
"""
A hackathon-quality script to look up github projects by name and record some metadata about them.
There's a lot wrong with this script in terms of maintainability and quality but it works.
"""
import requests
import json
import time


if __name__ == '__main__':
    # Get list of base elements and some constant properties about them (like their position on the table)
    with open('base_elements.json') as f:
        elements = json.load(f)

    formatted_results = []

    print('Requesting metadata for: ', end='', flush=True)
    for element in elements:
        print(element['name'], end=', ', flush=True)

        result = {'stargazers_count': 0, 'url': '', 'description': ''}  # Default data if there is no result.

        r = requests.get('https://api.github.com/search/repositories?q={}&sort=stars&order=desc'.format(element['name']))

        # Get the top-most result that has the element name. (They're returned from Github stored by star count).
        for page_metadata in r.json()['items']:
            if page_metadata['name'].lower() == element['name'].lower():
                result = page_metadata
                break

        # Format data, including only a few fields from what Github returned us.
        formatted_result = {
            **element,
            **{k: v for k, v in result.items() if k in ('stargazers_count', 'url', 'description')}
        }

        formatted_results.append(formatted_result)
        time.sleep(6)  # Don't request too fast or we'll get throttled.

    # JSONify the output data, then prepend a global variable name (because we use data.js as a JS object)
    output = 'tableData = ' + json.dumps(formatted_results, ensure_ascii=False, indent=4)

    with open('data.js', 'w') as f:
        f.write(output)
