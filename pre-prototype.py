#attempt to make a grid

def my_print_square(d):
    all_ = d * d
    x = list(range(all_))
    x.sort(reverse=True)  
    i=0
    while i < all_:
       print(" ".join(map(str, x[i:i+d])))
       i += d


