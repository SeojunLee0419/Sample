#list: 
#ex: lst = [90, 20, "30"]
#score = [90, 80, 30, 40]
#score2 = [10, 20, 50, 60]
#max(score) -> 90
#min(score) -> 30
#sum(score) ->240

#score[0] -> 90
#score[1] ->80
#score[-1] -> 40
#score[-4] -> 90

#[m:n] from m to n-1
#score[1:2] -> 80
#score[1:3] -> 80, 30

#score + score2 -> [90, 80, 30, 40, 10, 20, 50, 60]
#score *2 -> [90, 80, 30, 40, 90, 80, 30 , 40]

#score.append([100,100]) -> [90, 80, 30, 40, [100, 100]]
#score.extend([90, 90]) ->[90, 80, 30, 40, 90, 90]

#del score[3] -> [90, 80, 30]
#score[2:] =[] -> [90, 80] From 2 and onwards delete

#score3 = score # its not copying, but score3 is pointing at the same thing that score is pointing
#score4 = score[:] #this is copying
#score[0]='a'
#print(score) = ['a', 80, 30,40]
#print(score3) = ['a', 80, 30,40]
#print(score4) = [90, 80, 30,40]


#list(range(10)) -> [0,1,2,3,4,5,6,7,8,9]
#list(range(0,10)) -> [0,1,2,3,4,5,6,7,8,9]
#list(range(0,10,2)) -> [0,2,4,6,8]

#----------------------------------------------------


#Tuple: similar with list, but cannot change the values after creating it
#tpl = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#tpl[1] = 2 -> error

#--------------------------------------------

#Set: cannot have duplicate things in the array, cannot index or slice as the order does not matter, its like an actual set in math

#---------------------------------------

#Dictionary: 
#ex: {key1:value1, key2:value2}
#information = {"name: seojun", "age: 18", "height: 178"}
#type(information) -> dict
#information.items() -> dict_items([("name": "seojun"), ("age": "18"), ("height": "178")])
#information.keys() -> dict_keys(['name', 'age', 'height'])
#information.values() -> dict_values(["seojun", "18", "178"])

