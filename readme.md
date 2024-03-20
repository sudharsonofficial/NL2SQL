# NL2SQL Model - README

This file contains an NL2SQL model, which is based on the T5 (SimpleT5) model. The NL2SQL model is trained on two different datasets: the Spider Dataset and our custom dataset. 

## Dataset

- Spider Dataset: The Spider Dataset can be downloaded and used from the datasets library. Please refer to the code for details on how to download and utilize this dataset.

- Custom Dataset: We have also trained the model on our custom dataset.

## Model Variants

We provide two variants of the NL2SQL model, each trained on a different dataset. The differences between the variants are as follows:

1. Spider Dataset Variant:
   - Trained on the Spider Dataset.
   - Due to resource constraints, this variant was trained for fewer epochs compared to the custom dataset variant.
   - However, it still yields considerably good results.

2. Custom Dataset Variant:
   - Trained on our custom dataset.
   - This variant has been trained for a sufficient number of epochs to achieve good performance.

## Model Training

To further train the NL2SQL models or obtain more detailed information, please refer to the Model Training notebook included in this file. The notebook provides step-by-step instructions on training the models, as well as additional insights and details about the training process.

## Usage

To use the NL2SQL model, follow the steps below:

1. Install the required dependencies.
2. Download .
3. Select the appropriate model variant (Spider Dataset or Custom Dataset) based on your needs.
4. Provide input text in English, specifying the NL2SQL task, and receive SQL query predictions from the model.

## Acknowlegements

For more information, kindly visit https://github.com/Shivanandroy/simpleT5
For more information on Spider dataset , visit https://huggingface.co/datasets/spider#citation-information
