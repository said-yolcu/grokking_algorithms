# Put an array and a hash function together, and you have a hash table

# Returns 1 always
def hash_1(x):
    return 1

# Returns length of string modulo 10
def hash_len(x):
    return len(x) % 10

# Adds up int values of chars and returns modulo 10
def hash_char(x):
    val = ord(x[0])
    if ord('A') <= val <= ord('Z'):
        return (val-ord('A')) % 10
    elif ord('a') <= val <= ord('z'):
        return (val - ord('a')) % 10
    else:
        return None

# Each character has a prime value. For each input string adds up
# prime values of its char and returns this val modulo 10
def hash_prime(x):
    arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
           43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    sum = 0

    for char in x:
        sum += arr[(ord(char)-ord('a'))%26]

    return sum % 10

# Each array hash function pair represents a hash table

arr_1 = [list() for i in range(10)]

arr_len = [list() for i in range(10)]

arr_char = [list() for i in range(10)]

arr_prime = [list() for i in range(10)]

# Test function adds the input to each hash table. In each test we see 
# that the prime hash table distributes the given input more balancedly
def test(input):
    for el in input:
        arr_1[hash_1(el)].append(el)
        arr_len[hash_len(el)].append(el)
        arr_char[hash_char(el)].append(el)
        arr_prime[hash_prime(el)].append(el)


if __name__ == "__main__":
    input_1 = ["Esther", "Ben", "Bob", "Dan"]
    input_2 = ["A", "AA", "AAA", "AAAA"]
    input_3 = ["Maus", "Fun", "Home", "Watchmen"]
    test(input_3)

    print("arr_1", arr_1)
    print("arr_len", arr_len)
    print("arr_char", arr_char)
    print("arr_prime", arr_prime)
