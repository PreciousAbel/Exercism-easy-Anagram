def find_anagrams(word, candidates):
    sorted_target = sorted(word.lower())
    return [candidate for candidate in candidates if sorted(candidate.lower()) == sorted_target and candidate.lower() != word.lower()]
