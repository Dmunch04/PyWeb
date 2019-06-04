# Find X Center: (ScreenWidth / 2) - (ElementWidth / 2)
# Find Y Center: (ScreenHeight / 2) - (ElementHeight / 2)

import os
from DavesLogger import Logs

_Classes = {}
_Elements = {}

_TextTypes = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
_Keywords = ['left', 'middle', 'right', 'upper', 'lower']

class Site:
    def __init__ (self, FileName, FilePath = ''):
        self.FileName = FileName
        self.FilePath = FilePath

        _Elements[FileName] = {}
        _Classes[FileName] = {}

        self.Color = '#ffffff'
        self.FavIcon = ''
        self.Title = 'Untitled'

        self.H1 = _Text ('h1', 'Sans-Serif', 32, '#000000')
        self.H2 = _Text ('h2', 'Sans-Serif', 24, '#000000')
        self.H3 = _Text ('h3', 'Sans-Serif', 18.72, '#000000')
        self.H4 = _Text ('h4', 'Sans-Serif', 16, '#000000')
        self.H5 = _Text ('h5', 'Sans-Serif', 13.28, '#000000')
        self.H6 = _Text ('h6', 'Sans-Serif', 12, '#000000')
        self.P = _Text ('p', 'Sans-Serif', 16, '#212121')

    def Add (self, _Type, _Class, _Position, _Text, _Button_Size = '', _IsLink = False, _Link = '#'):
        if not isinstance (_Class, Class):
            #print ('Class must be a class element!')
            Logs.Error ('Class must be a class element!')
            return

        if not _Type in _Elements[self.FileName].keys():
            _Elements[self.FileName][_Type] = []

        if not _Class in _Classes[self.FileName].keys():
            _Classes[self.FileName][_Class] = []

        _Elements[self.FileName][_Type].append([_Class, _Position, _Text, _Button_Size, _IsLink, _Link])

    def Draw (self, _Type, _Path, _Position, _Size = '', _IsLink = False, _Link = '#'):
        if not _Type in _Elements[self.FileName].keys ():
            _Elements[self.FileName][_Type] = []

        if _Size == '':
            size = (50, 50)
            _Size = size

        _Elements[self.FileName][_Type].append ([_Path, _Position, _Size, _IsLink, _Link])

    def Complete (self):
        FinishedPath = os.path.join (self.FilePath + self.FileName) + '.html'

        HTML = Evaluate (_Elements, self)

        with open (FinishedPath, 'w+') as File: File.write (HTML)

        Logs.Success ('Successfully created the HTML file at: ' + FinishedPath)

class Class:
    def __init__ (self, Name, _Site, TextType, Color = '#000000', Bg_Color = '#ffffff', IsBold = False):
        if not isinstance (_Site, Site):
            #print ('Site needs to be a site element!')
            Logs.Error ('Site needs to be a site element!')
            return

        elif not isinstance (TextType, _Text):
            #print ('Text needs to be a text element!')
            Logs.Error ('Text needs to be a text element!')
            return

        self.Name = Name
        self._Site = _Site
        self.TextType = TextType
        self.Color = Color
        self.Bg_Color = Bg_Color
        self.IsBold = IsBold

        if not Name in _Classes[_Site.FileName].keys():
            _Classes[_Site.FileName][Name] = [TextType, Color, Bg_Color, IsBold]

class _Text:
    def __init__ (self, Name, Font, Size, Color):
        self.Name = Name
        self.Font = Font
        self.Size = Size
        self.Color = Color

def Evaluate (_Data, _Site):
    _HTML = '<html><head><title>{Title}</title><link rel = "shortcut icon" type = "image/png" href = "{Icon}" /><style>{{Style}}</style></head><body>{{Elements}}</body></html>'

    _Style_, _Elements_ = '', ''

    _HTML = _HTML.format (Title = _Site.Title, Icon = _Site.FavIcon)

    _Style_ += '*{background-color:' + _Site.Color + ';}'
    for Element in _Classes[_Site.FileName]:
        CurClass = _Classes[_Site.FileName][Element]

        if not CurClass: continue

        if CurClass[3] == True:
            _Style_ += f'.{Element}' + '{' + 'font-family:{0};font-size:{1};background-color:{2};color:{3};font-weight:{4};position:absolute;border:none;'.format (CurClass[0].Font, CurClass[0].Size, CurClass[2], CurClass[1], 'bold') + '}'

        else:
            _Style_ += f'.{Element}' + '{' + 'font-family:{0};font-size:{1};background-color:{2};color:{3};position:absolute;border:none'.format (CurClass[0].Font, CurClass[0].Size, CurClass[2], CurClass[1]) + '}'

    Object = _Data[_Site.FileName]
    _Texts = Object.get ('TEXT')
    _Buttons = Object.get ('BUTTON')
    _Images = Object.get ('IMAGE')

    try:
        for Element in _Texts:
            Current = ''

            Type = Element[0].TextType
            Name = Element[0].Name
            Value = Element[2]
            Left = Element[1][0]
            Top = Element[1][1]
            IsLink = Element[4]
            Link = Element[5]

            if Left.lower () == 'center':
                Left = (1920 / 2) - (ElementWidth / 2)

            _Link = '<a href = "{Link_}">{{Value_}}</a>'.format (Link_ = Link)

            if Type.Name.lower () in _TextTypes:
                Current = '<{0} class = "{1}" style = "left:{2}px;top:{3}px;">{4}</{5}>'.format (Type.Name.lower(), Name, Left, Top, Value, Type.Name.lower ())

            else:
                #print ('Unkown text element!')
                Logs.Error ('Unkown text element!')
                return

            if IsLink: _Elements_ += _Link.format (Value_ = Current)

            else: _Elements_ += Current

    except: Logs.Debug ('No text elements..')

    try:
        for Element in _Buttons:
            Left = Element[1][0]
            Top = Element[1][1]

            if Element[2] != '':
                Width = Element[2][0]
                Height = Element[2][1]

                _Elements_ += '<form action = "{0}"><input class = "{1}" style = "left:{2}px;top:{3}px;width:{4};height:{5};" type = "submit" value = "{6}" /></form>'.format (Element[5], Element[0].Name, Left, Top, Width, Height, Element[3])

            else:
                _Elements_ += '<form action = "{0}"><input class = "{1}" style = "left:{2}px;top:{3}px;" type = "submit" value = "{4}" /></form>'.format (Element[5], Element[0].Name, Left, Top, Element[3])

    except: Logs.Debug ('No button elements..')

    try:
        for Element in _Images:
            Left = Element[1][0]
            Top = Element[1][1]
            Width = Element[2][0]
            Height = Element[2][0]
            IsLink = Element[3]
            Link = Element[4]

            if IsLink:
                _Elements_ += '<a href = "{0}"><img src = "{1}" width = "{2}" height = "{3}" style = "position:absolute;left:{4}px;top:{5}px;"></a>'.format (Link, Element[0], Width, Height, Left, Top)

            else:
                _Elements_ += '<img src = "{0}" width = "{1}" height = "{2}" style = "position:absolute;left:{3}px;top:{4}px;">'.format (Element[0], Width, Height, Left, Top)

    except: Logs.Debug ('No image elements..')

    return _HTML.format (Style = _Style_, Elements = _Elements_)

Text = 'TEXT'
Button = 'BUTTON'
Image = 'IMAGE'
Center = 'CENTER'
