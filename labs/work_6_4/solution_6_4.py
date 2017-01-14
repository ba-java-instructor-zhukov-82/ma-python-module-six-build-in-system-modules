# Set coding of the script as “utf8”
# -*- coding: utf8 -*-

# Import argparse module
import argparse


# Create parser object
parser = argparse.ArgumentParser()


# Add parser argument with key “–l”, string type, “ua” as default value and add any
# help string for key. Store this value into lang variable
parser.add_argument("-l",'--lang', type=str, default='ua',
                    help= "Choose language abbreviation! (Ex. 'ua','en')")


# Add parser argument with key “–c”, string type, “word” as default value and add
# any help string for key.Store this value into keyword variable
parser.add_argument("-c", '--keyword', type=str, default='word',
                    help= "Choose word for filter! (Ex. 'hello')")


# dd parser argument with key “–m”, integer type, “0” as default value and add
# any help string for key.Store this value into value variable
parser.add_argument("-m", '--value', type=int, default=0,
                    help= "Choose number of the best moody for tweets! (Ex. '10', '-12')")


# Check that executable script __name__ variable is equal to "__main__"
# If yes print next:
# 3 variables are script arguments

args = parser.parse_args()
lang = args.lang
keyword = args.keyword  # .encode('utf8')
value = args.value


if __name__ == '__main__':
    print ('Parcer initialized!')
    print (lang, keyword, value)


# PyCharm Terminal:
#
# cd labs/work_6_4
# python3 solution_6_4.py -l 'en' -c 'hello' -m '5'
# python3 solution_6_4.py -l 'ua' -c 'привіт' -m '5'
