import re
line = "To call this movies clich&#xE9; is an insult to the word clich&#xE9;."
print line
line = re.sub(r"\&....;","",line)
print line


