from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class BFHLInput(BaseModel):
    data: List[str]


class BFHLResponse(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    odd_numbers: List[str]
    even_numbers: List[str]
    alphabets: List[str]
    special_characters: List[str]
    sum: str
    concat_string: str


app = FastAPI()


@app.post("/bfhl", response_model=BFHLResponse)
async def solve(payload: BFHLInput):
    arr = payload.data

    userId = "anirudh_sridhar_29082025"
    email = "anirudhsridhar1064@gmail.com"
    rollNumber = "22BCE5252"

    evens = [x for x in arr if x.isnumeric() and int(x) % 2 == 0]
    odds = [x for x in arr if x.isnumeric() and int(x) % 2 != 0]
    alphabets = [x.upper() for x in arr if isinstance(x, str) and x.isalpha()]
    specials = [
        x for x in arr if isinstance(x, str) and not (x.isalpha() or x.isalnum())
    ]

    sum_nums = 0
    for i in arr:
        if i.isnumeric():
            sum_nums += int(i)

    concat = "".join(alphabets)[::-1]
    alt_caps = "".join(
        ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(concat)
    )

    return BFHLResponse(
        is_success=True,
        user_id=userId,
        email=email,
        roll_number=rollNumber,
        even_numbers=evens,
        odd_numbers=odds,
        alphabets=alphabets,
        special_characters=specials,
        sum=str(sum_nums),
        concat_string=alt_caps,
    )
