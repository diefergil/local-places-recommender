from typing import TypedDict, List

class Review(TypedDict):
    rating: float
    reviewerName: str
    reviewText: str
    categories: List[str]
    gPlusPlaceId: str
    unixReviewTime: int
    reviewTime: str
    gPlusUserId: str