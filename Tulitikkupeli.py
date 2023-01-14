"""
COMP.SC.100 Tulitikkupeli
Tekijä: Anna Koskinen
"""
def main():
    print("Game of sticks")
    miinus=21
    while miinus>0:
        player_1 = int(input("Player 1 enter how many sticks to remove: "))
        while player_1 > 3 or player_1<=0:
            print("Must remove between 1-3 sticks!")
            player_1=int(input("Player 1 enter how many sticks to remove: "))
        miinus = miinus - player_1
        if miinus<=0:
            loser="1"
            pass
        else:
            print(f"There are {miinus} sticks left")
        if miinus>0:
            player_2=int(input("Player 2 enter how many sticks to remove: "))
            while player_2>3 or player_2<=0:
                print("Must remove between 1-3 sticks!")
                player_2=int(input("Player 2 enter how many sticks to remove: "))
            miinus=miinus-player_2
            if miinus<=0:
                loser="2"
                pass
            else:
                print(f"There are {miinus} sticks left")
    print(f"Player {loser} lost the game!")

if __name__ == "__main__":
    main()