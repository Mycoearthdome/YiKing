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
    0b000000: "1 - The Creative (Heaven) – The noble man acts with strength and determination, leading by example.",
    0b111111: "2 - The Receptive (Earth) – The noble man is receptive and humble, embracing the wisdom of patience.",
    0b011101: "3 - Initial Difficulty (Water over Thunder) – The noble man faces difficulties with calm perseverance and clear purpose.",
    0b101110: "4 - Youthful Folly (Mountain over Water) – The noble man provides guidance in times of confusion, helping others find clarity.",
    0b000101: "5 - Waiting (Water over Heaven) – The noble man is patient, waiting for the right moment to act, like water flowing steadily.",
    0b101000: "6 - Conflict (Heaven over Water) – The noble man seeks resolution through peace, never allowing conflict to consume him.",
    0b101111: "7 - The Army (Earth over Water) – The noble man leads with courage, organizing others with wisdom and discipline.",
    0b111101: "8 - Holding Together (Water over Earth) – The noble man fosters unity, drawing people together to accomplish a common goal.",
    0b000100: "9 - The Taming Power of the Small (Wind over Heaven) – The noble man handles small matters with gentleness, showing kindness in every action.",
    0b001000: "10 - The Clinging (Heaven over Lake) – The noble man moves forward with purpose, but also with respect for the environment around him.",
    0b000111: "11 - Peace (Earth over Heaven) – The noble man creates peace through balanced action, bringing harmony to difficult situations.",
    0b111000: "12 - Standstill (Heaven over Earth) – The noble man remains steadfast and unmoved in the face of adversity, maintaining integrity.",
    0b010000: "13- Fellowship (Heaven over Fire) – The noble man builds community, reaching out to others with sincerity and warmth.",
    0b000010: "14 - Possession in Great Measure (Fire over Heaven) – The noble man possesses wisdom and abundance, but uses it selflessly for the greater good.",
    0b110111: "15 - Modesty (Earth over Mountain) – The noble man remains humble, understanding that true strength comes from humility.",
    0b111011: "16 - Enthusiasm (Thunder over Earth) – The noble man inspires others with enthusiasm, leading through passion and vision.",
    0b011001: "17 - Following (Lake over Thunder) – The noble man follows the path with steady confidence, knowing that persistence leads to success.",
    0b100110: "18 - Work on What Has Been Spoiled (Mountain over Wind) – The noble man works to rectify flaws, restoring balance and harmony to the world.",
    0b001111: "19 - Approach (Earth over Lake) – The noble man approaches challenges with grace, knowing when to step forward and when to yield.",
    0b111100: "20 - Contemplation (Wind over Earth) – The noble man reflects deeply, gaining insight from quiet contemplation and observation.",
    0b011010: "21 - Biting Through (Fire over Thunder) – The noble man takes decisive action when necessary, addressing obstacles with strength and clarity.",
    0b010110: "22 - Grace (Mountain over Fire) – The noble man embodies grace, radiating beauty through inner harmony and outward humility.",
    0b111110: "23 - Splitting Apart (Mountain over Earth) – The noble man knows when to dismantle old structures to create space for new growth.",
    0b011111: "24 - Return (Earth over Thunder) – The noble man embraces cycles of renewal, always returning to the path of wisdom after every setback.",
    0b011000: "25 - Innocence (Heaven over Thunder) – The noble man acts with innocence, trusting that his purity of heart will guide him.",
    0b000110: "26 - Great Taming (Mountain over Heaven) – The noble man masters great power with restraint, knowing when to hold back and when to act.",
    0b011110: "27 - The Nourishing (Mountain over Thunder) – The noble man ensures sustenance for all, wisely guiding the flow of resources.",
    0b100001: "28 - The Preponderance of the Great (Lake over Wood) – The noble man understands the weight of responsibility and bears it with grace and dignity.",
    0b101101: "29 - The Abysmal (Water over Water) – The noble man faces the unknown with bravery, navigating life's uncertainties with wisdom.",
    0b010010: "30 - The Li (Fire over Fire) – The noble man is bound by his integrity, his actions guided by an unwavering sense of truth.",
    0b110001: "31 - Influence (Lake over Mountain) – The noble man attracts others through his gentleness and inner strength.",
    0b100011: "32 - Duration (Thunder over Wind) – The noble man endures, finding strength in his consistent actions and principles.",
    0b110000: "33 - Retreat (Heaven over Mountain) – The noble man knows when to withdraw, allowing time for reflection and preparation for future action.",
    0b000011: "34 - Power of the Great (Thunder over Heaven) – The noble man harnesses great power with discernment and courage.",
    0b111010: "35 - Progress (Fire over Earth) – The noble man advances steadily, making progress while remaining grounded in truth.",
    0b010111: "36 - Darkening of the Light (Earth over Fire) – The noble man adapts to dark times, using insight to navigate through confusion.",
    0b010100: "37 - The Family (Wind over Fire) – The noble man builds a strong, supportive family, nurturing growth and harmony.",
    0b001010: "38 - Opposition (Fire over Lake) – The noble man meets opposition with calmness, overcoming obstacles with patience and wisdom.",
    0b110101: "39 - Obstruction (Water over Mountain) – The noble man rises above obstacles, meeting adversity with resilience and strength.",
    0b101011: "40 - Liberation (Thunder over Water) – The noble man frees others from oppression, offering liberation with compassion and foresight.",
    0b001110: "41 - Decrease (Mountain over Lake) – The noble man finds strength in humility, knowing that less is often more.",
    0b011100: "42 - Increase (Wind over Thunder) – The noble man grows by uplifting others, expanding through cooperation and generosity.",
    0b000001: "43 - Breakthrough (Lake over Heaven) – The noble man is decisive, cutting through confusion with clear, resolute action.",
    0b100000: "44 - Coming to Meet (Heaven over Wind) – The noble man is open to new opportunities, meeting challenges with openness and wisdom.",
    0b111001: "45 - Gathering Together (Lake over Earth) – The noble man gathers wisdom and strength by drawing together with others.",
    0b100111: "46 - The Pushing Upward (Earth over Wood) – The noble man rises through hard work and integrity, leading others by example.",
    0b101001: "47 - Exhaustion (Lake over Water) – The noble man endures hardship, never losing hope even in times of exhaustion.",
    0b100101: "48 - The Well (Water over Wood) – The noble man seeks wisdom from the depths, drawing knowledge from within.",
    0b010001: "49 - Revolution (Lake over Fire) – The noble man embraces change, growing through transformation with grace.",
    0b100010: "50 - The Cauldron (Fire over Wood) – The noble man nourishes the spirit of others, providing warmth and strength.",
    0b011011: "51 - The Arousing (Thunder over Thunder) – The noble man awakens others with his energy and inspires with his actions.",
    0b110110: "52 - Keeping Still (Mountain over Mountain) – The noble man is steadfast, remaining grounded in times of stillness and reflection.",
    0b110100: "53 - Development (Wood over Mountain) – The noble man progresses steadily, laying a solid foundation for long-term growth.",
    0b001011: "54 - The Marrying Maiden (Thunder over Lake) – The noble man joins with another in mutual respect and understanding, building a strong partnership.",
    0b010011: "55 - Abundance (Thunder over Fire) – The noble man shares abundance generously, never hoarding resources for himself.",
    0b110010: "56 - The Wanderer (Fire over Mountain) – The noble man journeys with purpose, finding wisdom in every step of his travels.",
    0b100100: "57 - The Gentle (Wood over Wood) – The noble man is gentle yet powerful, like the wind that shapes the world.",
    0b001001: "58 - The Joyous (Lake over Lake) – The noble man brings joy and serenity, uplifting those around him with his presence.",
    0b101100: "59 - Dispersing (Wind over Water) – The noble man dissolves barriers, bringing people together with compassion.",
    0b001101: "60 - Limitation (Water over Lake) – The noble man understands the power of limits, knowing when to restrain his actions for the greater good.",
    0b001100: "61 - Inner Truth (Wind over Lake) – The noble man seeks truth from within, guiding others through inner wisdom.",
    0b110011: "62 - Preponderance of the Small (Thunder over Mountain) – The noble man excels in small things, mastering the details to achieve great results.",
    0b010101: "63 - After Completion (Water over Fire) – The noble man reflects on his achievements with humility, ready for the next challenge.",
    0b101010: "64 - Before Completion (Fire over Water) – The noble man prepares for success with careful planning and clear intent."
}

YIKING_JUDGMENTS = {
    0b000000: "The Creative works sublime success, furthering through perseverance.",
    0b111111: "The Receptive brings about sublime success, furthering through perseverance.",
    0b011101: "The difficulty at the beginning is like a stream trying to find its course. Perseverance is necessary.",
    0b101110: "Youthful folly leads to regret, but a noble man remains true to the path and does not falter.",
    0b000101: "Waiting is required, for there is no movement. Patience and persistence will bring success.",
    0b101000: "Conflict, though painful, must be resolved with understanding and the ability to see things from all sides.",
    0b101111: "The army works with order and discipline, guided by wisdom and leadership.",
    0b111101: "Holding together brings about strength in unity. People must unite to succeed in their endeavors.",
    0b000100: "Small things can have great impact when applied with caution and precision.",
    0b001000: "The Clinging calls for perseverance, for one’s path must be pursued with consistency and purpose.",
    0b000111: "Peace arises from a combination of balance, yielding, and the harmonizing of opposing forces.",
    0b111000: "Standstill warns against stagnation. Time for reflection is important, but movement must follow.",
    0b010000: "Fellowship is achieved through mutual trust and shared goals. People of similar ideals will come together.",
    0b000010: "Possessing great abundance brings responsibility. Use resources with care, for they should be shared.",
    0b110111: "Modesty brings success. A noble man must always be humble in the face of greatness.",
    0b111011: "Enthusiasm leads to great things. The noble man leads with passion and draws others to him.",
    0b011001: "Following leads to success when one is faithful to their path and follows with patience and strength.",
    0b100110: "Work on what has been spoiled to restore balance and rectify previous errors.",
    0b001111: "Approach wisely, know when to go forward and when to retreat. Timing is key.",
    0b111100: "Contemplation allows one to reflect deeply and gain insight into the truth of the matter.",
    0b011010: "Biting through indicates the necessity to deal directly with obstacles. Power and clarity bring success.",
    0b010110: "Grace is the ability to make difficult things look easy. Inner harmony creates outer beauty.",
    0b111110: "Splitting apart allows for renewal. Dismantling what no longer serves to make room for new growth.",
    0b011111: "Return is about cyclical renewal. The noble man returns to the path after setbacks and finds clarity.",
    0b011000: "Innocence leads to clarity and success. Trust in your pure heart to guide you forward.",
    0b000110: "Restrain great power with wisdom. Strength must be used wisely and carefully.",
    0b011110: "Nourishment is about sustaining and providing for others. Ensure the flow of resources.",
    0b100001: "Great responsibility must be handled with grace. Balance is essential to bear such weight.",
    0b101101: "The Abysmal shows the challenges of navigating through uncertainty. Stay strong and rely on your inner wisdom.",
    0b010010: "The Clinging asks for consistency. One’s actions must be guided by a pure and unwavering commitment to truth.",
    0b110001: "Influence is achieved through gentleness and humility, attracting others through inner strength.",
    0b100011: "Duration is the strength gained through perseverance. Steady progress leads to enduring success.",
    0b110000: "Retreat is necessary for contemplation. Know when to withdraw to prepare for future action.",
    0b000011: "Great power must be handled with discernment. It must be used judiciously for maximum effectiveness.",
    0b111010: "Progress moves steadily. The noble man advances with purpose while remaining grounded.",
    0b010111: "The Darkening of the Light requires caution and wisdom during difficult times. One must endure and adapt.",
    0b010100: "The Family is the root of stability. Care for those closest to you, as unity strengthens the foundation.",
    0b001010: "Opposition is faced with composure. Difficulties are overcome with patience and resilience.",
    0b110101: "Obstruction is an obstacle to be overcome. Face difficulties with resilience, and they will eventually be cleared.",
    0b101011: "Deliverance is achieved by freeing oneself from what holds one back, moving with compassion and understanding.",
    0b001110: "Decrease can lead to growth. Sometimes less is more. Restrain yourself for a greater outcome.",
    0b011100: "Increase comes through generosity and cooperation. The noble man grows by giving freely.",
    0b000001: "Breakthrough comes through decisive action. Cut through confusion with clarity and determination.",
    0b100000: "Coming to meet requires openness. Be receptive to new ideas and challenges.",
    0b111001: "Gathering Together leads to strength through unity. By bringing people together, success is ensured.",
    0b100111: "Pushing Upward calls for continuous effort and gradual progress toward greater heights.",
    0b101001: "Oppression tests one’s resolve. Endurance and faith bring eventual relief.",
    0b100101: "The Well represents the flow of wisdom. Draw from deep sources for nourishment and guidance.",
    0b010001: "Revolution demands transformation. Embrace change and allow for renewal and growth.",
    0b100010: "The Cauldron represents transformation. Proper nourishment and preparation lead to creation and success.",
    0b011011: "The Arousing indicates an awakening. Energy surges and new opportunities arise.",
    0b110110: "Keeping Still requires stillness and reflection. Inner strength emerges during periods of calm.",
    0b110100: "Development is slow but steady. Build a strong foundation for future growth.",
    0b001011: "The Marrying Maiden signifies a time of transformation and union, where both parties bring value to the relationship.",
    0b010011: "Abundance requires sharing. Generosity leads to growth and prosperity.",
    0b110010: "The Wanderer finds wisdom through experiences and journeys. Every step brings clarity.",
    0b100100: "The Gentle indicates patience and persistence. Like the wind, it shapes the world subtly but profoundly.",
    0b001001: "The Joyous brings uplifting energy to those around. Joyful expression fosters peace.",
    0b101100: "Dispersion dissolves barriers. Bring about unity through compassion and understanding.",
    0b001101: "Limitation provides structure. It is necessary to recognize one’s boundaries and act within them.",
    0b001100: "Inner Truth emerges from deep self-reflection. Only by following the heart can true wisdom be found.",
    0b110011: "Preponderance of the Small leads to great success through the mastery of details and precision.",
    0b010101: "After Completion suggests a time of reflection. Success is realized but must be handled with care.",
    0b101010: "Before Completion requires thorough preparation and the willingness to adapt to changing circumstances."
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

House = 0
Count = 0

inverted_dict = {v: k for k, v in Le_Livre_Des_Transformations_KEYS.items()}

while not End_Program:    
    House += 1
    if House > 5:
        if Draw:
            Count += 1
            Drawed = bin(int("".join(Hexagram[bit] for bit in Hexagram), 2))[2:].zfill(6)
            yijing_lines = convert_to_yiking_lines(Drawed)
            Drawed = int(Drawed, 2)
            print(f"\r  DRAW #{Count}\n\n{hexagrams_dict[inverted_dict[Drawed_NOW]]} \n{yijing_lines_NOW}\nJUGEMENT:{YIKING_JUDGMENTS[inverted_dict[Drawed_NOW]]}\n\nBECOMES\n\nDRAW #{Count}-(future)\n\n{hexagrams_dict[inverted_dict[Drawed]]}\n{yijing_lines}\nJUGEMENT:{YIKING_JUDGMENTS[inverted_dict[Drawed]]}\n\n")
            Draw = False
        else:
            Drawed_NOW = bin(int("".join(Hexagram_NOW[bit] for bit in Hexagram_NOW), 2))[2:].zfill(6)
            yijing_lines_NOW = convert_to_yiking_lines(Drawed_NOW)
            Drawed_NOW = int(Drawed_NOW, 2)
        House = 0

    order_YinYang(YinYang, House)

    