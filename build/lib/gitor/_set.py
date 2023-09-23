def find_value_in_json(JSON: set, attribute: str, value: str):
    """
    Find the set that has attribute that is equal to value
    """
    for i in JSON:
        if i[attribute] == value:
            return i
        
    print(f"Error: could not find {attribute} - {value}")