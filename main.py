import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
champain = '''
                        *
                         *
        *       *       []
         _*    *_       ||
        |*|    |*|     |* |
        |_|    |_|     |__|
        \*/    \*/     | *|
        _|_    _|_     |__|

'''
#Write your code below this line 👇
hra = [rock , paper, scissors]

print(f"rock{rock}\n paper{paper}\n scissors{scissors}\n Vitajte v hre , trufate si zahrat?")
vyber = input("Pre kamen dajte 1, pre papier dajte 2, pre noznicky dajte 3. Vas vyber:")
znak = int(vyber)-1
user= hra[znak]

pc = random.randint(0,2)
# print(hra[pc])
pc_vyber = hra[pc]
print(f"\n player choose\n{user}\n pc choose \n {pc_vyber}")
# if user == rock and pc_vyber == paper :
  # 2print
if znak == 0 and pc == 2:
  print("You win",champain)
  
elif znak == 2 and pc == 0:
  print("You lose")
elif pc > znak:
  print("You lose")
elif znak > pc:
  print("You win!",champain)
elif pc == znak :
  print("It's a draw")
