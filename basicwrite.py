import os, sys # for file path
import re  # mod strings regex
import fnmatch as wildcardhandler # to remove files in copy directory

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if not path in sys.path:
    sys.path.insert(1, path)
del path


#Todo: add in some functionality to split human format,
# single columns included in bad csv file to text description file,
# csv data to seperate csv file

#Todo: steps: Convert cvs non column match to descriptive txt.
# Convert column data to pd dataframe, and dataframe to Csv file.
# Load csv into mysql table.  Load descriptive file into mysql table.  Link with common Identifier.

#Bug exist:  code is NOT being executed within skip path, as only 1 dupe occures at a time.
#Howver, when still in non skip path there is a bug where it fails to check for dupe, thus there will always be one off

def format_file():

    DataDirectory = '/TestData'  # ) sources the path to the csv file for format standardization

    # Define working directory (Read file directory)
    working_dir = ''.join([os.getcwd(), DataDirectory, '/'])

    # Define file directory for copy placement, make sure to not dupe any files in here (write directory)
        #Todo: add in wild card handler to skip directory so it handles sub directories and files

    skip_copy_directory = ''.join([working_dir, 'Copy_Formatted_Files','/'])
    #skip_copy_directory = ''.join([working_dir, 'Copy_Formatted_CSV_Files','/'])
    #skip_copy_directory_txt = ''.join([working_dir, 'Copy_Formatted_TXT_Files', '/'])



    # ) walks thru every file/dir/root in working directory

    for root, dirs, files in os.walk(working_dir):

        current_path = root

        for filename in files:  # looks thru every file

            # if not skipdirectory then do the below logic
            if current_path != wildcardhandler.fnmatch(skip_copy_directory, '*'):  # try and prevent any logic from executing in directory and sub/files not 100% successful
                print(current_path)

                    #Todo:  try instead of adding it to harcoded path, instead add fnmatch to if logic in order
                    # to skip directory and prevent duplicates

                # check if copy file already exist/ delete if old version/ create new if none
                exist_dircheck = os.path.isdir(skip_copy_directory)
                exist_filecheck = os.path.isfile(''.join([skip_copy_directory, filename]))


                # Make files in new directory, Remove and remake if already there
                if exist_dircheck:
                    if exist_filecheck:

                        try:
                            os.remove(wildcardhandler.fnmatch(exist_filecheck,'*')) #remove dupes, does not preventtheir creation tho (!!!! failed !!!)
                        except:
                            pass

                        file = open(''.join([skip_copy_directory, filename, '_formatted.csv']), 'w+') # (this is the write file for csv conversion moved inside if logic to fix dup bug
                    else:
                        file = open(''.join([skip_copy_directory, filename, '_formatted.csv']),'w+')  # (this is the write file for csv conversion moved inside if logic to fix dup bug

                else:
                    os.mkdir(skip_copy_directory)
                    file = open(''.join([skip_copy_directory, filename, '_formatted.csv']), 'w+') # (this is the write file for csv conversion moved inside if logic to fix


                # dupe bug still present

                #Todo Write Text file (create file) code goes here



                #)File content formatting and duplications Steps


                with open(os.path.join(working_dir,'Test.csv'), 'r', newline='') as file_data: # this is the read file

                    #Todo Strip mismatched column data goes here, count max columns,
                    # only write if column data equal to max columns,
                    # write anything less then max columns into text file





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