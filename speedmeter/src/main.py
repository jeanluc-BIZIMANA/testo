from flet import *
import speedtest 
import time

def main(page:Page):
    page.theme_mode = ThemeMode.LIGHT
    def toggle_theme(e):
        # Toggle theme between light and dark
        page.theme_mode = ThemeMode.DARK if page.theme_mode == ThemeMode.LIGHT else ThemeMode.LIGHT
        page.update()
    
    page.appbar = AppBar(
            leading=IconButton(icons.MENU,on_click=lambda e: page.open(drawer)),
            leading_width=40,
            title=Text("SPEED  TEST"),
            center_title=True,
    )


    def handle_change(e):
        page.add(Text(f"Selected Index changed: {e.selected_index}"))
        # page.close(drawer)     
    drawer = NavigationDrawer(
        on_change=handle_change,
        controls=[
            Container(height=12),
            NavigationDrawerDestination(
                label="about us",
                icon=icons.PERSON_2_OUTLINED,
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                icon_content=Icon(icons.MAIL_OUTLINED),
                label="version 1.0.0",
                selected_icon=icons.MAIL,
            ),
            NavigationDrawerDestination(
                icon_content=Icon(icons.MAIL),
                label="Mail us",
            ),
        ],
    )
    
    def testing(e):
        try:
           btn.text="Testing"
           not_connected.opacity=0
           progressing.opacity=1
           st = speedtest.Speedtest()
           page.update()
           download_speed = st.download()/1000000
           upload_speed = st.upload()/10000000
           page.update()
           print(download_speed)
           page.controls.append(
            Row([
                Text(f'your internet download speed is: \n {download_speed} Mbps \ndownload speed is:\n {upload_speed} Mbps',color=colors.BLUE_700,size=20),
            ],
            alignment=MainAxisAlignment.CENTER
            ),
           )

           page.update()
        except:
            btn.text="Retest"
            progressing.opacity=0
            not_connected.opacity=1
            page.update()
        testing(e)
    progressing=ProgressBar(
                    width=100,
                    color=Colors.AMBER_ACCENT,
                    opacity=0
                )
    btn=Button(
                    text="Test",
                    color=colors.BLUE_200,
                    on_click=testing

                )
    not_connected=IconButton(
        icon=Icons.SIGNAL_WIFI_CONNECTED_NO_INTERNET_4_OUTLINED,
        opacity=0,
        icon_color="red",
        tooltip="NOT CONNECTED"
    ) 
    t=Container(
        content=Column([
            Row([
                     Image(
                        src="speed.png",
                        height=100,
                        width=100,
                        fit=ImageFit.CONTAIN,
                        border_radius=60,
                    )
                
            ],
            alignment=MainAxisAlignment.CENTER
            
            ),
            Row([
                
                progressing
            ],
            alignment=MainAxisAlignment.CENTER
            ),
            
           
            Row([
                
                btn
            ],
            alignment=MainAxisAlignment.CENTER
            ),
            Row([
                not_connected

            ],
            alignment=MainAxisAlignment.CENTER
            ),

        ]
        
        )
    )
    page.add(t,FloatingActionButton(icon=Icons.MODE_NIGHT_OUTLINED,on_click=toggle_theme))
            



app(target=main,assets_dir='assets')