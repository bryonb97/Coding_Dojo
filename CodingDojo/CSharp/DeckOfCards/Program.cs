using System;

namespace DeckOfCards
{
    class Program
    {
        static void Main(string[] args)
        {
            Deck myDeck = new Deck();
            Player playerOne = new Player("Player One");
            Console.WriteLine($"There are {myDeck.cards.Count} cards in this deck!");

            playerOne.DrawCard(myDeck);
            Console.WriteLine($"{playerOne.Name} has {playerOne.Hand.Count} cards in their hand!");

            playerOne.DrawCard(myDeck);
            playerOne.DrawCard(myDeck);
            playerOne.DrawCard(myDeck);
            playerOne.DrawCard(myDeck);
            playerOne.DrawCard(myDeck);

            playerOne.DiscardCard(3);
            Console.WriteLine($"{playerOne.Name} has {playerOne.Hand.Count} cards in their hand!");

        }
    }
}
