from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    result_words = []

    for line in lines:
        unique_words =[]
        seen = set()

        for word in line.split():
            if word not in seen:
                unique_words.append(word)
                seen.add(word)
        if word_number < len(unique_words):
            result_words.append(unique_words[word_number])
    return ' '.join(result_words)

print(build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1))
