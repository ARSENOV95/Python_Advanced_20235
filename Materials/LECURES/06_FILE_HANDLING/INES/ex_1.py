import os 
from ABSOLUTE_PATH import ABSOLUTE_PROJECT_PATH

#relative path
#path = os.path.join('Materials','LECURES','06_FILE_HANDLING','INES','LAB_FILES','EX_1','text.txt')
path = os.path.join(ABSOLUTE_PROJECT_PATH,'LAB_FILES','EX_1','text.txt')
#abolsute path gives for the patho from D drive till the root dirctory of the ABSOLUTE_PATH file - ..\06_FILE_HANDLING\INES
#ABOSLUTE PATH is the better practice as we only need to chagne tha abpslute path to the project path 

try:
    open(path)
    print('File found')
except:
    print('File not found')

#Note - use pwd to to find current direcotry and navigate D:\Files\SOFT_UNI\Python_Advanced_20235>