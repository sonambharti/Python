"""
# Q1. Find the K-th Character in String Game I

"""


def kthCharacter(k):
    word = ["a"]

    while len(word) < k :
        nxt = []
        for c in word:
            nxt.append(chr((ord(c) - ord('a') + 1) % 26 + ord('a')))
        word.extend(nxt)
    return word[k-1]
    
if __name__ == "__main__":
    k = 7
    res = kthCharacter(k)
    print("the K-th Character in String Game I: ", res)
