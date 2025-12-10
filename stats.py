def get_num_words(text):
        count = 0
        for word in text.split():
                count += 1
        return count
def get_char_count(text):
	dictionary = {}
	for character in text:
		current = character.lower()
		if current in dictionary:
			dictionary[current] += 1
		else:
			dictionary[current] = 1
	return dictionary
def sort_on(tiny_dict):
        return tiny_dict["num"]
def sort_dict(char_count):
	seperated_dict = []
	for index in char_count:
		small_dict =  {"char": index, "num":char_count[index]}
		seperated_dict.append(small_dict)
	seperated_dict.sort(reverse=True, key=sort_on)
	return seperated_dict

