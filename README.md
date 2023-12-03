# Df-to-bibtex
Python code aiming to convert bibliographic data stored in a generic panda dataframe into a bibtex file.
The bibliographic data are stored in a file named bibliography.csv.
They are converted into a bibtex compatible file, and saved in a file called references.bib
The bibtex key generated respect the format NameYear-of-publication. In case of redundancy of the keys, the redundancy is respected and have to be treated in a next step.
