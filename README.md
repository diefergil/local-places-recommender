# local-places-recommender


## Data

[Link](https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local)

### Description

These datasets contain reviews about businesses from Google Local (Google Maps). Data includes geographic information for each business as well as reviews.

### Basis stadistics

| File       | Rows        |
|------------|-------------|
|Reviews     |11,453,845   |
|Users       |4,567,431    |
|Businesses  |3,116,785    |

### Metadata

* Metadata
* reviews and ratings
* GPS coordinates and address
* User information (places lived, jobs)
* timestamps
* business category, opening hours, etc.

### Examples

#### Review
```json
{
  'rating': 3.0,
  'reviewerName': u'an lam',
  'reviewText': u'Ch\u1ea5t l\u01b0\u1ee3ng t\u1ea1m \u1ed5n',
  'categories': [u'Gi\u1ea3i Tr\xed - Caf\xe9'],
  'gPlusPlaceId': u'108103314380004200232',
  'unixReviewTime': 1372686659,
  'reviewTime': u'Jul 1, 2013',
  'gPlusUserId': u'100000010817154263736'
}
```

#### Bussines
```json
{
  'name': u'Diamond Valley Lake Marina',
  'price': None,
  'address': [u'2615 Angler Ave', u'Hemet, CA 92545'],
  'hours': [[u'Monday', [[u'6:30 am--4:15 pm']]], [u'Tuesday', [[u'6:30 am--4:15 pm']]], [u'Wednesday', [[u'6:30 am--4:15 pm']], 1], [u'Thursday', [[u'6:30 am--4:15 pm']]], [u'Friday', [[u'6:30 am--4:15 pm']]], [u'Saturday', [[u'6:30 am--4:15 pm']]], [u'Sunday', [[u'6:30 am--4:15 pm']]]],
  'phone': u'(951) 926-7201',
  'closed': False,
  'gPlusPlaceId': '104699454385822125632',
  'gps': [33.703804, -117.003209]
```

### Citation

* Translation-based factorization machines for sequential recommendation, Rajiv Pasricha, Julian McAuley, RecSys, 2018
* [pdf](https://cseweb.ucsd.edu/~jmcauley/pdfs/recsys18a.pdf)

* Translation-based recommendation, Ruining He, Wang-Cheng Kang, Julian McAuley, RecSys, 2017
* [pdf](https://cseweb.ucsd.edu/~jmcauley/pdfs/recsys17.pdf)