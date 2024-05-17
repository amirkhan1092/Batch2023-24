import pandas as pd
data = pd.read_csv("basic2.csv")
data2 = pd.DataFrame(data)
data2.index = range(1,5)
print(data2)

 
#average of math score
score1 = data2['Math_Score']
print("Average of Maths score is ",sum(score1)/len(score1))

#Highest marks in  science
score2 = data2['Science_Score']
print(f'Highest marks in science is {max(score2)}')

#Total score for each student
name = data2['Name']
print("Total marks of each student:")
score =[]
for i in range(1,len(name)+1):
    score.append(score1[i]+score2[i])

for i in range(1,len(name)+1):
    print(f'Total marks of {name[i]} is {score[i-1]}')


#highest marks in total score
high = max(score)
high_mark = []
for i in score:
    if high == i:
        high_mark.append(name[i])
print("Student those who get highest marks")
for i in high_mark:
    print(i)



