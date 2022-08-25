sentence = input("enter your sentence:")
word = input("enter your word:")


def get_sentence(sentence):
    is_valid = True
    split_sentence = sentence.split(" ")
    if len(split_sentence) < 4 or not sentence.endswith("."):
        is_valid = False

        return is_valid


def find_word(sentence, word):
    is_exact = False
    is_approx = False
    split_sentence = sentence.split(" ")
    word_char = word[0:2]
    if word in split_sentence:
        is_exact = True
    if not is_exact:
        if word_char in split_sentence[0]:
            is_approx = True
    return {"is_exact": is_exact, "is_approx": is_approx}


result = find_word(sentence, word)
if result["is_exact"]:
    print("the word was found in sentence")
elif result["is_approx"]:
    print("the word was not found in sentence")
