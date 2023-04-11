/**
 * CS 1 22fa
 * Mini Project 8: PokeLife Simulator (Part A)
 * Student name: Lea Grohmann
 *
 * Represents a PokePixel instance for the PokeLife game.
 * A PokePixel represents a "Pokemon" object with a type for the game.
 */
import java.util.Random;

public class PokePixel {
    // Class constants
    private final String[] TYPES = {"Fire", "Water", "Grass", 
                                    "Electric", "Ground"};
    // Random object for assigning a random type upon initialization 
    private static final Random rand = new Random();

    // Class field
    private String type; 
   
    /**
     * Initializes a PokePixel with a randomly assigned type, from "TYPES".
     */
    public PokePixel() {
        int index = rand.nextInt(this.TYPES.length);
        this.type = this.TYPES[index];
    }

    /**
     * Changes this PokePixel's type to the provided one
     * (does not do any validation of type String; this is optional).
     * 
     * @param type The type to change the PokePixel to
     */
    public void changeType(String type) {
        this.type = type;
    }

    /**
     * Returns the full type name of this PokePixel
     * 
     * @return The PokePixel type
     */
    public String getType() {
        return this.type;
    }

    /**
     * String representation of this PokePixel, such as "Fir" for "Fire".
     * 
     * @return The first three characters of the type string, to 
     * represent the PokePixel.
     */
    public String toString() {
        return this.type.substring(0,3);
    }
}
