import random

def get_image():
    file = open("manga_covers.txt", "r")
    URL_list = []
    for line in file.readlines():
        URL_list.append(line.strip())
    file.close()
    rand_val = random.randint(0, len(URL_list)-1)
    manga_URL = URL_list[rand_val]

    file = open("URL.txt", "w")
    file.write(manga_URL)