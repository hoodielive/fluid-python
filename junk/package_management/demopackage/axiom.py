from pkgutil import get_data
get_data('example', 'data/datafile.txt').decode('utf-8')
