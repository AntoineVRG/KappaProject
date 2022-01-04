#!/usr/bin/env python3

import sys
import os
import glob

def main():
    if len(sys.argv) == 3 :
        tbl = glob.glob(sys.argv[1])
        for i in tbl :
            newfile = open(i, 'r')
            for line in newfile:
                if line.find("Kappa")!=-1 or line.find("LUL")!=-1:
                    with open(sys.argv[2], 'r+') as f:
                        f.seek(0, os.SEEK_END)
                        f.write(line)
    else:
        sys.exit(84)
    
main()