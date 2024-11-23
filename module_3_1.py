
calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    string_  = str(string)
    result = (len(string_), string_.upper(), string_.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result
print(string_info('Piramida'))
print(string_info('Tank'))
print(is_contains('boom', ['gan', 'dinamit', 'trotl'])) # No matches
print(is_contains('AniMAlS', ['Bear', 'PanDa', 'CrocodilE', 'PuMA'])) # Urban ~ urBAN

print(calls)