import re

#funtion1
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
print(result)  # Bram:6


#funtion 2 

def mark_and_split(text):
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|")
    return sub_sentences

def calculate_ego_score(sub_sentences):
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.strip().lower()
        if len(sentence) > 0:
            words = sentence.split(' ')
            if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
                ego_score += 1
    return ego_score


text = "Geachte heer/mevrouw,Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren. Ik ben buitengewoon slim en in staat om snel nieuwe informatie te verwerken en te gebruiken om de beste beslissingen te nemen voor het bedrijf. Ik ben er zeker van dat ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf, en ik zal in staat zijn om snel resultaten te boeken en uw bedrijf naar de top te brengen. Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij. Ik verdien daarom een plek in uw team.Ik kijk er naar uit om te horen wanneer ik op gesprek mag komen, zodat ik u persoonlijk kan overtuigen van mijn geschiktheid voor deze functie."
sub_sentences = mark_and_split(text)
score = calculate_ego_score(sub_sentences)
print(score)
