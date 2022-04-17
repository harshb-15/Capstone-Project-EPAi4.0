// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables, must_be_immutable

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class SquareTab extends StatelessWidget {
  IconData icn;
  String txt1, txt2;
  SquareTab({Key key, @required this.icn, @required this.txt1, @required this.txt2}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var deviceWidth = MediaQuery.of(context).size.width;
    var deviceHeight = MediaQuery.of(context).size.height;
    return Container(
      width: deviceWidth / 2,
      child: Column(
        children: [
          Icon(
            icn,
            size: 50,
          ),
          Container(
            margin: EdgeInsets.only(top: 5),
            child: Text(
              txt1,
              style: GoogleFonts.montserrat(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
              textAlign: TextAlign.center,
            ),
          ),
          Text(
            txt2,
            style: GoogleFonts.montserrat(
              fontSize: 14,
            ),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }
}
