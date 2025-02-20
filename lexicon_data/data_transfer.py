current_language = {'lang':'en'}

dictionary = { 
    'human':'человек',
    'elf':'эльф',
    'ork':'орк',
    'beastmen':'зверолюд',
    'demon':'демон',
    'undead':'нежить',
    'warrior':'воин',
    'mage':'маг',
    'rogue':'плут',
    }

def data_return(word:str) -> str:

    if current_language['lang'].lower() == 'ru':
        return dictionary[word.lower()].title()
    elif current_language['lang'].lower() == 'en':
        return word.title()

