items_in_stock = [

    {"item_id": 0,
    "item_name": "Adana Dürüm",
    'item_price': 50,
    },
    {"item_id": 1,
    "item_name": "İce Tea",
    'item_price': 10,
    },
    {"item_id": 2,
    "item_name": "Piskevit",
    "item_price": 15,
    },
    {"item_id": 3,
    "item_name": "Muzlu Süt",
    "item_price": 35,
},
{
    "item_id": 4,
    "item_name": "Bici Bici",
    "item_price": 40,
},
]

the_item = []

reciept = """
\t\tÜrünler -- Fiyat
"""
sun = 0
run = True

print("----------Kerem Otomat----------\n\n")
print("----------Stoktaki Ürünler----------\n\n")

for i in items_in_stock:
    print(f"Ürün:{i['item_name']} --- Fiyat:{i['item_price']} --- Ürün No: {i['item_id']}")

def machine(items_in_stock, run, the_item):
    while run:
        buy_item = int(input("\n\nSatın almak istediğiniz ürünün kodunu girin: "))

        if buy_item < len(items_in_stock):
            the_item.append(items_in_stock[buy_item])
        else:
            print("YANLIŞ ÜRÜN IDI!")
        more_items = str(input("daha fazla öge eklemek için 1 tuşa basın veya  çıkmak için 0 tuşuna basın.. "))
      
        if more_items == "1":
            run = False

        if more_items == "0":
            run = False

    rec_bool = int(input(("1. Fişinizi yazdırn 2. alnızca toplam tutarı yazdırın.. ")))
    if rec_bool == 1:
        print(create_reciept(the_item, reciept))
    elif rec_bool ==2:
        print(sum(the_item))
    else:
        print("GEÇERSİZ GİRİŞ")

def sum(the_item):
    sum = 0

    for i in the_item:
        sum += i["item_price"]
    
    return sum

def create_reciept(the_item, reciept):
    for i in the_item:
        reciept += f"""
        \t{i["item_name"]} -- {i['item_price']}
        """
    
    reciept += f"""
    \tTotal --- {sum(the_item)}

     """
     
    return reciept

if __name__ == "__main__":
    machine(items_in_stock, run, the_item)
