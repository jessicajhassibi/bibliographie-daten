import json
import record

def is_gnd_url(url):
    """Checks if url is a gnd-url."""

    return 'd-nb.info/gnd' in url

def tip(url):
    return url.split("/")[-1]

def pairs(sequence):
    """
    Combines all elements of a list with each other as tuples. 

    Args: 
        sequence (list): List of Strings

    Returns:
        list: List of Tuples (combined elements)
    """
    result = []

    length = len(sequence)
    for i in range(length):
        for j in range(i+1, length):
            result.append((sequence[i], sequence[j]))

    return result


def matched(record, gnd_ids):
    """
    Returns True if at least 2 persons mentioned in the record are in our mastertable, else False.

    Args:
        record (Record): Record object.
        gnd_ids (list): List of ids.

    Returns:
        bool
    """

    persons_gnd = record.person_ids()
    count = 0
    for person_id in persons_gnd:
    # if at least 2 persons are in our mastertable -> valid record
        if person_id in gnd_ids:
            count += 1
    if count >=2:
        return True
    else:
        return False

def record_match(id_as_txt, records_as_gz, records_result):
    """
    Matches records according to person ids and writes matched records to txt file.

    Args:
        id_as_txt (TextIOWrapper): Opened TXT file containing ids.
        records_as_gz (GZipFile): Opened GZ file containing records. 
        records_result (BufferedWriter): Opened TXT file for records output.
    """ 

    gnd_ids = set()                   
    for id in id_as_txt:
        id = id.replace("\n", "")
        gnd_ids.add(id)

    lines = records_as_gz.readlines()
    for line in lines:
        rec = json.loads(line)
        rec = record.Record(rec)
        matches = matched(rec, gnd_ids)
        if matches:
            records_result.write(line)
    return (records_result)
