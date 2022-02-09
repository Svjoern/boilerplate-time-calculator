Weekdays = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

def add_time(start, duration, dayofWeek=""):
  days = 0
  day_index = 0
  if dayofWeek!= "":
    day_index = Weekdays.index(dayofWeek.upper())
    print(day_index, "test")
  
  print("start\t\t\t\t",start,duration,dayofWeek)
  
  times = start[-2:]
  if times == "PM":
    hours = 12 + int(start[0:2])
  elif times == "AM":
    hours = 0 + int(start[0:2])

  minutes = int(start[-5:-3]) + int(duration[-2:])

  print("hours-transform\t\t",hours,":", minutes, times, days, "days")

  minutes = int(start[-5:-3]) + int(duration[-2:])
  if minutes > 60:
    minutes -= 60
    hours_over = 1
  print("minutes-transform\t",hours+hours_over,":", minutes, times, days, "days")

  hours += int(duration.split(":")[0]) + hours_over
  print("hours-added\t\t\t",hours+hours_over,":", minutes, times, days, "days")

  while hours > 24:
    days += 1
    hours -= 24
  if hours > 12:
    times = "PM"
    hours -= 12
  else:
    times = "AM"
  
  if dayofWeek!= "":
    days = (day_index + days)%7
  else:
    if days == 1:
      days = "(next day)"
      print("days", days, Weekdays[days])
    else:
      days = "( " + str(days) + "days later)"
      print("days", days)
  print("days-transform\t\t",hours,":", minutes, times, days)
 

  return str(hours) + ":" + str(minutes) + " " + times + " " + str(days) + "days"