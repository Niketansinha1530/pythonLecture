import calendar
import myModule

cal=calendar.month(2024,11)
print(cal)

print(type(cal))

print(calendar.isleap(2024))
print(calendar.isleap(2026))
print(calendar.isleap(2020))

print(dir(calendar)) #Getting all function from module

#  https://docs.python.org/3/py-modindex.html


# My module

myModule.greet("Niketan")
myModule.goodbye("Shweta")