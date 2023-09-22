# Customer Churn Prediction App

## Overview

This project is a machine learning classifier for predicting whether a bank customer is likely to churn (leave) or not. It includes a Streamlit web application that allows users to interact with the predictive model and visualize the results.

## Table of Contents

- [Demo](#demo)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
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
# Example:
# Python and pip
Python 3.8
pip install -r requirements.txt
```

### Installation

Provide step-by-step instructions on how to install and run your project. Include any configuration files or environment variables that need to be set.

```bash
# Clone the repository
git clone https://github.com/juliusmarkwei/Customer-Churn-EDA-Balancing-and-ML.git

# Change directory
cd Customer-Churn-EDA-Balancing-and-ML

# Install dependencies
pip install -r requirements.txt
```

## Usage

Explain how to use your machine learning classifier. Include code snippets or examples if applicable.

```python
# Example usage:
from churn_classifier import ChurnClassifier

# Load the model
model = ChurnClassifier.load_model('model.pkl')

# Make predictions
customer_data = [...]  # Replace with customer data
prediction = model.predict(customer_data)
```

## Streamlit App

Describe the features and functionality of your Streamlit app. Provide instructions on how users can run the app locally.

```bash
# Run the Streamlit app
streamlit run app.py
```

## Model Training

Explain how the machine learning model was trained, including data preprocessing, model selection, and evaluation metrics.

## Visualization

Discuss the visualization page and the types of charts or visualizations included. Provide examples of how to generate these visualizations.

## Contributing

Explain how others can contribute to your project. Include guidelines for reporting issues, making pull requests, and any coding standards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Acknowledge any libraries, datasets, or resources that you used or were inspired by in your project.
