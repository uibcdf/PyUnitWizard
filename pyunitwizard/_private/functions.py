import inspect

def caller_name(skip=3):

    return inspect.stack()[skip].function

    #all_stack_frames = stack()
    #caller_stack_frame = all_stack_frames[1]
    #caller_name = caller_stack_frame[3]

