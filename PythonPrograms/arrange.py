
#use this with the 'inputfile' which is a binary text file 100 lines long each of 100 bytes 


import binascii
import string

def read_file(file_path):
    record_size = 100  # Each record is 100 bytes
    with open(file_path, 'rb') as f:
        record_num = 0
        unsortedkey = []
        unsortedref = []
        while True:
            # Read 100 bytes for each record
            record = f.read(record_size)
            if not record:
                break  # EOF reached
            
            # Separate the first 4 bytes (key) and the remaining 96 bytes
            key = record[:4]
            data = record[4:]
            
            
            # Convert key and data to hexadecimal strings for readability
            key_hex = key.hex()
            data_hex = data.hex()
            
            unsortedkey.append(key_hex)#(int(key_hex,16))
            unsortedref.append(data_hex)

            # Print key and data
            #print(f"Record {record_num+1}: Key = {key_hex}, Data = {data_hex}")
            record_num += 1
        
        
        for i in range(1, len(unsortedkey)):
            j = i
            while unsortedkey[j -1] > unsortedkey[j] and j > 0:
                unsortedkey[j-1], unsortedkey[j] = unsortedkey[j], unsortedkey[j-1]
                unsortedref[j-1], unsortedref[j] = unsortedref[j], unsortedref[j-1]
                j -= 1
        
        #print(unsortedkey)
        #for x in unsortedkey:
            #print(x)
        #print (unsortedref[0])


        f = open("outputfileascii.txt", "w")
        f.write("")
        f.close
        f = open("outputfilehex.txt", "w")
        f.write("")
        f.close
        i = 0
        while i <100:
            
            x = unsortedkey[i]
            y = unsortedref[i]  
            i += 1
            b = 0
            newarrayOne = []
            newarrayTwo = []
            newarrayThree = []
            stringOne = ""
            for a in x:
                b += 1
                stringOne += a
                if b == 2:
                    newarrayOne.append(stringOne)
                    newarrayThree.append(stringOne)
                    stringOne = ""
                    b = 0
            for c in y:
                b += 1
                stringOne += c
                if b == 2:
                    newarrayTwo.append(stringOne)
                    newarrayThree.append(stringOne)
                    stringOne = ""
                    b = 0
            #print(newarrayOne)
            #print(newarrayThree)
            
            k = 0
            ascii_string = ""
            for d in newarrayThree:
                value = int(d, 16)
        
                # Check if the value is within readable ASCII range
                if 0 <= value <= 127: #32<= value <= 126: << no corruption.
                    # Convert to ASCII character and append to result
                    ascii_string = chr(value)
                else:
                    # Use a dot or space as placeholder for non-printable characters
                    ascii_string = "."
            
                k += 1
                f = open("outputfilehex.txt", "a")
                f.write(d)
                #print(binascii.unhexlify(d))
                if k == 4:
                    f.write("   ")
                f.close

                f = open("outputfileascii.txt", "a")
                f.write(ascii_string)
                #print(binascii.unhexlify(d))
                if k == 4:
                    f.write("   ")
                f.close
            f = open("outputfileascii.txt", "a")   
            f.write("\n")
            #print(ascii_string)
            f.close
            f = open("outputfilehex.txt", "a")   
            f.write("\n")
            f.close

            

    
        #print (unsortedref[0])

            #print(initialkey)


            



read_file('inputfile')
