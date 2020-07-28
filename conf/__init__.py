""" dynamically load settings

author baiyu
"""
import conf.global_settings as settings

class Settings:
    def __init__(self, settings):

        for attr in dir(settings):
            if attr.isupper():
                setattr(self, attr, getattr(settings, attr))

settings = Settings(settings)

if __name__ == "__main__":
    print(dir(settings))
    print(getattr(settings, 'EPOCH'))
    print(settings.EPOCH)