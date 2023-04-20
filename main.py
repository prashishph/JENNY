# Importing the 'pyttsx3' module. Official documentation at https://pypi.org/project/pyttsx3/
import pyttsx3

if __name__ == '__main__': # Code executed only when program is run directly
    
    engine = pyttsx3.init() # Initialiaze a new instance of the text-to-speech engine
    
    # Set the properties of the engine's voice
    engine.setProperty('rate',170) # Set the voice rate at 170 per minute
    engine.setProperty('volume',1.0) # Set the volume to maximum {min(0) max(1)}
    voices = engine.getProperty('voices') # Get the list of available voices
    engine.setProperty('voice',voices[1].id) # Set the engine's voice to available at second on the list. male(0) female(1)
    
    # Introduction of program
    print('-----  JENNY 1.1  -----')
    print('Enter \'exit\' to stop program.\n')

    while True: # Infinite loop that repeatedly asks for the user input
        text = input('Text: ')  # Take input text
        
        # Code to end program when the user wants
        if text == 'exit': 
            engine.say('Deactivating Jenny!') 
            engine.runAndWait() # wait for the end of speech
            break #break the loop and end of program

        engine.say(text) # to convert text-to-speech
        engine.runAndWait() # wait for the speech to finish before continuing the execution of program
