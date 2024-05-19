# Image Generation Machine Learning Model for Chess Piece Classification using the Image Data Set:
 **Data-set** https://www.kaggle.com/datasets/niteshfre/chessman-image-dataset
 **Google Drive Link:** https://drive.google.com/drive/folders/1VBTOCduA1bPF0c9Rur5MYaoxbF5m9y0L?usp=sharing
**Written By:** Alejandro Ruiz Garcia Rojas

## Selected Data Set
The selected Dataset was a dataset procuring images of chess pieces intended for their classification. The Data set is divided in 6 classes, depicting the diferent pieces within the game, regardless of their color, only taking into account their shape. The idea of this Model is to use this data-set to be able to clasify any chess piece by it's type, regardless of the color that the piece is.

The Data-set was obtained from kaggle, through the following link:
 https://www.kaggle.com/datasets/niteshfre/chessman-image-dataset
 
## Data Set Splitting
When generating Models it is important that we divide our Data-Sets in a Testing and Training Distribution, so that we can avoid any bias from the model when it comes to real/unforseen data. That is to say, we won't know for sure how the model would perform with real data, if we only know how it'd perform with training data. Because of that, we split our data in two, so that we can keep the training data as a "Real Example/Unseen example" and validate it's performance with data with which it was not trained on.

How do you determine the split however? Common practice indicates the use of the Pareto Principle, which states that 20% of the causes lead to 80% of all outcomes in most probability cases. [1] This has been empirically proven throughout history to be a common trend when it comes to data, and as such, it is a good practice to base our model on, as we will recieve 80% of the results we would obtain by using a 20% distribution of testing data. 

So the split of the data would be distributed like so:
- 80% - Training Data
- 20% - Testing Data

But we can split our training data even further, to allow for "validation", a process similar to testing, but used for the purpose of re-aligning or fixing hyperparameters within the model. Sort of like a "fine-tuning" process to better train the model once more after the initial training was done.

With that in mind, we can split our Data like so:
- 70% - Train Data
- 10% Validation Data
- 20% Testing Data

This split is conducted by importing the library ```split-folders```[2] which automatically splits the folders according to the parameters you give it.

We use ```splitfolders.ratio('Data',output="output",seed=1337,ratio=(0.7,0.1,0.2))```. The first parameter being the input folder, followed by the output folder, then a seed for randomation, followed by the ratio in which the images should be distributed.

The command should procure the following result:

- train
- val
- test

each folder containing it's appropriate distribution of images.

From then on, we use ```tensorflow``` in order to train, test, and pre-process our model. [4]

## Data Augmentation and Pre-Processing
Data Augmentation is a method in which we gather more data for our model, by editing, changing, rotating, or altering our pre-existing images and allowing the model to also train itself with the altered images. Using matrix operations, we generate more images or variations of them in order to give our model more data to train on. [3]

Within the code, we can see this being done through the functions of
- ```rescale``` rescaling the image
- ```rotation_range``` rotating the image within a given range
- ```width_shift_range``` Changing width within a range.
- ```height_shift_range``` Changing height within a range.
- ```shear_range``` Stretching out an image within a range.
- ```zoom_range``` Zooming in or out of the image within a range.
- ```horizontal_flip``` Flipping the image horizontally.

### Storing to disk
When training, you can store the model to the local disk by using ```save_to_dir``` giving it the corresponding path.
Additionally, you can add a prefix and format using ```save_prefix``` and ```save_format```

## Building and Training Model:
WIP

## References
[1] R. Dunford "The Pareto Principle" *Plymouth*,2014 Available: https://pearl.plymouth.ac.uk/bitstream/handle/10026.1/14054/TPSS-2014-Vol7n1_140-148Dunford.pdf?sequence=1&isAllowed=y [Accessed May 17,2024]
[2]J. Filter "splitfolders" 2022 Available: https://pypi.org/project/split-folders/ [Accessed May 17,2024]
[3] "What Is Data Augmentation?" *Amazon Web Services*, 2024 Available: https://aws.amazon.com/what-is/data-augmentation/#:~:text=Data%20augmentation%20is%20the%20process,machine%20learning%20(ML)%20models. [Accessed May 17,2024]
[4] "Tensorflow API Documentation" *Tensorflow* Available: https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator#flow_from_directory [Accessed May 17, 2024]


