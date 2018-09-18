
def additive_sequence(sequence):
    is_additive_sequence = True
    if not all(isinstance(item,int) for item in sequence):
        return False
    if len(sequence) < 3:
        return False
    if sequence[0] + sequence[1] == sequence[2] and len(sequence)>3:
        is_additive_sequence = True
        return(additive_sequence(sequence[1:]))
    if sequence[0] + sequence[1] != sequence[2]:
        is_additive_sequence = False
        return False
    else:
        return is_additive_sequence
        
print(additive_sequence([2,11, 13]))

        