from sqlalchemy.orm import Session
from ..models import Vehicle as M_Vehicle
from ..schemas import Vehicle as S_Vehicle
from ..utils import get_path_save_image
from sqlalchemy import extract, func, text
from datetime import datetime

async def counter(db: Session):
	# db_test = db.query(M_Vehicle).\
	#     filter(func.DATE(M_Vehicle.timestamp) == datetime.today().day).\
	#     group_by(M_Vehicle.rest_area).all()
	# # time.strftime("%D %H:%M", time.localtime(int(M_Vehicle.timestamp)))
	year, month, day 	= datetime.today().year, datetime.today().month, datetime.today().day
	month 				= month if len(str(month)) == 2 else '0'+str(month)
	day 				= day if len(str(day)) == 2 else '0'+str(day)

	sql_query = text(
		f"SELECT \
		COUNT(*) as count, vehicle_type, rest_area \
		FROM tb_vehicle \
		WHERE  datetime(timestamp, 'unixepoch', 'localtime') > '{year}-{month}-{day} 00:00:00' \
		GROUP BY rest_area, vehicle_type"
	)
	result		= db.execute(sql_query)
	result_list = result.fetchall()

	result_dict = dict()
	for count, vehicle, rest_area in result_list:
		count_dict = dict()
		for countx, vehiclex, rest_areax in result_list:
			if rest_areax == rest_area:
				count_dict.update({vehiclex: countx})
		result_dict.update({rest_area: count_dict})
	return result_dict