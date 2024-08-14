import importlib.resources as resources
import os


class Gptzzzs:


    def __init__(self):
        ""


    def test(self):
        testTwo = resources.files("gptzzzs").joinpath('data').joinpath("zaibacu.json")
        print(os.path.exists(str(testTwo)))

