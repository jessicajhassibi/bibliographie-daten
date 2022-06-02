import gzip
import json
import os
from unicodedata import normalize

from pymarc.marcxml import XmlHandler, parse_xml


class RecordProcessor:
    UNLIMITED = -1

    def __init__(self, handle, limit=None):
        self.handle = handle
        self.limit = self.UNLIMITED if limit is None else limit
        self.count = 0

    def process_record(self, record):
        self.count += 1
        if self.limit != self.UNLIMITED and self.count > self.limit:
            raise ValueError(f"Exceeded limit of {self.limit}!")

        output = normalize('NFC', f"{record.as_json()}\n")
        self.handle.write(output)
