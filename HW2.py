'''
Question 1: 5 points

Queue
A queue follows FIFO (first-in, first-out). FIFO is the case where the
first element added is the first element that can be retrieved. Consider
a list with values [2, 5, 3, 6]. Create a class called MyQueue that will have
two methods: queueadd and queueretrieve to add and pop elements
from the list in FIFO order respectively. After each function call,
print the contents of the list. Add 7 to the queue and then follow the
FIFO rules to pop elements until the list is empty.

Your call to the class will be as follows
a = [2, 5, 3, 6]
q = MyQueue(a)
q.queueadd(7)
q.queueretrieve()

The output on the screen should similar to
5 3 6 7
3 6 7
6 7
7
'''
class MyQueue:
    def __init__(self, head = None):
        self.storage = head

    def queueadd(self, v):
        self.storage.append(v)


    def queueretrieve(self):
        while self.storage:
            ret = self.storage
            self.storage = self.storage[1:]
            print(' '.join(str(x) for x in ret))


sol = MyQueue()
a = [2, 5, 3, 6]
q = MyQueue(a)
q.queueadd(7)
q.queueretrieve()


'''
Question 2: 5 points

Please ensure that you use space instead of tab for indentation. 
Then paste your code directly into the response box.

Write a program that will read the file, 
'red-headed-league.txt', count the frequency of the words and store 
it as a csv file.

Create a class called WordCounter with the following methods.

def __init__(self,filename) where filename is the name of the text file, 
'red-headed-league.txt'. This function should read the text file

def removepunctuation(self) must remove all the punctuations and leave 
only alphabets and numbers in each word

def findcount(self) must count the frequency of each word and store it 
in a instance variable called countdict

def writecountfile(self,csvfilename) writes the content of the countdict 
variable to a csv file with two columns. The first column is the word 
and second column is the count.

Create an instance of the class and call appropriate method
and store the result in a csv file. Printout the five most popular words. 
NOTE: DO NOT USE THE COUNTER DATA STRUCTURE IN COLLECTIONS MODULE.
'''
import operator
import string


class WordCounter:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.origin_lines = f.readlines()

    def remove_punctuation(self):
        self.revised_lines = map(lambda line: line.translate(str.maketrans('', '', string.punctuation)),
                                 self.origin_lines)

    def find_count(self):
        self.count_dict = dict()
        for line in self.revised_lines:
            for w in line.strip().split():
                if w not in self.count_dict:
                    self.count_dict[w] = 0
                self.count_dict[w] += 1

    def write_count_file(self, filename):
        with open(filename, 'w') as f:
            for w, cnt in self.count_dict.items():
                f.write('{WORD}, {COUNT}\n'.format(WORD=w, COUNT=cnt))


def main():
    word_counter = WordCounter(filename='red-headed-league.txt')
    word_counter.remove_punctuation()
    word_counter.find_count()
    word_counter.write_count_file(filename='count_word.csv')

    sorted_res = sorted(word_counter.count_dict.items(), key=operator.itemgetter(1), reverse=True)
    for w, cnt in sorted_res[:5]:
        print('{WORD}, {COUNT}'.format(WORD=w, COUNT=cnt))


if __name__ == '__main__':
    main()

