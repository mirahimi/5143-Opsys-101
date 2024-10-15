# GET query to API
# check if parameters are in File or Database tables
# if a file, API selects the file content information and posts it with new PID
# if a database, API selects all the files with the relevant database PID and posts it to Files table with new PID
# error is thrown if file already exists, or is trying to push a database to a file