import traceback

try:
    raise Exception('This is error message')
except:
    errorfile = open('error_info.txt','w')
    errorfile.write(traceback.format_exc())
    errorfile.close()
    print('The traceback info was written to errorinfo.txt')