import sys
from workflows import get_likes

if __name__ == "__main__":
    arg = sys.argv[1].lower()
    
    if arg == "get_likes":
        get_likes.get_likes('NawazGafar')