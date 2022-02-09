Weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

def add_time(start, duration, dayofWeek=""):
  print("start\t\t\t\t",start,duration,dayofWeek)
  hours_over=0
  days = 0
  day_index = 0
  if dayofWeek!= "":
    day_index = Weekdays.index(dayofWeek.lower())
    # print(day_index, "day_index")
  
  times = start.split(" ")[1]
  hours = int(start.split(":")[0])
  if times == "PM":
    hours += 12
  # print("hours-transform\t\t",hours,":", times, days, "days")
  
  minutes = int(start[-5:-3]) + int(duration[-2:])
  if minutes > 60:
    minutes -= 60
    hours_over = 1

  if minutes < 10:
    minutes = "0"+str(minutes)
  else: 
    minutes = str(minutes)

  # print("minutes-transform\t",hours+hours_over,":", minutes, times, days, "days")

  hours_chg = int(duration.split(":")[0]) + hours_over
  print("hours-added\t\t\t",hours+hours_chg,":", minutes, times, days, "days")

  hours = hours+hours_chg

  while hours >= 24:
    days += 1
    hours -= 24
    print("here")
  if hours >= 13:
    times = "PM"
    hours -= 12
  else:
    times = "AM"
  
  if dayofWeek!= "":
    days = (day_index + days)%7
    day_name = Weekdays[days][0].upper()+Weekdays[days][1:]
    if days == 0:
      days = ", " + day_name
    elif days == 1:
      days = ", " + day_name + " (next day)"
      # print("days", days, Weekdays[days])
    else:
      days = ", " + day_name + " (" + str(days) + " days later)"
      # print("days", days)  
  else:
    if days == 0:
      days = ""
    elif days == 1:
      days = " (next day)"
      # print("days", days, Weekdays[days])
    else:
      days = " (" + str(days) + " days later)"
      # print("days", days)
  # print("days-transform\t\t",hours,":", minutes, times, days)
 

  return str(hours) + ":" + minutes + " " + times + str(days)