class Configuracao:
    _instance = None

    def new(cls):
        if cls._instance is None:
            cls._instance = super(Configuracao, cls).new(cls)
        return cls._instance

config1 = Configuracao()
config2 = Configuracao()

print(config1 is config2)