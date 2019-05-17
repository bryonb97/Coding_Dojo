class Human {
    // Fields for Human
    public string name;
    public int strength;
    public int intelligence;
    public int dexterity;
    private int health;

    // add a public "getter" property to access health
    public int Health 
    {
        get 
        {
            return health;
        }
    }

    // Add a constructor that takes a value to set Name, and set the remaining fields to default values
    public Human(string val) 
    {
        name = val;
        strength = 3;
        intelligence = 3;
        dexterity = 3;
        health = 100;
    }

    // Add a constructor to assign custom values to all fields
    public Human(string name, int strength, int intelligence, int dexterity, int health) 
    {
        this.name = name;
        this.strength = strength;
        this.intelligence = intelligence;
        this.dexterity = dexterity;
        this.health = health;
    }
    // Build Attack method
    public int Attack (Human target) 
    {
        int damage = target.health - (5 * this.strength);
        System.Console.WriteLine($"{this.name} hit {target.name}! {target.name} has {target.health - damage} hp left!");
        return damage;
        
    }
}