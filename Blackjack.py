#!/usr/bin/env python
# coding: utf-8

# In[167]:


import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')



values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[168]:


class Deck():
    def __init__(self):
        
        self.all_cards = []
        for i in range(3):
            for suit in suits:
                for rank in ranks:
                    #create card
                    created_card = Card(suit,rank)

                    self.all_cards.append(created_card)
    def shuffle(self):
        
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()


# In[169]:


class Player():
    
    
    def __init__(self,name,cash = 0, bank=0):
        self.name = name
        self.all_cards = []
        self.cash = cash
        self.bank = bank
    
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Hráč {self.name} má {self.cash} korun.'
    
    def bet(self):
        
        self.bank = 0
        self.bank += int(input('Zadejte výši své sázky: '))
        self.cash -= self.bank
    
    def win(self):
        self.cash += 2*self.bank
        self.bank = 0
    
    def loss(self):
        self.bank = 0
    
    def tie(self):
        self.cash += self.bank
        self.bank = 0
        
        
    


# In[207]:


def replay():
    answer = 'spatne'
    global game_on

    while answer.upper() not in ['A', 'N']:
        answer = input(f'Chceš hrát znovu? Napiš "A"(jako "ANO") nebo "N"(jako "NE"): ')
        if answer.upper() == 'A':
            bank = 0
            game_on = True
            break
        elif answer.upper() == 'N':
            game_on = False
            break
    return game_on


   


# In[212]:


#game setup

human = Player(input('Napište prosím svoje jméno: '))
dealer = Player('Dealer')

human.cash = 500
print(f'{human.name}, dáváme vám vstupní bonus {human.cash} korun!')

new_deck = Deck()


game_on = True


while game_on == True:
    human.all_cards = []
    dealer.all_cards = []
    print(f'Váš zůstatek je nyní {human.cash} korun.')
    if len(new_deck.all_cards) < 12:
        new_deck = Deck()
        
    new_deck.shuffle()
    
    human.bet()
    for i in range(2):
        dealer.add_cards(new_deck.deal_one())
        human.add_cards(new_deck.deal_one())
    print('Máš nyní tyto karty:')
    for i in human.all_cards:
    
        print(f'{i}, hodnota: {i.value}')
    print('A dealer má:')
    print(f'{dealer.all_cards[0]}, hodnota: {dealer.all_cards[0].value}')
    player_blackjack = False
    stojim = False
    dealer_blackjack = False
    while player_blackjack == False:
        
        total = 0
        for i in human.all_cards:
            total += i.value
        while total <= 21:
            otazka = 1
            while otazka not in ['B','S']:
                
                otazka = input('Bereš(napiš "B") nebo stojíš (napiš "S"): ')
                otazka = otazka.upper()
                if otazka not in ['B','S']:
                    print('napiš "B" pro možnost BERU nebo "S" pro možnost STOJÍM.')
            if otazka == 'B':
                human.add_cards(new_deck.deal_one())
                for i in human.all_cards:
    
                    print(f'{i}, value: {i.value}')
                total = 0
                totalvalues = []
                for i in human.all_cards:
                
                    total += i.value
                    totalvalues.append(i.value)
                if total > 21 and 11 in totalvalues:
                    total -= 10
                    continue
                    
                
                
                    print(total)
                elif total > 21:
                    human.loss()
                    print('BUST! PROHRÁVÁŠ!')
                    player_blackjack = True
                    dealer_blackjack = True
                    replay()
                    break
                
            elif otazka == 'S':
                
                
                break
        player_blackjack = True
                
                
        
        
    
    
    
    
    while dealer_blackjack == False:
        print('Nyní je na řadě dealer.')    
        
        d_total = 0
        d_totalvalues = []
        for i in dealer.all_cards:
            d_total += i.value
            print(f'{i}, hodnota: {i.value}')
        while d_total < 17:
            
            
            dealer.add_cards(new_deck.deal_one())
            print(f'{dealer.all_cards[-1]}, hodnota: {dealer.all_cards[-1].value}')
            
            
            for i in dealer.all_cards:
                
                d_total += i.value
                d_totalvalues.append(i.value)
            if d_total > 21 and 11 in d_totalvalues:
                d_total -= 10
                continue
                
                
                
                
            elif d_total > 21:
                human.win()
                print(f'BUST! DEALER PROHRÁVÁ! Nyní máš na kontě {human.cash} korun.')
                dealer_blackjack = True
                replay()
                break
                
            
                
            else:
                
                break
        if d_total in range(17,22):
            print(f'Tvoje hodnota: {total}')
            print(f'Dealerova hodnota: {d_total}')
            if total > d_total:
                human.win()
                print(f'Gratulujeme, vyhráváš! Nyní máš na kontě {human.cash} korun.')
                replay()
            elif total < d_total:
                human.loss()
                print(f'Tentokrát to nevyšlo. Nyní máš na kontě {human.cash} korun.')
                replay()
            else:

                human.tie()
                print(f'Remíza, vracíme ti sázku. Nyní máš na kontě {human.cash} korun.')
                replay()
            dealer_blackjack = True
    dealer_blackjack = True
    #comparison
   
        
            
        
       
            
                
            
                    
                
            




