# Fun with Encryption!

### Video Demo:  [TODO]

### Description
Every day people are using emoji's in messages. Why not make your entire message an EMOJI!!! I know exciting right! Well why not use them for encrypting your messages like Hyroglyphics.

Based on the message file or message entered you can Encrypt your text to Emoji's, send them to your friends and they can decrypt your text!

### Implementation Details
This project uses the [Emoji library](https://pypi.org/project/emoji/) for processing the text into standard Emoji's nad back to text.

The main function handles getting the user input for what files to encrypt/decripted and how many iterations to go over the file/text.

Included in this repo is a encrypted and decrypted files which is used in the pytest tests.

### Challenges

Copy and Pasting a emoji message was a hurdle to get by. The output for the selected emoji's on reading them back in interpreted :polor_bear: as :bear:. So I had to test each
translation and fix until I got the emoji's out that I put in.

Copy and Paste also added wierd symbols to the command line so I had to limit the command line to one pass over the emoji's but for files it wrote and read them just fine.

This  : :🧑🥯🥯🐭📣🥯:  <- copy
Became: :🧑🥯🥯��📣🥯: <- paste
On copy and paste from the long 2 pass encryption below. But you can grab parts and decode it that way.

So a 2 pass encryption ::🥶😜🐔🧑::🐔🐼🐭::🧬🎮🥨🥯🐧_🧸🐔🐞🥯::🦘🐧_🦘🐧: :🧬🎮🥨🥯🐧_🧸🐔🐞🥯::🦘🐧_🦘🐧: :🥶🐜🎮🥶🥇🥯🐼: :🐞🐧👑🪀🥯::🧑🐔🧸🥯📣::🦘🐧_🦘🐧::🐞🐧👑🪀🥯:.. :🥶🐜🎮🥶🥇🥯🐼: :🐞🐧👑🪀🥯::🧑🐔🧸🥯📣::🦘🐧_🦘🐧::🐞🐧👑🪀🥯: :❤️🥯🐼🧸👑🎮🐼::🪀🐜🐧🍳🥯😜: :🐞🐧👑🪀🥯::🐔🐼🐭::🧑🐔🧸🥯📣: :🧑🐔🧸🥯📣::🧑🥯🥯🐭📣🥯::🪀🐭👑🥶🥇_🐧👑🐭_🐭🐧🐼🧸👑🥯_🍳🎮🐼🥇🎮🐼🧸_🥯🦘🥯::🐭🥯🥨🥨🦘_🧑🥯🐔😜::🥶🐜🎮🥶🥇🥯🐼::❤️🐔🐼🥨🐔_🚿🐔🥶🥯::🥶🐧📣🥨_🚿🐔🥶🥯::🥇🐔🐼🧸🐔😜🐧🐧: :🐔🥨👑📣🐭::🪀🐭👑🥶🥇_🐧👑🐭_🐭🐧🐼🧸👑🥯_🍳🎮🐼🥇🎮🐼🧸_🥯🦘🥯::🥶🐜🎮🥶🥇🥯🐼::❤️😜🥯🐭😽🥯📣::🥶🐧📣🥨_🚿🐔🥶🥯::🥶🐜🎮🥶🥇🥯🐼::🦘🐧_🦘🐧::🐞🐧👑🪀🥯: :❤️🐔🐼🥨🐔_🚿🐔🥶🥯::🧑🐔🧸🥯📣::🐞🐧👑🪀🥯::🥯🧸🧸::❤️🥯🐼🧸👑🎮🐼::🪀🐭👑🥶🥇_🐧👑🐭_🐭🐧🐼🧸👑🥯_🍳🎮🐼🥇🎮🐼🧸_🥯🦘🥯::🦖🪀🐭_❤️📣🐔🥶🥯_🐞🥯🥨🐔📣:...

You can grab from : to : and just decrypt parts of it at a time so the �� do not show up.

### How to Run
The reccomended way to run the program is with passing in files to encrypt or decrypt.

If you are decrypting a file it is required to pass in the -fie AND -fod
IF you are encrypting a file it is required to pass in the -fid AND -foe

usage: Message Encoder/Decoder [-h] [-n NUMBER_OF_PASSES] [-fie ENCRYPTED_READ_FILE_LOCATION] [-foe ENCRYPTED_WRITE_FILE_LOCATION] [-fid DECRYPTED_READ_FILE_LOCATION]
                               [-fod DECRYPTED_WRITE_FILE_LOCATION]

Encodes and Decodes basic messages

options:
  -h, --help            show this help message and exit
  -n NUMBER_OF_PASSES   number of encryption/decryptions
  -fie ENCRYPTED_READ_FILE_LOCATION
                        File to read in the encrypted message from to decrypt
  -foe ENCRYPTED_WRITE_FILE_LOCATION
                        File to save the encrypted message to.
  -fid DECRYPTED_READ_FILE_LOCATION
                        File to read in the decrypted message from to encrypt
  -fod DECRYPTED_WRITE_FILE_LOCATION
                        File to save the decrypted message to.

Basic encryption for fun!

You can also use plain old: python project.py - this will prompt for inputs from the user for a message, encrpt or decrypt and the number of passes.


### Sample Encrypt/Decrypt:
See the included Sample Files in the repo.