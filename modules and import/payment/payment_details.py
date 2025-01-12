# import os,sys
# from os.path import dirname , join,abspath
# sys.path.insert(0,abspath(join(dirname(__file__),"..")))
# from courses import course_details
# def payment():
#     print("this is my payment details")

import os,sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))
from courses import course_details

def payment():
    """Prints payment details."""
    print("This is my payment details.")

if __name__ == "__main__":
    course_details.course()
    payment()