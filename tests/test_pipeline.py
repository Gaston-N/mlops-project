import pytest
from pathlib import Path
import yaml


def test_makefile_exists():
    # check there's a makefile file
    assert Path("Makefile").exists()


def test_makefile_instructions():
    # makefile has required instructions
    makefile = Path("Makefile").read_text()
    
    required = ['requirements', 'setup', 'data']
    for target in required:
        assert target in makefile, f"Missing target: {target}"


def test_github_workflow_exists():
    # check github workflow file exists
    workflow = Path(".github/workflows/dagger.yml")
    assert workflow.exists()


def test_github_workflow_structure():
    # check correct structure in github workflow
    workflow = Path(".github/workflows/dagger.yml")
    content = yaml.safe_load(workflow.read_text())
    
    assert 'jobs' in content
    assert 'dagger' in content['jobs']


def test_pipeline_file_exists():
    # check pipeline file exists
    assert Path("pipeline.go").exists()


def test_pipeline_has_steps():
    # check pipeline has necessary steps
    pipeline = Path("pipeline.go").read_text()
    
    steps = ['preprocessing.py', 'train.py', 'model_select.py', 'model_deploy.py']
    for step in steps:
        assert step in pipeline, f"Missing step: {step}"


def test_requirements_file_exists():
    # check requirements txt exists and has important dependencies
    assert Path("requirements.txt").exists()

    requirements = Path("requirements.txt").read_text()
    
    deps = ['scikit-learn', 'pandas', 'mlflow']
    for dep in deps:
        assert dep in requirements, f"Missing dependency: {dep}"


def test_src_structure():
    # check src directory structure
    src = Path("src")
    assert src.exists()
    assert (src / "preprocessing.py").exists()
    assert (src / "modeling" / "train.py").exists()


def test_pipeline_exports_artifacts():
    # check pipeline exports artifacts correctly
    pipeline = Path("pipeline.go").read_text()
    assert 'Export' in pipeline
    assert 'artifacts' in pipeline