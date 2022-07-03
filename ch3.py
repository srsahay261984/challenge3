import json
data = '{"a":{"b":{"c":"d"}}}'
print("Object: ", data)
print("---------------------------")
json_str = json.loads(data)

# Get value for the first occurance of the key
def get_value_by_key(dataobject, key):
    if key in dataobject:
        return dataobject[key]
    for key, value in dataobject.items():
        if type(value) is dict:
            data = get_value_by_key(value, key)
            if data is not None:
                return data

def get_value(dataobject, key):
    if type(key) is str:
        return get_value(dataobject, key.split("/"))
    elif len(key) == 0:
        return dataobject
    else:
        key1 = key[0]
        if key1 != '' and key1 in dataobject:
            return get_value(dataobject[key1], key[1:])
        else:
            return

if __name__ == "__main__":
    key = input("Enter Key\n")
    print("key: ", key)
    print("---------------------------")
    print("Value: ", get_value(json_str, key))
