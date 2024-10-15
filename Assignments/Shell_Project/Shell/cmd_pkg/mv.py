# GET query to API
# check if parameters are in File or Database tables
# if a file, API selects the file content information and posts it with new PID
    # check if file already exists. If it does, rename the file with new name
# if a database, API selects all the files with the relevant database PID and posts it to Files table with new PID
    # check if directory already exists. If it does, rename the directory with new name
# error is thrown if moving a directory to a file