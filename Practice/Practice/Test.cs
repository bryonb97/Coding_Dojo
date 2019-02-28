namespace Practice
{
    public class Test
    {

        #region Structs
        struct Customers
        {
            private string name;
            private double balance;
            private int id;
        

            public void createCust(string n, double b, int i)
            {
                name = n;
                balance = b;
                id = i;
            }

            public void showCust()
            {
                System.Console.WriteLine("Name " + name);
                System.Console.WriteLine("Balance " + balance);
                System.Console.WriteLine("Id " + id);
            }
        }

        #endregion
        }
        
    }
