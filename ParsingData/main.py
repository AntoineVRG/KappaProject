#!/usr/bin/env python3

import sys
import os
import glob
import csv

def main():
    if len(sys.argv) == 3 :
        file = open(sys.argv[1], 'r')
        new = open(sys.argv[2], 'w')
        csvreader = csv.reader(file)
        writer = csv.writer(new)
        rows = []
        for row in csvreader:
            
            incr = 0
            string = ""
            for i in row[0]:
                if incr != 3:
                    if i == ':':
                       incr = incr + 1
                    string += i
            row[0] = row[0][len(string)+1:]
            if row[1] != "3" and row[1] != "" and row[1] != "4":
                rows.append(row)

        # for row in rows:
        #     print(row[0])
        writer.writerows(rows)
        file.close()
    else:
        sys.exit(84)
    
main()