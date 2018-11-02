#https://www.codewars.com/kata/decode-the-morse-code

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
	morseCodeList = morse_code.split(' ')
	plainText = []
	for i in range(len(morseCodeList)):
		if morseCodeList[i] == '':
			if morseCodeList[i] == morseCodeList[i - 1]:
				continue
			plainText.append(' ')
		else:
			plainText.append(MORSE_CODE[morseCodeList[i]])
	return ''.join(plainText).strip()
