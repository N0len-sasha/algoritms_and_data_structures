def format_text(text):
    text = text.replace(",", ", ")
    words = text.split()
    max_word_length = max(len(word) for word in words)
    max_line_length = max_word_length * 3

    formatted_text = ""
    current_line = ""
    for word in words:
        if len(current_line) + len(word) <= max_line_length:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            formatted_text += current_line + "\n"
            current_line = word

    if current_line:
        formatted_text += current_line + "\n"

    formatted_text = formatted_text.replace(" ,", ",")

    return formatted_text


if __name__ == "__main__":
    text = input().strip()
    print(format_text(text))
