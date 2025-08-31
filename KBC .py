questions=[
    ["current prime minister of india?","A.Modi","B.Draupadhi murmu","C.SV patel","D.jana gana mana","A"],
    ["president of india?","A.Modi","B.Draupadhi murmu","C.SV patel","D.jana gana mana","B"],
    ["iron man of india?","A.Modi","B.Draupadhi murmu","C.SV patel","D.jana gana mana","C"],
    ["national anthem of india?","B.Modi","B.Draupadhi murmu","C.SV patel","D.jana gana mana","D"]
]

print("WELCOME TO K.B.C")
print()
l=0
for i in range(len(questions)):
    q=questions[i]
    print(q[0])
    print(q[1]    ,     q[2],sep='        ')
    print(q[3]     ,    q[4],sep='    ')
    a=input("choose an option(A/B/C/D)")
    if(a.upper()==q[5]):
        print("correct answer")
        l=l+10
        print("you earned:",l)
        
    else:
        print("wrong answer") 
        l=l+0
        print("you earned:",l)   
        
print("total point earned is:",l)        