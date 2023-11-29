def get_value(data: str, separator: str, position: int) -> str:
    split_values = data.split(separator)  # split de komma

    if 0 <= position < len(split_values):
        value = split_values[position]  # krijg ew waarde van de postiti
    else:
        value = None

    return value  # keer de waarde terug

# Test the function
toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
position = 8  # position of Bram

result = get_value(toets_data, separator, position)
print(result)  # It should print: Bram:6
