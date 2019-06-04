import PyWeb

Website = PyWeb.Site ('Main', '')

Website.Color = '#000000'
Website.Title = 'Munchii'

Header = PyWeb.Class ('header', Website, Website.H1, 'D8D8D8', '000000')
Website.Add (PyWeb.Text, Header, (PyWeb.Center, 50), 'MUNCHII')

Website.Complete ()
