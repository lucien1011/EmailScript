from Emailer.Utils import sendQuickMail
import sys

sendQuickMail(
        "BBF-HZZ-Analysis@cern.ch",
        "Minutes for BBF meeting",
        "Hi guys,\n\nPlease find the meeting minutes here: {link}note/.\n\nKind regards,\nLucien".format(link=sys.argv[1]),
        )
