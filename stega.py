from Decode import *
from Encode import *

def isNeedToEncode():
    while True:
    # Ask the user to enter the cover text in Sinhala
        action = input("What do you want to do now? encode a text (E) or decode a text (D) ")
        if action.upper() in ("E", "D"):
            if action.upper() == "E":
                return True
            else:
                return False
        else:
            print("Invalid action provided. Only supports E or D")

def main():
    print("Welcome to STEGA in සිංහල")
    if isNeedToEncode():
        encode()
        decode()
    
    else:
        decode()

if __name__ == "__main__":
  main()
    
