import io
import json
import unittest

from bibliographiedaten import record


class TestRecord(unittest.TestCase):

    def test_should_find_no_persons_in_record1(self):
        rec1 = record.Record(self.marc1)

        actual = rec1.person_ids()
        expected = set()
        self.assertSetEqual(actual, expected)

    def test_should_find_persons_in_record2(self):
        rec2 = record.Record(self.marc2)

        actual = rec2.person_ids()
        expected = {'118523341'}
        self.assertSetEqual(actual, expected)

    def test_should_convert_record2_into_csv_rows(self):
        rec2 = record.Record(self.marc2)
        actual = rec2.as_rows()
        expected = [
            {
                'bvnumber': 'BV000024723',
                'title': 'Musikalischer Realismus',
                'place': 'München',
                'date': '1982',
                'title_type': '',
                'relationship': 'steht in Beziehung zu',
                'source': 'Dahlhaus, Carl (118523341, Verfasser, aut)',
                'target': '',
            }
        ]
        self.assertListEqual(actual, expected)

    def setUp(self):
        self.marc1 = {
            "leader": "00812nam a2200253 cc4500",
            "fields": [
                {
                    "001": "BV000028404"
                },
                {
                    "264": {
                        "subfields": [
                            {
                                "a": "Hagen"
                            }
                        ],
                        "ind1": " ",
                        "ind2": "1"
                    }
                }
            ]
        }

        self.marc2 = {
            "leader": "01345nam a2200409 cb4500",
            "fields": [
                {
                    "001": "BV000024723"
                },
                {
                    "003": "DE-604"
                },
                {
                    "005": "20080418        "
                },
                {
                    "007": "t"
                },
                {
                    "008": "870612s1982             |||| 00||| ger d"
                },
                {
                    "020": {
                        "subfields": [
                            {
                                "a": "349200539X"
                            },
                            {
                                "9": "3-492-00539-X"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "035": {
                        "subfields": [
                            {
                                "a": "(OCoLC)230244927"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "035": {
                        "subfields": [
                            {
                                "a": "(DE-599)BVBBV000024723"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "040": {
                        "subfields": [
                            {
                                "a": "DE-604"
                            },
                            {
                                "b": "ger"
                            },
                            {
                                "e": "rakwb"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "041": {
                        "subfields": [
                            {
                                "a": "ger"
                            }
                        ],
                        "ind1": "0",
                        "ind2": " "
                    }
                },
                {
                    "049": {
                        "subfields": [
                            {
                                "a": "DE-12"
                            },
                            {
                                "a": "DE-19"
                            },
                            {
                                "a": "DE-37"
                            },
                            {
                                "a": "DE-384"
                            },
                            {
                                "a": "DE-473"
                            },
                            {
                                "a": "DE-703"
                            },
                            {
                                "a": "DE-739"
                            },
                            {
                                "a": "DE-20"
                            },
                            {
                                "a": "DE-824"
                            },
                            {
                                "a": "DE-Gp1"
                            },
                            {
                                "a": "DE-1259"
                            },
                            {
                                "a": "DE-B170"
                            },
                            {
                                "a": "DE-188"
                            },
                            {
                                "a": "DE-N32"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "084": {
                        "subfields": [
                            {
                                "a": "LR 19506"
                            },
                            {
                                "2": "rvk"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "084": {
                        "subfields": [
                            {
                                "a": "LP 19505"
                            },
                            {
                                "2": "rvk"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "100": {
                        "subfields": [
                            {
                                "a": "Dahlhaus, Carl"
                            },
                            {
                                "d": "1928-1989"
                            },
                            {
                                "e": "Verfasser"
                            },
                            {
                                "0": "(DE-588)118523341"
                            },
                            {
                                "4": "aut"
                            }
                        ],
                        "ind1": "1",
                        "ind2": " "
                    }
                },
                {
                    "245": {
                        "subfields": [
                            {
                                "a": "Musikalischer Realismus"
                            },
                            {
                                "b": "zur Musikgeschichte des 19. Jahrhunderts"
                            },
                            {
                                "c": "Carl Dahlhaus"
                            }
                        ],
                        "ind1": "1",
                        "ind2": "0"
                    }
                },
                {
                    "264": {
                        "subfields": [
                            {
                                "a": "München"
                            },
                            {
                                "b": "Piper"
                            },
                            {
                                "c": "1982"
                            }
                        ],
                        "ind1": " ",
                        "ind2": "1"
                    }
                },
                {
                    "300": {
                        "subfields": [
                            {
                                "a": "165 S."
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "336": {
                        "subfields": [
                            {
                                "b": "txt"
                            },
                            {
                                "2": "rdacontent"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "337": {
                        "subfields": [
                            {
                                "b": "n"
                            },
                            {
                                "2": "rdamedia"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "338": {
                        "subfields": [
                            {
                                "b": "nc"
                            },
                            {
                                "2": "rdacarrier"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                },
                {
                    "490": {
                        "subfields": [
                            {
                                "a": "Serie Piper"
                            },
                            {
                                "v": "239"
                            }
                        ],
                        "ind1": "1",
                        "ind2": " "
                    }
                },
                {
                    "648": {
                        "subfields": [
                            {
                                "a": "Geschichte 1814-1914"
                            },
                            {
                                "2": "gnd"
                            }
                        ],
                        "ind1": " ",
                        "ind2": "7"
                    }
                },
                {
                    "650": {
                        "subfields": [
                            {
                                "a": "Realismus"
                            },
                            {
                                "0": "(DE-588)4048680-1"
                            },
                            {
                                "2": "gnd"
                            }
                        ],
                        "ind1": "0",
                        "ind2": "7"
                    }
                },
                {
                    "650": {
                        "subfields": [
                            {
                                "a": "Musik"
                            },
                            {
                                "0": "(DE-588)4040802-4"
                            },
                            {
                                "2": "gnd"
                            }
                        ],
                        "ind1": "0",
                        "ind2": "7"
                    }
                },
                {
                    "689": {
                        "subfields": [
                            {
                                "a": "Realismus"
                            },
                            {
                                "0": "(DE-588)4048680-1"
                            },
                            {
                                "D": "s"
                            }
                        ],
                        "ind1": "0",
                        "ind2": "0"
                    }
                },
                {
                    "689": {
                        "subfields": [
                            {
                                "a": "Musik"
                            },
                            {
                                "0": "(DE-588)4040802-4"
                            },
                            {
                                "D": "s"
                            }
                        ],
                        "ind1": "0",
                        "ind2": "1"
                    }
                },
                {
                    "689": {
                        "subfields": [
                            {
                                "5": "DE-604"
                            }
                        ],
                        "ind1": "0",
                        "ind2": " "
                    }
                },
                {
                    "689": {
                        "subfields": [
                            {
                                "a": "Musik"
                            },
                            {
                                "0": "(DE-588)4040802-4"
                            },
                            {
                                "D": "s"
                            }
                        ],
                        "ind1": "1",
                        "ind2": "0"
                    }
                },
                {
                    "689": {
                        "subfields": [
                            {
                                "a": "Geschichte 1814-1914"
                            },
                            {
                                "A": "z"
                            }
                        ],
                        "ind1": "1",
                        "ind2": "1"
                    }
                },
                {
                    "689": {
                        "subfields": [
                            {
                                "5": "DE-604"
                            }
                        ],
                        "ind1": "1",
                        "ind2": " "
                    }
                },
                {
                    "830": {
                        "subfields": [
                            {
                                "a": "Serie Piper"
                            },
                            {
                                "v": "239"
                            },
                            {
                                "w": "(DE-604)BV000000181"
                            }
                        ],
                        "ind1": " ",
                        "ind2": "0"
                    }
                },
                {
                    "999": {
                        "subfields": [
                            {
                                "a": "oai:aleph.bib-bvb.de:BVB01-000000818"
                            }
                        ],
                        "ind1": " ",
                        "ind2": " "
                    }
                }
            ]
        }
