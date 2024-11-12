import json
import re

pattern = (r'(^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[([^\]]+)\] "(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS) ([^"]+)" (\d{3}) (\d+|-) "(http:\/\/semicomplete\.com\/presentations\/logstash-monitorama-2013\/)")

with open('apache_logs. txt', r')as Lines:
    jsonExtract = []
    for line in lines:
        values = re. finditer (pattern, Line)
        for match in values:
            jsonData = {"ip";match. group(1), "Date": match. group(2), "time" :match group (3), "Method"smatch. group (4), "Path" :match group (5), "parameters": match
            jsonExtract. append (jsonData)
    print(json .dumps(jsonExtract, indent=4))l