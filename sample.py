# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python
# test() TASK1
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys

# test_a() TASK2
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys, but you have to extract the attributes from the "insr" tag
# and add them to the list for the dictionary key "insr"

## adding more commit
##adding more to check

##further checking to check the push

import xml.etree.ElementTree as ET
import os
import csv
import pandas

DATADIR = "/Users/Priya/Documents/Data Analysis/Data"
article_file = "exampleResearchArticle.xml"
csvfile = "temp.csv"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()
    


def get_authors(root):
    authors = []
    print ("in get Authors")
# useful methods that help iterate recursively over all the sub-tree below it (its children, their children, and so on). For example
    #for au in root.iter('au'):
    #    print (au.attrib)
    
    
    for au in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None
        }
        data["fnm"] = au.find('fnm').text
        data["snm"] = au.find('snm').text
        data["email"] = au.find('email').text

        authors.append(data)

    return authors
    
def get_authors_a(root):
    authors = []
    print ("in get Authors")
# useful methods that help iterate recursively over all the sub-tree below it (its children, their children, and so on). For example
    #for au in root.iter('au'):
    #    print (au.attrib)
    
    
    for au in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []
        }
        data["fnm"] = au.find('fnm').text
        data["snm"] = au.find('snm').text
        data["email"] = au.find('email').text
        insr = au.findall('insr')
        for i in insr:    
            data["insr"].append(i.attrib["iid"])
        
        authors.append(data)

    return authors


def test():
    solution = [{'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'}, {'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'}, {'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'}, {'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'}, {'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'}, {'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'}, {'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'}, {'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
    
    datafile = os.path.join(DATADIR,article_file)
    csv_file = os.path.join(DATADIR,csvfile)    
    #with open(datafile,'rt') as infile:
    #with open(csv_file,'rt') as infile:
    #    reader = csv.reader(infile,delimiter=',')
    #    for row in reader:
    #    print (row)
            
    root = get_root(datafile)
    
    for child in root:
        print (child.tag)
    data = get_authors(root)
    print (data)

    assert data[0] == solution[0]
    
    assert data[1]["fnm"] == solution[1]["fnm"]
    
def test_a():
    solution = [{'insr': ['I1'], 'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'},
                {'insr': ['I2'], 'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'},
                {'insr': ['I3', 'I4'], 'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'},
                {'insr': ['I3'], 'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'},
                {'insr': ['I8'], 'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'},
                {'insr': ['I3', 'I5'], 'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'},
                {'insr': ['I6'], 'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'},
                {'insr': ['I7'], 'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]

    datafile = os.path.join(DATADIR,article_file)
    root = get_root(datafile)
    for child in root:
        print (child.tag)
    data = get_authors_a(root)
    print (data)

    assert data[0] == solution[0]
    assert data[1]["insr"] == solution[1]["insr"]


#test()
test_a()