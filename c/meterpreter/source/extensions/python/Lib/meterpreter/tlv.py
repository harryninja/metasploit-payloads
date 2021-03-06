from meterpreter.core import *

TLV_STDAPI_EXTENSION     = 0
TLV_INCOGNITO_EXTENSION  = 20000
TLV_PRIV_EXTENSION       = 20000
TLV_KIWI_EXTENSION       = 20000

# Stdapi constants
TLV_TYPE_COMPUTER_NAME         = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 1040)
TLV_TYPE_OS_NAME               = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 1041)
TLV_TYPE_USER_NAME             = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 1042)
TLV_TYPE_ARCHITECTURE          = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 1043)
TLV_TYPE_LANG_SYSTEM           = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 1044)
TLV_TYPE_SID                   = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 1045)
TLV_TYPE_DOMAIN                = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 1046)
TLV_TYPE_LOGGED_ON_USER_COUNT  = TLV_META_TYPE_UINT   | (TLV_STDAPI_EXTENSION + 1047)

TLV_TYPE_MOUNT                 = TLV_META_TYPE_GROUP  | (TLV_STDAPI_EXTENSION + 1207)
TLV_TYPE_MOUNT_NAME            = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 1208)
TLV_TYPE_MOUNT_TYPE            = TLV_META_TYPE_UINT   | (TLV_STDAPI_EXTENSION + 1209)
TLV_TYPE_MOUNT_SPACE_USER      = TLV_META_TYPE_QWORD  | (TLV_STDAPI_EXTENSION + 1210)
TLV_TYPE_MOUNT_SPACE_TOTAL     = TLV_META_TYPE_QWORD  | (TLV_STDAPI_EXTENSION + 1211)
TLV_TYPE_MOUNT_SPACE_FREE      = TLV_META_TYPE_QWORD  | (TLV_STDAPI_EXTENSION + 1212)
TLV_TYPE_MOUNT_UNCPATH         = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 1213)

TLV_TYPE_PID                   = TLV_META_TYPE_UINT   | (TLV_STDAPI_EXTENSION + 2300)
TLV_TYPE_PROCESS_NAME          = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 2301)
TLV_TYPE_PROCESS_PATH          = TLV_META_TYPE_STRING | (TLV_STDAPI_EXTENSION + 2302)
TLV_TYPE_PROCESS_GROUP         = TLV_META_TYPE_GROUP  | (TLV_STDAPI_EXTENSION + 2303)
TLV_TYPE_PROCESS_ARCH          = TLV_META_TYPE_UINT   | (TLV_STDAPI_EXTENSION + 2306)
TLV_TYPE_PARENT_PID            = TLV_META_TYPE_UINT   | (TLV_STDAPI_EXTENSION + 2307)
TLV_TYPE_PROCESS_SESSION       = TLV_META_TYPE_UINT   | (TLV_STDAPI_EXTENSION + 2308)

# Priv constants
TLV_TYPE_ELEVATE_TECHNIQUE     = TLV_META_TYPE_UINT   | (TLV_PRIV_EXTENSION   + 200)
TLV_TYPE_ELEVATE_SERVICE_NAME  = TLV_META_TYPE_STRING | (TLV_PRIV_EXTENSION   + 201)

# Kiwi constants
TLV_TYPE_KIWI_PWD_ID           = TLV_META_TYPE_UINT    | (TLV_KIWI_EXTENSION  + 1)
TLV_TYPE_KIWI_PWD_RESULT       = TLV_META_TYPE_GROUP   | (TLV_KIWI_EXTENSION  + 2)
TLV_TYPE_KIWI_PWD_USERNAME     = TLV_META_TYPE_STRING  | (TLV_KIWI_EXTENSION  + 3)
TLV_TYPE_KIWI_PWD_DOMAIN       = TLV_META_TYPE_STRING  | (TLV_KIWI_EXTENSION  + 4)
TLV_TYPE_KIWI_PWD_PASSWORD     = TLV_META_TYPE_STRING  | (TLV_KIWI_EXTENSION  + 5)
TLV_TYPE_KIWI_PWD_AUTH_HI      = TLV_META_TYPE_UINT    | (TLV_KIWI_EXTENSION  + 6)
TLV_TYPE_KIWI_PWD_AUTH_LO      = TLV_META_TYPE_UINT    | (TLV_KIWI_EXTENSION  + 7)
TLV_TYPE_KIWI_PWD_LMHASH       = TLV_META_TYPE_STRING  | (TLV_KIWI_EXTENSION  + 8)
TLV_TYPE_KIWI_PWD_NTLMHASH     = TLV_META_TYPE_STRING  | (TLV_KIWI_EXTENSION  + 9)

# Incognito constants
TLV_TYPE_INCOGNITO_LIST_TOKENS_DELEGATION      = TLV_META_TYPE_STRING  | (TLV_INCOGNITO_EXTENSION + 2)
TLV_TYPE_INCOGNITO_LIST_TOKENS_IMPERSONATION   = TLV_META_TYPE_STRING  | (TLV_INCOGNITO_EXTENSION + 3)
TLV_TYPE_INCOGNITO_LIST_TOKENS_TOKEN_ORDER     = TLV_META_TYPE_UINT    | (TLV_INCOGNITO_EXTENSION + 4)
TLV_TYPE_INCOGNITO_IMPERSONATE_TOKEN           = TLV_META_TYPE_STRING  | (TLV_INCOGNITO_EXTENSION + 5)
TLV_TYPE_INCOGNITO_GENERIC_RESPONSE            = TLV_META_TYPE_STRING  | (TLV_INCOGNITO_EXTENSION + 6)
TLV_TYPE_INCOGNITO_USERNAME                    = TLV_META_TYPE_STRING  | (TLV_INCOGNITO_EXTENSION + 7)
TLV_TYPE_INCOGNITO_PASSWORD                    = TLV_META_TYPE_STRING  | (TLV_INCOGNITO_EXTENSION + 8)
TLV_TYPE_INCOGNITO_SERVERNAME                  = TLV_META_TYPE_STRING  | (TLV_INCOGNITO_EXTENSION + 9)
TLV_TYPE_INCOGNITO_GROUPNAME                   = TLV_META_TYPE_STRING  | (TLV_INCOGNITO_EXTENSION + 10)

