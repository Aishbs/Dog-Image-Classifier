# Image Classification for a City Dog Show

## **Overview**

This project is a dog image classifier project using a pre-trained convolutional neural network (CNN). The goal of the project is to determine which CNN model architecture (ResNet, AlexNet, or VGG) best achieves the following objectives:

* Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs.
* Correctly classify the breed of dog, for the images that are of dogs.

## **Model Architectures**

The three CNN model architectures used in this project are:

* **ResNet:** A deep residual network that has been shown to achieve state-of-the-art results on a variety of image classification tasks.
* **AlexNet:** A classic CNN architecture that was first introduced in 2012.
* **VGG:** A family of CNN architectures that are known for their depth and complexity.

## **Results**

The following table shows the results of the CNN models on the Oxford IIIT Pet Image Dataset:

| CNN Model Architecture: | % Not-a-Dog Correct | % Dogs Correct | % Breed Correct | % Match Labels |
|---|---|---|---|---|
| ResNet | 90.0% | 100.0% | 90.0% | 82.5% |
| AlexNet | 100.0% | 100.0% | 80.0% | 75.0% |
| VGG | 100.0% | 100.0% | 93,3% | 87.5% |

Given our results, the "best" model architecture is VGG. It outperformed both of the other architectures when considering both objectives 1 and 2. You will notice that ResNet did classify dog breeds better than AlexNet, but only VGG and AlexNet were able to classify "dogs" and "not-a-dog" at 100% accuracy. The model VGG was the one that was able to classify "dogs" and "not-a-dog" with 100% accuracy and had the best performance regarding breed classification with 93.3% accuracy.

## **Conclusion**

The VGG model is the best CNN model architecture for classifying dog images.
