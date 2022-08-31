import configparser


class Config:
    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.parser.read('/Users/teo/Desktop/SeniorDesignP2/Test/Config/settings.plugin.conf')
        print('done')
    def setup(self):
        self.args = []
        for sections in self.parser.sections():
            self.args.append({'title': self.parser[sections]['stationnumber'],
            'active': self.parser[sections]['active'],'author': self.parser[sections]['author']
            ,'date_posted': self.parser[sections]['date_posted'],
            'title': self.parser[sections]['title'],'content': self.parser[sections]['content']})
        return self.args
    def run(self):
        self.tpl = []
        for lines in self.args:
            self.tpl = (lines,self.args)
        return self.tpl[1]

