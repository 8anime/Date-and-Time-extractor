
import re

def extractDateFromInput(inputData):
    """This method extracts dates from the input it receives"""
    datePatterns = [
        r'\d{4}-\d{2}-\d{2}',    # YYYY-MM-DD
        r'\d{4}/\d{2}/\d{2}',    # YYYY/MM/DD
        r'\d{2}/\d{2}/\d{4}',    # MM/DD/YYYY
        r'\d{2}/\d{2}/\d{2}',    # MM/DD/YY
        r'\d{4}-\d{2}',          # YYYY-MM
        r'\d{4}/\d{2}',          # YYYY/MM
        r'\d{2} \w+,? \d{4}',    # DD Month, YYYY or DD Mon, YYYY
        r'\d{2}:\d{2}:\d{2}',    # HH:MM:SS (timestamp)
        r'\d{2}:\d{2}',          # HH:MM (time format)
        r'\w+ \d{1,2},? \d{4}',  # Month DD, YYYY or Mon DD, YYYY
        r'\w+ \d{1,},? \d{4}',   # Month DD, YYYY or Mon DD, YYYY
        r'\w+ \d{1,2} \d{4}',    # Month DD YYYY or Mon DD YYYY
        r'\w+ \d{4}',            # Month YYYY or Mon YYYY
    ]

    extractedDates = []

    # Extract dates using regular expressions
    for dateFormat in datePatterns:
        datesFound = re.findall(dateFormat, inputData)
        extractedDates.extend(datesFound)

    # Extract dates from informal mentions using dateutil.parser
    words = inputData.split()
    for i in range(len(words)):
        word = words[i].lower()  # Convert to lowercase for case-insensitive matching
        if word in [
            'yesterday', 'today', 'tomorrow', 'nextweek',
            'yesterday,', 'today,', 'tomorrow,', 'nextweek,',
            'yesterday.', 'today.', 'tomorrow.', 'nextweek.',
        ]:
            extractedDates.append(word)

    return extractedDates






















