#!/usr/bin/env python3.12

def count_up(int_tgt, int_current=0) :
    
    if int_tgt == int_current :
        return int_tgt
    
    print(int_current)
    
    return count_up(int_tgt, int_current+1)

print(count_up(5))

def count_down(int_tgt) :

    if int_tgt == 0 :
        return int_tgt
    
    print(int_tgt)

    return count_down(int_tgt-1)

print(count_down(5))