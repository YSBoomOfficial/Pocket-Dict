import clean_data as data
import re

def clean_input_str(text: str) -> str:
    # remove leading and trailing whitespace
    text = text.lower().strip()
    # remove extra whitespace eg: '   ' + ' '
    text = re.sub(r'\s+', ' ', text)
    # remove non-alphanumeric characters
    text = re.sub(r'[^a-z0-9 ]', '', text)
    # remove leading and trailing whitespace that may have been the result of the string cleaning
    text = text.lower().strip()

    return text

def find_all(search_string: str) -> list[str]:
    results = []

    for key, value in data.data_dict.items():
        if search_string in key:
            for item in value:
                results.append(item)

    return sorted(results, key=len)

# Reduce the scope of the search so that the length of the translations are only twice as long as the input string to avoid long and random translations that may not be relevant.
def reduce_results(search_string: str, data_list: list[str]) -> list[str]:
    results = []

    for item in data_list:
        if len(item) <= (2*len(search_string)) :
            results.append(item)

    return sorted(results, key=len)

##### FILTER NOUN NOT WORKING #####
# Filter for only nouns
# def get_nouns(data_list: list[str]) -> list[str]:
#     results = []

#     for item in data_list:
#         # filter all posible articles which are always followed by nouns
#         if ('le ' in item) or ('la ' in item) or ('les ' in item) or ('l\'' in item) or ('un ' in item) or ('une ' in item) or ('de la ' in item) or ('du ' in item) or ('des ' in item) or ('à la ' in item) or ('au ' in item) or ('aux ' in item):
#             results.append(item)

#     return results

##### FILTER NOUN NOT WORKING #####
# get results for search text
# def get_result(search_text: str, show_less: bool, only_nouns: bool) -> list[str]:
#     # clean the input string
#     search_text = clean_input_str(search_text)

#     # find all possible translations
#     all_results = find_all(search_text)

#     if show_less and only_nouns:
#         # reduce the scope of the results and filter for nouns
#        return get_nouns(reduce_results(search_text, all_results))
#     elif show_less:
#         # reduce the scope of the results
#         return reduce_results(search_text, all_results)
#     elif only_nouns:
#         # filter all results for nouns
#         return get_nouns(all_results)
#     else:
#         return all_results


# get results for search text
def get_result(search_text: str, show_less: bool = False) -> list[str]:
    # clean the input string
    search_text = clean_input_str(search_text)

    # find all possible translations
    all_results = find_all(search_text)

    if show_less:
        # reduce the scope of the results
        return reduce_results(search_text, all_results)
    else:
        # return all results
        return all_results