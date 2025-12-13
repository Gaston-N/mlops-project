import pytest
import pandas as pd
import numpy as np

# This file contains a pytest fixture for generating sample data so it will be available in all the tests

@pytest.fixture
def sample_data():
    np.random.seed(42)
    n = 100
    
    return pd.DataFrame({
        'lead_id': [i for i in range(n)],
        'lead_indicator': np.random.choice([0.0, 1.0], n),
        'date_part': pd.date_range('2024-01-01', periods=n, freq='D'),
        'source': 'signup',
        'customer_group': np.random.randint(1, 10, n),
        'onboarding': np.random.choice([True, False], n),
        'customer_code': [''.join(chr(c) for c in np.random.randint(65, 91, 10)) for _ in range(n)],
        'purchases': np.random.uniform(0, 1, n),
        'time_spent': np.random.uniform(0, 1, n),
        'n_visits': np.random.uniform(0, 1, n),
        'bin_source': 'group_1'
    })

