                            # Example 1
def cleanword(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return cleanword(word[1:])
    else:   # stash ['WORLD']
        return word[0] + cleanword(word[1:])
print(cleanword("wwwoooorrrldddddddddddd"))



                        # Example 2
'''
def fib(n):
   if n < 0:
        raise ValueError
   elif n in (0, 1):
       return n
   else:
       return(fib(5-1) + fib(5-2))

def fib(4):
   if n < 0:
        raise ValueError
   elif n in (0, 1):                    # 3 + 2
       return n
   else:
       return(fib(3) + fib(2))

def fib(3):
   if n < 0:
        raise ValueError
   elif n in (0, 1):                     # 2 + 1
       return n
   else:
       return(fib(2) + fib(1))

def fib(2):
   if n < 0:
        raise ValueError
   elif n in (0, 1):                     # 1 + 1
       return n
   else:
       return(fib(1) + fib(0))
 def fib(1):
    if n < 0:
         raise ValueError                  # 1
    elif n in (0, 1):
        return n
    else:
        return(fib(0) + fib(0))
'''
