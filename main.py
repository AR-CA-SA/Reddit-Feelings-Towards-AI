from gather import gather_information_subreddit, clean_data


pd_Art_long = gather_information_subreddit("ArtistLounge", "relevance", "AI", 5)

pd_Tech = gather_information_subreddit("technology", "relevance", "AI", 5)
print(pd_Art_long.head(5))
print(pd_Tech.head(5))

# pd_Art_long.to_csv('pdArtLounge.csv', index = False)

# pd_Tech.to_csv('pdTech.csv', index = False)
