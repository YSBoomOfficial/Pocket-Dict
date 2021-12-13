import pandas as pd

# lists that will contain all the data
en_data = []
fr_data = []
data_dict = dict()


def clean_en(text):
    if ' ' in text:
        text = text.replace(' ', ' ')

    if '\"' in text:
        text = text.replace('\"', '')

    if '!' in text:
        text = text.replace('!', '')

    if '?' in text:
        text = text.replace('?', '')

    if '.' in text:
        text = text.replace('.', '')

    return text


def clean_fr(text):
    if ' ' in text:
        text = text.replace(' ', ' ')

    if '\"' in text:
        text = text.replace('\"', '')

    if '!' in text:
        text = text.replace(' !', '')

    if '?' in text:
        text = text.replace(' ?', '')

    if '.' in text:
        text = text.replace('.', '')

    return text


with open('eng-french.txt', 'r', encoding='utf-8') as f:
    txt_data = f.read().split('\n')


# deal with the data in the txt file
txt_data_en = []
txt_data_fr = []

for row in txt_data:
    data = row.split('\t')

    if data[0] == '':
        break

    en = data[0]
    fr = data[1]

    txt_data_en.append(clean_en(en).lower())
    txt_data_fr.append(clean_fr(fr).lower())


csv_data = pd.read_csv("eng_-french.csv")
csv_data = csv_data.rename(columns={'English words/sentences': 'English',
                                    'French words/sentences': 'French'})

# deal with the data in the csv file
csv_data_en = []
csv_data_fr = []

for i, en in enumerate(csv_data.English):
    csv_data_en.append(clean_en(en).lower())

for i, fr in enumerate(csv_data.French):
    csv_data_fr.append(clean_fr(fr).lower())

en_data = txt_data_en + csv_data_en
fr_data = txt_data_fr + csv_data_fr

# make sure both lists are the same length
# assert len(en_data) == len(fr_data) == 325484

# given that there may be many translations for a given english word/phrase, putting the english phrase in a dictionary with a list of translations as it's values is best.
# Dict access is O(1) so this is a good way to store the data. as supposed to looping over two lists which would be O(n^2)
for i in range(0, len(en_data)):
    if en_data[i] in data_dict:
        data_dict[en_data[i]].add(fr_data[i])
    else:
        data_dict[en_data[i]] = set()
        data_dict[en_data[i]].add(fr_data[i])

# given that the datasets may have duplicates, using a set will avoid data duplication and then converting it back to a list will make the data easier to access
for key, value in data_dict.items():
    data_dict[key] = list(value)