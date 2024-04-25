image lovense_background = "_lovense/images/background.webp"
image lovense_discover_page = "_lovense/images/discover_page.png"
image lovense_frame = Frame("_lovense/images/frame.png", 3, 3)
image lovense_game_mode_example = "_lovense/images/game_mode_example.png"
image lovense_game_mode_page = "_lovense/images/game_mode_page.png"
image lovense_home_page = "_lovense/images/home_page.png"
image lovense_remote_download = "_lovense/images/lovense_remote_download.webp"
image lovense_scan_qr_button = "_lovense/images/scan_qr_button.png"

#region Game Mode
image lovense_remote_discover_frame = Transform("lovense_frame", xysize=(75, 75))
image lovense_remote_discover = Composite((498, 1080), (0, 0), "lovense_home_page", (275, 970), "lovense_remote_discover_frame")

image lovense_remote_game_mode_frame = Transform("lovense_frame", xysize=(468, 100))
image lovense_remote_game_mode = Composite((498, 1080), (0, 0), "lovense_discover_page", (15, 650), "lovense_remote_game_mode_frame")

image lovense_enable_lan_frame = Transform("lovense_frame", xysize=(85, 70))
image lovense_enable_lan = Composite((498, 1080), (0, 0), "lovense_game_mode_page", (385, 222), "lovense_enable_lan_frame")

image lovense_input_local_ip_frame = Transform("lovense_frame", xysize=(468, 65))
image lovense_input_local_ip = Composite((498, 1080), (0, 0), "lovense_game_mode_example", (15, 338), "lovense_input_local_ip_frame")

image lovense_input_http_port_frame = Transform("lovense_frame", xysize=(468, 65))
image lovense_input_http_port = Composite((498, 1080), (0, 0), "lovense_game_mode_example", (15, 400), "lovense_input_http_port_frame")
#endregion Game Mode

#region QR Code
image lovense_plus_view_frame = Transform("lovense_frame", xysize=(56, 55))
image lovense_plus_view = Composite((498, 1080), (0, 0), "lovense_home_page", (428, 68), "lovense_plus_view_frame")

image lovense_scan_qr_frame = Transform("lovense_frame", xysize=(223, 75))
image lovense_scan_qr = Composite((498, 1080), (0, 0), "lovense_scan_qr_button", (275, 313), "lovense_scan_qr_frame")
#endregion QR Code