"""
Displays flower ASCII art
"""

import sys

__version__ = "0.0.1"

# ASCII art from https://www.asciiart.eu/plants/flowers
# Because I have the artistic skills of a potato
ROSE = r"""
        _____
      /  ___  \
    /  /  _  \  \
  /( /( /(_)\ )\ )\
 (  \  \ ___ /  /  )
 (    \ _____ /    )
 /(               )\
|  \             /  |
|    \ _______ /    |
 \    / \   / \    /
   \/    | |    \/
         | |
         | |
         | |
"""

SUNFLOWER = r"""
             .-.'  '.-.
          .-(   \  /   )-.
         /   '..oOOo..'   \
 ,       \.--.oOOOOOOo.--./
 |\  ,   (   :oOOOOOOo:   )
_\.\/|   /'--'oOOOOOOo'--'\
'-.. ;/| \   .''oOOo''.   /
.--`'. :/|'-(   /  \   )-'
 '--. `. / //'-'.__.'-;
   `'-,_';//      ,  /|
        '((       |\/./_
          \\  . |\; ..-'
           \\ |\: .'`--.
            \\, .' .--'
             ))'_,-'`
       jgs  //-'
           //
          //
         |/
"""

TULIP =         r"""
         ,
     /\^/`\
    | \/   |
    | |    |
    \ \    /
     '\\//'
       ||
       ||
       ||
       ||  ,
   |\  ||  |\
   | | ||  | |
   | | || / /
    \ \||/ /
jgs  `\\//`
    ^^^^^^^^
"""


def rose():
    print(ROSE)

def sunflower():
    print(
        SUNFLOWER
    )


def tulip():
    print(TULIP)


def main(args):
    """
    Entry point to flowerpot
    """
    if not args:
        raise ValueError("Ask for a flower, try: python flowerpot.py sunflower")
    if len(args) > 1:
        raise ValueError("Ask for one flower at a time. :)")

    flower = args[0]
    flowers = {
        "rose": rose,
        "sunflower": sunflower,
        "tulip": tulip,
    }

    try:
        display = flowers[flower]
    except KeyError:
        raise ValueError("Not a valid flower. Try rose, sunflower, or tulip!")
    else:
        display()


if __name__ == "__main__":
    main(sys.argv[1:]) # pragma: no cover
