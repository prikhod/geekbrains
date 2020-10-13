from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self, red_time=7, yellow_time=3, green_time=6):
        self._color = [['красный', red_time], ['желтый', yellow_time], ['зеленый', green_time], ['желтый', yellow_time]]

    def running(self):
        for el in cycle(self._color):
            print(el[0])
            sleep(el[1])


if __name__ == '__main__':
    tl = TrafficLight(5, 2, 3)
    tl.running()
