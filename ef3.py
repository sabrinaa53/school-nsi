def class_file() : 
    return []

def enqeue(file, element) : 
    return file.append(element)

def dequeue(file) : 
    return file.pop(0)

def front(file):
    return file[0]

def is_empty(file) : 
    if len(file) == 0 : 
        return True 
    else : 
        return False 

def size(file) : 
    return len(file)