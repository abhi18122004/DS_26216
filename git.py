import time
def animated_text(*args):
    for i in args:
        for char in i:
            print(char,end="",flush=True)
            time.sleep(0.02)
animated_text("Deviyo aur sajjano...Abhinandan aabhar..!!!!  Welcome to Kaun Banega Crorepati....!!\n")
animated_text("Game ke rules to aap sabhi ko clear hi honge...\n")
animated_text("Note: To specify correct answer you have to type correct option number!!!\n")
ques_list=[["Who invented pyhton?","Narendra modi","Guido van rossoum","Amit shah","Raj nath singh"],
          ["In which year pyhton was invented","1999","1969","1991","2005"],["What is the capital of India?",
                                                                     "New Delhi","Mumbai","Kolkata","Patna"],
           ["8th wonder of the world is situated in which country","Italy","India","South Korea","Cambodia"],
           ["Famous romantic novel 'It ends with us' is written by who?","Yashwanth singh","Colleen Hoover","Elon Musk"
               ,"Baby doll"]]
dhanraashi= [100000,200000,700000,1000000,2000000]
answers=[2,3,1,4,2]
Dhan=0
i=k=0
for i in range (5) :
    animated_text("Sawal aapki screen prrr:\n")
    animated_text(ques_list[i][0],"\n")
    animated_text("Options:\n","1.",ques_list[i][1],"\t","2.",ques_list[i][2],"\n","3.",ques_list[i][3],"\t","4.",
          ques_list[i][4],"\n")

    ans=int(input("choose option number: \n"))
    if (ans==answers[i]):
        animated_text("Awesome..Correct answer!\n",str(dhanraashi[i])," added to your winning amount.\n")
        k+=1
        Dhan+=dhanraashi[i]
    else:
        animated_text("Ohh shit wrong answer...\n")
        break

if (k==5):
    animated_text("Congratulations you have won the maximum amount\n")
animated_text("Your final winnings ",str(Dhan))