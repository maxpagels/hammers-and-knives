# This script reads a CSV and generates
# 0-N CSV files based on a given column name (passed as second paramter)

import csv
import sys
import os

csv.register_dialect('dial', delimiter=',', quoting=csv.QUOTE_ALL)

if len(sys.argv) < 3:
    print("\nusage: python3 " + sys.argv[0] + " <input> <split>")
    print("\t<input> : CSV file")
    print("\t<split> : column to split by\n")
    exit()

splitby = sys.argv[2]
encountered_values = {}

with open(sys.argv[1]) as f:
    reader = csv.reader(f, "dial")
    tmp = list(reader)
    split_index = -1    
    for i, column in enumerate(tmp[0]):
        if column == splitby:
            split_index = i
            break
    if split_index == -1:
        print("could not split by " + sys.argv[1] + ", no such column found")
        exit()
    else:
        for i in range(1, len(tmp)):
            if tmp[i][split_index] not in encountered_values:
                encountered_values[tmp[i][split_index]] = [tmp[i]]
            else:
                encountered_values[tmp[i][split_index]].append(tmp[i])
    os.makedirs("chunks-" + splitby)
    for item in encountered_values.keys():
        with open("chunks-" + splitby + "/" + item + ".csv", 'w') as f:
            writer = csv.writer(f, "dial")
            writer.writerows([tmp[0]])
            writer.writerows(encountered_values[item])
