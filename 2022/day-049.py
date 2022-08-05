#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2022/8/4 10:30
# @Author   : Zhang JinLei
# @Describe :

users_visited_phuket = [{"first_name": "Sirena",
                         "last_name": "Gross",
                         "phone_number": "650-568-0388",
                         "date_visited": "2018-03-14",
                         },

                        {"first_name": "Siri",
                         "last_name": "Groeey",
                         "phone_number": "640-538-0388",
                         "date_visited": "2019-03-14",
                         },

                        ]

users_visited_nz = [{"first_name": "Justin",
                     "last_name": "Malcom",
                     "phone_number": "267-282-1964",
                     "date_visited": "2011-03-13", },

                    {"first_name": "Jimmy",
                     "last_name": "Madfasd",
                     "phone_number": "257-262-1664",
                     "date_visited": "2018-03-13", },

                    ]


from dataclasses import dataclass, field
@dataclass(frozen=True)
class VisitRecordDC:
    first_name: str
    last_name: str
    phone_number: str    
    date_visited: str = field(compare=False)　　

def find_potential_customers_v4():    
    return set(VisitRecordDC(**r) for r in users_visited_puket) - set(VisitRecordDC(**r) for r in users_visited_nz)


result = find_potential_customers_v4()

list(result)
