from tqdm import tqdm
import click
import pandas as pd
from typing import Union, List
from places_recommender.data_models.raw_data import Review, Place, UserData 
from config import RAW_DATA_DIR, PROCESSED_DATA_DIR

def load_data_raw(file_name: str) -> Union[List[Review], List[Place], List[UserData]]:
    lines = []
    i = 0
    with open(RAW_DATA_DIR / file_name, encoding='utf-8') as file:
        for index, line in enumerate(tqdm(file)):
            lines.append(eval(line))
    
    return lines
    

@click.command()
@click.option(
    '--files', 
    default="reviews.json,places.json,users_data.json", 
    help='File names of the data to be saved'
    )
def create_dataset(files: str) -> None:
    files = files.split(",")
    for file in files:
        lines = load_data_raw(file)
        df = pd.DataFrame(lines)
        df.to_pickle(PROCESSED_DATA_DIR / file.replace("json", "pkl"))

if __name__ == "__main__":
    # reviews = load_data_raw('reviews.json')
    # places = load_data_raw('places.json')
    # user_data = load_data_raw('users_data.json')
    create_dataset()