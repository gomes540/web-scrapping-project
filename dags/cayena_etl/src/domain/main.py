from cayena_etl.src.domain.transform_data import *
from cayena_etl.src.domain.web_scraping import *
from cayena_etl.src.domain.transform_data_settings import CleanDF
from cayena_etl.src.domain.local_loader import LocalPath

def etl_web_scrapping(ingestion_date: str) -> None:
    all_valid_urls = get_all_valid_urls()
    
    all_books_information = get_all_books_in_website(all_valid_urls)
    print(f"fetched a total of {len(all_books_information)} books")
    
    all_titles, all_ratings, all_prices = get_title_name_price_lists(all_books_information)
    books_dict = {"title": all_titles, "rating": all_ratings, "price": all_prices}
    books_dataframe = pd.DataFrame(books_dict)
    
    book_copies_dict = count_books_copies(all_titles)
    copies_books_aux = create_copies_dataframe(book_copies_dict)
    
    # Join dataframes to get full dataframe
    full_books_df = books_dataframe.merge(copies_books_aux, left_on='title', right_on='title', how="inner")
    
    # Clean rating column
    full_books_df_clean = df_map_values(full_books_df, 'rating', 'rating', CleanDF.RATING_MAP.value)    
    full_books_df_clean["ingestion_date"] = ingestion_date
    print(full_books_df_clean.head())
    
    print(f"saving dataframe book locally in: {LocalPath.DATAFRAME_BOOK_PATH.value}")
    full_books_df_clean.to_csv(LocalPath.DATAFRAME_BOOK_PATH.value, index=False)