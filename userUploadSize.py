import os

# A little deceptive, because of the name, but this gets the total space used in the user upload directory
# The point is to restrict user uploads to 500MB, so as not to have all our server space wasted by malicious users

def getuserUploadSize(start_path = './user/userUploads'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size