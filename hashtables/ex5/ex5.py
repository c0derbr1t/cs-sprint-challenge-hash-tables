# Your code here
cache = {}

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    for file in files:
        file_split = file.split("/")
        if file_split[-1] in cache:
            cache[file_split[-1]].append(file)
        else:
            cache[file_split[-1]] = [file]

    results = []

    for query in queries:
        if query in cache:
            for item in cache[query]:
                results.append(item)

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/usr/bar/foo'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
