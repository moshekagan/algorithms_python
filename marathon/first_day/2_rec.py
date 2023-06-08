def my_fuc(count):
    print("Hello! :)")

    if count > 0:
        my_fuc(count-1) # 1
    else:
        return


my_fuc(5)
