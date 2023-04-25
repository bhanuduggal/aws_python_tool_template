import json

with open('Pipfile.lock') as f:
    data = json.load(f)

deps = data.get('default', {})

with open('requirements.txt', 'w') as r:
    r.write('\n'.join(f'{k}{v["version"]}' for k, v in deps.items()))
