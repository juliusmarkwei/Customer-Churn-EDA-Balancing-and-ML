# Customer Churn Prediction App

## Overview

This project is a machine learning classifier for predicting whether a bank customer is likely to churn (leave) or not. It includes a Streamlit web application that allows users to interact with the predictive model and visualize the results.

## Table of Contents

- [Demo](#demo)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Streamlit App](#streamlit-app)
- [Model Training](#model-training)
- [Visualization](#visualization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Demo

Click [here](https://customerchurnpredict.streamlit.app/) to view the prediction app in your web browser.

Here are some pictures of what the app looks like:

<font size=4 color="#ffffff">1. Prediction Page</font>

<hr><br>
<img src="./assets/images/prediction image.png">
<br>

<br><br>
<font size=4 color="#ffffff">2. Visualization Page</font>
<hr><br>
<img src="./assets/images/viz image.png">

## Getting Started

### Prerequisites

List the prerequisites that users need to have installed or set up before using the project.

```bash
python>=3.8
requirements.txt
```

### Installation

To use my application, follow this steps below to successfully install and run the program.

```bash
# Clone the repository
git clone https://github.com/juliusmarkwei/Customer-Churn-EDA-Balancing-and-ML.git

# Change directory
cd Customer-Churn-EDA-Balancing-and-ML/

# Install dependencies
pip install -r requirements.txt
```

## Streamlit App

Carefully type the command below in your teminal of the "Customer-Churn-EDA-Balancing-and-ML/" directory to run the app.
```bash
# Run the Streamlit app
streamlit run app.py
```


## Model Training

Our machine learning model was trained using a dataset containing [describe your dataset]. The training process involved the following steps:

- **Data Preprocessing:** We performed data cleaning, handled missing values, and encoded categorical features as part of data preparation.

- **Model Selection:** We selected the Random Forest model for the prediciton app after evaluation as the base model due to its suitability for our problem.

- **Model Evaluation:** The model's performance was evaluated using metrics accuracy and F1-score. Cross-validation was used to assess its generalization ability.

- **Hyperparameter Tuning:** We fine-tuned the model's hyperparameters to optimize performance.

For detailed information on the model training process, please refer to the [training notebook](https://github.com/juliusmarkwei/Customer-Churn-EDA-Balancing-and-ML/notebooks/main.ipynb).


## Contributing

We welcome contributions to improve this project! Whether it's bug reports, feature suggestions, or code contributions, we appreciate your help.

- **Reporting Issues:** If you encounter a problem or have a suggestion, [open an issue](https://github.com/juliusmarkwei/Customer-Churn-EDA-Balancing-and-ML/issues) with details.

- **Making Pull Requests:** Feel free to submit pull requests for fixes or enhancements. Follow common coding standards and provide clear descriptions for your changes.

Thank you for your contributions!

---
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.