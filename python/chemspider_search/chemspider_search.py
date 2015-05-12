# Authored by Max Pagels, Wednesday 19 February 2014
# Uses the ChemSciPy Python wrapper for ChemSpider

import chemspipy
import sys
import fileinput

terms = []

print "Enter your search terms, one per line. When done, hit  Crtl+D on an empty line to start the search."

for line in fileinput.input():
    if len(line.strip()) > 0:
        terms.append(line.strip())
    pass

for term in terms:
    d = {}
    c = chemspipy.find_one(term)
    if not c:
        continue
    d["imageurl"] = c.imageurl
    d["mf"] = c.mf
    d["smiles"] = c.smiles
    d["inchi"] = c.inchi
    d["inchikey"] = c.inchikey
    d["averagemass"] = c.averagemass
    d["molecularweight"] = c.molecularweight
    d["monoisotopicmass"] = c.monoisotopicmass
    d["nominalmass"] = c.nominalmass
    d["alogp"] = c.alogp
    d["xlogp"] = c.xlogp
    d["commonname"] = c.commonname
    #d["image"] = c.image
    d["mol"] = c.mol
    print "\n\nSEARCH TERM: " + term
    print "-----------------"
    for key, item in d.iteritems():
        print key + ": " + str(item)
    print "-----------------"