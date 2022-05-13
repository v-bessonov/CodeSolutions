from SlidingWindowBestTimeToBuySellStock import SlidingWindowBestTimeToBuySellStock
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


def sliding_window_best_time_to_buy_sell_stock_test():
    profit = SlidingWindowBestTimeToBuySellStock.max_profit([7, 1, 5, 3, 6, 4])
    print(f'SlidingWindowBestTimeToBuySellStock max profit {profit}')


if __name__ == '__main__':
    # print_hi('PyCharm')
    sliding_window_best_time_to_buy_sell_stock_test()
    trie_test()

