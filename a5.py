# Python Lab 5 Assignment
# Student name:- Sunny Kriplani
# Student Id:- 119220438


from email.parser import Parser
import os
PRINT_SIZE = 30
PATH = "/users/shared/enron"


# This function print all the emails sent from a particular user shared in
# dictionary from base path
def emails_from(suspects):
    print_num = PRINT_SIZE
    for susp in suspects.keys():
        file_lst = []
        susp_email = suspects[susp]
        # This create the path for each user suspected
        base_path = os.path.join(PATH, susp)
        if os.path.exists(base_path):
            # Retrieve all files inside as subdirectories are also included
            for root, dirs, files in os.walk(base_path):
                for file in files:
                    file_lst.append(os.path.join(root, file))
            for mail in file_lst:
                fp = open(mail)
                try:
                    e = Parser().parse(fp, headersonly=False)
                except:
                    print("Some error has occured")
                if (e["From"] in susp_email) and print_num:
                    print_num -= 1
                    to = (e["To"]).split(",")[0]
                    d = e["Date"].split(" ")
                    date = d[1] + " " + d[2] + " " + d[3]
                    print("[" + date + "] " + e["From"] + " -> " + to)
                    print("Subject " + e["Subject"])
