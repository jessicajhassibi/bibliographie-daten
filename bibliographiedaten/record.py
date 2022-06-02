from enum import Enum
import json
import utils


class Field(Enum):
    """List of all fields: https://www.loc.gov/marc/bibliographic/"""

    CONTROL_NUMBER = '001'
    PHYSICAL_DESCRIPTION = '007'
    FIXED_LENGTH_DATA_ELEMENTS = '008'
    PERSONAL_NAME = '100'
    PERSONAL_NAME_ADDED_ENTRY = '700'
    TITLE_STATEMENT = '245'
    PRODUCTION_PUBLICATION_DISTRIBUTION_MANUFACTURE_COPYRIGHT_NOTICE = '264'

class Record:
    """Holds useful methods to retrieve certain record information."""

    def __init__(self, marc):
        self.marc = marc
        self.valid = self.set_valid()

    def __field(self, key):
        if isinstance(key, Field):
            key = key.value

        fields = self.marc.get("fields")
        for field in fields:
            if key in field:
                return field[key]
        return None

    def __person_fields(self, key):
        if isinstance(key, Field):
            key = key.value

        fields = self.marc.get("fields")
        person_fields = []
        for field in fields:
            if key in field:
                person_fields.append(field[key])
        return person_fields
        
    def set_valid(self):
        """Returns True if material of data is text, else False."""

        material = self.material()
        if material == 'not a text':
            return False
        else: 
            return True

    def material(self):
        """Returns information if material of data is text or not."""

        field = self.__field(Field.PHYSICAL_DESCRIPTION)
        try: 
            if 'q' in field[:1]:
                # Notated music
                return 'not a text'
            elif 's' in field[:1]:
                # Sound recording
                return 'not a text'
            elif 'v' in field[:1]:
                # Video recording
                return 'not a text'
            else:
                return 'text'
        except:
            return 'text'

    def person_ids(self):
        """
        Takes all persons mentioned in record and adds their gnd-ids to result set.

        Returns:
            result: Set of ids 
        """
        result = set()
        personal_name = '100'
        personal_name_added_entry = '700'
        person_tags = [personal_name, personal_name_added_entry]
        AUTHORITY_RECORD_CONTROL_NUMBER = "0"

        fields = self.marc.get("fields", [])
        for field in fields:
            for tag in person_tags:
                person_field = field.get(tag, '')
                if person_field:
                    for subfield in person_field["subfields"]:
                        if AUTHORITY_RECORD_CONTROL_NUMBER in subfield:
                            authority_record_number = subfield[AUTHORITY_RECORD_CONTROL_NUMBER]
                            if "(DE-588)" in authority_record_number:
                                record_gnd_id = authority_record_number[8:]
                                result.add(record_gnd_id)

        return result

    def bvnumber(self):
        """Returns bv number of record."""

        field = self.__field(Field.CONTROL_NUMBER)
        return field

    def title(self):
        """Returns Title of record."""

        field = self.__field(Field.TITLE_STATEMENT)
        try:
            return field["subfields"][0]["a"]
        except:
            return field

    def title_remainder(self):
        """Returns Title remainder of record."""

        field = self.__field(Field.TITLE_STATEMENT)
        try:
            remainder = ""
            for subfield in field["subfields"][1]:
                if "a" in subfield:
                    continue
                else:
                    remainder = remainder + str(field["subfields"][1][subfield])
            return remainder
        except:
            return '' #changed

    def date(self):
        """Returns date of record."""

        field = self.__field(Field.PRODUCTION_PUBLICATION_DISTRIBUTION_MANUFACTURE_COPYRIGHT_NOTICE)
        try:
            for subfield in field["subfields"]:
                if "c" in subfield:
                    return subfield["c"]
        except:
            return field

    def place(self):
        """Returns place of record."""

        field = self.__field(Field.PRODUCTION_PUBLICATION_DISTRIBUTION_MANUFACTURE_COPYRIGHT_NOTICE)
        try:
            for subfield in field["subfields"]:
                if "a" in subfield:
                    return subfield["a"]
        except:
            return field

    def title_types(self):
        """Returns list of all title types of record which are of interest for the project."""

        field = self.__field(Field.FIXED_LENGTH_DATA_ELEMENTS)
        title_types = []
        try:
            if 'a' in field[24:28]:
                title_types.append("Abstract")
            elif 'b' in field[24:28]:
                title_types.append("Bibliographie")
            elif 'c' in field[24:28]:
                title_types.append("Katalog")
            elif 'd' in field[24:28]:
                title_types.append("Lexikon")
            elif 'e' in field[24:28]:
                title_types.append("Enzyklopädie")
            elif 'f' in field[24:28]:
                title_types.append("Handbuch")
            elif 'i' in field[24:28]:
                title_types.append("Index/ Verzeichnis")
            elif 'm' in field[24:28]:
                title_types.append("Thesis")
            elif field[29] == '1':
                title_types.append("Konferenz Publikation")
            elif field[30] == '1':
                title_types.append("Festschrift")
            elif field[33] == 'e':
                title_types.append("Aufsatz")
            elif field[33] == 'i':
                title_types.append("Brief")
            elif field[33] == 's':
                title_types.append("Rede")
            elif field[34] == 'a':
                title_types.append("Autobiographie")
            elif field[34] == 'b':
                title_types.append("Individuelle Biographie")
            elif field[34] == 'c':
                title_types.append("Kollektive Biographie")
            elif field[34] == 'd':
                title_types.append("Enthält biographische Information")
            return title_types
        except:
            return title_types

    def persons(self):
        """
        Returns all persons mentioned in the record.

        Returns:
            persons: List of Strings holding person name, gnd-number, relator (can be author etc.) and relationship (abbreviation of relator)
        """
        
        persons = []
        person_names = set() # to check if we had a person already, if yes don't take the duplicate (less info than the first appearence)
        person_fields = []
        for field in self.__person_fields(Field.PERSONAL_NAME_ADDED_ENTRY):
            person_fields.append(field)
        for field in self.__person_fields(Field.PERSONAL_NAME):
            person_fields.append(field)
        for field in person_fields:
            try:
                new_person = person_name = person_gnd = None
                relator = relationship = ""
                for subfield in field["subfields"]:
                    if "a" in subfield:
                        person_name = subfield["a"]
                    elif "0" in subfield and "(DE-588)" in subfield["0"]:
                        person_gnd_full = subfield["0"]
                        person_gnd = person_gnd_full[8:]
                    elif "e" in subfield:
                        relator = subfield["e"]
                    elif "4" in subfield:
                        relationship = subfield["4"]
                
                if person_name in person_names: 
                    continue
                else:
                    person_names.add(person_name)
                new_person = person_name + " (" + person_gnd + ", " + relator + ", " + relationship + ")"
                persons.append(new_person)
            except:
                continue
        return persons

    def as_rows(self):
        """
        Saves relevant information for the record in a list of rows (dictionaries), for each combination of persons a new row will be created.

        Returns:
            result: List of Dicts (rows to write to a csv file later)
        """
        result = []

        bvnumber = self.bvnumber() if self.bvnumber() else ''
        title = self.title() if self.title() else ''
        title_remainder = self.title_remainder() if self.title_remainder() else ''
        place = self.place() if self.place() else ''
        date = self.date() if self.date() else ''
        title_types = self.title_types() if self.title_types() else ''

        row = {
            'bvnumber': bvnumber,
            'title': title,
            'title_remainder': title_remainder,
            'place': place,
            'date': date,
            'title_types': title_types,
            'relationship': 'steht in Beziehung zu',
            'person1_name': '', 
            'person1_gnd_id': '', 
            'person1_function': '',
            'person2_name': '', 
            'person2_gnd_id': '', 
            'person2_function': '',
        }

        persons = self.persons()
        persons_length = len(persons)

#       if persons_length == 0:
#            result.append(row)
            
#        elif persons_length == 1:
# Dont return Records without persons
# match pairs with gnd_id here 

        if persons_length == 1:
            person = persons[0]
            person1_name = person.split(" (")[0]
            person1_gnd_id = person.split(" (")[1].split(", ")[0]
            person1_function = person.split(" (")[1].split(", ")[2][:-1]
            row['person1_name'] = person1_name
            row['person1_gnd_id'] = person1_gnd_id
            row['person1_function'] = person1_function
            result.append(row)
        else:
            for source, target in utils.pairs(persons):
                pair_row = dict(row)
                person1_name = source.split(" (")[0]
                person1_gnd_id = source.split(" (")[1].split(", ")[0]
                person1_function = source.split(" (")[1].split(", ")[2][:-1]
                pair_row['person1_name'] = person1_name
                pair_row['person1_gnd_id'] = person1_gnd_id
                pair_row['person1_function'] = person1_function
                person2_name = target.split(" (")[0]
                person2_gnd_id = target.split(" (")[1].split(", ")[0]
                person2_function = target.split(" (")[1].split(", ")[2][:-1]
                pair_row['person2_name'] = person2_name
                pair_row['person2_gnd_id'] = person2_gnd_id
                pair_row['person2_function'] = person2_function
                result.append(pair_row)

        return result
