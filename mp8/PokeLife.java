/**
 * CS 1 22fa
 * Mini Project 8: PokeLife Simulator (Part B)
 * Student name: Lea Grohmann
 *
 * Represents a PokeLife instance for the PokeLife game.
 * The PokeLife board provides functionality to run iterations
 * of the game simulator.
*/
public class PokeLife {
    // Class constants
    // A 5-element array of types
    private String[] TYPES = {"Fire", "Water", "Grass", 
                              "Electric", "Ground"};
    // A 5-element array of weaknesses, where each String corresponds to the type
    // in types at that index
    private String[] WEAKNESSES = {"Water,Ground", "Grass,Electric", "Fire", 
                                   "Ground", "Water,Grass"};

    // Class fields
    // width and height of a the "PokeLife" game
    private int width;
    private int height;
    // 2D array holding width * height PokePixel instances
    private PokePixel[][] board;
    // if true, will randomly populate board, otherwise
    // will always populate the same pixel types for a given
    // (width, height)
    private boolean isRandom;
    
    /**
     * Initializes a PokeLife board, with a given width and height.
     *
     * @param width The width of the PokeLife board
     * @param height The height of the PokeLife board
     * @param isRandom Whether to randomly-populate the initialized board
     * @throws IllegalArgumentException if either width or height are < 1
     */
    public PokeLife(int width, int height, boolean isRandom) { 
        if (width <= 0 || height <=0) {
            throw new IllegalArgumentException("width and height must be > 0");
        }
        this.width = width;
        this.height = height;
        this.isRandom = isRandom;
        this.board = this.initializeBoard(width, height);
    }

    /**
     * Getter method for this PokeLife width.
     *
     * @return The width of this PokeLife
     */
    public int getWidth() {
        return this.width;
    }

    /**
     * Getter method for this PokeLife height. 
     * 
     * @return The height of this PokeLife
     */
    public int getHeight() {
        return this.height;
    }
   
    /**
     * Get the PokePixel at the given x and y position on the board.
     *
     * @param x Desired x coordinate.
     * @param y Desired y coordinate. 
     *
     * @return The PokePixel at (x, y)
     * @throws IllegalArgumentException if (x, y) is an invalid position:
     * - both must be >= 0
     * - x must be < width of board, y must be < height of board
     */
    public PokePixel getPoke(int x, int y) {
        if (x < 0 || x >= this.width || y < 0 || y >= this.height) {
            throw new IllegalArgumentException("Invalid x and/or y coordinate.");
        }
        return this.board[x][y];
    }

    /**
     * Returns the weaknesses for the given type.
     * 
     * @param type The type you would like the weaknesses for.
     * 
     * @return A 1D array containing all of the weaknesses of the given type, 
     * or null if none exists (the given type is unknown).
     */ 
    public String[] getWeaknesses(String type) {
        int index = this.getTypeIndex(type);
        if (index < 0) {
            return null;
        }
        return WEAKNESSES[index].split(",");
    }

    /**
     * Returns true if at least count of the neighbors of the PokePixel at 
     * position (x, y) of the board are of the given type. 
     *  
     * @param x The x coordinate of the desired PokePixel
     * @param y The y coordinate of the desired PokePixel
     * @param type The type to check the neighbors for
     * @param count Minimum count of neighbors having the passed type
     *
     * @return true if 3+ neighbors match the type, else false
     */
    public boolean isSurroundedBy(int x, int y, String type, int count) {
        String[] neighborTypes = this.getNeighborTypes(x, y);
        int actual = 0;
        for (int i = 0; i < neighborTypes.length; i++) {
            if (neighborTypes[i].equals(type)) {
                actual++;
            }
        }
        return actual >= count;
    }

    /**
     * Gets the weakness of the relevant PokePixel, and checks its neighbors'
     * types. If at least 3 neighbors are of a type the PokePixel is weak to, 
     * its type should be updated. 
     * 
     * @param x The x coordinate to check neighbors of 
     * @param y The y coordinate to check neighbors of 
     * @param current The PokePixel at the relevant coordinates
     */
    private void updateType(int x, int y, PokePixel current) {
        String[] weaknesses = this.getWeaknesses(current.getType());
        
        for(int i = 0; i < weaknesses.length; i++) {
            if (isSurroundedBy(x, y, weaknesses[i], 3)) {
                current.changeType(weaknesses[i]);
            }
        }
    }

    /**
     * (PROVIDED, DO NOT CHANGE)
     * Given a type string, returns its index in the TYPES array.
     * @return index of type in TYPES array (-1 if not found)
     */
    private int getTypeIndex(String type) {
        for (int i = 0; i < TYPES.length; i++) {
            if (TYPES[i].equals(type)) {
                return i;
            }
        }
        return -1;
    }

    /**
     * Returns the PokePixel type that occurs most on the current state of the
     * board, breaking ties by the latest type tying for the max count 
     * in TYPES.
     */
    public String getWinningType() {
        // Tallies for types:
        // {"Fire", "Water", "Grass", "Electric", "Ground"}
        int[] tallies = {0, 0, 0, 0, 0};
        for (int i = 0; i < this.board.length; i++) {
            PokePixel[] row = this.board[i];
            for (int j = 0; j < row.length; j++) {
                PokePixel cell = row[j];
                int typeIndex = this.getTypeIndex(cell.getType());
                tallies[typeIndex] += 1;
            }
        }

        int maxIndex = 0;
        int maxTally = 0;
        for (int i = 0; i < tallies.length; i++) {
            if (tallies[i] >= maxTally) {
                maxTally = tallies[i];
                maxIndex = i;
            }
        }
        return TYPES[maxIndex];
    }

    // Provided helper methods (do not change in Parts A/B,
    // you may modify in an optional PokeLife2.java submission for Part C)

    /**
     * Initializes the PokePixel board, populating with as a grid (2D array)
     * of PokePixel instances. If the life is initialized with
     * a randomness flagged true, will randomly allocate the board,
     * otherwise the allocation will always be the same for a given
     * x/y.
     * 
     * Implementation tool for solution -- students not required to implement.
     * @param x number of columns for the board
     * @param y number of rows for the board
     * @return populated board of PokePixel elements.
     */
    private PokePixel[][] initializeBoard(int x, int y) {
        PokePixel[][] board = new PokePixel[x][y];
        int currTypeIndex = 0; 
        // counter for testing without randomness;
        // where we assign types in order, cycling through TYPES 
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                board[i][j] = new PokePixel();
                if (!this.isRandom) {
                    board[i][j].changeType(TYPES[currTypeIndex]);
                    // fix a formula for assigning the current index
                    // (just cycling by 1 is a boring horizontal-striped result)
                    currTypeIndex = ((currTypeIndex + 1) * i + j) % TYPES.length;
                }
            }
       }
       return board;
    }

    /**
     * Returns an 8-element array of all the neighbors types, starting 
     * north and going counterclockwise. 
     * 
     * @param x The x coordinate of the PokePixel 
     * @param y The y coordinate of the PokePixel
     * @return 8-element array of all neighbor types
     */
    private String[] getNeighborTypes(int x, int y) {
        String[] neighborsCW = new String[8];
        int down = (y + 1) % this.height; 
        // Ternary syntax: cond ? result1 : results2
        // if (cond) { result1 } else { result2 }
        // if (y == 0) { this.height - 1 } else { y - 1 }
        int up = y == 0 ? this.height - 1 : (y - 1);
        int left = x == 0 ? this.width - 1 : (x - 1);
        int right = (x + 1) % this.width;
        neighborsCW[0] = this.board[x][up].getType(); 
        neighborsCW[1] = this.board[left][up].getType(); 
        neighborsCW[2] = this.board[left][y].getType();
        neighborsCW[3] = this.board[left][down].getType();
        neighborsCW[4] = this.board[x][down].getType(); 
        neighborsCW[5] = this.board[right][down].getType(); 
        neighborsCW[6] = this.board[right][y].getType(); 
        neighborsCW[7] = this.board[right][up].getType();
        return neighborsCW;
    }

    /**
     * Runs a cycle of the PokeLife game, where all pixels check their neighbors 
     * for their respective weaknesses. 
     * If the criteria is met, the type of that given pixel changes for the 
     * next cycle. In the case of two groups weaknesses around the pixel, 
     * the one that appears second later in the weaknesses string should win. 
     */
    public void lifeCycle() {
        for (int i = 0; i < this.width; i++) {
            for (int j = 0; j < this.height; j++) {
                PokePixel curr = this.board[i][j]; 
                updateType(i, j, curr);
            }
        }
    }

    /**
     * 2D grid string representation of the current PokeLife game, where each
     * line of the board represents a row of pixels, ending with "\n".
     * 
     * @return A string representation of this PokeLife.
     */
    public String toString() {
        String result = "";
        for (int i = 0; i < this.width; i++) {
            for (int j = 0; j < this.height; j++) {
                result += this.board[i][j].toString() + " ";
            }
            result += "\n";
        }
        return result;
    }
}
