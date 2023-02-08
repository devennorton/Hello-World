char_position = 0
lowecase_chars = ['countat1','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
return_message = "Position of alphabet: {char_position}"
character_argument_max_len = 1
    
def position(character_argument: str) -> str:
    """with a letter, return its position in the alphabet
    
    Args:
    String, a single character 
    
    Returns
    String, a string in the format of 'Position of alphabet: char_position'
    
    Raises
    ca
    """
    
    # Sanity Checks
    if not (isinstance(character_argument, str) and len(character_argument) == character_argument_max_len):
        raise ValueError("You're SOOO stoooodpid.")
        
    if character_argument not in lowecase_chars:
        raise ValueError("YOU GET NOTHING")
    
    # Logic
    char_position = lowecase_chars.index(character_argument)
    
    return return_message.format(char_position=char_position)
