import json
import requests


def load_data():
    """ Gets Data from API """
    API_KEY = 'UN4D5vRBaN8ybUMEfq5x3g==OQ4jGHiWAkmE0Zxf'
    SEARCH = "Fox"
    url = f'https://api.api-ninjas.com/v1/animals?name={SEARCH}'
    res = requests.get(url, headers={'X-Api-Key': API_KEY})
    return json.loads(res.text)


def load_template(file_path):
    """ Loads a HTML Tamplate """
    with open(file_path, encoding="UTF-8", errors="ignore") as gettemp:
        return gettemp.read()


def serialize_animal(animal):
    """Serialization of the animal objects"""
    output = ""
    output += "<li class='cards__item'>\n"
    output += f"<div class='card__title'>{animal["name"]}<br/>\n</div><br/>"
    try:
        output += f"<div class='card__text'>\n <ul>\n<li><strong>Diet: </strong>{animal["characteristics"]["diet"]}</li>\n"
    except KeyError:
        pass
    try:
        output += f"<li><strong>Prey: </strong>{animal["characteristics"]["prey"]}</li>"
    except KeyError:
        pass
    output += "<li><strong>Location: </strong>"
    output += f" {", ".join(animal["locations"])}</li>\n"
    try:
        output += f"<li><strong>Type: </strong>{animal["characteristics"]["type"]}</li>\n"
    except KeyError:
        pass
    output += "</ul>"
    output += "</div>"
    output += "</li>"
    return output


def combine_data_template():
    animals_data = load_data()
    template = load_template("animals_template.html")
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    temp_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)
    return temp_with_data


def main():
    temp_with_data = combine_data_template()
    with open("animals2.html", "w") as makepage:
        makepage.write(temp_with_data)


if __name__ == "__main__":
    main()