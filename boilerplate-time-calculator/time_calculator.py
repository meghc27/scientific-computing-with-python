def add_time(start, duration, day = None):
  mid = start.split(' ')[1]
  h = int(start.split(' ')[0].split(':')[0])
  m = int(start.split(' ')[0].split(':')[1])

  if mid == 'PM':
    h += 12
    # h %= 24
  
  durh = int(duration.split(":")[0])
  durm = int(duration.split(":")[1])

  new_min = (m + durm) % 60
  new_hr = (h + durh) + (m + durm) // 60

  days = new_hr // 24

  if len(str(new_min)) == 1:
    min_disp = '0' + str(new_min)
  else:
    min_disp = str(new_min)
    
  hr_disp = new_hr % 12
  if hr_disp == 0:
    hr_disp = 12

  midday = ['AM', 'PM']
  mid = midday[(new_hr % 24) // 12]

  new_time = str(hr_disp) + ':' + str(min_disp) + ' ' + mid

  week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  if day is not None:
    weekday = week[(week.index(day.capitalize()) + days) % 7]
    new_time += ', {}'.format(weekday)

    
  if days == 1:
    new_time += ' (next day)'
  elif days > 1:
    new_time += ' ({} days later)'.format(days)
      
  return new_time