from gather import gather_information_subreddit, is_bot, is_useless


pd_Art_long = gather_information_subreddit("ArtistLounge", "relevance", "AI", 5)

pd_Tech = gather_information_subreddit("technology", "relevance", "AI", 5)
df_cleaned = pd_Art_long[~pd_Art_long["Comment"].apply(is_bot)]
df_cleaned2 = df_cleaned[~df_cleaned["Comment"].apply(is_useless)]


df_cleaned2.to_csv('art_longue.csv', index = False)
print(df_cleaned2)

