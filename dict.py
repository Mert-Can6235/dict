meme_dict = {
             "CRINGE": "Garip ya da utandırıcı bir şey",
             "LOL": "Komik bir şeye verilen cevap",
             "NPC": "İng. Not Player Character   Tur. Oyuncu olmayan karakter",
             "AFK": "Donmuş Oyuncu",
             "TROLL": "Hile yapan oyuncu"
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Kelime bulunamadı")
