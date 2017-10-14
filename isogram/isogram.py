def is_isogram(string):
    import re

    string = re.sub(r'[^a-z]', '', string.lower())
    str_set = set(string)

    if len(str_set) == len(string):
        return True
    return False
