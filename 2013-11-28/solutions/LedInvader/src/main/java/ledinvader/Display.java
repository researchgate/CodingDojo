package ledinvader;

import com.googlecode.lanterna.terminal.Terminal;

public class Display {

    public static final int size = 4;
    public static final int border = 3;

    private boolean[][] grid = new boolean[size][size];

    public void on(int x, int y) {
        grid[x][y] = true;
    }

    public void off(int x, int y) {
        grid[x][y] = false;
    }

    public String toCommand() {
        StringBuilder sb = new StringBuilder();
        for (int y = 0; y < size; y++) {
            for (int x = 0; x < size; x++) {
                sb.append(grid[x][y] ? '1' : '0');
            }
        }
        return sb.toString();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int y = 0; y < size; y++) {
            for (int x = 0; x < size; x++) {
                sb.append(grid[x][y] ? '*' : '_');
            }
            sb.append('\n');
        }
        return sb.toString();
    }

    public void drawOnTerminal(Terminal terminal) {
        // terminal.clearScreen();
        for (int y = 0; y < size; y++) {
            for (int x = 0; x < size; x++) {
                terminal.moveCursor(x, y);
                terminal.putCharacter(grid[x][y] ? '*' : '_');
            }
        }
    }

}
