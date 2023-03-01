def read_file(file_name):
    ### WRITE SOLUTION HERE
    j=""
    with open(file_name) as f:
        j=f.read()
    return j

    raise NotImplementedError()

def read_file_into_list(file_name):
    ### WRITE SOLUTION HERE
    l=[]
    with open(file_name) as f:
        l=f.readlines()
    return l
    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    ### WRITE SOLUTION HERE
    with open(output_filename,"w") as f:
        f.write(file_contents.partition('\n')[0])
    return file_contents.partition('\n')[0]

    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    ### WRITE SOLUTION HERE
    k=[]
    list=[]
    with open(file_name,'r') as f:
        k=f.readlines()
    for i in range(len(k)):
        if i%2!=0:
            list.append(k[i])
    return list
    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    l=[]
    list=[]
    with open(file_name,"r") as f:
        l=f.readlines()
    for i in range(len(l)):
        print(i)
        list.append(l[-(i+1)])
    print(list)
    return 0

    raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()