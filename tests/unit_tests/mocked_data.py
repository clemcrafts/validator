
VALID_DATAFRAME = {"guid": 'a18347e0-3dcc-537e-9f0e-b24a79c37cfe', "age": "54", "birthday": "3/25/1967", "signup_date": "10/23/2045", "account_type": "other"}

INVALID_HEADER_FIELD_MISSING = {"age": "54", "birthday": "3/25/1967", "signup_date": "10/23/2045", "account_type": "other"}
INVALID_HEADER_EXTRA_SPACE = {" guid": 'a18347e0-3dcc-537e-9f0e-b24a79c37cfe', " age": "54", " birthday": "3/25/1967", " signup_date": "10/23/2045", " account_type": "other"}
INVALID_HEADER_WRONG_DELIMITER = {"guid;age;birthday;signup_date;account_type": 'a18347e0-3dcc-537e-9f0e-b24a79c37cfe'}
INVALID_HEADER_EXTRA_FIELD = {"foo": "bar", "guid": "a18347e0-3dcc-537e-9f0e-b24a79c37cfe", "age": "54", "birthday": "3/25/1967", "signup_date": "10/23/2045", "account_type": "other"}

INVALID_DATA_WITH_NAN = {"guid": 'a18347e0-3dcc-537e-9f0e-b24a79c37cfe', "age": "NaN", "birthday": "3/25/1967", "signup_date": "10/23/2045", "account_type": "other"}
INVALID_DATA_WITH_INVALID_DATES = {"guid": 'a18347e0-3dcc-537e-9f0e-b24a79c37cfe', "age": "NotADate", "birthday": "NotADate", "signup_date": "NotADate", "account_type": "other"}
INVALID_DATA_WITH_INVALID_ACCOUNTS = {"foo": "bar", "guid": "a18347e0-3dcc-537e-9f0e-b24a79c37cfe", "age": "54", "birthday": "3/25/1967", "signup_date": "10/23/2045", "account_type": "???"}