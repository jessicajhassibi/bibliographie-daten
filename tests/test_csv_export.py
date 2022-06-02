import gzip
import csv

from bibliographiedaten.utils import matched
from bibliographiedaten.record import Record

with gzip.open('input.jsonl.gz', 'rt', encoding='utf8') as jsonfile, open('gnd_ids.txt', encoding='utf8') as gndfile:
    with open('test.csv', 'w', encoding='utf8') as csvfile:
        fieldnames = [
            'bvnumber',
            'title',
            'place',
            'date',
            'title_type',
            'relationship',
            'source',
            'target'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        gnd_ids = set()                   # set of gnd ids in mastertabelle
        for id in id_as_txt:
            gnd_ids.add(id[:-1])

        for line in jsonfile:
            record = json.loads(line)
            matches = matched(record, gnd_ids)
            if matches:
                for row in record.as_rows():
                    pass
                    # records_result.write(line)
