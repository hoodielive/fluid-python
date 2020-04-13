import re 


regex = re.compile(r'[0-9]{1,3}')

match = regex.match(text)
all_matches = match.groups()
print(match, all_matches)

match = regex.search(text)
all_matches = match.groups()
print(match, all_matches)

replace = regex.sub(replacement, text)
