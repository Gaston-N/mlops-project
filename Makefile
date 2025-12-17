################################################################################
# GLOBALS
################################################################################

PROJECT_NAME = mlops_project
PYTHON_VERSION = 3.10
PYTHON_INTERPRETER = python3
DATA_URL = https://raw.githubusercontent.com/Jeppe-T-K/itu-sdse-project-data/refs/heads/main/raw_data.csv
ARTIFACTS_DIR = artifacts

################################################################################
# COMMANDS
################################################################################

.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install --upgrade pip
	$(PYTHON_INTERPRETER) -m pip install --requirement requirements.txt

.PHONY: setup
setup:
	mkdir --parents $(ARTIFACTS_DIR)

.PHONY: data
data:
	dvc import-url $(DATA_URL) $(ARTIFACTS_DIR)/raw_data.csv --force

.PHONY: test
test:
	pytest

.PHONY: test-data
test-data:
	pytest tests/test_data.py

.PHONY: test-model
test-model:
	pytest tests/test_model.py

.PHONY: test-pipeline
test-pipeline:
	pytest tests/test_pipeline.py