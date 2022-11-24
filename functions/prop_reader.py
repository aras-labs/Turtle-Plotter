
def prop_reader(file_name):
    """Reads a file and returns a dictionary of the properties."""
    with open(file_name, 'r') as f:
        lines = f.readlines()
    properties = {}
    for line in lines:
        if line[0] == '#':
            continue
        line = line.strip()
        if line == '':
            continue
        key, value = line.split('=')

        array = key.split('.')
        dic = properties
        for ps in array:
            if ps not in dic.keys() and ps != array[-1]:
                dic[ps.strip()] = {}
            elif ps == array[-1]:
                dic[ps.strip()] = value.strip()
            dic = dic[ps.strip()]

    return properties

if __name__ == '__main__':
    filename = "files/kamal.properties.txt"
    d = prop_reader(file_name=filename)
    print(d["controller"]["page"]["width"])