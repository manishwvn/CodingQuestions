class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        def count(year,month,day):
            n=0
            for i in range(0,year):
                if leap(i):
                    n+=366
                else:
                    n+=365
            n+=day
            if leap(year):
                for i in range(0,month-1):
                    n+=monthdays2[i]
            else:
                for i in range(0,month-1):
                    n+=monthdays1[i]       
            return n
        def leap(year):
            if (year%4)==0:
                if (year%100==0):
                    if (year%400==0):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

        monthdays1 = [31, 28, 31, 30, 31, 30,  
                        31, 31, 30, 31, 30, 31 ]
        monthdays2= [31, 29, 31, 30, 31, 30,  
                        31, 31, 30, 31, 30, 31 ]
        dat1=date1.split('-')
        dat2=date2.split('-')
        year1,month1,day1=dat1[:]
        year2,month2,day2=dat2[:]
        y1=count(int(year1),int(month1),int(day1))
        y2=count(int(year2),int(month2),int(day2))
        return abs(y2-y1)
            
            