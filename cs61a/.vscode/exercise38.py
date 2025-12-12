import sqlite3
import random
import time

# --- 1. 简单的数据库测试代码 (已修复 CREATE TABLE 错误) ---

def run_simple_db_test():
    """
    演示基础的 CREATE, INSERT, SELECT 和 COMMIT 操作。
    """
    print("\n--- 运行基础数据库测试 (n.db) ---")
    
    # 建立独立的数据库连接
    db_test = sqlite3.connect("n.db")
    
    try:
        # **【修正 1】**：添加 DROP TABLE IF EXISTS 避免重复运行报错
        db_test.execute("DROP TABLE IF EXISTS nums")
        
        db_test.execute("CREATE TABLE nums AS SELECT 2 UNION SELECT 3")
        print("表 'nums' 创建成功，初始数据: 2, 3")

        # 插入数据 (参数化查询)
        db_test.execute("INSERT INTO nums VALUES (?),(?),(?);", range(4, 7))
        print("数据 4, 5, 6 插入成功。")

        # 查询数据
        result = db_test.execute("SELECT * FROM nums;").fetchall()
        print(f"查询结果 (全部数据): {result}")

        # 提交更改
        db_test.commit()
        
    except sqlite3.OperationalError as e:
        print(f"数据库操作失败: {e}")
        db_test.rollback()
        
    finally:
        # 确保关闭连接
        db_test.close()
        print("基础数据库测试完成。")


# --- 2. Blackjack 游戏代码 (已修复 INSERT VALUES 错误) ---

# --- 2.1 数据定义与初始化 ---

points = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
points.update({str(n): n for n in range(2, 11)})
SUITS = ['♠', '♥', '♦', '♣']

def create_deck_list():
    cards = []
    for suit in SUITS:
        for card_rank in list(points.keys()):
            cards.append(suit + card_rank) 
    return cards

FULL_DECK = create_deck_list()
DB_NAME_GAME = 'cards.db'


# --- 2.2 数据库连接与表设置 ---

def setup_db(db_conn):
    """初始化 cards.db 数据库表和牌堆。"""
    print("\n--- 正在初始化 Blackjack 数据库 ---")
    
    db_conn.execute('DROP TABLE IF EXISTS cards') 
    db_conn.execute('CREATE TABLE cards (player TEXT, card TEXT, value INTEGER, discarded INTEGER)')
    
    # 将完整的牌堆插入数据库
    for card_with_suit in FULL_DECK:
        rank = card_with_suit[1:] 
        value = points[rank]
        
        # **【修正 2】**：将 SQL 语句中的 '0' 改为占位符 '?'
        # 确保占位符 (4个) 与参数 (4个) 数量一致
        db_conn.execute("INSERT INTO cards VALUES (?, ?, ?, ?)", ('Deck', card_with_suit, value, 0)) 
        
    db_conn.commit()
    print("52 张牌已放入 'cards' 表。")


# --- 2.3 核心函数 ---

def hand_score(hand):
    total = sum(points[card[1:]] for card in hand)
    num_aces = sum(1 for card in hand if card[1:] == 'A')

    while num_aces > 0 and total + 10 <= 21:
        total += 10
        num_aces -= 1
        
    return total

def deal(db_conn, card, who):
    """更新数据库中卡牌的持有者状态。"""
    db_conn.execute("UPDATE cards SET player=?, discarded=0 WHERE card=? AND player='Deck'", (who, card))
    db_conn.commit()

def get_deck_cards(db_conn):
    """获取当前牌堆中所有未发出的卡牌。"""
    cursor = db_conn.execute("SELECT card FROM cards WHERE player='Deck' AND discarded = 0")
    return [row[0] for row in cursor.fetchall()]

def get_hand(db_conn, who):
    """获取当前玩家或庄家的手牌。"""
    cursor = db_conn.execute("SELECT card FROM cards WHERE player=? AND discarded = 0", (who,))
    return [row[0] for row in cursor.fetchall()]

def deal_busted(db_conn, who):
    """检查是否爆牌并打印手牌点数。"""
    hand = get_hand(db_conn, who)
    score = hand_score(hand)
    
    print(f"\n{who} 的手牌: {hand} (点数: {score})")
    
    if score > 21:
        print(f"!!! {who} 爆牌 (Busted)! 点数: {score}")
        return True, score
    else:
        return False, score

# --- 2.4 游戏主逻辑 ---

def play_blackjack():
    
    db_game = sqlite3.connect(DB_NAME_GAME)
    
    try:
        setup_db(db_game) # 初始化数据库
        
        print("\n--- 游戏开始 (Dealing...) ---")
        current_deck = get_deck_cards(db_game)
        random.shuffle(current_deck) # 洗牌
        
        # 初始化发牌
        for i in range(4):
            card_to_deal = current_deck.pop(0)
            who = 'Player' if i % 2 == 0 else 'Dealer'
            deal(db_game, card_to_deal, who)
        
        # 玩家回合
        while True:
            busted, player_score = deal_busted(db_game, 'Player')
            if busted:
                return "Player Busted!"

            dealer_hand_show = get_hand(db_game, 'Dealer')
            print(f"庄家亮出的牌: [{dealer_hand_show[0]}]")
            
            if player_score == 21:
                print("Player Blackjack!")
                break
            
            action = input("Hit (要牌) or Stay (停牌)? (h/s): ").lower()
            
            if action == 'h':
                current_deck = get_deck_cards(db_game)
                if not current_deck:
                    return "牌堆空了，无法要牌。"
                    
                new_card = current_deck.pop(0)
                deal(db_game, new_card, 'Player')
            elif action == 's':
                break
            else:
                print("无效输入，请重新输入 'h' 或 's'。")

        # 庄家回合 (仅在玩家未爆牌时)
        dealer_busted = False
        print("\n--- 庄家回合 ---")
        while True:
            dealer_busted, dealer_score = deal_busted(db_game, 'Dealer')
            
            if dealer_busted:
                return "Dealer Busted! Player Wins!"
            
            if dealer_score < 17:
                print("Dealer Hits (庄家点数小于 17，必须要牌)...")
                current_deck = get_deck_cards(db_game)
                if not current_deck:
                    return "牌堆空了，无法要牌。"
                    
                new_card = current_deck.pop(0)
                deal(db_game, new_card, 'Dealer')
                time.sleep(1)
            else:
                print("Dealer Stays (庄家点数大于等于 17，停牌)...")
                break
        
        # 结算结果
        player_score = hand_score(get_hand(db_game, 'Player'))
        dealer_score = hand_score(get_hand(db_game, 'Dealer'))

        print("\n--- 最终结算 ---")
        print(f"玩家点数: {player_score}")
        print(f"庄家点数: {dealer_score}")
        
        if player_score > dealer_score:
            return "Player Wins!"
        elif player_score < dealer_score:
            return "Dealer Wins!"
        else:
            return "Push (平局)!"
            
    finally:
        db_game.close()

# --- 3. 主程序入口 ---

if __name__ == "__main__":
    # 运行第一个数据库测试
    run_simple_db_test()
    
    # 运行 Blackjack 游戏
    game_result = play_blackjack()
    print("\n==================================")
    print(f"Blackjack 游戏结果: {game_result}")
    print("==================================")