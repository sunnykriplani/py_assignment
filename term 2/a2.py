# Lab 2 assignment Python
# Autho: Sunny Kriplani
# Student number : 119220438

import re


# This function finds all the strings containing EUR amount specified in a
# specific format

def moolah(text):
    regexp = re.compile(r'EUR\s?\d+(\.\d+)?')
    lst = []
    for m in regexp.finditer(text):
        lst.append(m.group())
    return lst


# This functoin bleeps all 4-letter words and replace them with ****
def bleep(text):
    regex = re.compile(r"\b[a-zA-Z]{4}\b")
    text = regex.sub('****', text)
    return text


# This function finds digits in a string and adds english words to it
def to_english(text):
    regex = re.compile(r"\d+\ ?")
    lst = ["zero", "one", "two", "three", "four", "five", "six", "seven",
           "eight", "nine"]
    values = regex.findall(text)
    values = [x.strip(' ') for x in values]
    val = []
    for i in values:
        if i not in val:
            val.append(i)
    for m in val:
        eng = ""
        reg = re.compile(r"\d")
        eng = m + " "
        eng += "("
        for n in reg.finditer(str(m)):
            eng += lst[int(n.group())]
            eng += " "
        eng = eng[:-1]
        eng += ")"
        pattern = re.compile(r'\b%s\b' % m)
        text = re.sub(pattern, eng, text)
    return text


# This function finds all the emails address in a given string
def harvest_emails(text):
    regexp = re.compile(r'[\w.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    lst = regexp.findall(text)
    emails = []
    for m in lst:
        lst = re.split(r"\@", m)
        local = lst[0]
        domain = lst[1]
        if (local[0] != "." and local[-1] != "." and (local.find("..") < 0)
                        and local.find("-") < 0):
            if(domain[0] != "-" and domain[-1] != "-"):
                emails.append(m)
    # To sort the emails based on the local and domain names
    emails = sorted(emails, key=lambda x: (x.split("@", 1)[::-1], x))
    if len(emails) == 0:
        return None
    else:
        return emails
