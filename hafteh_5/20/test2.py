mylist=["maryam","ali","mahdi","ali","hasan"]
print("mylist: ",mylist)
user_input = input("dovomin nafar che kasi ra mokhahid hazf konid: ")
counter_ali = 0
for i in range(len(mylist)):
    if user_input in mylist: 
        if mylist[i]==user_input:
            counter_ali+=1
            if counter_ali == 2:
                #ali_second_index_number = i
                mylist.pop(i)
                break
            elif counter_ali!= 2:
                print(mylist[i]," dovom peyda nashod")
    else:
        print("in shakhs dar list nist")
        break
print("mylist jadid: ",mylist)
                
