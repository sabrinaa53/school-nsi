def class_pile() : 
    return [] 

def push(pile,element): 
    return pile.append(element)

def pop(pile) : 
    return pile.pop()

def peek(pile) : 
    return pile[0]

def is_empty(pile) : 
    if len(pile) == 0 : 
        return True 
    else : 
        return False