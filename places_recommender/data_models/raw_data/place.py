from typing import TypedDict, List, Tuple
    

class Place(TypedDict):
    name: str
    price: str
    address: List[str]
    hours: List[Tuple[str, List[str]]]
    phone: str
    closed: bool
    gPlusPlaceId: str
    gps: str