import gzip
import shutil
with open('data/test/karl_nef_example.xml', 'rb') as f_in:
    with gzip.open('data/test/karl_nef_example.xml.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)