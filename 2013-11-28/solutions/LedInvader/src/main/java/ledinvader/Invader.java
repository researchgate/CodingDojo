package ledinvader;

import java.util.Random;

public class Invader {

    private static final Random random = new Random();
    private int x;
    private int y;

    public Invader(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Invader() {
        this.y = 0;
        this.x = random.nextInt(Display.size);
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void moveDown() {
        y++;
    }

    public void restart() {
        x = random.nextInt(Display.size);
        y = 0;
    }

}
