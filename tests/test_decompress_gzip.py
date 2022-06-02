import gzip
import shutil

def decompress_gzip(source, target):
    with open(source, 'rb') as f_in:
        with gzip.open(target, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

decompress_gzip("../data/test/01_jsonl.jsonl.gz", "../data/test/01_jsonl.jsonl")

