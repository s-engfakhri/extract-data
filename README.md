# extract-data

Salary Dataset Analysis and Visualization
This project aims to perform an in-depth analysis of a salary dataset containing job titles, salaries, and derived features such as experience and age. The dataset includes multiple job roles, and through various data preprocessing techniques and visualizations, this project provides insights into salary trends, age distribution, and job title comparisons.

Project Overview
The Salary Dataset Analysis project focuses on analyzing salary-related data for job titles like Front End Developer, Software Development Engineer, Web Developer, and Test Engineer. The analysis includes calculating derived metrics (experience and age) and visualizing the relationships between job title, salary, and age using various plots and charts.

Key Features:
Data Preprocessing: The dataset is cleaned by handling missing values and generating new features (e.g., experience, age).

Exploratory Data Analysis (EDA): Detailed analysis using:

Line plots to show salary and age trends by job title.

Scatter plots to explore the relationship between salary and age.

Pie charts to visualize the distribution of age across job titles.

Bar charts to compare total salaries across different job titles.

Job Titles Analyzed: Front End Developer, Software Development Engineer, Web Developer, Test Engineer.

Visualizations
The following visualizations are generated to help understand the dataset:

Salaries by Job Title (Line Plot): Trends of salaries across different job titles.

Ages by Job Title (Line Plot): Age distribution trends by job title.

Salaries vs Age (Scatter Plot): Exploring the relationship between age and salary for each job title.

Age Distribution by Job Title (Pie Chart): Visualizing the proportion of ages by job title.

Total Salaries by Job Title (Bar Chart): Comparing the total salary sums across different job titles.

Installation
To run this project locally, follow the steps below.

Prerequisites
Ensure you have Python 3.x installed on your local machine.

Step 1: Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/your-username/salary-dataset-analysis.git
Step 2: Install Required Dependencies
Navigate to the project directory:

cd salary-dataset-analysis
Install the required dependencies using pip:


pip install -r requirements.txt
Step 3: Dataset
Make sure the dataset file Salary_Dataset_with_Extra_Features.csv is located in the same directory as the script. The dataset should have the following structure:

Job Title: The job title of the individual (e.g., Front End Developer, Software Development Engineer, etc.)

Salary: The salary of the individual.

Age: The age of the individual.

Experience: The number of years of experience (calculated from salary or provided).

