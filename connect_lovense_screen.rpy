screen connect_lovense():
    tag menu
    modal True
    predict False

    default server_status = lovense.server_status()

    add "lovense_background"

    imagebutton:
        idle "return_button_idle"
        hover "return_button_hover"
        action Return()

    text "Connect to Lovense App" xalign 0.5 ypos 50 style "montserrat_extra_bold_64"

    hbox:
        align (0.5, 1.0)
        spacing 100

        # Game Mode
        vbox:
            align (0.5, 1.0)
            yoffset -200
            spacing 10

            add "lovense_game_mode_example" xalign 0.5

            null height 30

            button:
                idle_background "blue_button_idle"
                hover_background "blue_button_hover"
                action ui.callsinnewcontext("lovense_connect_via_game_mode")
                padding (40, 25)
                align (0.5, 0.5)

                text "Connect With Game Mode" align (0.5, 0.5)

            text "No connection to external servers (LAN Only)" xalign 0.5

        # QR Code
        if server_status:
            vbox:
                align (0.5, 1.0)
                yoffset -200
                spacing 10

                add "lovense_qr_code.jpg" xalign 0.5

                null height 30

                button:
                    idle_background "blue_button_idle"
                    hover_background "blue_button_hover"
                    action ui.callsinnewcontext("lovense_connect_via_qr_code")
                    padding (40, 25)
                    xalign 0.5

                    text "Connect With QR Code" align (0.5, 0.5)

                text "Requires connection to Lovense Server" xalign 0.5

        vbox:
            yalign 1.0
            yoffset -200

            text "User Settings" xalign 0.5 style "montserrat_extra_bold_32"

            null height 25

            text "Local IP: {}".format(lovense.local_ip)
            text "HTTP Port: {}".format(lovense.http_port)
            text "Last Updated: {}".format(lovense.last_updated.strftime("%Y-%m-%d %H:%M:%S"))

            if lovense.toys:
                null height 25

                text "Connected Toys" style "montserrat_extra_bold_24" xalign 0.5

                null height 10

                vbox:
                    for toy in lovense.toys.values():
                        if toy.get("nickname"):
                            text "{} ({}) : {}%".format(toy["name"], toy["nickname"], toy["battery"])
                        else:
                            text "{} : {}%".format(toy["name"], toy["battery"])

            null height 50

            button:
                idle_background "blue_button_idle"
                hover_background "blue_button_hover"
                action Function(lovense.refresh)
                padding (40, 25)
                xalign 0.5

                text "Refresh" align (0.5, 0.5)

            null height 5

            text "Last Refresh: {}".format(lovense.last_refresh.strftime("%Y-%m-%d %H:%M:%S")) xalign 0.5


    if lovense.status_message:
        text "Status Message: {}".format(lovense.status_message):
            xpos 20
            yalign 1.0
            yoffset -20
            xsize 750

    vbox:
        align (1.0, 1.0)
        offset (-50, -50)

        textbutton "Get your Lovense toys here":
            action OpenURL("https://www.lovense.com/r/mw4xb8")
            text_size 32
