
import re

def extractDateFromInput(inputData):
    """This method extracts dates from the input it receives"""
    datePatterns = [
        r'(\d{2,4}-\d{2,4}(?:-\d{2,4})?)',  # YYYY-MM-DD or MM-DD-YYYY or DD-MM-YYYY or MM-YYYY
        r'(\d{2,4}/\d{2,4}(?:/\d{2,4})?)',  # MM/DD/YYYY or DD/MM/YYYY or YYYY/MM/DD or MM/YYYY
        r'(\d{2} \w+,? \d{4})',             # DD Month, YYYY or DD Mon, YYYY
        r'(\d{2}:\d{2}(?::\d{2})?)',        # HH:MM:SS (timestamp) or HH:MM (time format)
        r'(\b(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:\s+)?\d{2},? \d{4})', # Month DD, YYYY or Mon DD, YYYY
        r'(\b(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:\s+)?\d{4})',         # Month YYYY or Mon YYYY
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

    # Remove punctuation marks from extracted dates
    extractedDates = [date.strip('.,') for date in extractedDates]
    
    return extractedDates






















