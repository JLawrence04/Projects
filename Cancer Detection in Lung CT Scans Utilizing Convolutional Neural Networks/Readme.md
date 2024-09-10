# Cancer Detection in Lung CT Scans Utilizing Convolutional Neural Networks

One of the reasons I’ve decided to major in Data Science is the impact the field can have on people’s lives and possibly even save lives in the medical field through methods like computer vision and neural networks which I used in this project. I created a project utilizing neural networks and I tuned and experimented with a convolutional neural network (CNN) to accurately classify lung CT scans as normal, benign, or malignant. The tuning and experimentation was pretty successful as I was able to achieve a 95% classification rate on the test set, images the model was not exposed to during the training stage. This project helped me learn how data science and machine learning can be used to help doctors make diagnosis for patients


## Key Steps Taken in Project
- Pulled images from stored file one-by-one and stored file path and classification of image in dataframe
- Resized images to reduce computational cost and to have uniformity for the model.
- Split data into train and test sets, normalized pixel values and did random image augmentations on training images so the model could generalize the patterns of the images better.
- Experimented with DenseNet 121 CNN model, class weights, and creating CNN model from scratch to find best performing model.


## Dataset Used
Dataset of lung CT scans was found on Kaggle and can be accessed by clicking this [link](https://www.kaggle.com/datasets/adityamahimkar/iqothnccd-lung-cancer-dataset).


## Models Experimented With

### Using DenseNet 121 Model as Feature Extractor for CNN model
Unlike a traditional CNN, DenseNet models have 'connectivity' between layers, layers aren't just connected to their previous layer, they are connected to all layers preceeding them. This leads to less parameters being needed and the model being computationally more efficient.

With the relatively small dataset being used for this project, using a pretrained model like DenseNet 121 as the feature extractor can help prevent overfitting since the model has already been trained on a much larger dataset(Imagenet) and can be adjusted and generalized to the specific dataset being used in this project.

### DenseNet 121 Feature Extractor CNN model with Class Weights
When looking at the project Jupyter Notebook, there is a huge imbalance between the amounts of images for each classification. So I decided I would experiment to see if using class weights for each classifcation will improve model performance.

### Custom Made CNN
Last model I experimented with was my own CNN model from scratch and seeing if I can improve upon the performance of the DenseNet models. I wasn't able to achieve the same accuracy and validation loss metrics as the previous models, but through experimentation and tuning the model I was able to raise the final model accuracy from 45-50% the first time I ran the model, to an accuracy of 70-75%.


## Results/Takeaways
### Results (Test Set Accuracy)
**CNN Model With DenseNet 121 Feature Extractor**: ~95% accuracy

**CNN Model With DenseNet 121 Feature Extractor and Class Weights:** ~91-93% accuracy

**Custom/Scratch made CNN Model:** ~70-75 accuracy (Model performance varied much more between epochs compared to the DenseNet 121 models)

When it came to minimizing the model’s loss function, the DenseNet 121 model with no class weight performed the best again at around .15, the loss function value for the class weights model was around .3, and the custom/scratch model had a loss function value around .6 to .7(way more varied results for every epoch compared to the other models again).

### Conclusion

As shown by the accuracy and loss metrics, the models using transfer learning (DenseNet 121) performed much better than the CNN I built from scratch. The findings from this project kind of reinforce the idea of using a transfer learning model as the feature extractor for a CNN model when you are dealing with a relatively small dataset. DenseNet and other transfer models are trained on huge datasets which perform well at generalizing and adjusting to smaller datasets like the one used in this project. Using these transfer learning models as the feature extractors for an image recognition task that utilizes a small dataset helps preventing overfitting, as that became an issue with the custom CNN I made with custom feature extracting layers.
