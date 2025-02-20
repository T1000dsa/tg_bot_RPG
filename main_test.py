from database_data.Orm_logic import init, output_data, insert_data, drop_object, change_data
from database_data.models import TgUsersModel, ScoreModel
import asyncio
async def main():
    object = TgUsersModel(user_id='12535245245',
                        username='username_db',
                        firstname='firstname_db',
                        lastname='lastname_db',
                        bio='bio_db',
                        is_bot=True,
                        language_code='language_db')
    
    obj = ScoreModel(
        parent_id='12535245245',
        score=0
    )
    
   
    await init()
    res = await drop_object()
    print(res)
    

asyncio.run(main())