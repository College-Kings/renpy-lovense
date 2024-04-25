label lovense_connect_via_game_mode:
    scene black

    show lovense_remote_download
    "1. Download the Lovense Remote App (Compatibile: iOS, Android and Desktop)"
    hide lovense_remote_download

    show lovense_remote_discover
    "2. Head to the \"Discover\" view"
    hide lovense_remote_discover

    show lovense_remote_game_mode
    "3. Select \"Game Mode\""
    hide lovense_remote_game_mode

    show lovense_enable_lan
    "4. Enable LAN"
    hide lovense_enable_lan

    show lovense_input_local_ip
    $ lovense.local_ip = renpy.input("4. Enter Local IP", allow="0123456789.")
    hide lovense_input_local_ip

    show lovense_input_http_port
    $ lovense.http_port = renpy.input("5. Enter HTTP Port", allow="0123456789.")
    hide lovense_input_http_port

    return


label lovense_connect_via_qr_code:
    show black

    show lovense_remote_download
    "1. Download the Lovense Remote App (Compatibile: iOS, Android and Desktop)"
    hide lovense_remote_download

    show lovense_plus_view
    "2. Click on the \"+\" icon"
    hide lovense_plus_view

    show lovense_scan_qr
    "3. Select \"Scan QR\""
    hide lovense_scan_qr

    $ lovense.download_qr_code()

    show expression "lovense_qr_code.jpg" at truecenter
    "4. Scan the above QR code to connect"
    hide expression "lovense_qr_code.jpg"

    return