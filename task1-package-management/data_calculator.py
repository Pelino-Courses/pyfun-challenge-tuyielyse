from datetime import datetime 
def days_btn_2dates(date1_str, date2_str, date_format="%Y-%m-%d"):

    """calculatting days between two interval of time
    - dates must be string 
    -we use abs method to handle the problems of negative days
    _we use datetime.strp in order to use it to call for the standard time
    This wiil give us the good solution we want"""
    
    try:
        time1=datetime.strptime(date1_str, date_format)
        time2=datetime.strptime(date2_str, date_format)
        return f"{abs((time2-time1).days)} days "
    except ValueError:
        raise ValueError(f"you have passed the date in wrong way may be:{date1_str}or{date2_str}")

print(days_btn_2dates("2025-04-04", "2025-04-24"))
   
