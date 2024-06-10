package MusicPlayer;

import java.io.File;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.FloatControl;

public class MusicPlayer {

    public void playFile(String filepath) {
        try {
            File audioFile = new File(filepath);

            if (!audioFile.exists())
                throw new RuntimeException("cant find file :(");

            AudioInputStream audioInput = AudioSystem.getAudioInputStream(audioFile);
            Clip clip = AudioSystem.getClip();
            clip.open(audioInput);

            // set audio lower
            FloatControl gainControl = (FloatControl) clip.getControl(FloatControl.Type.MASTER_GAIN);
            gainControl.setValue(-10f); // decibels

            clip.start();

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}
