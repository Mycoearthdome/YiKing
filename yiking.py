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
    0b000000: "1- K'ien - Le Créateur - Heaven\n The noble man acts with strength and determination, leading by example.",
    0b111111: "2- K'ouen - Le Réceptif - Earth over Earth\n The noble man is receptive and humble, embracing the wisdom of patience.",
    0b011101: "3 - Tchouen' - La difficulté initiale - Water over Thunder\n The noble man faces difficulties with calm perseverance and clear purpose.",
    0b101110: "4 - Mong - La folie Juvénile - Mountain over Water\n The noble man provides guidance in times of confusion, helping others find clarity.",
    0b000101: "5 - Su - L'Attente / La Nutrition - Water over Heaven\n The noble man is patient, waiting for the right moment to act, like water flowing steadily.",
    0b101000: "6 - Soung - Le Conflit - Heaven over Water\n The noble man seeks resolution through peace, never allowing conflict to consume him.",
    0b101111: "7 - Sze -L'Armée - Earth over Water\n The noble man leads with courage, organizing others with wisdom and discipline.",
    0b111101: "8 - Pi - La solidarité / L'union - Water over Earth\n The noble man fosters unity, drawing people together to accomplish a common goal.",
    0b000100: "9 - Siao Tch'ou - Le pouvoir d'apprivoisement du petit - Wind over Heaven\n The noble man handles small matters with gentleness, showing kindness in every action.",
    0b001000: "10 - Liu - La Marche - Heaven over Lake\n The noble man moves forward with purpose, but also with respect for the environment around him.",
    0b000111: "11 - T'ai - La Paix - Earth over Heaven\n The noble man creates peace through balanced action, bringing harmony to difficult situations.",
    0b111000: "12 - P'i - La stagnation / L'immobilité - Heaven over Earth\n The noble man remains steadfast and unmoved in the face of adversity, maintaining integrity.",
    0b010000: "13 - T'ong jen - Communauté avec les hommes - Heaven over Fire\n The noble man builds community, reaching out to others with sincerity and warmth.",
    0b000010: "14 - Ta Yéou - Le grand avoir - Fire over Heaven: The noble man possesses wisdom and abundance, but uses it selflessly for the greater good.",
    0b110111: "15 - K'ien - L'humilité - Earth over Mountain\n The noble man remains humble, understanding that true strength comes from humility.",
    0b111011: "16 - Yu - L'enthousiasme - Thunder over Earth\n The noble man inspires others with enthusiasm, leading through passion and vision.",
    0b011001: "17 - Souei - La Suite - Lake over Thunder\n The noble man follows the path with steady confidence, knowing that persistence leads to success.",
    0b100110: "18 - Kou - Le travail sur ce qui est corrompu - Mountain over Wind\n The noble man works to rectify flaws, restoring balance and harmony to the world.",
    0b001111: "19 - Lin - L'approche - Earth over Lake\n The noble man approaches challenges with grace, knowing when to step forward and when to yield.",
    0b111100: "20 - Kouan - La contemplation - Wind over Earth\n The noble man reflects deeply, gaining insight from quiet contemplation and observation.",
    0b011010: "21 - Che Ho - Mordre au travers - Fire over Thunder\n The noble man takes decisive action when necessary, addressing obstacles with strength and clarity.",
    0b010110: "22 - Pi - La grâce - Mountain over Fire\n The noble man embodies grace, radiating beauty through inner harmony and outward humility.",
    0b111110: "23 - Po - L'éclatement - Mountain over Earth\n The noble man knows when to dismantle old structures to create space for new growth.",
    0b011111: "24 - Fou - Le retour (Le Tournant) - Earth over Thunder\n The noble man embraces cycles of renewal, always returning to the path of wisdom after every setback.",
    0b011000: "25 - Wou Wang - L'innocence (L'inatendu) - Heaven over Thunder\n The noble man acts with innocence, trusting that his purity of heart will guide him.",
    0b000110: "26 - Ta Tch'ou - Le pouvoir d'apprivoisement du grand - Mountain over Heaven\n The noble man masters great power with restraint, knowing when to hold back and when to act.",
    0b011110: "27 - Yi - Les commissures des lèvres (L'administration de la nourriture) - Mountain over Thunder\n The noble man ensures sustenance for all, wisely guiding the flow of resources.",
    0b100001: "28 - Ta Kouo - La préponderance du grand - Lake over Wood\n The noble man understands the weight of responsibility and bears it with grace and dignity.",
    0b101101: "29 - K'an - L'insondable, l'eau - Water over Water\n The noble man faces the unknown with bravery, navigating life's uncertainties with wisdom.",
    0b010010: "30 - Li - Ce qui s'attache, le feu - Fire over Fire\n The noble man is bound by his integrity, his actions guided by an unwavering sense of truth.",
    0b110001: "31 - Hien - L'influence (La demande en mariage) - Lake over Mountain\n The noble man attracts others through his gentleness and inner strength.",
    0b100011: "32 - Hong - La Durée - Thunder over wind\n The noble man endures, finding strength in his consistent actions and principles.",
    0b110000: "33 - Touen - La Retraite - Heaven over Mountain\n The noble man knows when to withdraw, allowing time for reflection and preparation for future action.",
    0b000011: "34 - Ta Tchouang - La puissance du grand - Thunder over Heaven\n The noble man harnesses great power with discernment and courage.",
    0b111010: "35 - Tsin - Le Progrès - Fire over Earth\n The noble man advances steadily, making progress while remaining grounded in truth.",
    0b010111: "36 - Ming YI - L'obcurcissement de la lumière - Earth over Fire\n The noble man adapts to dark times, using insight to navigate through confusion.",
    0b010100: "37 - Kia Jen - La Famille (Le Clan) - Wind over Fire\n The noble man builds a strong, supportive family, nurturing growth and harmony.",
    0b001010: "38 - K'ouei - L'opposition - Fire over Lake\n The noble man meets opposition with calmness, overcoming obstacles with patience and wisdom.",
    0b110101: "39 - Kien - L'obstacle - Water over Mountain\n The noble man rises above obstacles, meeting adversity with resilience and strength.",
    0b101011: "40 - Hiai - La Libération - Thunder over Water\n The noble man frees others from oppression, offering liberation with compassion and foresight.",
    0b001110: "41 - Souen - La Diminution - Mountain over Lake\n The noble man finds strength in humility, knowing that less is often more.",
    0b011100: "42 - Yi - L'Augmentation - Wind over Thunder\n The noble man grows by uplifting others, expanding through cooperation and generosity.",
    0b000001: "43 - Kouai - La percée (La résolution) - Lake over Heaven\n The noble man is decisive, cutting through confusion with clear, resolute action.",
    0b100000: "44 - Keou - Venir à la rencontre - Heaven over Wind\n The noble man is open to new opportunities, meeting challenges with openness and wisdom.",
    0b111001: "45 - Ts'ouei - Le Rassemblement (Le Recueillement) - Lake over Earth\n The noble man gathers wisdom and strength by drawing together with others.",
    0b100111: "46 - Cheng - La Poussée vers le haut - Earth over Wood\n The noble man rises through hard work and integrity, leading others by example.",
    0b101001: "47 - K'ouen - L'accablement (L'Épuisement) - Lake over Water\n The noble man endures hardship, never losing hope even in times of exhaustion.",
    0b100101: "48 - Tsing - Le Puit - Water over Wood\n The noble man seeks wisdom from the depths, drawing knowledge from within.",
    0b010001: "49 - Ko - La Révolution, la mue - Lake over Fire\n The noble man embraces change, growing through transformation with grace.",
    0b100010: "50 - Ting - Le Chaudron - Fire over Wood\n The noble man nourishes the spirit of others, providing warmth and strength.",
    0b011011: "51 - Tchen - L'Éveilleur, L'Ébranlement - Thunder over Thunder\n The noble man awakens others with his energy and inspires with his actions.",
    0b110110: "52 - Ken - L'immobilisation - Mountain over Mountain\n The noble man is steadfast, remaining grounded in times of stillness and reflection.",
    0b110100: "53 - Tsien - Le Développement (Le progrès graduel) - Wood over Mountain\n The noble man progresses steadily, laying a solid foundation for long-term growth.",
    0b001011: "54 - Kouei Mei - L'Épousée - Thunder over Lake\n The noble man joins with another in mutual respect and understanding, building a strong partnership.",
    0b010011: "55 - Fong - L'Abondance, La Plénitude - Thunder over Fire\n The noble man shares abundance generously, never hoarding resources for himself.",
    0b110010: "56 - Liu - Le Voyageur - Fire over Mountain\n The noble man journeys with purpose, finding wisdom in every step of his travels.",
    0b100100: "57 - Souen - Le doux (Le pénétrant, le vent) - Wood over Wood\n The noble man is gentle yet powerful, like the wind that shapes the world.",
    0b001001: "58 - Touei - Le Serein, Le Joyeux - Lake over Lake\n The noble man brings joy and serenity, uplifting those around him with his presence.",
    0b101100: "59 - Houan - La dissolution (La Dispersion) - Wind over Water\n The noble man dissolves barriers, bringing people together with compassion.",
    0b001101: "60 - Tsie - La Limitation - Water over Lake\n The noble man understands the power of limits, knowing when to restrain his actions for the greater good.",
    0b001100: "61 - Tchoung Fou - La vérité intérieure - Wind over Lake\n The noble man seeks truth from within, guiding others through inner wisdom.",
    0b110011: "62 - Siao Kouo - La prépondérance du petit - Thunder over Mountain\n The noble man excels in small things, mastering the details to achieve great results.",
    0b010101: "63 - Ki Tsi - Après L'Accomplissment - Water over Fire\n The noble man reflects on his achievements with humility, ready for the next challenge.",
    0b101010: "64 - Wei Tsi - Avant L'Accomplissment - Fire over Water\n The noble man prepares for success with careful planning and clear intent."
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

    