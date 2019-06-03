import os
import re

path = os.getcwd()

gazetteer = set(open(re.sub(r'/app.*?$', '', path) + '/gazetteers/cities.lst').read().split('\n'))
