blog_post_list = [["post1",3,4,5],["post2",4,4,4],["post3",5,3,5]]

for post in blog_post_list:
    sum_scores = 0
    for score in post[1:]:
        sum_scores += score
    ave = sum_scores/(len(post)-1)
    print("ave",post[0],": ",ave)
