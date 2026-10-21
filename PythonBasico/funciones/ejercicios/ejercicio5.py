def count_capitals_text(text):
    if not isinstance(text, str):
        raise TypeError("text debe ser un string")
    capital_count = 0
    lower_count = 0
    for character in text:
        if character.isupper():
            capital_count += 1
        elif character.islower():
            lower_count += 1
    return capital_count, lower_count

def format_capitals_message(capital_count, lower_count):
    return f"There's {capital_count} upper cases and {lower_count} lower cases"

print(count_capitals_text("I love Nación Sushi"))
print(count_capitals_text("There’s 3 upper cases and 13 lower cases"))