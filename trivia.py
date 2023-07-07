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
    var11 = input("What is the name for a group of penguins? ")
    if var11.lower() == "colony" or var11.lower() == "huddle" or var11.lower() == "raft" or var11.lower() == "rookery" or var11.lower() == "tuxedo" or var11.lower() == "waddle":
        print("Correct")
        score+=1
    var12 == input("What year did the first iPhone come out? ")
    if var12.lower() == "2007":
        print("Correct")
        score+=1
    var13 == input("Which of the 50 States was its own country for a while? ")
    if var13.lower() == "Texas":
        print("Correct")
        score+=1
    var14 == input("How many time zones are there in the world? ")
    if var14.lower() == "38":
        print("Correct")
        score+=1
    var15 == input("What makes Seattle's annual Fremont Solstice Parade unusual? ")  
    if var15.lower() == "Biking in the nude":
        print("Correct")
        score+=1
    var16 == input("What musical key do most cars honk in? ")
    if var16.lower() == "F#" or var16.lower() == "f sharp":
        print("Correct")
        score+=1 
    var17 == input("The term John Doe originated from what country?")
    if var17.lower() == "great britain" or var17.lower() == "britain":
        print("Correct")
        score+=1 
    var18 == input("What proffesion did Pope Francis do before becoming the Pope? ")
    if var18.lower() == "bouncer":
        print("Correct")
        score+=1 
    var19 == input("How many postage stamps does it tale to gain calorie when licking them?")
    if var19.lower() == "10":
        print("Correct")
        score+=1 
    var20 == input("What is the last letter added to the American alphabet?")
    if var20.lower() == "j":
        print("Correct")
        score+=1 
        
    break
print("Tirvia is over! You got ",score," out of 20 points")
