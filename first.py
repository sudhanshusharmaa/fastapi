import enum
from fastapi import FastAPI
from enum import Enum


app = FastAPI()

class solution(str,Enum):
    indian = "indian"
    american = "american"
    italian = "italian"


foods = {'indian':['Dosa','Samosa'],
        'italian':['pasta','margirita','pizza'],
        'american':['hot dog','apple pie','burger']}


@app.get('/getitems/{cusines}')
async def dishes(cusines:solution):
    return foods.get(cusines)    



coupon_code = { 1: '10%',
                2: '20%',
                3: '30%',
                4: '40%',
                5: '50%'}

@app.get("/get_coupons/{code}")
async def coupons(code:int):
    return {'discount amount ':coupon_code.get(code)}