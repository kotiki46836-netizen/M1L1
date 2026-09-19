meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            }
print('Czesc!To program do melenialów')
for i in range(5):
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ").upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('nic')
        
