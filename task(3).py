list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
list_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']


def encrypt_caesar(msg, shift=3):  # задание№3
    ret = ""
    for x in msg:
        if x in list_1:
            ind = list_1.index(x)
            ret += list_1[ind + shift]
        elif x in list_2:
            ind = list_2.index(x)
            ret += list_2[ind + shift]
        else:
            ret += x
    return ret


def decrypt_caesar(msg, shift=3):  # задание№4
    ret = ""
    for x in msg:
        if x in list_1:
            ind = list_1.index(x)
            ret += list_1[ind - shift]
        elif x in list_2:
            ind = list_2.index(x)
            ret += list_2[ind - shift]
        else:
            ret += x
    return ret


print(encrypt_caesar(input("Enter your encrypt word: ")))
print(decrypt_caesar(input("Enter your decrypt word: ")))
