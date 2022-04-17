// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:flutter/material.dart';
import 'tab.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        textTheme: TextTheme(bodyText1: TextStyle(), bodyText2: TextStyle()).apply(
          bodyColor: Color(0xff00FFC6),
        ),
      ),

      home: SettingScreen(),
    );
  }
}

class SettingScreen extends StatelessWidget {
  const SettingScreen({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var deviceWidth = MediaQuery.of(context).size.width;
    var deviceHeight = MediaQuery.of(context).size.height;
    return Scaffold(
      backgroundColor: Color(0xff247881),
      appBar: AppBar(
        backgroundColor: Color(0xff43919B),
        centerTitle: true,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: const [
            Text("Settings"),
          ],
        ),
      ),
      body: Container(
        width: deviceWidth,
        height: deviceHeight,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Row(
              children: [
                Container(
                  margin: EdgeInsets.symmetric(vertical: 10),
                  width: deviceWidth / 2,
                  // height: deviceHeight/6,
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      CircleAvatar(
                        radius: 75,
                        backgroundImage: AssetImage('assets/images/ppic.jpg'),
                      ),
                      Container(
                        margin: EdgeInsets.symmetric(vertical: 5),
                        child: Text(
                          "Harsh Bhansali",
                          style: GoogleFonts.montserrat(
                            fontSize: 20,
                            fontWeight: FontWeight.bold,
                          ),
                          textAlign: TextAlign.center,
                        ),
                      ),
                      Text(
                        "Ryoiki Tenkai",
                        style: GoogleFonts.montserrat(
                          fontSize: 14,
                        ),
                      )
                    ],
                  ),
                ),
                Container(
                  width: deviceWidth / 2,
                  child: Image.asset(
                    'assets/images/qrcode.png',
                    width: 125,
                    height: 125,
                  ),
                )
              ],
            ),
            Row(
              children: [
                SquareTab(
                  icn: Icons.key,
                  txt1: "Account",
                  txt2: "Privacy, security,\n change number",
                ),
                SquareTab(
                  icn: Icons.chat,
                  txt1: 'Chats',
                  txt2: 'Themes, wallpapers, \nchat history',
                )
              ],
            ),
            Row(
              children: [
                SquareTab(
                  icn: Icons.circle_notifications_outlined,
                  txt1: 'Notifications',
                  txt2: 'Message, group, \ncall tones',
                ),
                SquareTab(icn: Icons.sd_storage, txt1: 'Storage and data', txt2: 'Network Usage,\n auto-download'),
              ],
            ),
            Row(
              children: [
                SquareTab(icn: Icons.help_outline, txt1: 'Help', txt2: 'Help Center, contact us, \nprivacy policy'),
                SquareTab(icn: Icons.emoji_people, txt1: 'Invite a friend', txt2: '')
              ],
            ),
            Column(
              children: [
                Container(
                  margin: EdgeInsets.only(top: 20, bottom: 3),
                  child: Text(
                    'from',
                    style: GoogleFonts.montserrat(
                      fontSize: 14,
                    ),
                    textAlign: TextAlign.center,
                  ),
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.facebook),
                    Text(
                      "Meta",
                      style: GoogleFonts.montserrat(
                        fontSize: 14,
                      ),
                      textAlign: TextAlign.center,
                    ),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
