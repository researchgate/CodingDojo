package ledinvader;

import java.io.IOException;
import java.net.MalformedURLException;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.client.fluent.Request;
import org.apache.http.entity.ContentType;

import com.googlecode.lanterna.TerminalFacade;
import com.googlecode.lanterna.input.Key;
import com.googlecode.lanterna.terminal.Terminal;

public class LedInvader {

    public static void main(String[] args) throws InterruptedException, MalformedURLException {
        LedInvader game = new LedInvader();
        game.play();
    }

    private static final long moveInvaderAt = 500;
    private static final long newInvaderAt = 5000;

    private int user;
    private List<Invader> invaders;
    private boolean alive;
    private Display display;
    Terminal terminal;

    public LedInvader() {
        display = new Display();
        terminal = TerminalFacade.createTerminal(System.in, System.out, Charset.forName("UTF8"));
        terminal.enterPrivateMode();
        terminal.setCursorVisible(false);
        user = Display.border / 2;
        invaders = new ArrayList<>();
    }


    public void play() throws InterruptedException {
        while (true) {
            invaders.add(new Invader());
            alive = true;

            refreshDisplay();

            long turn = 0;
            while (alive) {
                turn++;
                Thread.sleep(1);

                if (turn % moveInvaderAt == 0) {
                    for (Invader invader : invaders) {
                        display.off(invader.getX(), invader.getY());
                        if (invader.getY() == Display.border) {
                            invader.restart();
                        } else {
                            invader.moveDown();
                        }

                        if (invader.getY() == Display.border && invader.getX() == user) {
                            alive = false;
                        }
                    }
                    refreshDisplay();
                }

                if (!alive) {
                    break;
                }

                if (turn % newInvaderAt == 0) {
                    invaders.add(new Invader());
                    refreshDisplay();
                }

                Key key = terminal.readInput();
                if (key == null) {
                    continue;
                }
                switch (key.getKind()) {
                case ArrowLeft:
                    if (user > 0) {
                        display.off(user, Display.border);
                        user--;
                        refreshDisplay();
                    }
                    break;
                case ArrowRight:
                    if (user < Display.border) {
                        display.off(user, Display.border);
                        user++;
                        refreshDisplay();
                    }
                    break;
                default:
                    break;
                }
            }

            for (int y = Display.border; y >= 0; y--) {
                for (int x = 0; x <= Display.border; x++) {
                    display.on(x, y);
                }
                refreshDisplay();
                Thread.sleep(100);
            }

            while (true) {
                Thread.sleep(1);
                Key key = terminal.readInput();
                if (key != null && key.getCharacter() == ' ') {
                    break;
                }
            }

            invaders.clear();
            for (int y = 0; y <= Display.border; y++) {
                for (int x = 0; x <= Display.border; x++) {
                    display.off(x, y);
                }
                refreshDisplay();
                Thread.sleep(100);
            }
        }
    }

    private void refreshDisplay() {
        for (Invader invader : invaders) {
            display.on(invader.getX(), invader.getY());
        }
        display.on(user, Display.border);
        display.drawOnTerminal(terminal);
        sendCommand("50-" + display.toCommand());
    }

    private void sendCommand(String command) {
        try {
            // System.out.println(command);
            Request.Post("http://192.168.178.134:8080").bodyString(command, ContentType.TEXT_PLAIN).execute().returnContent();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
