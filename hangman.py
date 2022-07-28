
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


print("WELCOME TO HANGMAN GAME")

WORD = "entrepreneur"
WORD=WORD.upper();
L = []
L1=[]
# L1=["_", "_", "_", "_", "_"]
# L = WORD.split("")

for i in WORD:
    L.append(i)
    L1.append("_")
# print(L)

# # global BOOL

# def check(L, L1, val, BOOL):
#     length = len(L)
#     for i in range(0,length):
#         if (L[i]==val):
#             L1[i] = val
#             BOOL = 1
#             print(f"BOOL IS NOW {BOOL}")   

count1  = 0
while(True):
    print(L1)
    if (count1 == 7):
      print("THE MAN DIED, YOU LOOSE.")
      break    
    if (L == L1):
      print("YOU WON MAN SAVED")
      break
    # print(f"Attemps left = {NO_INPUTS - count}")
    BOOL = 0
    val = input("ENTER THE LETTER")
    val = val.upper()
    length = len(L)
    for i in range(0,length):
        if (L[i]==val):
            L1[i] = val
            BOOL = 1
            # print(f"BOOL IS NOW {BOOL}") 
    # print(f"BOOL IS NOW {BOOL}")   
    if (BOOL == 0):
        print(HANGMANPICS[count1])
        count1=count1 + 1
    


