# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:songjingwei94819@used-car.cn8ylz4uqvgi.us-east-1.rds.amazonaws.com:3306/used_car'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'xjZE0CB11vnHvKhRuH8Du2FIK2XS6wxrtugqf2sa'
