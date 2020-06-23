# Python Lab 4 Assignment
# Student name: Sunny Kriplani
# Sudent Number: 119220438

from docx import Document
import re
import pyexcel as pe


# This function takes a word file and counts the frequency of words storing
# them in a spreadsheet
def analyze(file):
    doc = Document(file)
    final = []
    freq = {}
    regex = re.compile(r'(?=\[a-zA-Z0-9]*[\'-])?([a-zA-Z0-9\'-]+)')
    # Reading all paragraphs and storing them into a list
    for para in doc.paragraphs:
        words = regex.findall(para.text.lower())
        for word in words:
            final.append(word)
    # frequency of each word is added into dictionary
    for word in final:
        count = freq.get(word, 0)
        freq[word] = count + 1
    wrd_cnt = len(final)
    final.clear()
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # Words with only frequency 0.001 or higher has to be added to excel file
    for i in freq:
        val = i[1]
        if (val/wrd_cnt) >= 0.001:
            val = round(val/wrd_cnt, 3)
            final.append([i[0], val])
    FILENAME = file.split(".")[0] + "_word_stats"+".xlsx"
    pe.save_as(array=[], dest_file_name=FILENAME)
    book = pe.get_book(file_name=FILENAME)
    sheet = book[book.sheet_names()[0]]
    for l in final:
        data = l
        sheet.row += data
    sheet.name = 'Word Frequency Stats'
    book.save_as(FILENAME)
