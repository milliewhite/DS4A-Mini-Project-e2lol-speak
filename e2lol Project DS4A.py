#Millie White
#lolspeak Project
#4/10/2021

def opening_file(file_name): 
    """
    get file from user and open it and save as list of strings with newlines
    
    
    Arguments:
    file_name.
    
    Outputs:
    list of words.
    
    """
    file = open(file_name+'.txt', "r")
    words = file.readlines()
    return words  



def remove_newlines(word):
    """
    
    remove newlines from a list of strings
    
    Arguments:
    a list of strings with a newline character.
    
    Outputs:
    a list of strings with no newline character.
    
    """
    word = word.replace("\n", "")
    return word



def list_of_clean_words(words):
    """
    call remove_newlines function and remove newlines from strings and saves in new list
    
    Arguments:
    list of strings with newlines.
    
    Outputs:
    a list of strings without newlines.
    """
    list_of_words=[]
    for word in words:
        cleanword = remove_newlines(word)
        list_of_words.append(cleanword)
    return list_of_words






def finalize_list(big_list):
    """
    replace words in cleaned list appearing in the dictionary
    keys with the dictionary values
     
    Arguments:
    big_list - a list of lists
    
    Outputs:
    final_list

  """

    #load json file into dictionary
    
    import json, requests
    url = 'https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json'
    resp = requests.get(url)
    data = json.loads(resp.text)
   
    final_list = []
    for list_of_words in big_list:
        partof_final_list = [data.get(item,item) for item in list_of_words]
        final_list.append(partof_final_list)
        
    return final_list







def save_lolspeakfile(file_name,final_list):
    """
    Save the lines produced by `finalize_list()`
    to a file called `file_name_lolcat.txt`
    
    Arguments:
    file_name,final_list
    
    Outputs:
    None.
    """
    
    new_file = open(file_name+'_lolcat.txt',"w")
    
    for line in final_list:
        new_file.write(" ".join(line)+'\n' )
    new_file.close()


    
def main():

    #ask user for the name of the file using input
    file_name = input('Enter file name :  ') #ask user for file name
    words = opening_file(file_name) #open the file and save as a list
    #print(words)

    list_of_words = list_of_clean_words(words) #remove newlines from the list
    print('List of strings with no newline',list_of_words)
    
    #convert list of strings to list of lists
    big_list=[]
    for line in list_of_words:
        #print(line.split())
        split_line = line.split()
        big_list.append(split_line)
    big_list
    print('List of lists',big_list)

    #replace words in the list that match the dict key with corresponding value
    final_list = finalize_list(big_list)
                           

    print('List of lists converted to lolspeak',final_list) #print final list

    save_lolspeakfile(file_name,final_list) #create lol file
    
main()
    
    
    
    
    
    
    


    