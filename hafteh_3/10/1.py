country_list = ["china","usa","brazil","iran","germany" ]
pop_list = [1450881643, 335057747, 215725285, 86275736, 84340178]



for i in range(len(pop_list)):
    star = (pop_list[i]*50)//1450881643
    print(country_list[i],": ",star*"*")
    
    
