import sys
def error_msg_detaisl(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in script name [{1}] in the line number [{1}] and the error message details are [{2}]".format(
        filename,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_msg_detaisl(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message