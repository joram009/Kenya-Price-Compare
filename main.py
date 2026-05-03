import ollama
from h11 import RemoteProtocolError
from ollama import ResponseError
from ollama import chat
from config import config_file_path
def summarize_text_given():
    with (open(config_file_path(), 'r', encoding="utf-8") as content):
        data = content.read()
        if data.strip() != "":
            message_1 = f"""

                    You are a helpful shopping assistant specialized in price analysis.

                    Here is scraped product data from Shopping Websites in kenya for  items and Products . Each product block :
                    {data.strip()}
                    ---
                    Task:
                    1. Extract every product with its name and current price (in KSh) and use the title of the website name at the begining of said item. Ignore irrelevant items.
                    2. Convert all prices to numbers (remove "KSh", commas, etc.). If a price range is shown (e.g. KSh 100 - 150), use the lowest price.
                    3. List the top 10 cheapest products with their name and price.
                    4. Calculate and show a simple price summary:
                       - Lowest price overall
                       - Highest price overall
                       - Average price (approximate is fine)
                    5. Identify the **best value for money** products. Best value means:
                       - Good quality for the price (e.g. editors choice , best verified, Best seller )
                       - Or clearly cheaper than similar products
                       - Look for bulk packs, big sizes, or heavy discounts

                    Output format exactly like this:

                    **PRICE SUMMARY**
                    - Total products found: X
                    - Lowest price: KSh XXX
                    - Highest price: KSh XXX
                    - Average price: KSh XXX

                    **TOP 10 CHEAPEST PRODUCTS**
                    1. [Site] - Product name - KSh XXX
                    2. ...

                    **BEST VALUE RECOMMENDATIONS**
                    1. Best overall value: [Site] - [Product name] - Reason: [short reason, e.g. "biggest pack for lowest price per kg"]
                    2. Best value recommendation: Best overall value: [Site] - [Product name] - KSh XXX Reason: ...
                    3. ...
                    
                    **WHERE TO BUY**
                    - Best site for this search: [Site name]
                    - Reason: [cheapest overall / most products found / best variety]
                    
                    Be concise and accurate. If price information is missing for a product, skip it.
                  """
            try:
                print(" Analyzing Data .... Please Wait ...")
                for chunk in chat(
                        model="phi3:mini",
                        stream=True,
                        messages=[{"role": "user", "content": message_1}], ):
                    print(chunk.message.content, end="", flush=True)
            except UnboundLocalError:
                print("can't accsess the local variable")
            except RemoteProtocolError:
                print("There was a Remote Protocal Error The server has Been Disconnected")
            except ollama.RequestError:
                print("Do You Have The 'phi3:mini model' ... Install and Try Again")
            except AttributeError:
                print("The Attribute Doen't Exist ... Sorry")
