import os

gazetteer = set(open(os.getcwd().replace('/app/NER', '') + '/gazetteers/cities.lst').read().split('\n'))
