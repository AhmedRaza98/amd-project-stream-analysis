# AMD Project 7 - Stream Analysis

## Project title
Stream Analysis of the New York Times Articles and Comments Dataset

## Objective
This project implements stream analysis algorithms from scratch in Python 3 using the New York Times Articles and Comments dataset. The goal is to study approximate streaming methods for large-scale data and compare them with exact baselines.

## Algorithms implemented
- Bloom Filter for approximate membership testing
- Flajolet-Martin estimator for distinct counting
- AMS estimator for second moment estimation

## Repository structure
- `notebook/project7_stream_analysis.ipynb`: main notebook
- `src/`: Python modules with from-scratch implementations
- `report/report.tex`: project report

## Reproducibility
The dataset is downloaded dynamically at runtime using the Kaggle API. It is not stored in this repository.

## How to run
1. Install dependencies from `requirements.txt`
2. Configure Kaggle credentials
3. Launch Jupyter Notebook
4. Run `notebook/project7_stream_analysis.ipynb`

## Notes
The project is designed to run in sampled mode by default for faster execution and easier reproducibility.
