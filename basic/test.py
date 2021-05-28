import pandas as pd

my_dict = {'Computer':1500,'Monitor':300,'Printer':150,'Desk':250}
df = pd.DataFrame(list(my_dict.items()),columns = ['Products','Prices'])

print (df)