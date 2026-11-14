import json, pathlib, sys
from jsonschema import Draft202012Validator
root = pathlib.Path(__file__).resolve().parents[1]
path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'public/v1/guides.json'
raw = path.read_bytes()
assert len(raw) <= 1048576, 'File exceeds 1 MiB'
data = json.loads(raw)
Draft202012Validator(json.loads((root / 'schema/guides.schema.json').read_text())).validate(data)
ids = [b['id'] for b in data['brands']]
assert len(set(ids)) == len(ids) and ids.count('other') == 1, 'Duplicate IDs or missing Other'
for brand in data['brands']:
    sections = brand['sections']
    assert len({s['id'] for s in sections}) == len(sections), 'Duplicate section ID'
    for section in sections:
        assert section['steps'] or section['notes'], 'Empty section'
        for text in [section['title'], *section['steps'], *section['notes']]:
            assert all(value.strip() for value in text.values()), 'Blank translation'
if len(sys.argv) > 2:
    previous = json.loads(pathlib.Path(sys.argv[2]).read_text())
    if previous != data:
        assert data['contentVersion'] > previous['contentVersion'], 'Changed content must increment contentVersion'
print(f"PASS: {len(ids)} brands; content version {data['contentVersion']}")
