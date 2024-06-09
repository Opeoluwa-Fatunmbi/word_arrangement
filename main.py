import itertools

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = set(line.strip().lower() for line in file)
    return words

def find_combinations(words_set):
    found_words = set()
    all_combinations = set()
    
    for word in words_set:
        for i in range(1, len(word) + 1):
            for combo in itertools.permutations(word, i):
                combo_word = ''.join(combo)
                all_combinations.add(combo_word)
                if combo_word in words_set:
                    found_words.add(combo_word)
    
    return all_combinations, found_words

def main():
    words_file = 'words.txt'
    words_set = load_words(words_file)
    
    all_combinations, found_words = find_combinations(words_set)
    
    print(f"{len(all_combinations)} combinations found")
    print(f"{len(found_words)} words found")
    print("Words found in the file that can be formed with input letters:")
    for word in sorted(found_words):
        print(word)

if __name__ == "__main__":
    main()
