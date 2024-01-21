# Open the input file in read mode and output file in write mode
with open('input.txt', 'r') as infile, open('output10.txt', 'w') as outfile:
    # Read the numbers from the input file
    numbers = [int(num.strip()) for num in infile.readlines()]

    for num in numbers:
        abc = []
        temp_num = num
        while temp_num > 0: 
            temp = temp_num % 2 
            abc.append(temp) 
            temp_num = int(temp_num / 2) 
        abc.reverse() 

        # Write the binary representation to the output file
        outfile.write("Binary representation of " + str(num) + " is: " + str(abc) + "\n")
