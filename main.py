import sys
from stats import get_num_words
from stats import sort_dict
from stats import get_char_count
def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
	return file_contents
def main():
	
	if len(sys.argv) != 2:
    		print("Usage: python3 main.py <path_to_book>")
    		sys.exit(1)
	book = get_book_text(sys.argv[1])
	book_characters = get_char_count(book)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}")
	print("----------- Word Count ----------")
	print(f"Found {get_num_words(book)} total words")
	print("--------- Character Count -------")
	book_characters = sort_dict(book_characters)
	for i in book_characters:
		ch = i["char"]
		if ch.isalpha():
			print(f"{ch}: {i['num']}")
	print("============= END ===============")
main()
