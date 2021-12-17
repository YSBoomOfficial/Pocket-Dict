import clean_data as data
import re

def clean_input_str(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-z0-9 ]', '', text)

    # ensuring the input is not too long or too specific
    # if the input is too long or specific a translation may not exist
    # one of the longest pieces of data is around 57 characters long so 60 seemed like a good upper bound
    if len(text) > 60:
        raise ValueError("Input string is too long")


    return text

def get_all_data(search_string: str) -> list[str]:
    results = []

    for key, value in data.data_dict.items():
        if search_string in key:
            for item in value:
                results.append(item)

    return sorted(results, key=len)

# this will reduce the scope of the search so that the length of the translations are only twice as long as the input string. This will avoid long and random translations that may not be relevant.
def reduce_search_results(search_string: str, data_list: list[str]) -> list[str]:
    results = []

    for item in data_list:
        if len(item) <= (2*len(search_string)) :
            results.append(item)

    return sorted(results, key=len)