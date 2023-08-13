"""example without pySPARk required for this task"""

import json
from edx.analytics.tasks.tools.analyze.parser import LogFileParser



filename1 = 'ast.csv'
filename2 = 'eksmo.csv'
filename_out ='out.json'

MESSAGE_START_PATTERN  = r'(?P<ID>\d+)\t(?P<TIMESTAMP_X>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\t(?P<LOGIN>[\w._@%+-]+)\t(?P<PASSWORD>[\w.,_%$/]+)\t(?P<CHECKWORD>[\w.,_%$/]+)\t(?P<ACTIVE>[YN]?)\t' + \
    ur'(?P<NAME>[\w\S]*)\t(?P<LAST_NAME>[\w\S]*)\t' + \
r'(?P<EMAIL>[\w._%+-]+@[\w.-]+\.[\w-]{2,4})\t(?P<LAST_LOGIN>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\t(?P<DATE_REGISTER>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\t(?P<LID>\w+)\t'
# ur'(PERSONAL_PROFESSION\tPERSONAL_WWW\tPERSONAL_ICQ\tPERSONAL_GENDER\tPERSONAL_BIRTHDATE\tPERSONAL_PHOTO\tPERSONAL_PHONE\tPERSONAL_FAX\tPERSONAL_MOBILE\tPERSONAL_PAGER\tPERSONAL_STREET\tPERSONAL_MAILBOX\tPERSONAL_CITY\tPERSONAL_STATE\tPERSONAL_ZIP\tPERSONAL_COUNTRY\tPERSONAL_NOTES\tWORK_COMPANY\tWORK_DEPARTMENT\tWORK_POSITION\tWORK_WWW\tWORK_PHONE\tWORK_FAX\tWORK_PAGER\tWORK_STREET\tWORK_MAILBOX\tWORK_CITY\tWORK_STATE\tWORK_ZIP\tWORK_COUNTRY\tWORK_PROFILE\tWORK_LOGO\tWORK_NOTES\tADMIN_NOTES\tSTORED_HASH\tXML_ID\tPERSONAL_BIRTHDAY\tEXTERNAL_AUTH_ID\tCHECKWORD_TIME\tSECOND_NAME\tCONFIRM_CODE\tLOGIN_ATTEMPTS\tLAST_ACTIVITY_DATE\tAUTO_TIME_ZONE\tTIME_ZONE\tTIME_ZONE_OFFSET\tTITLE\tBX_USER_ID\tLANGUAGE_ID\tBLOCKED\tPASSWORD_EXPIRED\r\n'


log_file1= open(filename1, 'rb')
log_file2= open(filename2, 'rb')
log_file3= open(filename_out, 'w')
message1 = message2 = True

with open(filename_out, 'w') as log_file3:
    with open(filename1, 'rb') as log_file1:
        parser_ast= LogFileParser(log_file1, message_pattern=MESSAGE_START_PATTERN)
        with open(filename2, 'rb') as log_file2:
            parser_eksmo = LogFileParser(log_file2, message_pattern=MESSAGE_START_PATTERN)
            while message1:
                message1 = parser_ast.next_message()
                json.dump(message1, log_file3,indent=2)
                while message2:
                    message2 = parser_eksmo.next_message()
                    if message1['EMAIL'] == message2['EMAIL']:
                        print('found dublicate')
                    else: 
                        json.dump(message2, log_file3,indent=2)
                


