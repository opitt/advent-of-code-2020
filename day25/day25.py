#The handshake used by the card and the door involves an operation that transforms a subject number. 

def find_secret_loopsize(public_key):
    # The card transforms the subject number of 7 according to the card's secret loop size.
    # which we reverse engineer here, as we know the PK
    secret_subject_number = 7
    # To transform a subject number, start with the value 1. 
    value = 1
    # Then, a number of times called the loop size, perform the following steps:
    loop_size = 1
    while True:
        # Set the value to itself multiplied by the subject number.
        value *= secret_subject_number
        # Set the value to the remainder after dividing the value by 20201227.
        value = value % 20201227
        if value == public_key:
            break
        loop_size += 1
    return loop_size

def calc_key(my_loopsize, subject_numer):
    value = 1
    for _ in range(my_loopsize):
        value *= subject_numer
        value = value % 20201227
    return value

def main():    
    #input
    pk = [8252394, 6269621]
    loopsize = [find_secret_loopsize(p) for p in pk]
    for ls in list(zip(pk,loopsize)):
        print(f"(Public key, Loop size): {ls}") 
        # loopsize: [18739604,  5166072]
    
    # At this point, you can use either device 's loop size with the other device' s public key to calculate the encryption key.
    # Transforming the subject number of 17807724 (the door's public key) 
    # with a loop size of 8 (the card's loop size) produces the encryption key, 14897079. 
    encryption_key = calc_key(loopsize[0], pk[1])

    print(f"Encryption key: {encryption_key}") # 181800

main()
