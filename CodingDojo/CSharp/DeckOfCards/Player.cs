using System;
using System.Collections.Generic;

class Player
{
    public string Name;
    public List<Card> Hand;

    public Player(string name)
    {
        Name = name;
        Hand = new List<Card>();
    }

    public Card DrawCard(Deck myDeck)
    {
        Card myCard = myDeck.DealCard();
        Hand.Add(myCard);
        Console.WriteLine($"Player has {Hand.Count} cards");
        return myCard;
    }

    public Card DiscardCard(int cardNum)
    {
        if(cardNum < 0 || cardNum > Hand.Count)
        {
            Console.WriteLine("You don't have any cards you dingus!");
            return null;
        }
        else
        {
            Card myCard = Hand[cardNum];
            Hand.RemoveAt(cardNum);
            Console.WriteLine($"Removed {myCard.StringVal} of {myCard.Suit} from your hand!");
            return myCard;
        }
    }
}