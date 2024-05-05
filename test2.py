class Config:
    hello = 'default'
    number = 0
    state = False

class Hello(Config):
    def __init__(self):
        self.world = ['Hello inheritence!']

class Tools(Config):
    def sqr(self):
        self.world += [Config.number**2]
        return Config.number**2
    
class World(Config):
    def hello(self):
        self.world += [Config.hello + ' world!']
        return Config.hello + ' world!'
    
class App(Tools,World,Hello):
    def __init__(self, hello, num) -> None:
        Config.hello = hello
        Config.number = num
        super().__init__()

    
    def run(self):
        print('Running')
        print(self.sqr())
        print(self.hello())
        # print(self.world)
        # raise Exception("Idk.")

    def start(self):
        test = App("Hola", 10)
        try:    
            test.run()
            print(test.world)
        except Exception as error:
            print(test.world, error)

if __name__ == "__main__":
    try:
        f[1] =10
    except:
        print('123456789'[8:])
    test = App('',0)
    test.start()