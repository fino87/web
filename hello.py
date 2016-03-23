#!/usr/bin/env python

import re

def app(env, start_resp):
    query_string = env.get('QUERY_STRING')
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]

    if len(query_string) == 0:
        query_string = "ALL OK,\n but query string is empty.."
    query_string = re.sub(r'&','\n',query_string)

    #resp = bytes(query_string, encoding = 'utf-8')
    resp = bytes(query_string)
    start_resp(status, headers)
    return [resp]
