import codecs
import json
import csv

districts = codecs.open("./districts.geojson", 'r', 'utf-8-sig')
data = json.load(districts)
districts.close()

source = codecs.open("./data.csv", 'r', 'utf-8-sig')
csvreader = csv.reader(source, delimiter=';', quotechar='"')

features = data.get('features')
data.pop('features')
for feature in features:
    source.seek(0)
    properties = feature.get('properties')
    dist = properties.get('NAME')
    i = -1
    heads = ''
    for row in csvreader:
        i += 1
        if i == 0:
            heads = row
            continue
            
        if row[0] in dist:
            j = 1
            for col in range(1, len(heads)):
                s = row[j].replace('"', '').replace(',', '.')
                properties[heads[j]] = float(s)
                j += 1
            break

data['features'] = features
source.close()

result = codecs.open("./result.geojson", 'w', 'utf-8-sig')
result.write(json.dumps(data, ensure_ascii=False))
result.close()