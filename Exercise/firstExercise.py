import time

# current_time = time.ctime()
# print(f"current time in second since epoch: {current_time}")


# # print(time.asctime(time.localtime()))

# # print("Hours, in 24 hour formate",time.strftime("%H", time.localtime()))    # 24 hour format
# # print("Hours,12 hour formate",time.strftime("%I", time.localtime()))    # 12 hour format  (capital i)
# # print(time.strftime("%M", time.localtime()))    # Minutes   (capital m)
# # print(time.strftime("%S", time.localtime()))    # Seconds   (capital s)


# # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# # print(type(current_time))

# import time
# current_hour = time.localtime().tm_hour
# print(current_hour)  # This will print a number between 0 and 23

# import time
# formatted_time = time.strftime("%I:%M:%S %p", time.localtime())
# print(formatted_time)  # Example: 02:30:45 PM


#Exercise:

current_time=time.strftime("%I:%M:%S %p", time.localtime())


current_hour= int(time.strftime("%H", time.localtime()))
print(current_hour)  # This will print a number between 0 and 23

if current_hour>5 and current_hour<12:
    print(f"Good Morning {current_time}")
elif current_hour>=12 and current_hour<17:
    print(f"Good Afternoon {current_time}")
elif current_hour>=17 and current_hour<21:
    print(f"Good Evening {current_time}")
else:
    print(f"Good Night {current_time}")
