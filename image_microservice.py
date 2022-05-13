import random

while True:
    file = open("instructions.txt", "r")
    if file.readline().strip() == "run":

        # Delete contents in instructions.txt so that new URLs are not generated nonstop
        file = open("instructions.txt", "w")
        file.write("")
        file.close()  

        # Read txt file that contains cover URLs and convert to a list of URLs
        file = open("./manga_covers.txt", "r")
        URL_list = []
        for line in file.readlines():
            URL_list.append(line.strip())
        file.close()

        # Generated a pseudo-random number and use as index number to retrieve URL at that index
        rand_val = random.randint(0, len(URL_list)-1)
        manga_URL = URL_list[rand_val]

        # Write URL to txt file
        file = open("URL.txt", "w")
        file.write(manga_URL)
        file.close()
        
    else:
        file.close()