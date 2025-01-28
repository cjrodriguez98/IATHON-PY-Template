# Jupyter Notebook: Automated Report Generation using ChatGPT

## Overview

This Jupyter notebook demonstrates how to use OpenAI's ChatGPT to generate a comprehensive report based on a dataset. The notebook includes functions to create a title, summary, and statistical analysis of the data, as well as to fetch relevant images from Unsplash.

## Features

- **Data Loading**: Reads data from a CSV file (`jamb_exam_results.csv`).
- **Title and Summary Generation**: Uses ChatGPT to generate a title and summary for the report based on the dataset.
- **Statistical Analysis**: Generates statistical questions and tests using ChatGPT.
- **Image Retrieval**: Fetches relevant images from Unsplash based on the report content.
- **Dash App Creation**: Creates a Dash web application to display the report, including visualizations and images.

## Dependencies

The notebook requires the following Python packages:
- `requests`
- `pandas`
- `dash`
- `plotly`

These dependencies are specified in the `pyproject.toml` file.

## Usage

1. **Set API Keys**: Replace the placeholders for the OpenAI API key and Unsplash access key with your actual keys in the notebook.
2. **Run the Notebook**: Execute the cells in the notebook to generate the report content and create the Dash app.
3. **View the Report**: The generated Dash app will display the report, including the title, summary, statistical analysis, and images. 
```sh
python dash_app.py
```

## Files

- `playground.ipynb`: The main Jupyter notebook containing the code for generating the report.
- `dash_app.py`: The generated Dash application file.
- `jamb_exam_results.csv`: The dataset used for generating the report.

## Example

The notebook includes an example dataset with information about students' academic performance. The generated report provides insights into various factors influencing their performance, such as study hours, attendance rates, and teacher quality.

## License

This project is licensed under the MIT License.