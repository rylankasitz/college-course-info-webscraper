import lib.general.logger as logger

from os import listdir
from os.path import isfile, join, realpath, dirname

TYPES = ['integer', 'text', 'bit']
PREFIX_WORDS = ['CREATE', 'TABLE', 'IF', 'NOT', 'EXISTS']

TABLE_PATH = dirname(realpath(__file__)) + "/../../sql/tables/"
MODEL_PATH = dirname(realpath(__file__)) + "/../../bin/table_models/"

AUTO_GEN_COMMENT = '''#############################################################################
###################### THIS IS AN AUTO GENERATED CLASS ######################
#############################################################################\n\n'''

def generate_models():
    for f in listdir(TABLE_PATH):
        generate_model(TABLE_PATH + f)


def generate_model(file_name):
    attributes = []
    name = ''
    
    with open(file_name) as reader:
        content = reader.read()
        prefix = content.split('(', 1)[0]
        data = content.split('(', 1)[1]
        prefix_words = prefix.split(' ')

        for p_word in prefix_words:
            if not p_word.upper() in PREFIX_WORDS and not p_word == '':
                name = p_word

        words = data.split(' ')

        for i, word in enumerate(words):
            if word.lower().replace(',', '') in TYPES:
                attributes.append(words[i-1])
            
    generate_class_file(name, attributes)

def generate_class_file(name, attributes):
    f = open(MODEL_PATH + name + ".py", "w")

    f.write(AUTO_GEN_COMMENT)
    f.write("class " + name + ":\n\tdef __init__(self):\n")

    for attribute in attributes:
        f.write("\t\tself." + attribute + " = None\n")
    f.close()

    logger.log("created class model " + name)