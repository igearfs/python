from project import load_message_from_file, decrypt, encrypt, check_inputs, encrypt_the_encrypted, save_message
import pytest
import emoji

double_encrypted_text = ":🥶😜🐔🧑::🐔🐼🐭::🧬🎮🥨🥯🐧_🧸🐔🐞🥯::🦘🐧_🦘🐧: :🧬🎮🥨🥯🐧_🧸🐔🐞🥯::🦘🐧_🦘🐧: :🥶🐜🎮🥶🥇🥯🐼: :🐞🐧👑🪀🥯::🧑🐔🧸🥯📣::🦘🐧_🦘🐧::🐞🐧👑🪀🥯:.. :🥶🐜🎮🥶🥇🥯🐼: :🐞🐧👑🪀🥯::🧑🐔🧸🥯📣::🦘🐧_🦘🐧::🐞🐧👑🪀🥯: :❤️🥯🐼🧸👑🎮🐼::🪀🐜🐧🍳🥯😜: :🐞🐧👑🪀🥯::🐔🐼🐭::🧑🐔🧸🥯📣: :🧑🐔🧸🥯📣::🧑🥯🥯🐭📣🥯::🪀🐭👑🥶🥇_🐧👑🐭_🐭🐧🐼🧸👑🥯_🍳🎮🐼🥇🎮🐼🧸_🥯🦘🥯::🐭🥯🥨🥨🦘_🧑🥯🐔😜::🥶🐜🎮🥶🥇🥯🐼::❤️🐔🐼🥨🐔_🚿🐔🥶🥯::🥶🐧📣🥨_🚿🐔🥶🥯::🥇🐔🐼🧸🐔😜🐧🐧: :🐔🥨👑📣🐭::🪀🐭👑🥶🥇_🐧👑🐭_🐭🐧🐼🧸👑🥯_🍳🎮🐼🥇🎮🐼🧸_🥯🦘🥯::🥶🐜🎮🥶🥇🥯🐼::❤️😜🥯🐭😽🥯📣::🥶🐧📣🥨_🚿🐔🥶🥯::🥶🐜🎮🥶🥇🥯🐼::🦘🐧_🦘🐧::🐞🐧👑🪀🥯: :❤️🐔🐼🥨🐔_🚿🐔🥶🥯::🧑🐔🧸🥯📣::🐞🐧👑🪀🥯::🥯🧸🧸::❤️🥯🐼🧸👑🎮🐼::🪀🐭👑🥶🥇_🐧👑🐭_🐭🐧🐼🧸👑🥯_🍳🎮🐼🥇🎮🐼🧸_🥯🦘🥯::🦖🪀🐭_❤️📣🐔🥶🥯_🐞🥯🥨🐔📣:..."
bad_encrypted_text = "🦀🐜🎮🪀 🎮🪀 🐔 🐭🥯🪀🐭.. 🐔 🐭🥯🪀🐭 🐧🚿 🐭🐜🥯 🥯🐞😜🧸🐔🐼🐻🦘 🧑😜🐔🥨🐻🐔🪀🐭 🐼🥯🐭🍳🐧😜🥇..."
encrypted_text = "🦀🐜🎮🪀 🎮🪀 🐔 🐭🥯🪀🐭.. 🐔 🐭🥯🪀🐭 🐧🚿 🐭🐜🥯 🥯🐞😜🧸🐔🐼🥶🦘 🧑😜🐔🥨🥶🐔🪀🐭 🐼🥯🐭🍳🐧😜🥇..."
decrypted_text = "This is a test.. a test of the emrgancy bradcast network..."

def test_good_check_inputs():
    check_inputs(decrypted_text, "E")
    check_inputs(decrypted_text, "D")
    check_inputs(encrypted_text, "E")
    check_inputs(encrypted_text, "D")

    with pytest.raises(ValueError):
        check_inputs(decrypted_text, "F")

    with pytest.raises(ValueError):
        check_inputs(decrypted_text, "")

    with pytest.raises(ValueError):
        check_inputs(encrypted_text, "123")

    with pytest.raises(ValueError):
        check_inputs(encrypted_text, "$")

    with pytest.raises(ValueError):
        check_inputs("", "123")

    with pytest.raises(ValueError):
        check_inputs(".@#$", "$")

    with pytest.raises(ValueError):
        check_inputs("", "E")

    with pytest.raises(ValueError):
        check_inputs(".@#$", "D")

def test_load_message_from_file():
    save_message("encrypted_message.txt", encrypted_text)

    message = load_message_from_file("encrypted_message.txt")
    assert message == encrypted_text

    save_message("unencrypted_message.txt", decrypted_text)
    message = load_message_from_file("unencrypted_message.txt")
    assert message == "This is a test.. a test of the emrgancy bradcast network..."

def test_decrypt():
    message = encrypted_text
    decrypted_array = decrypt(message)
    decrypted_message = [str(x) for x in decrypted_array]
    assert "".join(decrypted_message) == decrypted_text

def test_encrypt():
    message = decrypted_text
    encrypted_array = encrypt(message)
    encrypted_message = [str(x) for x in encrypted_array]
    assert "".join(encrypted_message) == encrypted_text

def test_encrypt_the_encrypted():

    message = decrypted_text
    encrypted_array = encrypt(message)
    encrypted_message = [str(x) for x in encrypted_array]
    message = "".join(encrypted_message)

    encrypted_array = encrypt_the_encrypted(message)
    encrypted_message = [str(x) for x in encrypted_array]
    message = "".join(encrypted_message)
    assert message == double_encrypted_text

    decrypted_array = decrypt(message)
    decrypted_message = [str(x) for x in decrypted_array]
    message = "".join(decrypted_message)

    decrypted_array = decrypt(emoji.emojize("".join(message), language='alias'))
    decrypted_message = [str(x) for x in decrypted_array]
    message = "".join(decrypted_message)

    assert message == decrypted_text
