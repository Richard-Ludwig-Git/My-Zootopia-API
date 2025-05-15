import data_fetcher


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


def combine_data_template(user_animal_input):
    animals_data = data_fetcher.fetch_data(user_animal_input)
    template = load_template("animals_template.html")
    if len(animals_data) <= 2:
        output = f"<h2>The animal {user_animal_input} doesn't exist.</h2>"
        temp_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)
    if len(animals_data) > 2:
        output = ""
        for animal in animals_data:
            output += serialize_animal(animal)
        temp_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)
    return temp_with_data


def main():
    user_animal_input = input("Search for Animal: ")
    temp_with_data = combine_data_template(user_animal_input)
    with open(f"animal_repository_{user_animal_input}.html", "w") as makepage:
        makepage.write(temp_with_data)


if __name__ == "__main__":
    main()