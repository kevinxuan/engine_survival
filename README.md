# Engine Survival
The objective of the model is to predict when an airplane engine will fail, given the information of the condition of the engine parts. With a high model performance predictive model, we are able to help the company to be prepared in advance by purchasing new engine and having technicians to replace it, which results in siginificant reduction in cost.

## Data
The dataset is a time series data consisting data on the condition of an airplane engine and whether the engine is still operating normally. 

## Method
To solve this problem, I convert the time series data to binary classification data where the independent variables are the condition of the different parts inside the airplane engine and the dependent variable whether the airplane engine operates normally or not. Then, the data goes through the standard data quality checking and fixing process to ensure that it's able to be feed into the machine learning model LightGBM. The reason we uses LightGBM as our machine learning algorithm is that it has fast training speed with high model performance or accuracy compared to other algorithms. 
