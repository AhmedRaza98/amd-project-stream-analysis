# AMD Project 7 - Stream Analysis

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AhmedRaza98/amd-project-stream-analysis/blob/main/notebook/project7_stream_analysis.ipynb)

## Project Title
Stream Analysis of the New York Times Articles and Comments Dataset

## Objective
This project implements stream-analysis algorithms from scratch in Python 3 using the New York Times Articles and Comments dataset. The goal is to study approximate streaming methods for large-scale data and compare them with exact baselines.

## Algorithms Implemented
- Bloom Filter for approximate membership testing
- Flajolet-Martin estimator for distinct counting
- AMS estimator for second-moment estimation

## Repository Structure
- `notebook/project7_stream_analysis.ipynb`: main notebook
- `src/`: Python modules with from-scratch implementations
- `report/report.tex`: LaTeX report source
- `report/report.pdf`: compiled report
- `requirements.txt`: local Python dependencies

## Reproducibility
The dataset is downloaded dynamically at runtime using the Kaggle API. It is not stored in this repository.

The notebook is designed to run on **Google Colab**. During execution, the user must provide their own Kaggle credentials file (`kaggle.json`) in order to download the dataset.

## How to Run
### Option 1: Google Colab
1. Open `notebook/project7_stream_analysis.ipynb` in Google Colab
2. Run the notebook from top to bottom
3. Upload your own `kaggle.json` file when prompted
4. The notebook will install dependencies, download the dataset dynamically, and execute the experiments

### Option 2: Local Jupyter Notebook
1. Install dependencies from `requirements.txt`
2. Configure Kaggle credentials locally
3. Launch Jupyter Notebook
4. Run `notebook/project7_stream_analysis.ipynb`

## Notes
- The project is designed to run in sampled mode by default for faster execution and easier reproducibility
- The same pipeline can be extended to larger subsets or the full dataset
- The dataset itself is intentionally not committed to the repository