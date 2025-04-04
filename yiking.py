from pynput import keyboard
import threading
import random

Draw = False
End_Program = False

def on_press(key):
    global Draw
    try:
        Draw = True
    except AttributeError:
        print(f"Key pressed: {key}")

def on_release(key):
    global End_Program
    if key == keyboard.Key.esc:
    # Stop listener
        End_Program = True
        return False

def listen_for_keypresses():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

thread = threading.Thread(target=listen_for_keypresses)
thread.daemon = True  # Allow the program to exit even if the thread is still running
thread.start()

hexagrams_dict = {
    0b000000: "1- K'ien - Le Créateur - Heaven",
    0b111111: "2- K'ouen - Le Réceptif - Earth over Earth",
    0b011101: "3 - Tchouen' - La difficulté initiale - Water over Thunder",
    0b101110: "4 - Mong - La folie Juvénile - Mountain over Water",
    0b000101: "5 - Su - L'Attente / La Nutrition - Water over Heaven",
    0b101000: "6 - Soung - Le Conflit - Heaven over Water",
    0b101111: "7 - Sze -L'Armée - Earth over Water",
    0b111101: "8 - Pi - La solidarité / L'union - Water over Earth",
    0b000100: "9 - Siao Tch'ou - Le pouvoir d'apprivoisement du petit - Wind over Heaven",
    0b001000: "10 - Liu - La Marche - Heaven over Lake",
    0b000111: "11 - T'ai - La Paix - Earth over Heaven",
    0b111000: "12 - P'i - La stagnation / L'immobilité - Heaven over Earth",
    0b010000: "13 - T'ong jen - Communauté avec les hommes - Heaven over Fire",
    0b000010: "14 - Ta Yéou - Le grand avoir - Fire over Heaven",
    0b110111: "15 - K'ien - L'humilité - Earth over Mountain",
    0b111011: "16 - Yu - L'enthousiasme - Thunder over Earth",
    0b011001: "17 - Souei - La Suite - Lake over Thunder",
    0b100110: "18 - Kou - Le travail sur ce qui est corrompu - Mountain over Wind",
    0b001111: "19 - Lin - L'approche - Earth over Lake",
    0b111100: "20 - Kouan - La contemplation - Wind over Earth",
    0b011010: "21 - Che Ho - Mordre au travers - Fire over Thunder",
    0b010110: "22 - Pi - La grâce - Mountain over Fire",
    0b111110: "23 - Po - L'éclatement - Mountain over Earth",
    0b011111: "24 - Fou - Le retour (Le Tournant) - Earth over Thunder",
    0b011000: "25 - Wou Wang - L'innocence (L'inatendu) - Heaven over Thunder",
    0b000110: "26 - Ta Tch'ou - Le pouvoir d'apprivoisement du grand - Mountain over Heaven",
    0b011110: "27 - Yi - Les commissures des lèvres (L'administration de la nourriture) - Mountain over Thunder",
    0b100001: "28 - Ta Kouo - La préponderance du grand - Lake over Wood",
    0b101101: "29 - K'an - L'insondable, l'eau - Water over Water",
    0b010010: "30 - Li - Ce qui s'attache, le feu - Fire over Fire",
    0b110001: "31 - Hien - L'influence (La demande en mariage) - Lake over Mountain",
    0b100011: "32 - Hong - La Durée - Thunder over wind",
    0b110000: "33 - Touen - La Retraite - Heaven over Mountain",
    0b000011: "34 - Ta Tchouang - La puissance du grand - Thunder over Heaven",
    0b111010: "35 - Tsin - Le Progrès - Fire over Earth",
    0b010111: "36 - Ming YI - L'obcurcissement de la lumière - Earth over Fire",
    0b010100: "37 - Kia Jen - La Famille (Le Clan) - Wind over Fire",
    0b001010: "38 - K'ouei - L'opposition - Fire over Lake",
    0b110101: "39 - Kien - L'obstacle - Water over Mountain",
    0b101011: "40 - Hiai - La Libération - Thunder over Water",
    0b001110: "41 - Souen - La Diminution - Mountain over Lake",
    0b011100: "42 - Yi - L'Augmentation - Wind over Thunder",
    0b000001: "43 - Kouai - La percée (La résolution) - Lake over Heaven",
    0b100000: "44 - Keou - Venir à la rencontre - Heaven over Wind",
    0b111001: "45 - Ts'ouei - Le Rassemblement (Le Recueillement) - Lake over Earth",
    0b100111: "46 - Cheng - La Poussée vers le haut - Earth over Wood",
    0b101001: "47 - K'ouen - L'accablement (L'Épuisement) - Lake over Water",
    0b100101: "48 - Tsing - Le Puit - Water over Wood",
    0b010001: "49 - Ko - La Révolution, la mue - Lake over Fire",
    0b100010: "50 - Ting - Le Chaudron - Fire over Wood",
    0b011011: "51 - Tchen - L'Éveilleur, L'Ébranlement - Thunder over Thunder",
    0b110110: "52 - Ken - L'immobilisation - Mountain over Mountain",
    0b110100: "53 - Tsien - Le Développement (Le progrès graduel) - Wood over Mountain",
    0b001011: "54 - Kouei Mei - L'Épousée - Thunder over Lake",
    0b010011: "55 - Fong - L'Abondance, La Plénitude - Thunder over Fire",
    0b110010: "56 - Liu - Le Voyageur - Fire over Mountain",
    0b100100: "57 - Souen - Le doux (Le pénétrant, le vent) - Wood over Wood",
    0b001001: "58 - Touei - Le Serein, Le Joyeux - Lake over Lake",
    0b101100: "59 - Houan - La dissolution (La Dispersion) - Wind over Water",
    0b001101: "60 - Tsie - La Limitation - Water over Lake",
    0b001100: "61 - Tchoung Fou - La vérité intérieure - Wind over Lake",
    0b110011: "62 - Siao Kouo - La prépondérance du petit - Thunder over Mountain",
    0b010101: "63 - Ki Tsi - Après L'Accomplissment - Water over Fire",
    0b101010: "64 - Wei Tsi - Avant L'Accomplissment - Fire over Water",
}

Le_Livre_Des_Transformations_KEYS = {
    0b000000: 0,
    0b111111: 63,
    0b011101: 29,
    0b101110: 46,
    0b000101: 5,
    0b101000: 40,
    0b101111: 47,
    0b111101: 61,
    0b000100: 4,
    0b001000: 8,
    0b000111: 7,
    0b111000: 56,
    0b010000: 16,
    0b000010: 2,
    0b110111: 55,
    0b111011: 59,
    0b011001: 25,
    0b100110: 38,
    0b001111: 15,
    0b111100: 60,
    0b011010: 26,
    0b010110: 22,
    0b111110: 62,
    0b011111: 31,
    0b011000: 24,
    0b000110: 6,
    0b011110: 30,
    0b100001: 33,
    0b101101: 45,
    0b010010: 18,
    0b110001: 49,
    0b100011: 35,
    0b110000: 48,
    0b000011: 3,
    0b111010: 58,
    0b010111: 23,
    0b010100: 20,
    0b001010: 10,
    0b110101: 53,
    0b101011: 43,
    0b001110: 14,
    0b011100: 28,
    0b000001: 1,
    0b100000: 32,
    0b111001: 57,
    0b100111: 39,
    0b101001: 41,
    0b100101: 37,
    0b010001: 17,
    0b100010: 34,
    0b011011: 27,
    0b110110: 54,
    0b110100: 52,
    0b001011: 11,
    0b010011: 19,
    0b110010: 50,
    0b100100: 36,
    0b001001: 9,
    0b101100: 44,
    0b001101: 13,
    0b001100: 12,
    0b110011: 51,
    0b010101: 21,
    0b101010: 42,
}

YinYang = [6,7,8,9]

Hexagram = {
    0:"0",
    1:"0",
    2:"0",
    3:"0",
    4:"0",
    5:"0"
}

Hexagram_NOW = {
    0:"0",
    1:"0",
    2:"0",
    3:"0",
    4:"0",
    5:"0"
}

def order_YinYang(YinYang, House):
    global Hexagram_NOW, Hexagram
    for Key in Hexagram:
            Hexagram_NOW[Key] = Hexagram[Key]
    Status = random.choice(YinYang)
    
    if Status == 6 or Status == 9: # Changing...
        if Hexagram[House] == "0":
            Hexagram[House] = "1"
        else:
            Hexagram[House] = "0"
        

# Function to convert binary values to Yijing lines
def convert_to_yiking_lines(binary_str):
    return ''.join('--------\n' if bit == '0' else '---  ---\n' for bit in binary_str[::-1])

OLD_NEW = 5  
House = 0

inverted_dict = {v: k for k, v in Le_Livre_Des_Transformations_KEYS.items()}

while not End_Program:    
    House += 1
    if House > 5:
        if Draw:
            Drawed = bin(int("".join(Hexagram[bit] for bit in Hexagram), 2))[2:].zfill(6)
            yijing_lines = convert_to_yiking_lines(Drawed)
            Drawed = int(Drawed, 2)
            print(f"\r{hexagrams_dict[inverted_dict[Drawed_NOW]]} \n{yijing_lines_NOW} \nBECOMES\n\n {hexagrams_dict[inverted_dict[Drawed]]}\n{yijing_lines}")
            Draw = False
        else:
            Drawed_NOW = bin(int("".join(Hexagram_NOW[bit] for bit in Hexagram_NOW), 2))[2:].zfill(6)
            yijing_lines_NOW = convert_to_yiking_lines(Drawed_NOW)
            Drawed_NOW = int(Drawed_NOW, 2)
        House = 0

    order_YinYang(YinYang, House)

    