from collections import Counter
from typing import List
import pandas as pd

def count_books_copies(all_tiles: List[str]) -> dict:
  copies_num = dict(Counter(all_tiles))
  return copies_num

def create_copies_dataframe(repeted_books: dict) -> pd.DataFrame:
  copies_dataframe = pd.DataFrame.from_dict(repeted_books, orient='index', columns = ["copies"]).rename_axis('title').reset_index()
  return copies_dataframe

def df_map_values(dataframe: pd.DataFrame, new_column: str, target_column: str, dict_map: dict):
  dataframe[new_column] = dataframe[target_column].map(dict_map)
  return dataframe