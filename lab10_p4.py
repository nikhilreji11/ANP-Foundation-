#Define a generator function filter_strings that yields only strings from a list of mixed data types (integers, strings, floats, etc.).Use this generator to filter a list containing various data types and print only thestrings.
#Sample Data:
#mixed_data = [1, "hello", 3.14, "world", 42]

def filter_strings(data):
    for item in data:
        if isinstance(item, str):
            yield item
mixed_data = [1, "hello", 3.14, "world", 42]
for string in filter_strings(mixed_data):
    print(string)

