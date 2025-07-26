# Lightspeed Asset Risk ML Pipeline (WGU D502 Capstone)

## Overview

This repository implements a modular, reproducible ML pipeline for asset risk analysis, designed as part of the WGU BS Data Analytics Capstone project. The pipeline uses synthetic asset data to train and evaluate predictive models for identifying missing inventory and IPAM (IP Address Management) entries.

- **Tech stack:** Python, MLflow, Pandas, Scikit-learn, CSV (text file) data storage
- **Pipeline orchestration:** MLflow Projects
- **Storage:** All datasets and artifacts are stored as CSV/text files for transparency and ease of grading (no database required).

## Pipeline Steps

The project is fully automated via MLflow and modular Python scripts:

1. **Data Generation (`generate`):**
    - Generates a synthetic base asset dataset (`base_asset_dataset.csv`) of configurable size.
    - Labels the dataset for risk (e.g., missing in inventory or IPAM).
    - Saves outputs in `data/raw/`.

2. **Data Preparation (`prepare`):**
    - Enriches and processes the labeled dataset.
    - Saves the processed dataset in `data/processed/`.

3. **Model Training (`train-inventory`, `train-ipam`, `train-both`):**
    - Trains classification models to predict risk labels.
    - Saves model artifacts and evaluation reports.
    - Supports training inventory, IPAM, or both models at once.

4. **Full Pipeline (`pipeline`):**
    - Runs all steps above end-to-end in a single command.

## How to Run

All steps are orchestrated via MLflow.  
**Example (using local environment):**
```bash
mlflow run . -e generate --env-manager=local
mlflow run . -e prepare --env-manager=local
mlflow run . -e train-inventory --env-manager=local
mlflow run . -e train-ipam --env-manager=local
mlflow run . -e train-both --env-manager=local
mlflow run . -e pipeline --env-manager=local
```

## Directory Structure
```
.
├── config/                  # JSON configs for model training
├── data/
│   ├── raw/                 # Generated raw data files
│   └── processed/           # Processed/enriched datasets
├── reports/                 # Model evaluation and feature importance plots
├── src/
│   ├── generate/            # Data generation scripts
│   ├── prepare/             # Data preparation scripts
│   └── train/               # Model training scripts
├── main.py                  # MLflow entry point for all pipeline steps
├── MLproject                # MLflow Projects specification
├── README.md
└── requirements.txt
```

## Justification for Data Storage

- **CSV/text files** are used for all data storage to maximize reproducibility, ease of use, and transparency for graders.
- No external database is required; all steps are local and portable.
- This choice enables simple inspection and validation of intermediate and final datasets by reviewers, supporting the WGU capstone emphasis on transparency and professional communication.
- Should the project require database use in a future context (for scalability, normalized data, or advanced querying), the pipeline can be adapted without altering the core analytical methodology.

## Requirements

- Python 3.8+
- Install dependencies: 
    ```python
    pip install -r requirements.txt
    ```
- [MLflow](https://mlflow.org/)

## Deliverables

- All code, configuration files, datasets, and reports needed to fully reproduce results.
- Easy-to-follow logs and outputs suitable for inclusion in your final written report and Panopto video summary.

## WGU Capstone Alignment

- Meets all data pipeline, transparency, and reproducibility requirements.
- Data storage approach is justified per rubric—no database dependencies, all results verifiable and easy to submit.
- Demonstrates professional communication, ethical data handling, and clear documentation per WGU’s academic standards.

---

**For any questions, open an issue or contact the project maintainer.**