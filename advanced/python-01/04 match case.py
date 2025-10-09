# def http_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "internal server error"
#         case _:
#             return"Unknoen statue"
        

# print(http_status(200))
# print(http_status(404))
# print(http_status(500))
# print(http_status(66))



dict1 = {"a":4,"b":9}
dict2 = {"c":88,"d":99}

merged = dict1 | dict2
print(merged)