from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options = options
)

url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Hyderabad"
driver.get(url)
time.sleep(5)

listings = driver.find_elements(By.CLASS_NAME, "mb-srp__card")
data = []

for listing in listings:
    try:
        price = listing.find_element(By.CLASS_NAME,"mb-srp__card__price--amount").text
    except:
        price = None
    try:
        area = listing.find_element(By.CLASS_NAME,"mb-srp__card__summary--value").text
    except:
        area = None
    try:
        bhk = listing.find_element(By.CLASS_NAME,"mb-srp__card--title").text
    except:
        bhk = None
    try:
        location = listing.find_element(By.CLASS_NAME,"mb-srp__card--title").text
    except:
        location = None
    
    data.append({
        "Price": price,
        "Area": area,
        "BHK": bhk,
        "Location": location
    })

df = pd.DataFrame(data)
df.to_csv("magicbricks_raw.csv", index = False)
driver.quit()

df = pd.read_csv("magicbricks_raw.csv")

def convert_price_to_inr(price):
    price = price.replace("₹", "").replace("\n", "").strip()

    if "Cr" in price:
        value = float(price.replace("Cr", "").strip())
        return value * 10000000   # 1 Cr = 10,000,000

    elif "Lac" in price or "Lakh" in price:
        value = float(
            price.replace("Lac", "")
                 .replace("Lakh", "")
                 .strip()
        )
        return value * 100000     # 1 Lac = 100,000

    else:
        return None
df["Price_INR"] = df["Price"].apply(convert_price_to_inr)

df["Area_sqft"] = (
    df["Area"]
    .str.replace("sqft", "", regex=False)
    .str.strip()
    .astype(int)
)

df["BHK"] = df["BHK"].str.extract(r"(\d+)").astype(int)

df["Location"] = (
    df["Location"]
    .str.replace(r"\d+\sBHK\sFlat\sfor\sSale\sin\s", "", regex=True)
)

df[["Locality", "City"]] = df["Location"].str.rsplit(",", n=1, expand=True)

df["Locality"] = df["Locality"].str.strip()
df["City"] = df["City"].str.strip()

df["Price_per_SqFt"] = df["Price_INR"] / df["Area_sqft"]

df = df.drop(columns=["Price", "Area", "Location"])

df.to_csv("magicbricks_clean.csv", index=False)
