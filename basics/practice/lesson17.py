#search()
#Searches a string for a match and returns a match object if found.


match = re.search(r'\d+', 'There are 123 apples')
print(match.group())

