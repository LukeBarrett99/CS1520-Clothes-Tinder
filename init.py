from google.cloud import datastore
import user

clothes = []

clothes.append(user.Clothing("https://imgprd19.hobbylobby.com/2/4f/57/24f57e245a879cb2543edd1df4e090bfebf24a45/700Wx700H-1013689-0320.jpg", "casual"))
clothes.append(user.Clothing("https://m.media-amazon.com/images/I/51+YnzX6FTL._AC_.jpg", "casual"))
clothes.append(user.Clothing("https://n.nordstrommedia.com/id/sr3/aa5d4654-af21-4034-8224-abd0063355f6.jpeg?h=365&w=240&dpr=2", "formal"))


print('initialized')