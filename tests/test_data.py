import pandas as pd


def test_columns(sample_data):
    # check if all the columns are there
    columns = ['lead_id', 'lead_indicator', 'customer_group', 
                'onboarding', 'source', 'purchases', 'time_spent', 'n_visits']
    
    for col in columns:
        assert col in sample_data.columns, f"Missing column: {col}"


def test_missing_values(sample_data):
    # target variable should have no missing values
    assert sample_data['lead_indicator'].isnull().sum() == 0


def test_valid_lead_indicator(sample_data):
    # lead indicator should be only 0.0 or 1.0
    valid_values = [0.0, 1.0]
    unique = sample_data['lead_indicator'].unique()
    
    for val in unique:
        assert val in valid_values


def test_numeric_ranges(sample_data):
    # Numeric features should be between 0 and 1
    numeric_cols = ['purchases', 'time_spent', 'n_visits']
    
    for col in numeric_cols:
        assert sample_data[col].min() >= 0
        assert sample_data[col].max() <= 1


def test_no_duplicate_ids(sample_data):
    # IDs should be unique
    duplicates = sample_data['lead_id'].duplicated().sum()
    assert duplicates == 0


def test_date_format(sample_data):
    # check date format
    dates = pd.to_datetime(sample_data['date_part'])
    assert len(dates) == len(sample_data)


def test_missing_values_threshold(sample_data):
    # no more than 20% missing values per column
    max_missing = .2
    
    for col in sample_data.columns:
        missing_pct = sample_data[col].isnull().sum() / len(sample_data)
        assert missing_pct <= max_missing, f"{col} has {missing_pct:.1%} nulls"
        