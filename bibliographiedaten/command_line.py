import gzip
import sys
import fire
import utils 
import record
import json
import csv
from pymarc.marcxml import XmlHandler, parse_xml
from marcxml import RecordProcessor


def hello(name):
    print(f"Hello {name}!")

def marcxml2jsonl(source, target):
    """
    Converts MARCXML to JSONL.

    See also:

    * https://www.loc.gov/marc/bibliographic/
    * https://www.loc.gov/standards/marcxml/
    * http://jsonlines.org/

    Args:
        source (str): Input file in MARCXML format (compressed GZ).
        target (str): Output file in JSONL format (compressed GZ).
    """
    with gzip.open(target, 'wt', encoding='utf8') as fout:
        processor = RecordProcessor(fout)
        handler = XmlHandler()
        handler.process_record = processor.process_record
        with gzip.open(source, 'rb') as fh:
            try:
                parse_xml(fh, handler)
            except Exception as err:
                print(err, file=sys.stderr)


def record_match(source1, source2, target):
    """
    Returns matches of TXT containing records and JSONL judging by ids held in source1.
    Output as TXT.

    Args:
        source1 (str): 1st input file in TXT format.
        source2 (str): 2nd input file in JSONL format (compressed GZ).
        target (str): Output file in TXT format.
    """

    with open(source1, "r+") as fin1:
        with gzip.open(source2, 'r') as fin2:
            with open(target, "wb") as fout:
                utils.record_match(fin1, fin2, fout)

def matches2csv(source, target):
    """
    Takes matched json records. 
    Output as CSV.

    Args:
        source (str): 1st input file in TXT format.
        target (str): Output file in CSV format.
    """

    with open(source, 'rb') as fin:
        with open(target, 'w', encoding='utf-8', newline='') as fout:
            field_names = ['bvnumber', 'title', 'title_remainder', 'place', 'date', 'title_types', 'relationship', 'person1_name', 'person1_gnd_id', 'person1_function', 'person2_name', 'person2_gnd_id', 'person2_function']
            writer = csv.DictWriter(fout, fieldnames=field_names)
            writer.writeheader()
            i = 0
            for line in fin:
                metadata = json.loads(line.strip())
                rec = record.Record(metadata)

# Execute the code below if you want just texts, not recordings etc.
                if rec.valid:
                    rows = rec.as_rows()
                    for row in rows:
                        writer.writerow(row)

def merge_all(path, target):
    """
    Takes all 33 parts of the B3Kat which were filtered and converted to csv files.

    Args:
        path (str): Path to folder with the CSV files.
        target (str): Output file in CSV format.
    """

    files = []
    for i in range(33):
        if i < 9:
            file = path + "/result_on_b3kat_export_2021_11_teil0" + str(i+1) + ".xml.csv"
        else:
            file = path + "/result_on_b3kat_export_2021_11_teil" + str(i+1) + ".xml.csv"
        files.append(file)

    with open(target, 'w', newline='', encoding='utf8') as all_parts_file:
        header = ["bvnumber","title","title_remainder","place","date","title_types","relationship","person1_name","person1_gnd_id","person1_function","person2_name","person2_gnd_id","person2_function"]
        writer = csv.writer(all_parts_file)
        writer.writerow(header)

        for file in files:
            print("Processing ", file)
            print("---------------------------------------------------------------------------------------------------------------------------------------")

            with open(file, 'r', encoding='utf8') as data_file:
                reader = csv.reader(data_file)
                next(data_file)
                for row in reader:
                    writer.writerow(row)
                data_file.close()
    all_parts_file.close()

def main(): 
    fire.Fire({
        'hello': hello,
        'convert1': marcxml2jsonl,
        'match': record_match,
        'convert2': matches2csv,
        'merge': merge_all,
    })

if __name__ == "__main__":
    main()


