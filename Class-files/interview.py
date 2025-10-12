# import re

# def check_valid_email(s):
#     if re.search(r"[w+._0-9]+\@\w+.com", s):
#         return "Valid Email"
    

# check_valid_email("vishnu.bhandari@gmail.com")

# dummy_json = {"a": "A", "second": {"b": "B", "c":"C"}, "d":"D"}

# "a"  "second"  "d"
# {
#   "a": "A",
#   "second.b": "B",
#   "second.c": "C",
#   "d": "D"
# }

# d = {}
# temp_key=None
# def flatten_json(dict1):
#     for key, value in dummy_json.items(): # second {"b": "B", "c":"C"}
#         if isinstance(value, dict):
#             global temp_key
#             temp_key = f"{key}"
#             flatten_json(dict1)
#         if temp_key:
#             key = f"{temp_key}.{key}"
#         d[key] = value
#         temp_key = None
#     print(d)   

# flatten_json(dummy_json)

# import time

# def time_execution(f):
#     def inner():
#         t1 = time.time()
#         f()
#         t2 = time.time()
#         print(f"Time taken by {f.__name__} is {t2-t1}")
#     return inner

# @time_execution
# def main_func():
#     time.sleep(2)

# main_func()


# from flask import Flask, request
# flask_app = Flask('__main__')
# # jsonify
# # db configuration
# # db =

# class Users:
#     def to_dict():
#         pass

# @flask_app.route("/api/v1/get-users")
# def get_users_data():
#     all_users = Users.query.all()
#     return jsonify([d.to_dict(), for d in all_users]), 200


# table
# duplicate data -->
# keep one copy and remove deplicate
# name, secondname, lastname
# partition by --> 
# delete from employee where id in (
# select id from employee where group by (name, secondname, lastname))


# users login data

# user_id, last_login_date, platform


# count of users every day --> mobile api web

# table  -- each row {"date": {"web": 5, "api": 2, "mobile": 10}}

# impory mysql
# [(101, "21-09-2025", "web"), (), ()]

# def user_data():
#     d = {}
#     data = [(101, "21-09-2025", "web"), (101, "21-09-2025", "api"), (101, "21-09-2025", "api"), (101, "21-09-2025", "mobile")]
#     for record in data:
#         d[record[1]] = {"web"}


# user_data()



