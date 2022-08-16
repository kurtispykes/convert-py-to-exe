import os 

import pandas as pd 
from pandas.api.types import CategoricalDtype

def perform_validation(filename:str):
    """
    A function to validate inputs for NYC Airbnb Open data. 
    """
    path_to_data = "../../"
    data = pd.read_csv(f"{path_to_data}{filename}")

    # Convert neighbourhood_group to type category
    neighbourhood_group_to_cat = CategoricalDtype(
        categories=["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"], 
        ordered=False
        )
    
    data["neighbourhood_group"] = data["neighbourhood_group"].astype(neighbourhood_group_to_cat)

    # Convert room_type to type category 
    room_type_to_cat = CategoricalDtype(
        categories=["Entire home/apt", "Private room", "Shared room"],
        ordered=False
    )

    data["room_type"] = data["room_type"].astype(room_type_to_cat)

    # Convert last_review to datetime 
    data["last_review"] = pd.to_datetime(data["last_review"])

    # Minimum nights a person can stay is one night 
    assert data["minimum_nights"].min() >= 1 

    # Minimum number of reviews is 0 
    assert data["number_of_reviews"].min() >= 0
    
    # Minimum number of reviews per month
    assert data["reviews_per_month"].min() >= 0.00

    # Minimum amount of listings per host 
    assert data["calculated_host_listings_count"].min() >= 1

    # Number of days when listing is available for books 
    # Could be 0 if tennant has long term booking 
    assert data["availability_365"].min() >= 0 

    # Save validated data 
    data.to_csv("validated_ab_nyc_2019.csv", index=False)

if __name__ == "__main__": 
    # User inputs filename
    filename = input("Enter filename: ")
    
    # Ensure it's a string
    if not filename.isalpha(): 
        filename = str(filename)
    
    # Automated validation
    perform_validation(filename)






