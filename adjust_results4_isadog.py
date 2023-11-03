# PROGRAMMER: Aishwarya B S
# DATE CREATED: 31st Oct, 2023                                
# REVISED DATE: 2nd Nov 2023

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """  
    
    # Load the list of dogs from the dogfile
    with open(dogfile, "r") as f:
        dog_names = [line.rstrip() for line in f]

    # Iterate over the results dictionary
    for result in results_dic.values():
        # Get the pet label
        pet_label = result[0]

        # Get the classifier label
        classifier_label = result[1]

        # Set the is_a_dog flag
        is_dog = int(pet_label in dog_names)
        as_dog = int(classifier_label in dog_names)

        # Update the results dictionary
        result.append(is_dog)
        result.append(as_dog)
