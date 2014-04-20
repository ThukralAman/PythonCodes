"""

Copyright Aman Thukral.



"""
import os

class Dir(object):
    """Represents the directory in file system.
       
    attributes: dir_path, parent_dir, child_dirs, child_files
    """
    
    def __init__(self, dir_path = "", parent_dir = "", child_dirs = [], child_files = []):
        self.dir_path = dir_path
        self.parent_dir = parent_dir
        self.child_dirs = child_dirs
        self.child_files = child_files
        self.get_files_and_dirs_in_dir()
        
    def __str__(self):            #### __str__ is a special method, like __init__, that is supposed to return a string representation of an object.
        return """
        dir Path : %s 
        Parent Directory path :  %s 
        child dirs : %s
        child files : %s""" % (self.dir_path, self.parent_dir, self.child_dirs, self.child_files)
        
    def print_dir(self):
        print str(self)            ### converts the given str(parameter) === parameter.__str__()    
        
    def get_files_and_dirs_in_dir(self) :
        filenames = os.listdir(self.dir_path)
        for filename in filenames :
            path = os.path.join(self.dir_path,filename)
            if os.path.isdir(path) :
                self.child_dirs.append(path)
            else:
                self.child_files.append(path)
                
        return (self.child_dirs , self.child_files)
        
        
    def check_if_file_exists_in_current_dir(self,search_filename) :
        """ loops over child_files to find a match and returns the paths of the found file as a list  """
        search_file_path = False
        search_filename = search_filename.lower()
        for file_path in self.child_files :
            directory, filename = os.path.split(file_path)
            if filename.lower() == search_filename :
                search_file_path = file_path
            
        return search_file_path
        
    #def check_if_file_exists_in_child_dirs(search_filename) :
        
        
    def check_if_file_exists(self,search_filename) :
        self.get_files_and_dirs_in_dir()
        file_path_list_current_dir = self.check_if_file_exists_in_current_dir(search_filename)

        
     

        
        
        
        
######## END CLASS ########

def find_file(search_filename,root_dir) :
    file_paths = []
    val = 0
    search_file_path = root_dir.check_if_file_exists_in_current_dir(search_filename)
    if search_file_path :
        file_paths.append(search_file_path)
        return file_paths
        
    else :
        for child_dir in root_dir.child_dirs :
            child_dir_obj = Dir(child_dir,"",[],[])
            one_element_list= find_file(search_filename,child_dir_obj)
            file_paths = file_paths + one_element_list
            
        return file_paths
        
            


def main() :
    shared_dir = Dir(r"C:\Users\amthukra\Desktop\Aman\New_Courses\Python\Python_oo")
    file_path = find_file('DELETE_file.txt',shared_dir)
    print file_path
    
    
    
if(__name__ == "__main__") :
    main()
        