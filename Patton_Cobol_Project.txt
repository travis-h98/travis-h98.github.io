      *PATTON OEHLER
      *2/15/2022
      *This program is a printer spacing chart
      *for the albia soccer club fundraser
      *currently uses tables for most calculations
       IDENTIFICATION DIVISION.
       PROGRAM-ID CBLPLO06
       AUTHOR. PATTON OEHLER
       DATE-WRITTEN. 2/15/22.
       DATE-COMPILED.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT BOAT-MASTER
               ASSIGN TO 'C:\COBAL\CBLPOPSL.DAT'
               ORGANIZATION IS LINE sequential.

           SELECT PRTOUT
               ASSIGN TO 'C:\COBAL\CBLPOPSL.PRT'
               ORGANIZATION IS RECORD SEQUENTIAL.

           SELECT ERROR-OUT
               ASSIGN TO 'C:\COBAL\CBLPOPER.PRT'
               ORGANIZATION IS RECORD SEQUENTIAL.

       DATA DIVISION.

       FD BOAT-MASTER
           LABEL RECORD IS STANDARD
               RECORD CONTAINS 71 CHARACTERS
                   DATA RECORD IS I-REC.

       01 I-REC.
         05 I-LNAME        PIC X(15).
         05 I-FNAME        PIC X(15).
         05 I-ADDRESS      PIC X(15).
         05 I-CITY         PIC X(10).
         05 I-STATE        PIC XX.
         05 I-ZIP-1        PIC 9(5).
         05 I-ZIP-2        PIC 9(4).
         05 I-POP-TYPE     PIC 99.
         05 I-NUM-CASES    PIC 99.
         05 I-TEAM         PIC X.

       FD PRTOUT
           LABEL RECORD IS OMITTED
           RECORD CONTAINS 132 CHARACTERS
           LINAGE IS 60 WITH FOOTING AT 55
           DATA RECORD IS PRTLINE.

       01 PRTLINE PIC X(132).

       FD ERROR-OUT
          LABEL RECORD IS OMITTED
          RECORD CONTAINS 132 CHARACTERS
          LINAGE IS 60 WITH FOOTING AT 55
          DATA RECORD IS ERROR-PRTLINE.

       01 ERROR-PRTLINE PIC X(132).

       WORKING-STORAGE SECTION.
       01 I-DATE-TIME.
         05 I-DATE.
           10 I-YEAR   PIC 9(4).
           10 I-MONTH  PIC 99.
           10 I-DAY    PIC X(2).
         05 I-TIME     PIC X(11).

       01 WORK-AREA.
         05 PAGE_CTR       PIC 99      VALUE 0.
         05 ERROR-PAGE-CTR PIC 99      VALUE 0.
         05 MORE-RECS      PIC XXX     VALUE 'YES'.
         05 BLANK_LINE     PIC X(132)  VALUE SPACES.

         05 IS-VALID-DATA  PIC X.
         05 ERROR-COUNT    PIC 9(4) VALUE 0.

         05 C-DEPOSIT-AMT  PIC 999V99.
         05 C-TOTAL-SALE   PIC 9(4)V99.

         05 TEAM-I         PIC 99      VALUE 0.
         05 TEAM-GT-I      PIC 99      VALUE 0.
         05 POP-I          PIC 99      VALUE 0.


       01 GT-TOT-COST-TEAMS.
         05 FILLER PIC 9(38) VALUE 0.
         05 FILLER PIC 9(17) VALUE 0.

       01 GT-TOT-COST-TABLE REDEFINES GT-TOT-COST-TEAMS.
         05 GT-TOT-COST-T OCCURS 5.
           10 GT-TOT-COST PIC 9(9)V99.

       01 STATE-POP-TAX-TABLE.
         05 FILLER PIC X(4) VALUE 'IA05'.
         05 FILLER PIC X(4) VALUE 'NE05'.
         05 FILLER PIC X(4) VALUE 'WI05'.
         05 FILLER PIC X(4) VALUE 'MI10'.
         05 FILLER PIC X(4) VALUE 'IL00'.
         05 FILLER PIC X(4) VALUE 'MO00'.

       01 STATE-POP-TAX-T REDEFINES STATE-POP-TAX-TABLE.
         05 STATE-POP-TAX-TY OCCURS 6.
           10 STATE-POP-TAX-LETTERS  PIC XX.
           10 STATE-POP-TAX-PRICE    PIC V99.

       01 ERROR-MSG.
         05 FILLER PIC X(60) VALUE 'I-LNAME IS BLANK - THIS IS A REQUIRE
      -    'D FIELD'.
         05 FILLER PIC X(60) VALUE 'I-FNAME IS BLANK - THIS IS A REQUIRE
      -    'D FIELD'.
         05 FILLER PIC X(60) VALUE 'I-ADDRESS IS BLANK - THIS IS A REQUI
      -    'RED FIELD'.
         05 FILLER PIC X(60) VALUE 'I-CITY IS BLANK - THIS IS A REQUIRED
      -    ' FIELD'.
         05 FILLER PIC X(60) VALUE 'I-STATE DOES NOT HAVE A VALID STATE(
      -    'IA,IL,MI,MO,NE,WI)'.
         05 FILLER PIC X(60) VALUE 'I-ZIP IS NOT NUMERIC'.

         05 FILLER PIC X(60) VALUE 'I-POP-TYPE IS NOT NUMERIC'.

         05 FILLER PIC X(60) VALUE 'I-POP-TYPE DOES NOT CONTAIN A VALID 
      -    'NUMBER'.
         05 FILLER PIC X(60) VALUE 'I-NUM-CASES IS NOT NUMERIC'.

         05 FILLER PIC X(60) VALUE 'I-NUM-CASES DOES NOT CONTAIN A VALID
      -    ' NUMBER'.
         05 FILLER PIC X(60) VALUE 'I-TEAM DOES NOT CONTAIN A VALID VALU
      -    'E(A-E)'.

       01 ERROR-DESC-TABLE REDEFINES ERROR-MSG.
         05 ERROR-DESC OCCURS 11.
           10 ERROR-DESCRIPTION-TABLE PIC X(60).

       01 TEAM-NAMES.
         05 FILLER PIC X(5) VALUE 'ABCDE'.

       01 TEAM-NAME-TABLE REDEFINES TEAM-NAMES.
         05 TEAM-NAME-T OCCURS 5.
           10 TEAM-NAME PIC X.

       01 POP-TYPE-TABLE-F.
         05 FILLER PIC X(16) VALUE "COKE".
         05 FILLER PIC X(16) VALUE "DIET COKE".
         05 FILLER PIC X(16) VALUE "MELLO YELLO".
         05 FILLER PIC X(16) VALUE "CHERRY COKE".
         05 FILLER PIC X(16) VALUE "DIET CHERRY COKE".
         05 FILLER PIC X(16) VALUE "SPRITE".

       01 POP-TYPE-NAME-TABLE REDEFINES POP-TYPE-TABLE-F.
         05 POP-TYPE-NAME OCCURS 6.
           10 POP-TYPE PIC X(16).

       01 TOT-POP-TYPE-QUANTITY-TABLE.
         05 FILLER PIC 9(6) VALUE 0.
         05 FILLER PIC 9(6) VALUE 0.
         05 FILLER PIC 9(6) VALUE 0.
         05 FILLER PIC 9(6) VALUE 0.
         05 FILLER PIC 9(6) VALUE 0.
         05 FILLER PIC 9(6) VALUE 0.

       01 TOT-POP-TYPE-TBL REDEFINES TOT-POP-TYPE-QUANTITY-TABLE.
         05 POP-TYPE-TAB OCCURS 6.
           10 TOT-POP-TYPE PIC 9(6).

       01 COMPANY-TITLE-LINE-1.
         05 FILLER     PIC X(6)    VALUE 'DATE: '.
         05 O-MONTH    PIC 99.
         05 FILLER     PIC X       VALUE '/'.
         05 O-DAY      PIC 99.
         05 FILLER     PIC X       VALUE '/'.
         05 O-YEAR     PIC 9(4).
         05 FILLER     PIC X(36)   VALUE SPACES.
         05 FILLER     PIC X(28)   VALUE 'ALBIA SOCCER CLUB FUNDRAISER'.
         05 FILLER     PIC X(44)   VALUE SPACES.
         05 FILLER     PIC X(6)    VALUE 'PAGE: '.
         05 O-PAGE-NUM PIC Z9.

       01 COMPANY-TITLE-LINE-2.
         05 FILLER PIC X(8)  VALUE 'COBPLO05'.
         05 FILLER PIC X(48) VALUE SPACES.
         05 FILLER PIC X(19) VALUE '   PATTONS DIVISION'.
         05 FILLER PIC X(57) VALUE SPACES.

       01 COMPANY-TITLE-LINE-3.
         05 FILLER PIC X(60) VALUE SPACES.
         05 FILLER PIC X(12) VALUE "SALES REPORT".
         05 FILLER PIC X(60) VALUE SPACES.

       01 COLUMN-HEADERS.
         05 FILLER PIC X(3)  VALUE SPACES.
         05 FILLER PIC X(9)  VALUE 'LAST NAME'.
         05 FILLER PIC X(8)  VALUE SPACES.
         05 FILLER PIC X(10) VALUE 'FIRST NAME'.
         05 FILLER PIC X(7)  VALUE SPACES.
         05 FILLER PIC X(4)  VALUE 'CITY'.
         05 FILLER PIC X(8)  VALUE SPACES.
         05 FILLER PIC X(14) VALUE 'STATE ZIP CODE'.
         05 FILLER PIC X(4)  VALUE SPACES.
         05 FILLER PIC X(8)  VALUE 'POP TYPE'.
         05 FILLER PIC X(13) VALUE SPACES.
         05 FILLER PIC X(8)  VALUE 'QUANTITY'.
         05 FILLER PIC X(6)  VALUE SPACES.
         05 FILLER PIC X(11) VALUE 'DEPOSIT AMT'.
         05 FILLER PIC X(6)  VALUE SPACES.
         05 FILLER PIC X(13) VALUE 'TOTAL SALES   '.

       01 DETAIL-LINE.
         05 FILLER         PIC X(3)    VALUE SPACES.
         05 O-LAST-NAME    PIC X(15).
         05 FILLER         PIC X(2)    VALUE SPACES.
         05 O-FIRST-NAME   PIC X(15).
         05 FILLER         PIC X(2)    VALUE SPACES.
         05 O-CITY         PIC X(10).
         05 FILLER         PIC X(3)    VALUE SPACES.
         05 O-STATE        PIC X(2).
         05 FILLER         PIC X(3)    VALUE SPACES.
         05 O-ZIP-CODE-1   PIC 9(5).
         05 FILLER         PIC X       VALUE '-'.
         05 O-ZIP-CODE-2   PIC 9(4).
         05 FILLER         PIC X(2)    VALUE SPACES.
         05 O-POP-TYPE     PIC X(16).
         05 FILLER         PIC X(8)    VALUE SPACES.
         05 O-QUANTITY     PIC Z9.
         05 FILLER         PIC X(11)   VALUE SPACES.
         05 O-DEPOSIT-AMT  PIC $$$$.99.
         05 FILLER         PIC X(9)    VALUE SPACES.
         05 O-TOTAL-SALE   PIC $$,$$$.99.
         05 FILLER         PIC X(3)    VALUE SPACES.

       01 GRAND-TOTALS-TITLE-LINE.
         05 FILLER PIC X(13)   VALUE 'GRAND TOTALS:'.
         05 FILLER PIC X(119)  VALUE SPACES.

       01 GRAND-TOTAL-DETAIL-LINE.
         05 FILLER             PIC X(3)    VALUE SPACES.
         05 O-FIRST-POP-TYPE   PIC X(16).
         05 FILLER             PIC X       VALUE SPACE.
         05 O-FIRST-POP-TOTAL  PIC ZZZ,ZZ9.
         05 FILLER             PIC X(6)    VALUE SPACES.
         05 O-SECOND-POP-TYPE  PIC X(16).
         05 FILLER             PIC X       VALUE SPACE.
         05 O-SECOND-POP-TOTAL PIC ZZZ,ZZ9.
         05 FILLER             PIC X(6)    VALUE SPACES.
         05 O-THIRD-POP-TYPE   PIC X(16).
         05 FILLER             PIC X       VALUE SPACE.
         05 O-THIRD-POP-TOTAL  PIC ZZZ,ZZ9.
         05 FILLER             PIC X(45)   VALUE SPACES.

       01 TEAM-TOTALS-TITLE-LINE.
         05 FILLER PIC X(12)   VALUE 'TEAM TOTALS:'.
         05 FILLER PIC X(120)  VALUE SPACES.

       01 TEAM-TOTALS-DETAIL-LINE.
         05 FILLER         PIC X(3)    VALUE SPACES.
         05 TEAM-LETTER    PIC X.
         05 FILLER         PIC X       VALUE SPACE.
         05 TEAM-TOTAL     PIC $$$$,$$$,$$$.99.
         05 FILLER         PIC X(112)  VALUE SPACES.

       01 ERROR-TITLE-LINE-3.
         05 FILLER PIC X(60) VALUE SPACES.
         05 FILLER PIC X(12) VALUE 'ERROR REPORT'.
         05 FILLER PIC X(60) VALUE SPACES.

       01 ERROR-COLUMN-TITLES.
         05 FILLER PIC X(12) VALUE 'ERROR RECORD'.
         05 FILLER PIC X(60) VALUE SPACES.
         05 FILLER PIC X(17) VALUE 'ERROR DESCRIPTION'.
         05 FILLER PIC X(43) VALUE SPACES.

       01 ERROR-DETAIL-LINE.
         05 ERROR-RECORD       PIC X(71).
         05 FILLER             PIC X(1)    VALUE SPACE.
         05 ERROR-DESCRIPTION  PIC X(60).

       01 ERROR-TOTALS-LINE.
         05 FILLER         PIC X(13)   VALUE 'TOTAL ERRORS '.
         05 TOTAL-ERRORS   PIC Z,ZZ9.
         05 FILLER         PIC X(114)  VALUE SPACES.

       PROCEDURE DIVISION.

      *The starting point of the program
       0000-MAIN.
           PERFORM 1000-INIT.
           PERFORM 2000-MAINLINE
             UNTIL MORE-RECS = "NO".
           PERFORM 3000-CLOSING.
           STOP RUN.
      * Inititalizes the program
       1000-INIT.
           MOVE FUNCTION CURRENT-DATE TO I-DATE-TIME.
           MOVE I-DAY TO O-DAY.
           MOVE I-MONTH TO O-MONTH.
           MOVE I-YEAR TO O-YEAR.

           OPEN INPUT BOAT-MASTER.
           OPEN OUTPUT PRTOUT.
           OPEN OUTPUT ERROR-OUT.




           PERFORM 9100-HDG.
           PERFORM 9200-ERROR-HEADINGS.
           PERFORM 9000-READ.

           

      *Main loop
       2000-MAINLINE.
           PERFORM 2100-VALIDATE THRU 2200-EXIT.
           IF IS-VALID-DATA = 'Y'
               PERFORM 2300-CALCS
               PERFORM 2400-OUTPUT
           ELSE
               PERFORM 2500-ERROR-OUTPUT.
           PERFORM 9000-READ.

      *Validates the input
       2100-VALIDATE.
           MOVE 'N' TO IS-VALID-DATA.
           IF I-LNAME = spaces
               MOVE ERROR-DESCRIPTION-TABLE(1) to
                 ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           IF I-FNAME = spaces
               MOVE ERROR-DESCRIPTION-TABLE(2) to
                 ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           IF I-ADDRESS = spaces
               MOVE ERROR-DESCRIPTION-TABLE(3) to
                 ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           IF I-CITY = spaces
               MOVE ERROR-DESCRIPTION-TABLE(4) to
                 ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           if (NOT (I-STATE = "IA" OR I-STATE = "IL" OR I-STATE = "MI"
             OR I-STATE = "MO" OR I-STATE = "NE" OR I-STATE = "WI"))
               MOVE ERROR-DESCRIPTION-TABLE(5) to ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           IF I-ZIP-1 NOT NUMERIC
               MOVE ERROR-DESCRIPTION-TABLE(6) TO ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           IF I-ZIP-2 NOT NUMERIC
               MOVE ERROR-DESCRIPTION-TABLE(6) TO ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           IF I-POP-TYPE NOT NUMERIC
               MOVE ERROR-DESCRIPTION-TABLE(7) TO ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           IF NOT (I-POP-TYPE > 0 AND I-POP-TYPE < 7)
               MOVE ERROR-DESCRIPTION-TABLE(8)
                 TO ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           IF I-NUM-CASES NOT NUMERIC
               MOVE ERROR-DESCRIPTION-TABLE(9) TO ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           IF I-NUM-CASES < 1
               MOVE ERROR-DESCRIPTION-TABLE(10)
                 TO ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           if (NOT (I-TEAM >= 'A' AND I-TEAM <= 'E'))
               MOVE ERROR-DESCRIPTION-TABLE(11) to
                 ERROR-DESCRIPTION
               GO TO 2200-EXIT.

           MOVE 'Y' TO IS-VALID-DATA.

       2200-EXIT.
           EXIT.

      *Calculates things for output
       2300-CALCS.
           PERFORM VARYING POP-I FROM 1 BY 1 UNTIL
             STATE-POP-TAX-LETTERS(POP-I) = I-STATE.

           COMPUTE C-DEPOSIT-AMT = STATE-POP-TAX-PRICE(POP-I) * 24 *
             I-NUM-CASES.


           COMPUTE C-TOTAL-SALE = C-DEPOSIT-AMT + I-NUM-CASES * 18.71.

           PERFORM 2310-SET-GT-QUANTITY-COST.
           PERFORM 2320-SET-O-POP-TYPE.

       2310-SET-GT-QUANTITY-COST.
           PERFORM VARYING TEAM-I FROM 1 BY 1 UNTIL
             TEAM-NAME(TEAM-I) = I-TEAM.

           COMPUTE GT-TOT-COST(TEAM-I) = GT-TOT-COST(TEAM-I) +
             C-TOTAL-SALE.


       2320-SET-O-POP-TYPE.

           MOVE POP-TYPE(I-POP-TYPE) TO O-POP-TYPE.
           ADD I-NUM-CASES TO TOT-POP-TYPE(I-POP-TYPE).



      *Outputs a single detail line
       2400-OUTPUT.

           MOVE I-LNAME TO O-LAST-NAME.
           MOVE I-FNAME TO O-FIRST-NAME.
           MOVE I-CITY TO O-CITY.
           MOVE I-STATE TO O-STATE.
           MOVE I-ZIP-1 TO O-ZIP-CODE-1.
           MOVE I-ZIP-2 TO O-ZIP-CODE-2.
           MOVE I-NUM-CASES TO O-QUANTITY.
           MOVE C-DEPOSIT-AMT TO O-DEPOSIT-AMT.
           MOVE C-TOTAL-SALE TO O-TOTAL-SALE.

           WRITE PRTLINE
             FROM DETAIL-LINE
             AFTER ADVANCING 2 LINES
               AT EOP
                   PERFORM 9100-HDG.

       2500-ERROR-OUTPUT.
           ADD 1 TO ERROR-COUNT.

           MOVE I-REC TO ERROR-RECORD.

           WRITE ERROR-PRTLINE
             FROM ERROR-DETAIL-LINE
             AFTER ADVANCING 2 LINES
               AT EOP
                   PERFORM 9200-ERROR-HEADINGS.

      *Closes the files and runs the final subtotals/grandtotals
       3000-CLOSING.
           PERFORM 3100-TOTALS.
           PERFORM 3200-ERROR-TOTALS.

           CLOSE BOAT-MASTER.
           CLOSE PRTOUT.
           CLOSE ERROR-OUT.

      *Prints the totals lines
       3100-TOTALS.
           PERFORM 9100-HDG.

           WRITE PRTLINE
             FROM GRAND-TOTALS-TITLE-LINE
             AFTER ADVANCING 2 lines.


           PERFORM 3120-PRINT-POP-LINE VARYING TEAM-GT-I FROM 0 BY 1
             UNTIL TEAM-GT-I = 2.

           WRITE PRTLINE
             FROM TEAM-TOTALS-TITLE-LINE
             AFTER ADVANCING 3 lines.

           PERFORM 3110-PRINT-LINE VARYING TEAM-GT-I FROM 1 BY 1 until
             TEAM-GT-I = 6.

       3110-PRINT-LINE.
           MOVE GT-TOT-COST(TEAM-GT-I) TO TEAM-TOTAL.
           MOVE TEAM-NAME(TEAM-GT-I) TO TEAM-LETTER.
           WRITE PRTLINE
             FROM TEAM-TOTALS-DETAIL-LINE
             AFTER ADVANCING 2 lines.

       3120-PRINT-POP-LINE.
           MOVE POP-TYPE(1 +TEAM-GT-I * 3) TO O-FIRST-POP-TYPE.
           MOVE TOT-POP-TYPE(1 +TEAM-GT-I * 3) TO O-FIRST-POP-TOTAL.
           MOVE POP-TYPE(2 +TEAM-GT-I * 3) TO O-SECOND-POP-TYPE.
           MOVE TOT-POP-TYPE(2 +TEAM-GT-I * 3) TO O-SECOND-POP-TOTAL.
           MOVE POP-TYPE(3 +TEAM-GT-I * 3) TO O-THIRD-POP-TYPE.
           MOVE TOT-POP-TYPE(3 +TEAM-GT-I * 3) TO O-THIRD-POP-TOTAL.

           WRITE PRTLINE
             FROM GRAND-TOTAL-DETAIL-LINE
             AFTER ADVANCING 2 LINES.

       3200-ERROR-TOTALS.
           MOVE ERROR-COUNT TO TOTAL-ERRORS.

           WRITE ERROR-PRTLINE
             FROM ERROR-TOTALS-LINE
             AFTER ADVANCING 3 LINES.

      *Reads the file
       9000-READ.
           READ BOAT-MASTER
               AT END
                   MOVE "NO" TO MORE-RECS.

      *Prints the heading
       9100-HDG.
           ADD 1 TO PAGE_CTR.
           MOVE PAGE_CTR TO O-PAGE-NUM.

           WRITE PRTLINE
             FROM COMPANY-TITLE-LINE-1
             AFTER ADVANCING PAGE.

           WRITE PRTLINE
             FROM COMPANY-TITLE-LINE-2
             AFTER ADVANCING 1 LINE.

           WRITE PRTLINE
             FROM COMPANY-TITLE-LINE-3
             AFTER ADVANCING 1 LINE.

           WRITE PRTLINE
             FROM COLUMN-HEADERS
             AFTER ADVANCING 2 LINES.

           WRITE PRTLINE
             FROM BLANK_LINE
             AFTER ADVANCING 1 LINE.

       9200-ERROR-HEADINGS.
           ADD 1 TO ERROR-PAGE-CTR.
           MOVE ERROR-PAGE-CTR TO O-PAGE-NUM.

           WRITE ERROR-PRTLINE
             FROM COMPANY-TITLE-LINE-1
             AFTER ADVANCING PAGE.

           WRITE ERROR-PRTLINE
             FROM COMPANY-TITLE-LINE-2
             AFTER ADVANCING 1 LINE.

           WRITE ERROR-PRTLINE
             FROM ERROR-TITLE-LINE-3
             AFTER ADVANCING 1 LINE.

           WRITE ERROR-PRTLINE
             FROM ERROR-COLUMN-TITLES
             AFTER ADVANCING 2 LINES.
