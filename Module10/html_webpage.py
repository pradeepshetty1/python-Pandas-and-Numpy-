from win32com.shell import shell, shellcon
import os

class MyProjectPage(object):

    # project header template
    _header = '''
                <head>
                      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                      <title>My Projects</title>
                      <style type="text/css" media="screen">
                        table{
                            empty-cells:hide;
                        }
                        tr.row{
                            background-color: #EBF4FA;
                        }
                        tr.alt{
                            background-color: #ffffff;
                        }
                        td.cell{
                            width: 15em;
                            height: 2em;
                            border: black 1px solid;
                        }
                        td.vcell{
                            width: 25em;
                            height: 2em;
                            border: black 1px solid;
                            text-align: left
                        }
                      </style>
                </head>
              '''

    # project body template
    _body = '''
                <body>
                    <br>Below is a list of my projects : <br>
                    <br>
                      <table style="border: black 2px solid;">
                        <tr class="row">
                            <td class="cell">Project 1</td>
                            <td align="center" class="vcell">{p1_detail}</td>
                        </tr>
                        <tr class="alt">
                            <td class="cell">Project 2</td>
                            <td align="center" class="vcell">{p2_detail}</td>
                        </tr>
                        <tr class="row">
                            <td class="cell">Project 3</td>
                            <td align="center" class="vcell">{p3_detail}</td>
                        </tr>
                      </table>
                    <br>
                    <br>Above projects were implemented using Python. Please click <a href="{py_libraries}">here</a> to refer all python libraries.<br>
                    <br>Confidential. For Edureka Use Only. Information not to be distributed without permission.<br>
                    <br>@Generated from PyCharm.<br>
                </body>
            '''

    # initialise and setup body placeholders
    def __init__(self):
        self.html_placeholders = dict()
        self.html_placeholders['p1_detail'] = 'Text processing using NLTK.'
        self.html_placeholders['p2_detail'] = 'Web scraping using beautifulsoup.'
        self.html_placeholders['p3_detail'] = 'Data munging using pymongo and pyes.'
        self.html_placeholders['py_libraries'] = 'https://pypi.python.org/pypi'
        self.fill_content()

    # fill body template with actual values
    def fill_content(self):
        self.content = self._header + self._body.format(**self.html_placeholders)

    # write html output to file
    def write_to_file(self):
        if hasattr(self, 'content') and self.content is not None:
            desktop_path = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0)
            outfile = open(os.path.join(desktop_path, 'MyProjects.html'), 'w')
            outfile.write(self.content)
            outfile.close()


if __name__ == '__main__':
    mywebpg = MyProjectPage()
    mywebpg.write_to_file()