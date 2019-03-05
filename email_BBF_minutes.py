from Emailer.Utils import sendQuickMail
import sys

import datetime

date_format = "%d-%m-%Y"

meeting_date_str = sys.argv[1]
meeting_date = datetime.datetime.strptime(meeting_date_str, date_format).date()

sendQuickMail(
        "BBF-HZZ-Analysis@cern.ch",
        "Minutes for BBF meeting: "+meeting_date.strftime("%B %d, %Y"),
        "Hi guys,\n\nPlease find the meeting minutes here: {link}note/.\n\nKind regards,\nLucien".format(link=sys.argv[2]),
        )
