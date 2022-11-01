

download_data:
	wget -O data/raw_data/places.json.gz --no-check-certificate https://jmcauley.ucsd.edu/data/googlelocal/places.clean.json.gz
	wget -O data/raw_data/users_data.json.gz --no-check-certificate https://jmcauley.ucsd.edu/data/googlelocal/users.clean.json.gz
	wget -O data/raw_data/reviews.json.gz --no-check-certificate https://jmcauley.ucsd.edu/data/googlelocal/reviews.clean.json.gz
	
	gzip -d data/raw_data/users_data.json.gz
	gzip -d data/raw_data/places.json.gz
	gzip -d data/raw_data/reviews.json.gz