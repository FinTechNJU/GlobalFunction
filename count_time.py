def count_time(func):
    def time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        result = func(*args, **kwargs)
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序 %s 共计%s秒' %(str(func).split(" ")[1].ljust(15,"."),total_time))
        return result
    return time