from datetime import datetime

datetime_str = '21081221220260.jpg'

# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
datetime_object = datetime.strptime(datetime_str.split('.')[0], '%y%m%d%H%M%S%f')

print(type(datetime_object))
print(datetime_object.timestamp())  # printed in default format
