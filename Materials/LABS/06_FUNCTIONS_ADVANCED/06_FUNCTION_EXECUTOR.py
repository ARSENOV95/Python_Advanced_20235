def func_executor(*args):
    for tp in args:
        func_name = tp[0]
        fuc_args = tp[1]
        
        def func_name(fuc_args):
            pass

        func_name(fuc_args)


