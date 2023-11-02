# PROGRAMMER: Aishwarya B S 
# DATE CREATED: 31st Oct, 2023                                
# REVISED DATE: 2nd Nov 2023

# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Declare results dict
    results_dic = {}

    # Get the list of filenames in the image directory
    filenames = listdir(image_dir)

    # Extract the pet image labels from the filenames
    for name in filenames:
        if name.startswith('.'):
            continue
        pet_name = ""
        pre_name = name.lower().split("_")
        for word in pre_name:
            pet_name = ' '.join([word for word in pre_name if word.isalpha()])
        results_dic[name] = [pet_name.strip()]
        print("Filename=", name, "  Pet Label=", results_dic[name][0])
        
    # return results
    return results_dic
