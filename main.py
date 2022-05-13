from Trie import Trie
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def trie_test():
    trie = Trie()
    word1 = "apple"
    word2 = "ape"
    word3 = "bus"
    trie.insert(word1)
    trie.insert(word2)
    print(f'search {word1} {trie.search(word1)}')
    print(f'search {word1} {trie.search(word3)}')
    print(f'starts_with app {trie.starts_with("app")}')
    print(f'starts_with xx {trie.starts_with("xx")}')


if __name__ == '__main__':
    # print_hi('PyCharm')
    trie_test()

