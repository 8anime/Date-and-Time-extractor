
import pytest
from dateExtractor.extractDates import extractDateFromInput

# Define a fixture to set up the function under test.
# The fixuture will set up common conditons or data that your tests will need.
# The purpose of this fixture is to provide "extractDateFromInput" function to your test functions.
@pytest.fixture
def dateExtractor():
    return extractDateFromInput

# Define test cases for valid date formats.
# The primary purpose of '@pytest.mark.parametrize' is to enable parameterized testing. 
# Instead of writing separate test functions for each specific test case, you can write 
# a single test function that accepts parameters and is executed with different values.
@pytest.mark.parametrize(
    'inputText, expectedDates', [
        # Test case 1: YYYY-MM-DD format
        ('The date of admission is 2023-10-06.', ['2023-10-06']),

        # Test case 2: MM/DD/YYYY format
        ('Date of birth: 10/06/1990', ['10/06/1990']),

        # Test case 3: HH:MM:SS format
        ('The timestamp is 12:34:56', ['12:34:56']),

        # Test case 4: Informal date mention "yesterday"
        ('We met yesterday.', ['yesterday']),

        # Test case 5: Informal date mention "today"
        ('The event is today.', ['today']),

        # Test case 6: Informal date mention "tomorrow"
        ('Our appointment is tomorrow.', ['tomorrow']),

        # Test case 7: DD Month, YYYY format
        ('Meeting on 06 October, 2023', ['06 October, 2023']),

        # Test case 8: Month DD, YYYY format or Mon DD, YYYY
        ('Holiday on October 06, 2023', ['October 06, 2023']),

        # Test case 9: HH:MM format 
        ('The time is 12:00.', ['12:00']),

        # Test case 10: Month YYYY format or Mon YYYY format
        ('I want to see you on December 2023', ['December 2023']),

        # Test case 11: YYYY/MM/DD format
        ('The date of admission is 2023/10/06.', ['2023/10/06']),

        # Test case 12: MM-DD-YYYY format
        ('The day it all happened was on, 12-06-2019', ['12-06-2019']),

        # Test case: 13: DD-MM-YYYY format
        ('Her birthday is on 09-11-2013', ['09-11-2013']),

        # Test case 14: YYYY-MM format
        ('It was supposed to happen on 2010-11, but it was cancelled', ['2010-11']),

        # Test case 15: YYYY/MM format
        ('Why did it happen on 2013/09', ['2013/09']),

        # Test case 16: MM/YYYY format
        ('It was on 11/2019 that everything changed', ['11/2019']),

        # Test case 17: MM-YYYY format
        ('The eclispse will happen on 11-2030', ['11-2030']),
    ]
)
def testValidDateFormats(dateExtractor, inputText, expectedDates):
    parsedDates = dateExtractor(inputText)
    assert parsedDates == expectedDates

