# Import Goldsberry, PANDAS
import goldsberry
import pandas as pd

players2010 = goldsberry.PlayerList(Season='2010-11')
players2010 = pd.Dataframe(players2010.players())
players2010.head()
#
