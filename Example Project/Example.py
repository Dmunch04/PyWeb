# -- Import --
import PyWeb

# -- Create the site --
# (file name, file path, file type)
Website = PyWeb.Site ('index', '/Example Project', PyWeb.HTML)

# -- General Styling --
Website.Color = '#000000'       # Background color
Website.FavIcon = 'Icon.png'    # FavIcon for the website
Website.Title = 'Munchii'       # The websites title

# -- Classes --
# (name, site, text type, text color, background color)
header = PyWeb.Class ('header', Website, Website.H1, 'D8D8D8', '000000')
sub = PyWeb.Class ('sub', Website, Website.H3, '919191', '000000')
btn = PyWeb.Class ('btn', Website, Website.H5, 'D8D8D8', '101010')

# -- Elements --
# (element type, class, position[x, y], text)
Website.Add (PyWeb.Text, header, (900, 50), 'MUNCHII')
Website.Add (PyWeb.Text, sub, (830, 120), 'Developer  |  Designer  |  Optimist')

# (element type, path, position[x, y], size[width, height])
Website.Draw (PyWeb.Image, '1.svg', (800, 250), (150, 150))
Website.Draw (PyWeb.Image, '2.svg', (1000, 250), (150, 150))
Website.Draw (PyWeb.Image, '3.svg', (800, 450), (150, 150))
Website.Draw (PyWeb.Image, '4.svg', (1000, 450), (150, 150))
Website.Draw (PyWeb.Image, '5.svg', (800, 650), (150, 150))
Website.Draw (PyWeb.Image, '6.svg', (1000, 650), (150, 150))

# (element type, class, position[x, y], size[width, height, text])
Website.Add (PyWeb.Button, btn, (930, 870), (100, 50), 'CONTACT')

# -- Building --
Website.Complete ()
