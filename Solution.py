"""
Q1. Coding Question -

Given a list of maps below. Phrases in the same map are considered synonyms. Eg. {"Dg set": "Diesel generator"} implies "Dg set" and "Diesel generator" are synonyms.

If a phrase S1 is a synonym of phrase S2 and S3 is a synonym of S2, then S1, S2, S3 are synonyms of each other by associative property. S1,S2, S3 will be part of a "group".

A group can be of minimum two phrases or more.

Task of the question is: Given a Table of synonyms, Write a Program to find all groups of synonyms.

Input:

[ {"Dg set": "Diesel generator"}, {"Group": "Organization"}, {"Orange": "Kinnu"},

{"Organization": "Organisation"},

{"Orange": "narangi"}

Output:

[["Organization", "Organisation", "Group"], ["Dg set", "Diesel generator'], ["Orange", "Kinnu", "narangi"]
]"""

# Solution

data = [{'Dg set' : 'Diesel Generator'},
{'Organization' : 'Organisation'},
{'Group' : 'Organization'}, 
{'Orange' : 'Kinnu'},
{'Orange' : 'narangi'}]


L = []
flag = 0
for x in data:
    key = list(x.keys())[0]; value = list(x.values())[0];
    for y in L:
        if key  in y and value in y:
            flag = 1;
            break;
        if key in y and value not in y: 
            y.append(value);flag=1;
            break;
        if key not in y and value in y:
            y.append(key);
            flag=1;break

        else:
            flag=0;

    if (flag==0):
         L.append([key, value])
    else:
        continue;


print(L)

""" 
OUTPUT
[['Dg set', 'Diesel Generator'], ['Organization', 'Organisation', 'Group'], ['Orange', 'Kinnu', 'narangi']]
"""
