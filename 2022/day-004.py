# LBYL vs EAFP: Preventing or Handling Errors in Python
# Avoiding Race Conditions

# LBYL
# 当 is_active() 为真，但 connection 失败的时候，就无能为力了
connection = create_connection(db, host, user, password)

# Later in your code...
if connection.is_active():
    # Update your database here...
    connection.commit()
else:
    # Handle the connection error here...

# EAFP
# 只关心能否连上数据库，连接失败就返回异常
connection = create_connection(db, host, user, password)

# Later in your code...
try:
    # Update your database here...
    connection.commit()
except ConnectionError:
    # Handle the connection error here...


 