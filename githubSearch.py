import argparse

import github
import yaml

def search_github(keyword):
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining. Reset time: {rate.reset}')
 
    # FIXME -- despite limiting on language, this still seems to find Java files
    query = f'{keyword}+in:file+language:cpp'
    result = g.search_code(query, order='desc')

    max_size = 100
    print(f'Found {result.totalCount} file(s)')
    if result.totalCount > max_size:
        result = result[:max_size]

    output = []

    for file in result:
        output.append(file.html_url + "\n")

    return output

def load_config(filename='config.yaml'):
    with open(filename) as f:
        return yaml.safe_load(f)
 
if __name__ == '__main__':
    config = load_config()

    token = config.get('GITHUB_ACCESS_TOKEN')
    if not token:
        print("Enter the authentication token")
        token = input()

    # TODO: allow searching only a subset of keywords (those for just one
    # keyword), or specified keywords; use argparse to handle this
    keywords = list(set(sum(config['keywords'].values(), [])))

    print('keywords', keywords)

    g = github.Github(token)

    # TODO: don't overwrite previous results; write to a new file
    with open('myfile.txt', 'w') as output:
        for keyword in keywords:
            output.write(keyword+"\n")
            output.writelines(search_github(keyword))
            output.write("\n")
            # stop after one search for testing
            break
 
