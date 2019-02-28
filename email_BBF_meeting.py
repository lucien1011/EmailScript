from Emailer.Utils import sendQuickMail
import sys

sendQuickMail(
        "BBF-HZZ-Analysis@cern.ch",
        "Reminder for BBF meeting",
        "Hi guys,\n\nJust a kind reminder that we will have our BBF meeting at {time} {place}. Agenda here: {link}.\n\nKind regards,\nLucien".format(time=sys.argv[1],place=sys.argv[2],link=sys.argv[3]),
        )
