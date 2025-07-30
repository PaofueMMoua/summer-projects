class Solution:
    def reformatDate(self, date: str) -> str:
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", 
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", 
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        
        # Split the input date into day, month, and year
        day, month, year = date.split()
        
        day = day[:-2]  # Remove last two characters ('st', 'nd', 'rd', 'th')
        
        # Format the day to ensure two digits (e.g., '6' becomes '06')
        day = day.zfill(2)
        
        # Get the month as a 2-digit string using the month_map
        month = month_map[month]
        
        # Return the formatted date in YYYY-MM-DD format
        return f"{year}-{month}-{day}"
