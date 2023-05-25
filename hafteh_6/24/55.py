blog_post_list = [["post1",3,4,5],["post2",4,4,4],["post3",5,3,5]]
post_name = input("enter post name: ")

for post in blog_post_list :
    for score in post:
        if post_name == score[0]:
            print("bale")
        else:
            print("no")
