from bitarray import bitarray

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class TrieBloomFilter:
    def __init__(self, capacity):
        self.root = TrieNode()
        self.capacity = capacity
        self.bloom_filter = bitarray(capacity)
        self.bloom_filter.setall(False)

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

        # Set the corresponding bits in the bloom filter
        self.bloom_filter[self.get_hash(word)] = True

    def delete(self, word):
        node = self.root
        parent = None
        for char in word:
            if char not in node.children:
                return 0# Word not found
            parent = node
            node = node.children[char]

        if not node.is_end_of_word:
            return 0# Word not found

        # Check if the word is really present using the bloom filter
        if not self.bloom_filter[self.get_hash(word)]:
            return 0# Word not found

        # Delete the word from the trie
        node.is_end_of_word = False

        # Remove any unused nodes from the trie
        self._remove_unused_nodes(parent, word)

    def _remove_unused_nodes(self, parent, word):
        if not parent:
            return 0

        if len(parent.children) == 1 and not parent.is_end_of_word:
            char = word[len(parent.children)]
            if char in parent.children:
                del parent.children[char]
                self._remove_unused_nodes(parent, word)

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def get_hash(self, word):
        return hash(word) % self.capacity

    def display(self):
        words = []
        self._traverse(self.root, "", words)
        for word in words:
            print(word)

    def _traverse(self, node, current_word, words):
        if node.is_end_of_word:
            words.append(current_word)

        for char, child in node.children.items():
            self._traverse(child, current_word + char, words)


q=1 #exit condition
while(q>0):
    qwe=0
    x=int(input("Enter the required size of the Tri Bloom Filter :  "))
    trie=TrieBloomFilter(x)
    n=int(input("Enter the total number of elements you want to enter inside the Trie Bloom Filter : "))


    while(x>n):
        k=0
        while(k<n):
            data=input("Enter data item to be inserted : ")
            if(data.isalpha()==True):
                trie.insert(data)
                k=k+1
            else:
                print("Only strings are accepted")
                k=k-1
                n=n-1



        p=2
        while(p>1):
            print("Enter 1 to insert data")
            print("Enter 2 to delete data")
            print("Enter 3 to search data")
            print("Enter 4 to display the data in the Trie Bloom Filter")
            print("Enter 5 to EXIT")

            choice=int(input("Enter your choice : "))
            while(choice==1 or choice==2 or choice==3 or choice==4 or choice==5):
                if (choice==1):
                    n=int(input("Enter the number of elements you want to enter inside the Trie Bloom Filter : "))
                    k=0
                    while(k<n):
                        data=input("Enter data item to be inserted : ")
                        if(data.isalpha()==True):
                            trie.insert(data)
                            k=k+1
                        else:
                            print("Only strings are accepted")
                            k=k-1
                            n=n-1
                    break
                elif (choice==2):
                    data=input("Enter data item to be deleted : ")
                    if(trie.search(data)==False):
                        print("Enter Correct data item or the item present in the data structure")
                    elif(trie.search(data)==True):
                        trie.delete(data)
                        print("Successfully deleted "+data+" from the data structure")
                    break
                elif (choice==3):
                    data=input("Enter data item to be searched : ")
                    print(trie.search(data))
                    break
                elif(choice==4):
                    print("The list of items in the Trie Bloom Filter is : ")
                    trie.display()
                    break
                elif (choice==5):
                    p=0
                    qwe=1
                    break
                break
        else:
            print("EXIT SUCCESSFUL")
        if qwe==1:
            break
    

    else:
        print("Enter the number of items to be inputted less than the trie bloom's capacity")
    if qwe==1:
        break
    

else:
    q=q+1