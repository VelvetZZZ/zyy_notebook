#Iterators
s =[3, 4, 5]
t = iter(s)
print(next(t))
print(next(t))

u = iter(s)
print(next(u))
print(next(t))
print(next(u))#iterator is independent

s = [[1, 2], 3, 4, 5]
#If you print'next'here,you'll get a TypeError:'list' object is not an iterator
t = iter(s)
print(next(t))
print(next(t))
print(list(t))#We already used up the list[1, 2]&number3
#If you print'next(t)' here, Python will raise a stop iteration.This how you tell you're at the end.


#Dictionary Iteration
d = {'one': 1, 'two': 2, 'three': 3}
d['zero'] = 0#添加一个新的键值对（key-value pairs）
#获取键视图的迭代器
k = iter(d.keys())#or iter(d)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
# >>> next(k)  # 如果再调用一次，会引发 StopIteration
# 获取值视图的迭代器
v = iter(d.values())
print(next(v))
print(next(v))
print(next(v))
print(next(v))
#与键类似，d.values() 提供值的视图，iter() 创建迭代器 v。next(v) 按照对应键的插入顺序返回值。
# 获取项视图的迭代器
i = iter(d.items())
print(next(i))
print(next(i))
print(next(i))
print(next(i))
#***每个项是一个元组 (key, value)***


#使用for循环会更简洁
d = {'one': 1, 'two':2, 'three': 3}
d['zero'] = 0

print("Keys:")
for key in d :
    print(key)
print("\nValues:")#\n 是一个转义字符，代表一个换行符。所以这行代码会先换一行，然后再打印文本 "Values:"
for value in d.values():
    print(value)

print("\nItems:")
for key, value in d.items():#元组解包 (tuple unpacking)
    print(f"Key: {key}, Value: {value}")

#iterator is invalid 迭代器无效的情况
'''在迭代一个字典的过程中，不应该改变该字典的大小（即添加或删除元素）
如果你这么做了,Python 通常会抛出一个 RuntimeError'''
d = {'one': 1, 'two': 2}#字典 d 的大小是 2 (因为它包含两个元素)。
k = iter(d)
print(next(k))

d['zero'] = 0#向字典 d 中添加一个新的键值对：'zero': 0,字典 d 的大小从 2 变成了 3
#print(next(k))
"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration"""

print(d)
k = iter(d)
print(next(k))
print(next(k))
d['zero'] = 5
print(next(k))
#如果改变的是字典中已存在键的值，而不是添加或删除键（即不改变字典的大小），那么迭代通常可以继续（尽管这仍然可能导致逻辑上的困惑，但不会直接触发 RuntimeError）。(对键、值、项都一样)

#For Statements
r = range(3, 6)
ri = iter(r)
for i in ri:
    print(i)

for i in ri:
    print(i)#see nothing

for i in r:
    print(i)
for i in r:
    print(i)#for statement->able to go through the entire contents from beginning to end without worrying about changing.

#Built-In Iterator Functions迭代的内建函数 
bcd = ['b', 'c', 'd']
print([x.upper() for x in bcd])

map(lambda x: x.upper(), bcd)
m = map(lambda x: x.upper(), bcd)
print(next(m))
print(next(m))
print(next(m))

def double(x):
    print('**', x, '=>', 2*x, '**')
    return 2*x#在 Python 中，如果一个函数没有明确的 return 语句，它会默认返回 None.
map(double, [3, 5, 7])
m = map(double, [3, 5, 7])
print(next(m))
print(next(m))
print(next(m))#double applied lazily

m = map(double, range(3, 7))
f = lambda y: y >= 10
t = filter(f, m)#创建一个过滤函数
print(next(t))
print(next(t))

print(list(t))#3-6已经遍历完啦【Done】

print(list(filter(f, map(double, range(3, 7)))))


#trap
t = [1, 2, 3, 2, 1]
print(reversed(t))
print(reversed(t) == t)#iterator & list --> false
print(list(reversed(t)))
print(list(reversed(t)) == t)#list & list

#The Zip Function 遍历共同索引元组的迭代器
list1 = [1, 2]
list2 = [3, 4]
zipped_items = zip(list1, list2)
print(list(zipped_items)) 

print(list(zip([1, 2],[3, 4, 5],[6, 7])))

#Implement palindrome,which returns whether s is the same forward and backward
def palindrome(s):
  """
  判断一个序列 s 是否是回文。
  s 可以是列表、元组或字符串。
  """
  return s == s[::-1] # s[::-1] 是 Python 中获取序列反转副本的简洁方法
print(palindrome([3, 1, 4, 1, 3]))
print(palindrome([3, 1, 4, 1, 5]))
#同理
def palindrome(s):
    return list(s) == list(reversed(s))
print(palindrome([3, 1, 4, 1, 3]))
#同理
def palindrome(s):
    return all([a == b for a, b in zip(s, reversed(s))])
print(palindrome([3, 1, 4, 1, 3]))


#Example:Casino Blackjack
import random

# --- 卡牌和牌堆工具 (Card and Deck Utilities) ---

def create_deck():
    """创建并洗牌一副简化的牌堆 (只关心点数)"""
    # 点数: 2-10, J, Q, K, A
    # 为了简化，我们不区分花色，每种点数的牌有4张
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    deck = ranks * 4  # 每种点数4张
    random.shuffle(deck)
    return deck

def card_value(card_rank):
    """计算单张牌的点数 (A inicialmente算11点)"""
    if card_rank in ['J', 'Q', 'K']:
        return 10
    elif card_rank == 'A':
        return 11  # A 初始算 11
    else:
        return int(card_rank)

def hand_score(hand):
    """计算一手牌的总点数，智能处理 A (可以算1点或11点)"""
    score = 0
    num_aces = 0
    for card in hand:
        value = card_value(card)
        if card == 'A':
            num_aces += 1
        score += value

    # 如果总点数 > 21 并且手中有 A，则将 A 从 11点转为 1点
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    return score

# --- 策略函数 (Strategy Functions) ---

def basic_strategy(dealer_up_card, player_hand, print_func=lambda *args, **kwargs: None):
    """
    基础策略：如果玩家手牌点数小于等于11，则要牌 (Hit)。
    dealer_up_card 在这个极简策略中并未使用，但通常策略会考虑它。
    print_func 用于可选的策略内部打印，默认为不打印。
    """
    score = hand_score(player_hand)
    if score <= 11:
        # print_func(f"BasicStrategy: Score {score} <= 11. Hitting.")
        return True  # True 代表 Hit (要牌)
    else:
        # print_func(f"BasicStrategy: Score {score} > 11. Standing.")
        return False # False 代表 Stand (停牌)

def always_stand_strategy(dealer_up_card, player_hand, print_func=lambda *args, **kwargs: None):
    """一个总是停牌的策略，用于对比"""
    return False # Stand

# --- 安静函数 (Silent Function) ---

def shhh(*args, **kwargs): # 使用 *args, **kwargs 使其能接受任意参数，像 print 一样
    """不打印任何东西，也不做任何事。用于在模拟中静音输出。"""
    pass

# --- 游戏流程函数 (Game Flow Functions) ---

def player_turn(player_hand, dealer_up_card, deck, strategy_func, print_func):
    """处理玩家的回合"""
    print_func(f"【玩家回合】手牌: {player_hand}, 点数: {hand_score(player_hand)}")
    # print_func(f"庄家亮牌: {dealer_up_card}") # 庄家亮牌在 blackjack 函数开始时显示

    while hand_score(player_hand) < 21: # 如果没爆牌
        # 调用策略函数决定是否要牌
        if strategy_func(dealer_up_card, player_hand, print_func=print_func):
            new_card = deck.pop()
            player_hand.append(new_card)
            print_func(f"玩家选择 [要牌]，得到: {new_card}。新手牌: {player_hand}, 点数: {hand_score(player_hand)}")
            if hand_score(player_hand) > 21:
                print_func("玩家爆牌!")
                break
        else:
            print_func("玩家选择 [停牌]。")
            break
    return player_hand

def dealer_turn(dealer_hand, deck, print_func):
    """处理庄家的回合"""
    print_func(f"【庄家回合】初始手牌: {dealer_hand}, 点数: {hand_score(dealer_hand)}")
    # 庄家通常在点数小于17时要牌
    while hand_score(dealer_hand) < 17:
        new_card = deck.pop()
        dealer_hand.append(new_card)
        print_func(f"庄家选择 [要牌]，得到: {new_card}。新手牌: {dealer_hand}, 点数: {hand_score(dealer_hand)}")
        if hand_score(dealer_hand) > 21:
            print_func("庄家爆牌!")
            break
    if hand_score(dealer_hand) <= 21:
        print_func("庄家选择 [停牌]。")
    return dealer_hand

def blackjack(strategy_func, print_func=print):
    """
    进行一局简化的 Blackjack 游戏。
    返回: 1 代表玩家赢, -1 代表玩家输, 0 代表平局。
    """
    deck = create_deck()

    player_hand = []
    dealer_hand = []

    # 初始发牌 (各两张)
    for _ in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    dealer_up_card = dealer_hand[0] # 庄家的一张明牌

    print_func("\n--- 新的一局 Blackjack ---")
    print_func(f"庄家亮牌: {dealer_up_card}")
    # print_func(f"玩家初始手牌: {player_hand}, 点数: {hand_score(player_hand)}") # 会在 player_turn 中打印

    # 玩家回合
    player_hand = player_turn(player_hand, dealer_up_card, deck, strategy_func, print_func)
    player_final_score = hand_score(player_hand)

    # 如果玩家爆牌，庄家直接赢
    if player_final_score > 21:
        print_func("最终结果: 玩家爆牌，庄家赢。")
        return -1

    # 庄家回合 (只有在玩家没有爆牌时进行)
    print_func(f"庄家亮出底牌。完整手牌: {dealer_hand}, 点数: {hand_score(dealer_hand)}")
    dealer_hand = dealer_turn(dealer_hand, deck, print_func)
    dealer_final_score = hand_score(dealer_hand)

    print_func("--- 结算 ---")
    print_func(f"玩家最终手牌: {player_hand}, 点数: {player_final_score}")
    print_func(f"庄家最终手牌: {dealer_hand}, 点数: {dealer_final_score}")

    if dealer_final_score > 21:
        print_func("最终结果: 庄家爆牌，玩家赢！")
        return 1
    elif player_final_score > dealer_final_score:
        print_func("最终结果: 玩家赢！")
        return 1
    elif dealer_final_score > player_final_score:
        print_func("最终结果: 庄家赢。")
        return -1
    else: # player_final_score == dealer_final_score
        print_func("最终结果: 平局 (Push)。")
        return 0

# --- 模拟函数 (Simulation Function) ---

def gamble(strategy_func, num_hands=1000):
    """模拟多次游戏并统计结果"""
    print(f"\n\n--- 开始使用策略 '{strategy_func.__name__}' 模拟 {num_hands} 手游戏 ---")
    net_outcome = 0         # 玩家总输赢
    player_wins = 0
    dealer_wins = 0
    pushes = 0

    for i in range(num_hands):
        # 在模拟大量牌局时，我们不希望每一局都打印详细信息，所以传递 shhh 函数
        # 如果 num_hands 较小，或者你想调试，可以传递 print
        if (i + 1) % (num_hands // 20 if num_hands >= 20 else 1) == 0 or i == num_hands -1 : # 打印进度
            print(f"正在模拟第 {i+1}/{num_hands} 手...")

        result = blackjack(strategy_func, print_func=shhh) # 使用 shhh 来静音单局输出
        net_outcome += result
        if result == 1:
            player_wins += 1
        elif result == -1:
            dealer_wins += 1
        else:
            pushes += 1

    print("\n--- 模拟结果统计 ---")
    print(f"策略: {strategy_func.__name__}")
    print(f"总手数: {num_hands}")
    print(f"玩家赢: {player_wins} 次 ({(player_wins/num_hands)*100:.2f}%)")
    print(f"庄家赢: {dealer_wins} 次 ({(dealer_wins/num_hands)*100:.2f}%)")
    print(f"平局:   {pushes} 次 ({(pushes/num_hands)*100:.2f}%)")
    print(f"玩家净结果: {net_outcome} (赢1局计+1, 输1局计-1)")
    print("--------------------------")
    return net_outcome

# --- 主程序执行示例 ---
if __name__ == "__main__":
    # 玩一局游戏并打印详细过程
    print("--- 玩一局游戏 (使用 basic_strategy, 详细打印) ---")
    blackjack(basic_strategy, print_func=print)

    # 模拟 basic_strategy
    gamble(basic_strategy, num_hands=10000)

    # 模拟 always_stand_strategy (总是停牌的策略)
    gamble(always_stand_strategy, num_hands=10000)
