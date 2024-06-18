def remove_duplicated_words(line: str) -> str:
    words=line.split()
    seen=set()
    result=[]

    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)

print(remove_duplicated_words('cat cat dog 1 dog 2'))