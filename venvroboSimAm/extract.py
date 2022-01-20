#import Zip file.
import zipfile
# import rarfile
import rarfile
# for path checking.
import os.path
# deleting directory.
import shutil

def check_archrive_file(loc):
    '''
    check the file is an archive file or not.
    if the file is an archive file just extract it using the proper extracting method.
    '''
    # check if it is a Zip file or not.
    if (loc.endswith('.zip') or loc.endswith('.rar')):
        # chcek the file is present or not .
        if os.path.isfile(loc):
            #create a directory at the same location where file will be extracted.
            output_directory_location = loc.split('.')[0]
            # if os path not exists .
            if not os.path.exists(output_directory_location):
                # create directory .
                os.mkdir(output_directory_location)
                print(" Otput Directory " , output_directory_location)
                # extract
                if loc.endswith('.zip'):
                    extractzip(loc,output_directory_location)
                else:
                    extractrar(loc,output_directory_location)

            else:
                # Directory allready exist.
                print("Otput Directory " , output_directory_location)
                # deleting previous directoty .
                print("Deleting old Otput Directory ")
                ## Try to remove tree; if failed show an error using try...except on screen
                try:
                    # delete the directory .
                    shutil.rmtree(output_directory_location)
                    # delete success
                    print("Delete success now extracting")
                    # extract
                    if loc.endswith('.zip'):
                        extractzip(loc,output_directory_location)
                    else:
                        extractrar(loc,output_directory_location)
                except OSError as e:
                    print ("Error: %s - %s." % (e.filename, e.strerror))
        else:
            print("File not located to this path")
    else:
        print("File do not have any archrive structure.")


def extractzip(loc,outloc):
    '''
    using the zipfile tool extract here .
    This function is valid if the file type is Zip only
   '''
    with zipfile.ZipFile(loc,"r") as Zip_ref:
        # iterate over Zip info list.
        for item in Zip_ref.infolist():
            Zip_ref.extract(item,outloc)
        # once extraction is complete
        # check the files contains any Zip file or not .
        # if directory then go through the directoty.
        Zip_files = [files for files in Zip_ref.filelist if files.filename.endswith('.zip')]
        # print other Zip files
        # print(Zip_files)
        # iterate over Zip files.
        for file in Zip_files:
            # iterate to get the name.
            new_loc = os.path.join(outloc,file.filename)
            #new location
            # print(new_loc)
            #start extarction.
            check_archrive_file(new_loc)
        # close.
        Zip_ref.close()


def extractrar(loc,outloc):
    '''
    using the rarfile tool extract here .
    this function is valid if the file type is rar only
   '''
   #check the file is rar or not
    if(rarfile.is_rarfile(loc)):
        with rarfile.RarFile(loc,"r") as rar_ref:
                # iterate over Zip info list.
                for item in rar_ref.infolist():
                    rar_ref.extract(item,outloc)
                # once extraction is complete
                # get the name of the rar files inside the rar.
                rar_files = [file for file in rar_ref.infolist() if file.filename.endswith('.rar') ]
                # iterate
                for file in rar_files:
                    # iterate to get the name.
                    new_loc = os.path.join(outloc,file.filename)
                    #new location
                    # print(new_loc)
                    #start extarction.
                    check_archrive_file(new_loc)
                # close.
                rar_ref.close()
    else:
        print("File "+loc+" is not a rar file")

#location = input('Please provide the absolute path of the Zip/rar file-----> ')
#check_archrive_file('C:\\Users\\Equiplano\\Downloads\\SimAm\\2013\\00.zip')