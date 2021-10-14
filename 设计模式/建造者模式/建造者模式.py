import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract


# 设计模式之建造者模式
class Player:
    """
        初始化对象的各个部件
    """

    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        """
            __str__ 返回一个对象的描述信息
        """
        return '%s, %s, %s, %s' % (self.face, self.body, self.arm, self.leg)


# 构建建造者类
# 想要将上述的对象的各个部件，进行指定顺序的填充
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


# 根据建造者类实例化建造者1
class SexyGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "SexyGirl的脸蛋"

    def build_body(self):
        self.player.body = "SexyGirl的身体"

    def build_arm(self):
        self.player.arm = "SexyGirl的胳膊"

    def build_leg(self):
        self.player.leg = "SexyGirl的腿"


# 根据建造者类实例化建造者2
class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "Monster的脸蛋"

    def build_body(self):
        self.player.body = "Monster的身体"

    def build_arm(self):
        self.player.arm = "Monster的胳膊"

    def build_leg(self):
        self.player.leg = "Monster的腿"


class PlayDoctor:
    """
        用于控制建造的顺序
    """
    def build_player(self, builder):
        builder.build_face()
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# 客户端
# 1. 创建一个建造者，用于建造Player的各个部件
builder = SexyGirlBuilder()
# 2. 创建一个类，来控制建造各个部件的顺序，并返回建造的结果
doctor = PlayDoctor()
# 3. 构建出建造的结果
p = doctor.build_player(builder)
print(p)
