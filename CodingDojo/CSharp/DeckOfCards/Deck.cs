using System;
using System.Collections.Generic;

class Deck
{
    public List<Card> cards;

    public Deck()
    {
        ResetDeck();
        ShuffleDeck();
    }

    public Deck ResetDeck()
    {
        cards = new List<Card>();
        string[] Suit = {"hearts","diamonds","spades","clubs"};
        string[] StringVal = {"Ace","two","three","four","five","six","seven","eight","nine","ten","Jack","Queen","King"};

        // Foreach suit, assemble set of cards.
        foreach(string suit in Suit)
        {
            // build out individual cards.
            for(int i = 0; i < StringVal.Length; i++)
            {
                Card myCard = new Card(StringVal[i], suit, i + 1);
                cards.Add(myCard);
            }
        }
        return this;
    }

    public Deck ShuffleDeck()
    {
        Random rand = new Random();
        // Loop backwards in our deck
        for(int last = cards.Count - 1; last > 0; last--)
        {
            // select a random card
            int r = rand.Next(last);
            Card temp = cards[r];
            // swap it with the last card
            cards[r] = cards[last];
            cards[last] = temp;
        }
        return this;
    }

    public Card DealCard()
    {
        if(cards.Count > 0){
            Card topCard = cards[0];
            cards.Remove(topCard);
            Console.WriteLine($"Dealt {topCard.StringVal} of {topCard.Suit}");
            return topCard;
        }
        else
        {
            ResetDeck();
            return DealCard();
        }
    }
}