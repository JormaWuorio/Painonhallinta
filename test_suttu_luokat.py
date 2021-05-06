stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5,
}

def fillable(stock, merch, n):
    try:
        if stock[merch] >= n:
            return True
    except Exception as e:
        return False
    
        

fillable(stock, 'action figure', 1)