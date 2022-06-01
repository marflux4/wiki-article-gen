import webbrowser as web
from urllib.request import urlopen

def random_wiki_article():
    page = urlopen("https://en.wikipedia.org/wiki/Special:Random")
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    title_index = html.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html.find("</title>") - len(" - Wikipedia")

    title = html[start_index:end_index]

    want_to_read = input(f"Would you like to read a wikipedia article on {title}? (enter yes/no) ")

    while want_to_read != "yes" and want_to_read != "y" and want_to_read != "no" and want_to_read != "n":
        want_to_read = input("Please enter yes/no (or y/n) ")

    if want_to_read == "yes" or want_to_read == "y":
        web.open("https://en.wikipedia.org/wiki/" + title)
    elif want_to_read == "no" or want_to_read == "n":
        print("Oh okay, let me find another article for you...")
        random_wiki_article()

random_wiki_article()
