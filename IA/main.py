#!/usr/bin/env python3
import sys
import csv


class IA:
    def __init__(self):
        self.ironique = []
        self.none_ironique = []
        self.emoji = []
        self.pub = []
        self.uninterpretable = []
        self.count_words = []
        self.dict_word = []
        self.common_word = []

    def fill_tab_with_data(self):
        line = []

        if open(sys.argv[1], 'r'):
            file = open(sys.argv[1], 'r')
        csvreader = csv.reader(file)

        for line in csvreader:
            if line[1] == "1":
                self.ironique += [str(line[0])]
            if line[1] == "2":
                self.none_ironique += [line[0]]
            if line[1] == "3":
                self.emoji += [line[0]]
            if line[1] == "4":
                self.pub += [line[0]]
            if line[1] == "5":
                self.uninterpretable += [line[0]]

    def check_word_and_count(self):
        tmp = []
        status = False
        for x in self.ironique:
            words = x.split()
            for y in words:
                if len(self.dict_word) == 0:
                    tmp = [y, 1]
                    self.dict_word.append(tmp)
                    tmp = []
                    status = True
                else:
                    for z in range(len(self.dict_word)):
                        if y == self.dict_word[z][0]:
                            self.dict_word[z][1] += 1
                            status = True
                            break
                    if status == False:
                        tmp = [y, 1]
                        self.dict_word.append(tmp)
                        tmp = []
                status = False

    def clear_list_of_word(self):
        line = []
        status = False
        if open("list_of_common_word", 'r'):
            file = open("list_of_common_word", 'r')
        csvreader = csv.reader(file)
        for line in csvreader:
            for word in line:
                self.common_word.append(word)

        for x in range(len(self.dict_word)):
            for i in range(len(self.common_word)):
                if self.dict_word[x][0] == self.common_word[i]:
                    self.dict_word[x].clear()
                    break
                for j in range(len(self.common_word[i])):
                    upper_case = self.common_word[i][0].upper(
                    ) + self.common_word[i][1:len(self.common_word[i])]
                    if self.dict_word[x][0] == upper_case:
                        self.dict_word[x].clear()
                        status = True
                        break
                if status == True:
                    status = False
                    break

    def add_to_file(self):
        top = 0
        for i in range(len(self.dict_word)):
            if len(self.dict_word[i]) != 0 and top < int(self.dict_word[i][1]):
                top = int(self.dict_word[i][1])
        f = open("liste_des_mots_ironiques", "w")
        for i in range(len(self.dict_word)):
            if len(self.dict_word[i]) != 0 and int(self.dict_word[i][1]) > top / 2:
                print(self.dict_word[i][0])
                f.write(self.dict_word[i][0])
                f.write("\n")

    def parse_word(self):
        word = ""

        for line in range(len(self.ironique)):
            for c in range(len(self.ironique[line])):
                if self.ironique[line][c] == ' ' or c == len(self.ironique):
                    self.count_words.append(word)
                    word = ''
                else:
                    word += self.ironique[line][c]
            self.count_words.append(word)
            word = ''

    def core_programme(self):
        self.fill_tab_with_data()
        self.parse_word()
        self.check_word_and_count()
        self.clear_list_of_word()
        self.add_to_file()


if __name__ == '__main__':
    IA().core_programme()
