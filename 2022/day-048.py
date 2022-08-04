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


def find_potential_customers_v2():
    """ 找到去过普吉岛但是没去过新西兰的人，性能改进版"""
    # 首先，遍历所有新西兰旅客记录，创建查找索引
    nz_records_idx = {
        (rec['first_name'], rec['last_name'], rec['phone_number'])
        for rec in users_visited_nz
    }
    for rec in users_visited_phuket:
        key = (rec['first_name'], rec['last_name'], rec['phone_number'])
    if key not in nz_records_idx:
        yield rec


result = find_potential_customers_v2()

list(result)
