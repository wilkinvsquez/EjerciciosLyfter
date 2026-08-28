def count_capitals_text(text):
    capital_count = 0
    lower_count = 0
    for index in range(len(text)):
        if text[index].isupper():
            capital_count += 1
        else:
            lower_count += 1
    return f"There's {capital_count} upper cases and {lower_count} lower cases"

print(count_capitals_text("I love Nación Sushi"))
print(count_capitals_text("There’s 3 upper cases and 13 lower cases"))