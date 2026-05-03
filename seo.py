from the_scarper import jumuia_scrapper, kilimall_scrapper
from urllib.parse import quote_plus
from main import summarize_text_given
def master_app():
    user = input("what are you looking for today? ")
    clean_user = quote_plus(user)
    print(jumuia_scrapper(clean_user))
    print(kilimall_scrapper(clean_user))
    print(summarize_text_given())
master_app()