/**
 * CS 1 Fall 2022
 * Authors: Adam Abbas and El Hovik 
 * Provided code for CS 1 (DO NOT MODIFY)
 * Manages a GUI-based PokeLife Game with 5 Pokemon types.
 * 
 * Credits:
 * - Original idea inspired by https://twitter.com/matthen2/status/1543226572592783362
 * - Thank you to Adam Abbas for working on creating this CS 1 assignment!
 */
import java.awt.*;
import java.util.Map;
import java.util.HashMap;
import java.util.concurrent.TimeUnit;

public class Game {
    // 0 for random, 1 for small non-random, 2 for large non-random 
    // students can change this to 2 for the large non-random board
    // and 0 for the large random board
    public static final int testMode = 1; 

    /**
     * The main function setting up the game and initializing the animated
     * "PokePixel" variant of a game of life.
     */
    public static void main(String[] args) {
        int x = 60;
        int y = 60;
        // scale of px sizes
        int scale = 10;
        // number of cycles
        int lifetime = 35;
        int sleepTime = 500; // 0.5 s pause per cycle
        if (testMode == 1) {
            // testMode == 1 is the small non-random test mode
            x = 5;
            y = 4;
            lifetime = 4;
            scale = 30;
            sleepTime = 5000; // slower 5s pause for testing
        } else if (testMode == 2) {
            // testMode == 2 is the standard size non-random test mode
            sleepTime = 2000; // slower 2s pause for testing
        }
        // if TEST_RANDOM is false, fix the type allocation for easier testing
        // purposes (this is handled in the provided initializeBoard method)
        // testMode == 0 is true if we want to test randomness
        PokeLife life = new PokeLife(x, y, (testMode == 0));

        // Note: Java A Map is similar to a dictionary in Python,
        // mapping Strings to Color instances.
        Map<String, Color> typeToColor = new HashMap<>();
        typeToColor.put("Fire", Color.RED);
        typeToColor.put("Water", Color.BLUE); 
        typeToColor.put("Grass", Color.GREEN); 
        typeToColor.put("Electric", Color.YELLOW);
        typeToColor.put("Ground", new Color(102, 51, 0)); 

        // Initialize a DrawingPanel which is the canvas for the board.
        DrawingPanel board = new DrawingPanel(life.getWidth() * scale, 
                                              life.getHeight() * scale);
        Graphics g = board.getGraphics(); 
        
        int ctr = 0; 
        while (ctr < lifetime) {
            for (int r = 0; r < life.getWidth(); r++) {
                for (int c = 0; c < life.getHeight(); c++) {
                    // Get the PokemonPixel type at the (row, col) coordinates 
                    String pixType = life.getPoke(r, c).getType(); 
                    // Update the color on the graphics object
                    g.setColor(typeToColor.get(pixType));
                    // Draw a colored rectangle to represent the appropriate 
                    // PokemonPixel type
                    g.fillRect(r * scale,  c * scale, 
                               (r + 1) * scale, (c + 1) * scale);
                }
            }
            // Pause each iteration by 0.5 seconds
            try {
                TimeUnit.MILLISECONDS.sleep(sleepTime); 
            } catch (InterruptedException ex) {
                System.out.println("An interruption occurred: " + ex);
            }
            // If we're testing the small non-random board, print the board for 
            // each cycle
            if (testMode == 1) {
                System.out.println("Cycle: " + ctr);
                System.out.println(life);
            }
            life.lifeCycle();
            ctr++;
        }
        String winningType = life.getWinningType();
        System.out.println("Winning type: " + winningType);
    }   
}
