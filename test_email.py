from Emailer.Utils import sendQuickMail
import sys

import datetime

date_format = "%d-%m-%Y"

today = datetime.date.today()
meeting_date_str,meeting_time_str = sys.argv[1].split(",")
meeting_date = datetime.datetime.strptime(meeting_date_str, date_format).date()
date_diff = meeting_date - today
if date_diff.days == 1:
    date_diff_str = "tomorrow"
else:
    date_diff_str = str(date_diff.days)+" days later"

sendQuickMail(
        "kin.ho.lo@cern.ch",
        "Reminder for BBF meeting: "+meeting_date.strftime("%B %d, %Y"),
        "Hi guys,\n\nJust a kind reminder that we will have our BBF meeting at {time} {place}, {dateDiff}. Agenda here: {link}.\n\nKind regards,\nLucien".format(
            time=sys.argv[1],
            place=sys.argv[2],
            link=sys.argv[3],
            dateDiff=date_diff_str,
            ),
        )
