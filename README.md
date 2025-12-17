# Final MLOps Project – MLOps Pipeline


## Project Overview
---

This repository contains the **Final MLOps Project**, which implements a simple end-to-end **MLOps pipeline** following the **Cookiecutter Data Science (CCDS)** structure.
The project automates data preprocessing, model training, model selection, and deployment using **Dagger** and **GitHub Actions**.

The goal of this project is to restructure a Python monolith into a clean, modular MLOps project and demonstrate workflow automation and reproducibility.

---

## Table of Contents

* [Project Overview](#project-overview)
* [How to Trigger the Workflow](#how-to-trigger-the-workflow)

  * [Option 1: Push to main branch](#option-1-push-to-main-branch)
  * [Option 2: Manual trigger](#option-2-manual-trigger)
* [Pipeline Stages](#pipeline-stages)

  * [1. Data Preparation](#1-data-preparation)
  * [2. Model Training](#2-model-training)
  * [3. Model Selection](#3-model-selection)
  * [4. Model Deployment](#4-model-deployment)
* [Artifacts and Outputs](#artifacts-and-outputs)
* [CI/CD Integration](#cicd-integration)
* [How to Run Locally](#how-to-run-locally)

---

## How to Trigger the Workflow

The pipeline is fully automated using **GitHub Actions**.

### Option 1: Push to main branch

Any push to the `main` branch will automatically trigger the pipeline.

### Option 2: Manual trigger

1. Go to the **Actions** tab in the GitHub repository
2. Select the workflow
3. Click **Run workflow**

---

## Pipeline Stages

The pipeline executes the following steps:

### 1. Data Preparation

* Pulls raw data using **DVC**
* Cleans missing values and handles outliers using `preprocessing.py`

### 2. Model Training

* Trains models using **Scikit-Learn** and **XGBoost**
* Training logic is implemented in `train.py`

### 3. Model Selection

* Compares models based on evaluation metrics
* Selects the best-performing model (`model_select.py`)

### 4. Model Deployment

* Saves the selected model as an artifact
* Deployment logic handled in `model_deploy.py`

---

## Artifacts and Outputs

After a successful pipeline run:

* The trained model is saved as an artifact named **`model`**
* Artifacts are available in the **GitHub Actions → Artifacts** section
* Processed datasets and evaluation results are stored in the `output/` directory

---

## CI/CD Integration

The project uses multiple GitHub Actions workflows:

* **Tests workflow**

  * Runs unit and integration tests
  * Executed as a separate GitHub Action
  * Can be triggered independently and is executed before the main pipeline workflow
  * Helps identify failures early and isolate issues

* **Main pipeline workflow**

  * Runs the Dagger-based MLOps pipeline
  * Uploads the trained model as an artifact using `actions/upload-artifact`
  * Runs a model validation step to test inference

This setup ensures a **fully automated, test-first, and reproducible MLOps workflow**.

---

## How to Run Locally

```bash
dagger run go run pipeline.go
```

---

This project follows the concepts taught throughout the course, focusing on **clean structure**, **automation**, and **reproducibility**.
