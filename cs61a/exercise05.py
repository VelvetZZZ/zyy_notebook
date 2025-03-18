#Function Example:Sounds--WAV Files波形文件
#波形文件的作用：直接编码声波的样本

from wave import open
from struct import Struct
from math import floor#将数字四舍五入为小于该值的最大整数

frame_rate = 11025#frame rate帧速率/sampling rate采样率

def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    (See http://docs.python.org/3/library/struct.html)
    """
    i = int(16384 * x)
    return Struct('h').pack(i)#如何根据WAV文件要求编码值的方法

#以下是实际写入WAV文件的函数
def play(sampler, name="song.wav", seconds=2):
    """Write the output of a sampler function as a WAV file."""#描述我们试图生成的歌曲的波形
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    
    t = 0
    while t < seconds * frame_rate:#迄今为止歌曲已经经过的时间
        sample = sampler(t)
        out.writeframes(encode(sample))
        t += 1
    
    out.close()

def tri(frequency, amplitude=0.3):#frequency of the waves determines the pitch 波的频率决定了音调
    """A continuous triangle wave."""#the amplitude determines the volume振幅决定了音量
    period = frame_rate //frequency

    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave#锯齿波的绝对值乘以振幅得到三角波

    return sampler

c_freq,e_freq,g_freq = 261.63,329.63,392.00 #c音符的频率是261.63（fact）

def both(f,g):
    return lambda t: f(t) + g(t)

def note(f, start, end, fade=0.01):#fade为开头结尾添加的淡入淡出,fade越短声音越自然
    def sampler(t):#创建一个采样函数
        seconds = t / frame_rate#将t表达为秒
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler   

def mario_at(octave):
    c, e = tri(octave * c_freq), tri(octave * e_freq)
    g, low_g = tri(octave * g_freq),tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)
#编写和声

def mario(c, g, e, low_g):
    z = 0
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))
    z += 1/2
    return song
play(both(mario_at(1),mario_at(1/2)))




#详细注释R
from wave import open  # 导入 wave 模块，用于创建和操作 WAV 音频文件
from struct import Struct  # 导入 Struct 模块，用于二进制数据处理
from math import floor  # 导入 floor 函数，用于向下取整

# 设置帧速率（采样率），决定每秒采样多少个数据点
frame_rate = 11025  # 11025 Hz（较低的音频质量，适合简单声音）

def encode(x):
    """将 -1 到 1 之间的浮点数编码为两个字节的整数格式"""
    i = int(16384 * x)  # 放大音频信号，使其适应 16-bit 整数格式
    return Struct('h').pack(i)  # 转换为二进制数据（'h' 代表 short int，2 字节）

# 实际写入 WAV 文件的函数
def play(sampler, name="song.wav", seconds=2):
    """将采样函数的输出写入 WAV 文件"""
    out = open(name, 'wb')  # 以二进制写入模式打开文件
    out.setnchannels(1)  # 设置为单声道
    out.setsampwidth(2)  # 每个样本 2 字节（16-bit PCM）
    out.setframerate(frame_rate)  # 设定帧速率
    
    t = 0
    while t < seconds * frame_rate:  # 遍历整个音频时长
        sample = sampler(t)  # 计算当前时间点的采样值
        out.writeframes(encode(sample))  # 写入 WAV 文件
        t += 1  # 时间步进
    
    out.close()  # 关闭文件

def tri(frequency, amplitude=0.3):
    """生成一个连续的三角波，频率决定音高，振幅决定音量"""
    period = frame_rate // frequency  # 计算波形的周期（采样点数）

    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)  # 生成锯齿波
        tri_wave = 2 * abs(2 * saw_wave) - 1  # 变换为三角波
        return amplitude * tri_wave  # 调整振幅

    return sampler  # 返回一个采样函数

# 定义音符的频率（单位 Hz）
c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

def both(f, g):
    """返回一个函数，该函数的输出是两个输入函数的和（叠加声音）"""
    return lambda t: f(t) + g(t)

def note(f, start, end, fade=0.01):
    """创建一个音符，并添加淡入淡出效果"""
    def sampler(t):
        seconds = t / frame_rate  # 计算当前时间点（秒）
        if seconds < start:
            return 0  # 在开始前无声音
        elif seconds > end:
            return 0  # 在结束后无声音
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)  # 淡入
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)  # 淡出
        else:
            return f(t)  # 正常播放
    return sampler

def mario_at(octave):
    """创建 Super Mario 主题音乐，按倍频调整音高"""
    c, e = tri(octave * c_freq), tri(octave * e_freq)
    g, low_g = tri(octave * g_freq), tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)

def mario(c, g, e, low_g):
    """定义 Mario 主题音乐的音符序列"""
    z = 0  # 时间起点
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))
    z += 1/2
    return song  # 返回生成的音乐片段

# 播放 Mario 主题音乐的变体，一个原调，一个低八度
play(both(mario_at(1), mario_at(1/2)))
