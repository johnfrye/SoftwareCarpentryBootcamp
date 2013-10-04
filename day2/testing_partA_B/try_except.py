file_name = "test.csv"
default_file = "../../day1/partD/rodents.csv"

try:
    f = open(file_name)
# Execute this only if there is an IOError, only errors of
# that type will trigger this except
except IOError as e:
    # Print the actual error
    print e
    f = open(default_file)
except Exception as e:
    print e
    print "There was a problem"
    # Used in an except block, raises the exception that was caught in this block
    # If used anywhere else, it needs to come with the Exception it is raising
    # e.g. raise Exception("problem!")
    raise

print f.readline()
