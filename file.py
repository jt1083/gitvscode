# st = open("st.txt","w")
# st.write("Hi from python!Nice to meet you!")
# st.close

# st = open("st.txt", "w", encoding="utf-8")
# st.write("Pythonからこんにちは")
# st.close

# with open("st.txt","r") as f:
#     # f.write("Hi from python!!")
#     print(f.read()) 

# import csv

# with open("st.csv","w",newline="")as f:
#     w = csv.writer(f, delimiter=",")
#     w.writerow(["one","two","three"])
#     w.writerow(["four","five","six"])

# answer = input("好きな色は？")
# with open("fav_color.txt","w") as f:
#     f.write(answer)

import csv

movies =  [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv","w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)