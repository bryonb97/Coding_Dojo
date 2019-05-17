using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = MusicStore.GetData().AllArtists;
            List<Group> Groups = MusicStore.GetData().AllGroups;

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
            IEnumerable<Artist> myArtist = Artists.Where(x => x.Hometown == "Mount Vernon").ToList();
            foreach (var artist in myArtist)
            {
                System.Console.WriteLine($"Real Name: {artist.RealName} Age: {artist.Age}");
            }

            //Who is the youngest artist in our collection of artists?
            var youngArtist = Artists.OrderBy(x => x.Age).First();
            System.Console.WriteLine($"The youngest artist is: {youngArtist.ArtistName} with an age of {youngArtist.Age}");

            //Display all artists with 'William' somewhere in their real name
            var williams = Artists.Where(a => a.RealName.Contains("William")).Select(a => a.RealName);

            foreach (var william in williams)
            {
                Console.WriteLine(william);
            }   

            //Display the 3 oldest artist from Atlanta
            var atlanta = Artists.Where(a => a.Hometown == "Atlanta").OrderByDescending(a => a.Age).Take(3);
            foreach (var artist in atlanta)
            {
                Console.WriteLine(artist.RealName + " is " + artist.Age + " years old and is from " + artist.Hometown);
            }

            //(Optional) Display the Group Name of all groups that have members that are not from New York City

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
	        Console.WriteLine(Groups.Count);
        }
    }
}
