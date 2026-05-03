from config import config_file_path
from bs4 import BeautifulSoup
import requests
def jumuia_scrapper(search_here):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            request_from = requests.get(f"https://www.jumia.co.ke/catalog/?q={search_here}", headers=headers)
            request_from.raise_for_status()
            soup = BeautifulSoup(request_from.text, "html.parser")
            product_name = soup.find_all("h3", class_="name")
            price = soup.find_all("div", class_="prc")
            contents = zip(product_name, price)
            file_path = config_file_path()
            with open(file_path, "w", encoding="utf-8") as websites_path:
                websites_path.write("\nJumuia Product and Prices\n")
                for product_name, price in contents:
                    websites_path.write(f"\n{product_name.text}-{price.text}")
                return "Done Scrapping Products from Jumuia"
        except requests.exceptions.ConnectionError:
            print("Bro The Internet ¯_(ツ)_/¯")
        except requests.exceptions.Timeout:
            print("The Connection Has Timed out!")
        except requests.exceptions.HTTPError:
            print("Just A HttpError Nothing Big ")
def kilimall_scrapper(search_here):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        request_from = requests.get(f"https://www.kilimall.co.ke/search?q={search_here}&page=1&source=search|enterSearch|{search_here}", headers=headers)
        request_from.raise_for_status()
        soup = BeautifulSoup(request_from.text, "html.parser")
        pro_name = soup.find_all("p", class_="product-title")
        price_of_pro = soup.find_all("div", class_="product-price")
        content = zip(pro_name, price_of_pro)
        file_path = config_file_path()
        with open(file_path, "a", encoding="utf-8") as website_path:
            website_path.write("\nKilimall Products and Prices \n"  )
            for pro_name, price_of_pro in content:
                website_path.write(f"\n{pro_name.text}-{price_of_pro.text}\n")
            return "done scrapping kilimall Products"
    except requests.exceptions.ConnectionError:
        print("Bro The Internet ¯_(ツ)_/¯")
    except requests.exceptions.Timeout:
            print("The Connection Has Timed out!")
    except requests.exceptions.HTTPError:
            print("Just A HttpError Nothing Big ")


