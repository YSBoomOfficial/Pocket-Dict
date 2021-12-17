import clean_data as data

def clean_input_str(text: str) -> str:
    return text

def get_all_data(search_string: str) -> list[str]:
    results = []

    for key, value in data.data_dict.items():
        if search_string in key:
            for item in value:
                results.append(item)

    return sorted(results, key=len)


data = get_all_data('hello')

print(data)
