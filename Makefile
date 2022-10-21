

download_data:
	wget -O data/places.json.gz --no-check-certificate https://jmcauley.ucsd.edu/data/googlelocal/places.clean.json.gz
	wget -O data/users_data.json.gz --no-check-certificate https://jmcauley.ucsd.edu/data/googlelocal/users.clean.json.gz
	wget -O data/reviews.json.gz --no-check-certificate https://jmcauley.ucsd.edu/data/googlelocal/reviews.clean.json.gz
	
	gzip -d data/users_data.json.gz
	gzip -d data/places.json.gz
	gzip -d data/reviews.json.gz