print("Welcome to Trivia!")
score = 0
while True:
    var1 = input("What year was the first nuke dropped? ")
    if var1 == "1945":
        print("Correct")
        score+=1
    var2 = input("Whats the only food that doesnt expire? ")
    if var2.lower() == "honey":
        print("Correct")
        score+=1
    var3 = input("Name one country that has not missed a modern day olmpic: ")
    if var3.lower() == "greece" or var3.lower() == "australia":
        print("Correct")
        score+=1
    var4 = input("Which country borders 14 nations and crosses 8 time zones? ")
    if var4.lower() == "russia":
        print("Correct")
        score+=1
    var5 = input("The unicorn is the national animal of which country? ")
    if var5.lower() == "scotland":
        print("Correct")
        score+=1
    var6 = input("Which of Newton’s Laws states that ‘for every action, there is an equal and opposite reaction? ")
    if var6 == "3" or var6.lower == "third":
        print("Correct")
        score+=1
    var7 = input("Iceland diverted roads to avoid disturbing communities of what? ")
    if var7.lower() == "elves" or var7.lower() == "elf" or var7.lower() == "elfs":
        print("Correct")
        score+=1
    var8 = input("What TV show was the first to show an inter-racial kiss on American television? ")
    if var8.lower() ==  "star trek":
        print("Correct")
        score+=1
    var9 = input("What is the rarest M&M color? ")
    if var9.lower() == "brown":
        print("Correct")
        score+=1
    var10 = input("Who is the bass player for Pink Floyd? ")
    if var10.lower() == "roger waters":
        print("Correct")
        score+=1
    break
print("Tirvia is over! You got ",score," out of 10 points!")
