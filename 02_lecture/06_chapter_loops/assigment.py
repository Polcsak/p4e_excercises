text = "X-DSPAM-Confidence:    0.8475"
letter = text.find('0')
print(letter)
extracted_text = float(text[letter: letter + 7])
print(extracted_text)
format_text = format(extracted_text)
print(format_text)
