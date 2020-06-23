# Python lab assignment 3
# AuthorL: Sunny Kriplani
# Student ID: 119220438


# This program prints the possible match of two persons from a marriage
# record data
import re


f1 = open("mary_roche.txt")
f2 = open("nicholas.txt")
mary = f1.read()
nicho = f2.read()
mary_l = re.split("Marriage of ", mary)
nicho_l = re.split("Marriage of ", nicho)
# Remove the first list element as it is splitted on "Marriage of" so 1st
# element will always be empty of not required text
mary_l.remove(mary_l[0])
nicho_l.remove(nicho_l[0])

# Regex to fetch the year, quarter, location, page and Volume from a user data
regex_yr = re.compile(r"Returns Year.*")
regex_qtr = re.compile(r"Returns Quarter.*")
regex_loc = re.compile(r"SR District/Reg Area.*")
regex_pg = re.compile(r"Returns Page No.*")
regex_vol = re.compile(r"Returns Volume No.*")

for i in mary_l:
    yr_m = regex_yr.search(i).group().split("\t")[1]
    qtr_m = regex_qtr.search(i).group().split("\t")[1]
    loc_m = regex_loc.search(i).group().split("\t")[1]
    page_m = regex_pg.search(i).group().split("\t")[1]
    vol_m = regex_vol.search(i).group().split("\t")[1]
    for j in nicho_l:
        yr_n = regex_yr.search(j).group().split("\t")[1]
        qtr_n = regex_qtr.search(j).group().split("\t")[1]
        loc_n = regex_loc.search(j).group().split("\t")[1]
        page_n = regex_pg.search(j).group().split("\t")[1]
        vol_n = regex_vol.search(j).group().split("\t")[1]
        # Two persons are marriad if their location, volume, page, quarter
        # and year of marriage record matches
        if(yr_m == yr_n and qtr_m == qtr_n and page_m == page_n and
           loc_m == loc_n and vol_m == vol_n):
            print()
            bride = i.split("\n")[0]
            groom = j.split("\n")[0]
            print("Possible Match!")
            print(groom + " and " + bride + " in " + loc_m + " in " + yr_m)
            print("Quarter = " + qtr_m + ", Volume = " + vol_m + ", Page = "
                  + page_m)
