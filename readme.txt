
This file countains instructions for how to run the textural feature retrieval program for tag classification utilizing LBP in Python.
The scripts generate files in .arff format, mostly to be read by Marsyas (more information about Marsyas can be found at http://marsyas.sness.net ).

The scripts are divided into train.py and test.py. Both import the "localbinarypatterns" python script, located in the pyimagesearch folder (provided by http://pyimagesearch.com for texture and pattern identification and classification). This script uses the function "local_binary_pattern", provided by the skimage library to extract the textural features from the input images.

The values of points and radius parameters for the LBP are already pre-determined as 2 and 122, respectively. Though, it can be modified as the user demands. These values were chosen due to the best results at the tag classification after a lot of testing phases.

It is assumed that the train.txt is a training list file, countaining the image path and the respective tags for each training image, and the test.txt is a testing list file, countaining only the image path for each testing image. 
Additionally, a tags.txt is also needed, countaining a list of all the possible tags used in the training file. The tags must be comma-delimited and should not be duplicated.

It is important that all the files paths in the lists are correct for the feature extraction.
If somehow the file is not found, the message "Error reading X file", being X the file name, will pop out and the script execution will not proceed.

The train.txt and test.txt files must be in the directory specified in the commands. The tags.txt must be in the same directory as the train.txt.

Commands:
> python train.py D:\user\folder\
> python test.py D:\user\folder\

These two commands will generate the respectively .arff files in the directory the python script is being executed.
