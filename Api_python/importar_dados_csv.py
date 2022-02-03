import csv
from mongo_connection import MongoDB
import sys
from datetime import datetime
import uuid

if len(sys.argv) > 1:
    arq = sys.argv[1]
    print(arq)
    with open(arq, 'r') as file:
        reader = csv.reader(file)
        cards = []
        db_obj1 = MongoDB("cards")
        db_obj2 = MongoDB("tags")
        for row in reader:

            card = {}
            card["texto"] = row[0]
            data = datetime.today().strftime('%Y-%m-%d %H:%M')
            card_id = str(uuid.uuid1())
            card["id"] = card_id
            card["data_criacao"] = data
            card["data_modificacao"] = data
            card["tags"] = []

            

            tags = row[1].split(";")
            for t in tags:
                tag = {}
                tag["nome"] = t
                temp = db_obj2.find_by_name(tag)
                if temp is None:
                    tag_id = str(uuid.uuid1())
                    tag["id"] = tag_id
                    db_obj2.insert(tag)
                else:
                    tag_id = temp["id"]

                card["tags"].append(tag_id)

            cards.append(card)
            print(row)
        db_obj1.bulk_insert(cards)
else:
    print("Passar caminho do arquivo como argumento")


