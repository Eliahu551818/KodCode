nums =[]

while len(nums) < 3:
    nums.append(int(input("Enter a number: ")))

usage = input("Do you want to find the largest number using built-in func? (y/n): ")

if usage == "y":
    def check(list) -> int:
        indx = 0
        index2 = 1
        if index2 == len(list):
            return list[indx]
        
        if list[indx] > list[index2]:
            list.pop(index2)
            index2 +=1
            return check(list)
        else:
            list.pop(indx)
        index2 +=1
        return check(list)
        
    print("The largest number is", check(nums))
else:
    print("The largest number is", max(nums))

    
        


