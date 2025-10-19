from datetime import date
date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

def saturdays_between_two_dates(start,end):
  dates = []
  if start <= end:
    for d in range(start.toordinal(),end.toordinal()+1):
      if date.fromordinal(d).weekday() == 5:
        dates.append(date.fromordinal(d))
  else:
    for d in range(end.toordinal(),start.toordinal()+1):
      if date.fromordinal(d).weekday() == 5:
        dates.append(date.fromordinal(d))
  return len(dates)



print(saturdays_between_two_dates(date1, date2))
