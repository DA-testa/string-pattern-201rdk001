# python3
# Kristaps Arnolds Kaidalovs 16.grupa 201RDK001

file_input = False
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    global file_input
    
    input_type = input().strip()
    if (input_type.upper() == "F"):
        file_input = True
        # open file
        file = open("tests/06")
        # read pattern string and text string to search through
        return (file.readline().rstrip(), file.readline().rstrip())

    elif (input_type.upper() == "I"):
        # read pattern string and text string to search through
        return (input().rstrip(), input().rstrip())

    else:
        raise RuntimeError(f"Invalid input type ({input_type})")

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    global file_input
    print(' '.join(map(str, output)) + (" " if file_input else ""))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    occurances = []
    
    p_len = len(pattern)
    p_hash = get_hash(pattern, p_len)
    t_hash = get_hash(text, p_len)

    for i in range(len(text)-p_len+1):
        if (p_hash == t_hash):
            if (pattern == text[i:i+p_len]):
                occurances.append(i)
        
        if (i != len(text)-p_len):
            t_hash = get_next_hash(t_hash, text, i, i+p_len)

    return occurances

def get_hash(text: str, len: int) -> int:
    result = 0

    for i in range(len-1):
        result = (10 * (result + ord(text[i]))) % 1021

    return (result + ord(text[len-1])) % 1021

def get_next_hash(prev: int, text: str, idx: int, next_idx: int) -> int:

    mult = 1
    for i in range(1, next_idx-idx):
        mult = (mult * 10) % 1021

    prev -= (ord(text[idx]) * mult) % 1021
    return (prev * 10 + ord(text[next_idx])) % 1021


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

