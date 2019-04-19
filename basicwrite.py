import os, sys # for file path
import re  # mod strings regex

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if not path in sys.path:
    sys.path.insert(1, path)
del path

def format_file(symbols=None):

    DataDirectory = 'WorkDemo'  # ) sources the path to the csv file for format standardization

    if symbols:
        symList = symbols.copy()  # uses the symbol list passed in
    else:
        symList = ['']  # if not passed make it blank

    for symbol in symList:  # goes thru all symbol in symlist and looks for a subfolder (symbol) tha contains csv files

        # Define working directory
        working_dir = ''.join([os.getcwd(), DataDirectory, symbol, '/'])

        # Define file directory for copy placement, make sure to not dupe any files in here
        skip_copy_directory = ''.join([working_dir, 'Copy_Formatted_Files','/'])

    # ) walks thru every file/dir/root in working directory

        for root, dirs, files in os.walk(working_dir):

            current_path = root

            for filename in files:  # looks thru every file

                # if not skipdirectory then do the below logic
                if current_path != skip_copy_directory:

                    # check if copy file alrady exist/ delete if old version/ create new if none
                    exist_dircheck = os.path.isdir(skip_copy_directory)
                    exist_filecheck = os.path.isfile(''.join([skip_copy_directory, filename]))


                    # Make files in new directory, Remove and remake if already there
                    if exist_dircheck:
                        if exist_filecheck:

                            try:
                                os.remove(''.join([skip_copy_directory, filename.strip]))  # correct file name later  (not removing file and copying it instead)
                            except:
                                pass
                    else:
                        os.mkdir(skip_copy_directory)


                    file = open(''.join([skip_copy_directory, filename]),'w+') # rip the butt off reattach copy marker (this is the write file)


                    #)File content formatting and duplications Steps


                    with open(os.path.join(working_dir,'Test.csv'), 'r', newline='') as file_data: # this is the read file

                        #Convert import file to list to prepare for formatting and copying
                        listconversion = list(file_data) # filedata converted to list form
                        split_list = [elements.split(',') for elements in listconversion] # split list into elements

                        # Formatting Outter List(broad, every character in entire list in every pocket)
                        stripped_list = [re.sub(r'\"', '', str(line)) for line in split_list]  # regex strip quotes from list
                        stripped_list = [re.sub(r'\'', '', str(line)) for line in stripped_list]  # regex strip newline from list
                        stripped_list = [re.sub(r'\\n', '', str(line)) for line in stripped_list]  # regex strip newline from list
                        stripped_list = [re.sub(r'\\r', '', str(line)) for line in stripped_list]  # regex strip newline from list


                        # go one list deeper
                        for outer_list_element in stripped_list: # layer 1 deep

                            #Formatting Inner String(narrow)
                            outer_list_element = re.sub(r'\[', '', outer_list_element)  # regex strip list marker left from string
                            outer_list_element = re.sub(r'\]', '', outer_list_element)  # regex strip list marker right from string
                            outer_list_element = outer_list_element.rstrip() # remove right side end white spaces, or whatever pattern you put into strip function
                            outer_list_element = outer_list_element.lstrip() # remove left side lead  whitespaces or whatever pattern you put into strip function
                            outer_list_element = re.sub(r'\,+$', '', outer_list_element)  # regex strip last misc coma

                            # start appending to blank copy line by line
                            file.write(outer_list_element)
                            file.write('\n')

                    file.close()

    return