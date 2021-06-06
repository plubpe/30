command = ""
serial.redirect_to_usb()
bluetooth.start_uart_service()
basic.show_icon(IconNames.SMALL_SQUARE)

def on_bluetooth_connected():
    basic.show_icon(IconNames.SQUARE)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_uart_data_received():
    global command
    command = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    basic.show_string(command)
    if command.includes("1"):
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P8, 1)
    elif command.includes("2"):
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P8, 1)
    elif command.includes("3"):
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P8, 0)
    else :
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P8, 0)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE), on_uart_data_received)
