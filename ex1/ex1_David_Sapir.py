"""--------------------------------------------------------

file: ex1_David_Sapir.py

Written by:
David Sapir, id = 208917351, login = davidsa

Program Description:
The program receives requests from the user to preform
operations.

The available operations are:
1 - Counts the same digits between 2 numbers.
    Input: 2 whole numbers.
    Output: How many of the digits of the first number
            appear in the second number.

2 - Perform operations on a stack that contains strings.
    The available operations are:
    i - Inserts a string into the stack.
    e - Removes a string from a stack.
    p - Prints the content of the stack

3 - Displays the best gens found from a given list of
    gens.
    Input: non
    Output: List of the best gens from the list.

4 - Decoding according to ROT-13.
    Input: A string.
    Output: The string after Decoding according
            to ROT-13.
--------------------------------------------------------"""


# ---------------------- consts section -----------------------
# consts for the main loop that reads the user's requests
SAME_DIGITS = "1"
STR_STACK = "2"
BEST_GENS = "3"
ROT_13 = "4"


# consts for stack operations
PUSH_BACK_STR = "i"
PRINT_STACK = "p"
POP_STR = "e"


# consts that hold the abc letter amount
ABC_LETTERS = 26
ROT_13_SHIFT = 13

# consts for gens list
GENS_LEN = 3


# ------------ lists to print the available operations --------------

# List to hold the operations list the user can select to preform
op_list = ["------------ list of operations -----------",
           "1 - Count same digits",
           "2 - Strings stack",
           "3 - List of best gens",
           "4 - Decoding according to ROT-13",
           "-------------------------------------------"]

# List to hold the available operations on a stack
stack_op_list = ["\n---------- Stack list operations ----------",
                 "i - Insert a string into the stack",
                 "e - Remove a string from a stack",
                 "p - Print the content of the stack",
                 "-------------------------------------------"]


# List to work as a stack to hold strings.
str_stack = []

# List to hold the gens.
genes_list = """B2B,HLA_A,AMHR2,590,0.12
B2B,HLA_A,AMICA1,592,0.12
B2B,HLA_A,AMIGO1,593,0.12
B2B,HLA_A,AMIGO2,594,0.12
B2B,HLA_A,AMIGO3,595,0.12
B2B,HLA_A,AMMECR1L,596,0.12
B2B,HLA_A,AMMECR1,597,0.12
B2B,HLA_A,AMN1,598,0.12
B2B,HLA_A,AMN,599,0.12
B2B,HLA_A,AMOTL1,600,0.12
B2B,HLA_A,AMOTL2,601,0.12
B2B,HLA_A,AMOT,602,0.12
B2B,HLA_A,AMPD1,603,0.12
B2B,HLA_A,AMPD2,604,0.12
B2B,HLA_A,AMPD3,605,0.12
B2B,HLA_A,AMPH,606,0.0019
B2B,HLA_A,AMTN,607,0.12
B2B,HLA_A,AMT,608,0.12
B2B,HLA_A,AMY1A,609,0.12
B2B,HLA_A,AMY2A,610,0.0019
B2B,HLA_A,AMY2B,611,0.12
B2B,HLA_A,AMZ1,612,0.12
B2B,HLA_A,AMZ2P1,613,0.12
B2B,HLA_A,AMZ2,614,0.12
B2B,HLA_A,ANAPC10,615,0.12
B2B,HLA_A,ANAPC11,616,0.12
B2B,HLA_A,ANAPC13,617,0.12
B2B,HLA_A,ANAPC16,618,0.12
B2B,HLA_A,ANAPC1,619,0.12
B2B,HLA_A,ANAPC2,620,0.0019
B2B,HLA_A,ANAPC4,621,0.0019
B2B,HLA_A,ANAPC5,622,0.12
B2B,HLA_A,ANAPC7,623,0.12
B2B,HLA_A,ANGEL1,624,0.12
B2B,HLA_A,ANGEL2,625,0.12
B2B,HLA_A,ANGPT1,626,0.12
B2B,HLA_A,ANGPT2,627,0.12
B2B,HLA_A,ANGPT4,628,0.12
B2B,HLA_A,ANGPTL1,629,0.12
B2B,HLA_A,ANGPTL2,630,0.12
B2B,HLA_A,ANGPTL3,631,0.12
B2B,HLA_A,ANGPTL4,632,0.12
B2B,HLA_A,ANGPTL5,633,0.12
B2B,HLA_A,ANGPTL6,634,0.12
B2B,HLA_A,ANGPTL7,635,0.12
B2B,HLA_A,ANG,636,0.12
B2B,HLA_A,ANK1,637,0.0019
B2B,HLA_A,ANK2,638,0.0019
B2B,HLA_A,ANK3,639,0.12
B2B,HLA_A,ANKAR,640,0.12
B2B,HLA_A,ANKDD1A,641,0.12
B2B,HLA_A,ANKFN1,642,0.0019
B2B,HLA_A,ANKFY1,643,0.12
B2B,HLA_A,ANKHD1,645,0.12""".split('\n')


# --------------------------- same_digits ----------------------------
# Reads to integer numbers from the user, runs over the first numbers
# digits and check for every digits if it exists.
# --------------------------------------------------------------------
def same_digits():
    print("\n--------- Count same digits ----------")

    print("Amount of same digits = " +
          str(count_same_digits(input("Enter first number: "),
                                input("Enter second number: "))))

    print("--------------------------------------")


# -------------------- count_same_digits ---------------------
# Count the amount of identical digits between 2 numbers.
# Returns the amount of identical digits found.
# ------------------------------------------------------------
def count_same_digits(num1, num2):
    same_digit = 0

    for num in num1:
        if num in num2:
            same_digit += 1

    return same_digit


# ------------- string_stack_management -------------
# Manages a stack of strings.
# Directs the user to a function that will perform
# the desired action the user wants to perform.
# The available operations are:
# i - Insert a string into the stack
# e - Remove a string from a stack
# p - Print the content of the stack
# --------------------------------------------------
def string_stack_management():
    while True:
        op = get_operation(stack_op_list)
        if op == PUSH_BACK_STR:
            push_str()
        elif op == POP_STR:
            if not pop_str():
                break
        elif op == PRINT_STACK:
            print_stack()
        else:
            break
        print("")


# ----------------- push_str ------------------
# Inserts a new string into the stack(list).
# ---------------------------------------------
def push_str():
    str_stack.append(input("Enter a string: ")[1:])


# ------------ pop_str ------------
# Pops an element out of the stack.
# ---------------------------------
def pop_str():
    if not str_stack:
        return False
    else:
        str_stack.pop()
        return True


# ----------------- print_stack -------------------
# Prints the stack content.
# -------------------------------------------------
def print_stack():
    print("\n---------- stack contains ----------")

    if len(str_stack) == 0:
        print("The stack is empty")
    else:
        for i in range(len(str_stack)):
            print(str(i) + " | " + str_stack[i])

    print("------------------------------------")


# --------------- find_best_gens ---------------
# Finds good gens inside a list of gens.
# Prints the set of good gens after selecting
# them.
# ----------------------------------------------
def find_best_gens():
    good_gens = set([])
    for gens in genes_list:
        curr_gen = gens.split(',')
        if is_good_gen(curr_gen):
            for i in range(GENS_LEN):
                good_gens.add(curr_gen[i])

    print_good_gens(good_gens)


# ---------- is_good_gen ----------
# Returns if a gen is good or not.
# ---------------------------------
def is_good_gen(gens):
    if float(gens[-1]) < 0.1:
        return True
    else:
        return False


# ---------------------- print_good_gens -----------------------
# Prints the good gens found in the given list.
# --------------------------------------------------------------
def print_good_gens(good_gens):
    print("\n-------------- Good Gens List --------------\n" +
          str(sorted(good_gens)) +
          "\n--------------------------------------------")


# ----------------------- rot_13_decoding ----------------------
# Decoding according to ROT-13.
# Reads a string from the user and preforms a Decoding according
# to ROT-13.
# --------------------------------------------------------------
def rot_13_decoding():
    print("\n-------------- ROT-13 Decoding --------------")
    print("Decoded string: " +
          rot_13_decode(input("Enter a string to decode: ")))
    print("---------------------------------------------")


# --------------- rot_13_decode -----------------
# Runs over the characters of the string the
# user wants to wants to decode and changes
# the characters according to the ROT-13
# Decoding.
# -----------------------------------------------
def rot_13_decode(string):
    decoded_word = ""
    for s in string:
        decoded_word += decode_letter(s)

    return decoded_word


# --------------------- decode_letter ---------------------
# Receives a character and returns it after being decoded.
# ---------------------------------------------------------
def decode_letter(letter):
    if letter.islower():
        return lower_letter_decode(letter)
    elif letter.isupper():
        return upper_letter_decode(letter)
    else:
        return letter


# ------------------ lower_letter_decode -----------------------
# Decodes a lower letter using a Caesar cipher (ROT-13).
# --------------------------------------------------------------
def lower_letter_decode(letter):
    return chr(ord('a') + ((ord(letter) - ord('a') +
                            ROT_13_SHIFT) % ABC_LETTERS))


# ------------------ upper_letter_decode -----------------------
# Decodes a capital letter using Caesar cipher (ROT-13).
# --------------------------------------------------------------
def upper_letter_decode(letter):
    return chr(ord('A') + ((ord(letter) - ord('A') +
                            ROT_13_SHIFT) % ABC_LETTERS))


# ---------------- get_operation ----------------
# Get a wanted prompt and prints it to the user.
# After printing the prompt, it reads the wanted
# operation from the user.
# -----------------------------------------------
def get_operation(operations):
    print_prompt(operations)
    return input("Enter operation: ")


# -------- print_prompt ---------
# Prints a prompt.
# -------------------------------
def print_prompt(operations):
    for op in operations:
        print(op)


# ------------------------- run ---------------------------
# The main loop that receives requests from the user.
# Directs the user to a function that will perform the
# desired action the user wants to perform.
# The available operations are:
# 1 - Counts the same digits between 2 numbers.
# 2 - Perform operations on a stack that contains strings.
# 3 - Displays the best gens found from a given list of
#     gens.
# 4 - Decoding according to ROT-13.
# --------------------------------------------------------
def run():
    while True:
        request = get_operation(op_list)
        if request == SAME_DIGITS:
            same_digits()
        elif request == STR_STACK:
            string_stack_management()
        elif request == ROT_13:
            rot_13_decoding()
        elif request == BEST_GENS:
            find_best_gens()
        else:
            break
        print("")


run()
print("")

exit(0)
