marks = {"umesh":"73","babu":"87","harry":"88"}

print(marks.items())  # output is key value pairs

print(marks.keys())

print(marks.values())

print(len(marks))

print(marks.get("umesh"))

marks.update({"umesh":89})
marks.update({"vinay":99})


marks.pop("umesh")

print(marks)


print(marks.get("umesh4"))  # prints None


# print(marks["umesh4"])   # gives error

