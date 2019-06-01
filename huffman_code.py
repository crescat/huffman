from collections import Counter

def add_item(queue, item):
    return sorted(queue+[item], key = lambda x:x[0])


def make_tree(doc):
    counts = Counter(doc)
    queue = []
    for byte, freq in counts.items():
        queue = add_item(queue, (freq, byte))
    while len(queue) >= 2:
        f1, b1 = queue[0]
        f2, b2 = queue[1]
        queue = add_item(queue[2:], (f1+f2, (b1, b2)))
    return queue[0][1]


def tree_to_table(tree):
    if type(tree) is int:
        return [([], tree)]
    elif type(tree) is tuple:
        left = tree_to_table(tree[0])
        right = tree_to_table(tree[1])
        return [([0]+num, char) for num, char in left] +\
               [([1]+num, char) for num, char in right]


def encode(doc):
    tree = make_tree(doc)
    table = tree_to_table(tree)
    dic = {char:code for code, char in table}
    result = []
    for char in doc:
        result += dic[char]
    return result


def decode(tree, encoded_doc):
    cursor = tree
    result = ''
    for x in encoded_doc:
        cursor = cursor[x]

        if type(cursor) is int:
            result += cursor
            cursor = tree

    return result
