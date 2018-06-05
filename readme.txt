# References

description = ['Using DictReader to return an iterator that produces each row as needed.',
               'Converting the DictReader iterator into a list of dictionaries.',
               'Using Counter to count the occurrences of a list item.',
               'Getting the most common element from Counter.',
               'Using the datetime module from the standard library.',
               'Sample code for converting seconds to days, hours, minutes and seconds',
               'Using the pprint module from the standard library']

websites = ['https://docs.python.org/3/library/csv.html#csv.DictReader',
            'https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries/21572244',
            'https://stackoverflow.com/questions/2600191/how-to-count-the-occurrences-of-a-list-item',
            'https://www.robjwells.com/2015/08/python-counter-gotcha-with-max/',
            'https://docs.python.org/3/library/datetime.html',
            'https://www.w3resource.com/python-exercises/python-basic-exercise-65.php',
            'https://docs.python.org/3.6/library/pprint.html']

for i, desc in enumerate(description):
    print(str(i+1) + '. ' + desc + '\n\n' + websites[i] + '\n')
