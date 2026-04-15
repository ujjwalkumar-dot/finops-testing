import datetime
import random
import string
def pytest_addoption(parser):   # this function is used to add options to the pytest command
    parser.addoption(
        "--pipeline_name",
        action="store",
        default=''.join(random.choices(string.ascii_letters, k=6)),
        help="Pipeline name passed from npm" 
    )
    parser.addoption(
        "--pipeline_code",
        action="store",
        default=datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        help="Pipeline code passed from npm"
    )
    