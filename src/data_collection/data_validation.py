def validate_raw_data(df):
    # Check for missing values, duplicates, etc.
    return df.drop_duplicates().dropna()
