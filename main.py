# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


#print(add_time("11:55 PM", "48:20"))
# print(add_time("3:00 PM", "3:10"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("6:30 PM", "205:12"))

# Run unit tests automatically
main(module='test_module', exit=False)

# print(add_time("8:16 PM", "466:02", "tuesday"))
# print(add_time("11:40 AM", "0:25"))
# print(add_time("11:59 PM", "24:05", "Wednesday"))
# "6:18 AM, Monday (20 days later)"

# 6:10 PM
# 2:02 PM, MONDAY
# 12:03 AM
# 1:40 AM (next day)
# 0:03 AM, THURSDAY (3 days later)
# 7:42 AM (9 days later)