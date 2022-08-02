#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2022/8/2 17:40
# @Author   : Zhang JinLei
# @Describe : v1


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


def find_potential_customers_v1():
    """找到去过普吉岛但是没去过新西兰的人
    :return: 通过 Generator 返回符合条件的旅客记录
    """
    for puket_record in users_visited_phuket:
        is_potential = True
        for nz_record in users_visited_nz:
            if (puket_record['first_name'] == nz_record['first_name'] and
                    puket_record['last_name'] == nz_record['last_name'] and
                    puket_record['phone_number'] == nz_record['phone_number']):

                is_potential = False
                break

    if is_potential:

        yield puket_record

result = find_potential_customers_v1()

list(result)