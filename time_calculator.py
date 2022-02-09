Weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

def add_time(start, duration, dayofWeek=""):
  # print("start\t\t\t\t",start,duration,dayofWeek)
  hours_over=0
  days = 0
  day_index = 0

  if dayofWeek!= "":
    day_index = Weekdays.index(dayofWeek.lower())
  
  times = start.split(" ")[1]
  hours = int(start.split(":")[0])
  if times == "PM":
    hours += 12
  
  minutes = int(start[-5:-3]) + int(duration[-2:])
  if minutes >= 60:
    minutes -= 60
    hours_over = 1

  if minutes < 10:
    minutes = "0"+str(minutes)
  else: 
    minutes = str(minutes)

  hours_chg = int(duration.split(":")[0]) + hours_over
  hours = hours+hours_chg

  # print("hours-added\t\t\t",hours,":", minutes, times, days, "days")

  while hours >= 24:
    days += 1
    hours -= 24
    
  if hours > 12:
    times = "PM"
    hours -= 12
  elif hours == 12:
    times = "PM"
  elif hours == 0:
    times = "AM"
    hours = 12
  else:
    times = "AM"
  
  days_str = ""

  if dayofWeek == "":
    if days == 0:
      days_str = ""
      return str(hours) + ":" + minutes + " " + times + days_str
    elif days == 1:
      days_str = " (next day)"
      return str(hours) + ":" + minutes + " " + times + days_str
    else:
      days_str = " (" + str(days) + " days later)"
      return str(hours) + ":" + minutes + " " + times + days_str
  else:
    days_index = (day_index + days)%7
    day_name = Weekdays[days_index][0].upper()+Weekdays[days_index][1:]

    if days == 0:
      days_str = ", " + day_name
      return str(hours) + ":" + minutes + " " + times + days_str
    elif days == 1:
      days_str = ", " + day_name + " (next day)"
      return str(hours) + ":" + minutes + " " + times + days_str
    else:
      days_str = ", " + day_name + " (" + str(days) + " days later)"
      return str(hours) + ":" + minutes + " " + times + days_str