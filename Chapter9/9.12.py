class TV:
    MIN_VOLUME = 0
    MAX_VOLUME = 20
    MIN_CHANNEL = 0
    MAX_CHANNEL = 200

    def __init__(self, __volume, __channel, __is_on):
        self.__volume = __volume
        self.__channel = __channel
        self.__is_on = __is_on

        __volume = 5
        __channel = 0
        __is_on = False


    def __str__(self):
        return "볼륨 : ".format(self.__volume), ", 채널 : ".format(self.__channel)

    def toggle_power(self):
        if self.__is_on == True:
            self.__is_on = False

        else:
            self.__is_on = True

    def get_channel(self):
        return self.__channel

    def set_channel(self):
        try:
            self.__channel = int(input("채널을 입력하세요 : "))
            return self.__channel
        except:
            if self.__channel > 201 and self.__channel < 0:
                print("채널 오류")

    def get_volume(self):
        return self.__volume

    def set_volume(self):
        try:
            self.__volume = int(input("볼륨을 입력하세요 : "))
            return self.__volume
        except:
            if self.__volume > 201 and self.__volume < 0:
                print("볼륨 오류")

    def volume_up(self):
        if self.__volume <= self.MAX_VOLUME:
            self.__volume = self.__volume + 1

    def volume_down(self):
        if self.__volume >= self.MIN_VOLUME:
            self.__volume = self.__volume - 1

    def channel_up(self):
        self.__channel = self.__channel + 1
        if self.__channel >= 201:
            self.__channel = self.MIN_VOLUME

    def channel_down(self):
        self.__channel = self.__channel - 1
        if self.__channel <= 0:
            self.__channel = self.MAX_VOLUME


my_tv = TV(5, 0, False)
print(my_tv)
#my_tv.toggle_power()
#print(my_tv)
#my_tv.set_channel(45)
#print(my_tv)
#my_tv.volume_up()
#my_tv.channel_up()
#print(my_tv)