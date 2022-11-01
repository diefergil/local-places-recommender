from typing import TypedDict, List, Optional, Union, Tuple

class UserData(TypedDict):
    userName: str
    # Company name, job name, # date start, end: day, month, year, [], function
    jobs: Optional[List[Tuple[str, str, List[int], Optional[Union[List[str], str]], str]]]
    currentPlace: Optional[Tuple[str, Tuple[List[str], int, int, int]]]
    previousPlaces: Optional[Tuple[str, Tuple[List[str], int, int, int]]]
    education: Optional[Tuple[Tuple[str, str, List[int]], Optional[Union[List[str], str]], str]]
    gPlusUserId: str