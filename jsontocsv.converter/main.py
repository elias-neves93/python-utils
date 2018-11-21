import json

with open('colors.json', 'r') as infile, open('data.csv', 'w') as outfile:

    json_dict = json.loads(infile.read())

    for headers in json_dict.keys():
        line = '{}, '.format(headers)
        outfile.write(line)

    outfile.write('\n')

    for values in json_dict.values():
        line = '{}, '.format(values)
        outfile.write(line)
