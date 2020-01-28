'''
Generate a member_number
LLL-SSSSS-RRR-C ( 12 digits )

Organization number - Sequential member number - random digits - check digit

Start sequential digits at 00001.
Allows for 99,998 members in an organization.
Random digits in range (000-999).
Check digit.

Group like this for reading: ( four groups of three )
LLL-SSS-SSR-RRC
Uses the Damm algorithm to generate a check digit.
'''

import random

import damm

def get_org_id(base_id):
    if base_id:
        org_id = str(base_id)[0:3]
    else:
        org_id = '123'
    return org_id

def get_sequential_id(base_id):
    if base_id:
        sequential_id = str(base_id)[3:8]
    else:
        sequential_id = '00000'
    return sequential_id

def create_id(base_id):

    org_id = get_org_id(base_id)
    sequential_id = get_sequential_id(base_id)

    sequential_id = str(int(sequential_id)+1).zfill(5)

    random.seed()
    random_id = str(random.randint(0,999)).zfill(3)

    raw_id = str(org_id) + str(sequential_id) + str(random_id)

    check_digit = damm.encode(raw_id)

    next_id = raw_id + str(check_digit)

    return next_id

def check_id(member_id):
    return damm.check(member_id)

