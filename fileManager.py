from os import listdir
from os.path import isfile, join
import os
import shutil

def sort_files_in_a_folder(mypath):
    '''
    A function to sort the files in a download folder
    into their respective categories
    '''
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file_type_variation_list=[]
    filetype_folder_dict={}
    for file in files:
        try:
            filetype=file.split('.')[1]
            print('filetype is: ', filetype)
            if filetype == 'DS_Store':
                continue
            if filetype not in file_type_variation_list:
                file_type_variation_list.append(filetype)
                new_folder_name=mypath+'/'+ filetype + '_folder'
                filetype_folder_dict[str(filetype)]=str(new_folder_name)
                if os.path.isdir(new_folder_name)==True:  #folder exists
                    continue
                else:
                    os.mkdir(new_folder_name)
        except:
            pass
    for file in files:
        try:
            if file == '.DS_Store':
                continue
            src_path=mypath+'/'+file
            filetype=file.split('.')[1]
            if filetype in filetype_folder_dict.keys():
                dest_path=filetype_folder_dict[str(filetype)]
                shutil.move(src_path,dest_path)
            print(src_path + '>>>' + dest_path)
        except:
            pass

if __name__=="__main__":
    mypath='/Users/christiangould/Downloads'
    sort_files_in_a_folder(mypath)
