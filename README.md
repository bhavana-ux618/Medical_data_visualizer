# Medical Data Visualizer

## Overview

This project is part of the freeCodeCamp Data Analysis with Python certification. The goal is to analyze medical examination data and visualize relationships between cardiovascular disease, body measurements, blood markers, and lifestyle habits using Python data science libraries.

## Features

* Calculates Body Mass Index (BMI) and identifies overweight patients.
* Normalizes cholesterol and glucose values into binary categories.
* Creates a categorical plot to compare health indicators for patients with and without cardiovascular disease.
* Cleans the dataset by removing invalid and extreme values.
* Generates a correlation heatmap to identify relationships between medical variables.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Dataset

The dataset contains information collected during medical examinations, including:

* Age
* Height
* Weight
* Blood Pressure
* Cholesterol Level
* Glucose Level
* Smoking Status
* Alcohol Consumption
* Physical Activity
* Cardiovascular Disease Status

## Visualizations

### 1. Categorical Plot

Displays counts of:

* Cholesterol
* Glucose
* Smoking
* Alcohol Consumption
* Physical Activity
* Overweight Status

The data is grouped by cardiovascular disease status (`cardio`).

### 2. Correlation Heatmap

Shows correlations between all medical features after cleaning the dataset and removing outliers.

## Project Structure

```
├── medical_data_visualizer.py
├── medical_examination.csv
├── main.py
├── test_module.py
├── catplot.png
├── heatmap.png
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project directory:

```bash
cd medical-data-visualizer
```

3. Install required dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

## Usage

Run the project:

```bash
python main.py
```

The program will generate:

* `catplot.png`
* `heatmap.png`

## Learning Outcomes

Through this project, I learned:

* Data cleaning and preprocessing
* BMI calculation and feature engineering
* Data transformation using Pandas
* Creating categorical visualizations with Seaborn
* Correlation analysis and heatmap visualization
* Working with real-world medical datasets

## Acknowledgements

This project was completed as part of the freeCodeCamp Data Analysis with Python Certification.

## Author

Bhavana R
