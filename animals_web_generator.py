import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, encoding="UTF-8", errors="ignore") as handle:
        return json.load(handle)


def load_template(file_path):
    """ Loads a HTML Tamplate """
    with open(file_path, encoding="UTF-8", errors="ignore") as gettemp:
        return gettemp.read()


def serialize_animal(fox):
    """Serialization of the animal objects"""
    output = ""
    output += "<li class='cards__item'>\n"
    output += f"<div class='card__title'>{fox["name"]}<br/>\n</div><br/>"
    try:
        output += f"<div class='card__text'>\n <ul>\n<li><strong>Diet: </strong>{fox["characteristics"]["diet"]}</li>\n"
    except KeyError:
        pass
    try:
        output += f"<li><strong>Prey: </strong>{fox["characteristics"]["prey"]}</li>"
    except KeyError:
        pass
    output += "<li><strong>Location: </strong>"
    output += f" {", ".join(fox["locations"])}</li>\n"
    try:
        output += f"<li><strong>Type: </strong>{fox["characteristics"]["type"]}</li>\n"
    except KeyError:
        pass
    output += "</ul>"
    output += "</div>"
    output += "</li>"
    return output


def combine_data_template():
    animals_data = load_data("animals_data.json")
    template = load_template("animals_template.html")
    output = ""
    for fox in animals_data:
        output += serialize_animal(fox)
    temp_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)
    return temp_with_data


def main():
    temp_with_data = combine_data_template()
    with open("animals2.html", "w") as makepage:
        makepage.write(temp_with_data)


if __name__ == "__main__":
    main()