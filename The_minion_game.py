
def minion_game(string):
    vowels=('A','I','E','O','U')
    Kevin=0
    Stuart=0
    i=0

    while i !=len(string):

        if string[i:].startswith(vowels):
            Kevin +=len(string)-i
            i+=1
        else:
            Stuart+=len(string)-i
            i+=1

    if Kevin>Stuart :  
        print(f"Kevin {Kevin}")
    elif Kevin<Stuart:
        print(f"Stuart {Stuart}")
    else:
        print("Draw")


s=input().upper()
minion_game(s)
