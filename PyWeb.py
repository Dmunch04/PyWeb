_Classes = {}
_Elements = {}

class Site:
    def __init__ (self, file_name, file_type, file_path = ''):
        self.file_name = file_name
        self.file_type = file_type
        self.file_path = file_path

        _Elements[file_name] = {}
        _Classes[file_name] = {}

        self.Color = '#ffffff'
        self.FavIcon = ''
        self.Title = 'MyPage'

        self.H1 = _Text ('Sans-Serif', 32, '#000000')
        self.H2 = _Text ('Sans-Serif', 24, '#000000')
        self.H3 = _Text ('Sans-Serif', 18.72, '#000000')
        self.H4 = _Text ('Sans-Serif', 16, '#000000')
        self.H5 = _Text ('Sans-Serif', 13.28, '#000000')
        self.H6 = _Text ('Sans-Serif', 12, '#000000')
        self.P = _Text ('Sans-Serif', 16, '#212121')

    def Add (self, _Type, _Class, _Position, _Text, _Button_Size = '', _IsLink = False, _Link = '#'):
        if not isinstance (_Class, Class):
            print ('Class must be a class element!')
            return

        if not _Type in _Elements[self.file_name].keys():
            _Elements[self.file_name][_Type] = []

        if not _Class in _Classes[self.file_name].keys():
            _Classes[self.file_name][_Class] = []

        _Elements[self.file_name][_Type].append([_Class, _Position, _Text, _Button_Size, _IsLink, _Link])

    def Draw (self, _Type, _Path, _Position, _Size = '', _IsLink = False, _Link = '#'):
        if not _Type in _Elements[self.file_name].keys():
            _Elements[self.file_name][_Type] = []

        if _Size == '':
            size = (50, 50)
            _Size = size

        _Elements[self.file_name][_Type].append([_Path, _Position, _Size, _IsLink, _Link])

    def Complete (self):
        finished_file = self.file_path + '/' + self.file_name + '.html'

        html = Evaluate (self)

        with open (finished_file, 'w+') as file: file.write (html)

class Class:
    def __init__ (self, Name, _Site, TextType, Color = '#000000', Bg_Color = '#ffffff', IsBold = False):
        if not isinstance (_Site, Site):
            print ('Site needs to be a site element!')
            return

        elif not isinstance (TextType, _Text):
            print ('Text needs to be a text element!')
            return

        self.Name = Name
        self._Site = _Site
        self.TextType = TextType
        self.Color = Color
        self.Bg_Color = Bg_Color
        self.IsBold = IsBold

        if not Name in _Classes[_Site.file_name].keys():
            _Classes[_Site.file_name][Name] = [TextType, Color, Bg_Color, IsBold]

class _Text:
    def __init__ (self, Font, Size, Color):
        self.Font = Font
        self.Size = Size
        self.Color = Color

class _FileType:
    def __init__ (self, type):
        self.type = type

def Evaluate (Site):
    _HTML = '<html><head><title>{title}</title><link rel = "shortcut icon" type = "image/png" href = "{icon}" /><style>{{style}}</style></head><body>{{elements}}</body></html>'

    Data = _Elements

    _style_ = ''
    _elements_ = ''

    _HTML = _HTML.format (title = Site.Title, icon = Site.FavIcon)

    _style_ += '*{background-color:' + Site.Color + ';}'
    for element in _Classes[Site.file_name]:
        cur_class = _Classes[Site.file_name][element]

        if not cur_class: continue

        if cur_class[3] == True:
            _style_ += f'.{element}' + '{' + 'font-family:{0};font-size:{1};background-color:{2};color:{3};font-weight:{4};position:absolute;border:none;'.format (cur_class[0].Font, cur_class[0].Size, cur_class[2], cur_class[1], 'bold') + '}'
        else:
            _style_ += f'.{element}' + '{' + 'font-family:{0};font-size:{1};background-color:{2};color:{3};position:absolute;border:none'.format (cur_class[0].Font, cur_class[0].Size, cur_class[2], cur_class[1]) + '}'

    try: _texts = Data[Site.file_name]['TEXT']
    except: pass
    try: _buttons = Data[Site.file_name]['BUTTON']
    except: pass
    try: _images = Data[Site.file_name]['IMAGE']
    except: pass

    try:
        for element in _texts:
            current = ''

            type = element[0].TextType
            name = element[0].Name
            cnt = element[2]
            left = element[1][0]
            top = element[1][1]
            is_link = element[4]
            link = element[5]

            _link = '<a href = "{link_}">{{cnt_}}</a>'.format (link_ = link)

            if type == Site.H1:
                current = '<h1 class = "{0}" style = "left:{1}px;top:{2}px;">{3}</h1>'.format (name, left, top, cnt)

            elif type == Site.H2:
                current = '<h2 class = "{0}" style = "left:{1}px;top:{2}px;">{3}</h2>'.format (name, left, top, cnt)

            elif type == Site.H3:
                current = '<h3 class = "{0}" style = "left:{1}px;top:{2}px;">{3}</h3>'.format (name, left, top, cnt)

            elif type == Site.H4:
                current = '<h4 class = "{0}" style = "left:{1}px;top:{2}px;">{3}</h4>'.format (name, left, top, cnt)

            elif type == Site.H5:
                current = '<h5 class = "{0}" style = "left:{1}px;top:{2}px;">{3}</h5>'.format (name, left, top, cnt)

            elif type == Site.H6:
                current = '<hack6 class = "{0}" style = "left:{1}px;top:{2}px;">{3}</h6>'.format (name, left, top, cnt)

            elif type == Site.P:
                current = '<p class = "{0}" style = "left:{1}px;top:{2}px;">{3}</p>'.format (name, left, top, cnt)

            else:
                print ('Unkown text element!')
                return

            if is_link:
                _elements_ += _link.format (cnt_ = current)
            else:
                _elements_ += current
    except: pass
    try:
        for element in _buttons:
            left = element[1][0]
            top = element[1][1]
            if element[2] != '':
                width = element[2][0]
                height = element[2][1]

                _elements_ += '<form action = "{0}"><input class = "{1}" style = "left:{2}px;top:{3}px;width:{4};height:{5};" type = "submit" value = "{6}" /></form>'.format (element[5], element[0].Name, left, top, width, height, element[3])
            else:
                _elements_ += '<form action = "{0}"><input class = "{1}" style = "left:{2}px;top:{3}px;" type = "submit" value = "{4}" /></form>'.format (element[5], element[0].Name, left, top, element[3])
    except: pass
    try:
        for element in _images:
            left = element[1][0]
            top = element[1][1]
            width = element[2][0]
            height = element[2][0]
            is_link = element[3]
            link = element[4]

            if is_link:
                _elements_ += '<a href = "{0}"><img src = "{1}" width = "{2}" height = "{3}" style = "position:absolute;left:{4}px;top:{5}px;"></a>'.format (link, element[0], width, height, left, top)
            else:
                _elements_ += '<img src = "{0}" width = "{1}" height = "{2}" style = "position:absolute;left:{3}px;top:{4}px;">'.format (element[0], width, height, left, top)
    except: pass

    return _HTML.format (style = _style_, elements = _elements_)

Text = 'TEXT'
Button = 'BUTTON'
Image = 'IMAGE'
HTML = _FileType ('HTML')
CSS = _FileType ('CSS')
