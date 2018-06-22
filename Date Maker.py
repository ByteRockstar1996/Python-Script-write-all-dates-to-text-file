days_in_year=[31,28,31,30,31,30,31,31,30,31,30,31]
days_in_leap_year=[31,29,31,30,31,30,31,31,30,31,30,31]   

with open('Dates.txt','w') as dates:
     for year in range(1900,2018):
        if year%4==0:
            for month in range(1,13):
                for day in range(1,int((days_in_leap_year[month-1]+1))):
                    day=str(day)
                    if len(day)<2:
                        day=day.zfill(2)
                    month=str(month)
                    if len(month)<2:
                        month=month.zfill(2)
                    year=str(year)
                    dates.write(day+month+year+'\n')                
            else:
                for month in range(1,13):
                    for day in range(1,int((days_in_year[month-1]+1))):
                        day=str(day)
                        if len(day)<2:
                            day=day.zfill(2)
                        month=str(month)
                        if len(month)<2:
                            month=month.zfill(2)
                        year=str(year)
                        dates.write(day+month+year+'\n')
                        

