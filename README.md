#** Directions API (JSON Return)**

### Googld API address JSON return that returns direction from Toronto Pearson International Airpot to CN Tower.
https://maps.googleapis.com/maps/api/directions/json?origin=Toronto+Pearson+International+Airport&destination=CN+Tower&key=AIzaSyA5a1FoKmbmQ1djPh6pRx7oiknBf3ACNOE


Result:
{
   "geocoded_waypoints" : [
      {
         "geocoder_status" : "OK",
         "place_id" : "ChIJkdQtwEo5K4gRxQ4DxOldHbQ",
         "types" : [ "airport", "establishment", "point_of_interest" ]
      },
      {
         "geocoder_status" : "OK",
         "place_id" : "ChIJmzrzi9Y0K4gRgXUc3sTY7RU",
         "types" : [ "establishment", "point_of_interest", "tourist_attraction" ]
      }
   ],
   "routes" : [
      {
         "bounds" : {
            "northeast" : {
               "lat" : 43.695908,
               "lng" : -79.38665709999999
            },
            "southwest" : {
               "lat" : 43.6134662,
               "lng" : -79.61291299999999
            }
         },
         "copyrights" : "Map data ©2021 Google",
         "legs" : [
            {
               "distance" : {
                  "text" : "27.4 km",
                  "value" : 27413
               },
               "duration" : {
                  "text" : "20 mins",
                  "value" : 1217
               },
               "end_address" : "290 Bremner Blvd, Toronto, ON M5V 3L9, Canada",
               "end_location" : {
                  "lat" : 43.641677,
                  "lng" : -79.38665709999999
               },
               "start_address" : "Toronto Pearson International Airport (YYZ), 6301 Silver Dart Dr, Mississauga, ON L5P 1B2, Canada",
               "start_location" : {
                  "lat" : 43.6858094,
                  "lng" : -79.6041328
               },
               "steps" : [
                  {
                     "distance" : {
                        "text" : "4 m",
                        "value" : 4
                     },
                     "duration" : {
                        "text" : "1 min",
                        "value" : 0
                     },
                     "end_location" : {
                        "lat" : 43.6858047,
                        "lng" : -79.6041812
                     },
                     "html_instructions" : "Head \u003cb\u003ewest\u003c/b\u003e",
                     "polyline" : {
                        "points" : "iksiGxtzdN@H"
                     },
                     "start_location" : {
                        "lat" : 43.6858094,
                        "lng" : -79.6041328
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "1.1 km",
                        "value" : 1112
                     },
                     "duration" : {
                        "text" : "1 min",
                        "value" : 65
                     },
                     "end_location" : {
                        "lat" : 43.689754,
                        "lng" : -79.612101
                     },
                     "html_instructions" : "Keep \u003cb\u003eright\u003c/b\u003e at the fork, follow signs for \u003cb\u003eON-409\u003c/b\u003e/\u003cwbr/\u003e\u003cb\u003eON-401\u003c/b\u003e/\u003cwbr/\u003e\u003cb\u003eON-427\u003c/b\u003e",
                     "maneuver" : "fork-right",
                     "polyline" : {
                        "points" : "gksiGbuzdNAB?FAB?BDnA@j@Dp@?ND|@BtA@NBbADzA@XDdA@n@BhA?F@p@?HAb@?BAf@?HEjAEbBATAj@?DA`@?X@X?L@P@h@BZ@T@h@AXARAXETG`@K\\Uf@GJMRgA~@IDEBSJGBG@QDG@MBK@W?O?KA[IYECAWEI?SAm@KeASy@OOCSEgASWEg@KWGUKUQ"
                     },
                     "start_location" : {
                        "lat" : 43.6858047,
                        "lng" : -79.6041812
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "0.5 km",
                        "value" : 454
                     },
                     "duration" : {
                        "text" : "1 min",
                        "value" : 20
                     },
                     "end_location" : {
                        "lat" : 43.6936892,
                        "lng" : -79.61060619999999
                     },
                     "html_instructions" : "Continue onto \u003cb\u003eON-409 E\u003c/b\u003e",
                     "polyline" : {
                        "points" : "}ctiGrf|dNwG{AKAwAY{@WoAg@s@UiDkAm@O"
                     },
                     "start_location" : {
                        "lat" : 43.689754,
                        "lng" : -79.612101
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "5.4 km",
                        "value" : 5381
                     },
                     "duration" : {
                        "text" : "3 mins",
                        "value" : 207
                     },
                     "end_location" : {
                        "lat" : 43.66532660000001,
                        "lng" : -79.5725685
                     },
                     "html_instructions" : "Take the exit onto \u003cb\u003eON-427 S\u003c/b\u003e toward \u003cb\u003eON-401 W\u003c/b\u003e",
                     "maneuver" : "ramp-right",
                     "polyline" : {
                        "points" : "q|tiGh}{dNUUIG}@_@gAe@w@Yk@_@OIGEUUGIQSGGGIEGEI[m@M[EOEMKm@Ge@Ci@@m@Bk@@IF_@Lm@Ne@Vg@V_@\\YnAw@jC{AvAw@FEbB_AhAk@bAg@j@Y`@QbAc@f@UfCeAh@Uf@WNERI~@_@v@[l@WlAe@JGd@Qf@U^QjAm@PKBCVc@h@YVOLGFEHELIdBeARQvDiCDCv@o@n@i@hAmAbByBVo@t@eBp@aBh@}Ab@kA@AHUPa@Pc@Pg@Rk@Zs@N_@P_@P]^m@PW\\e@^i@d@k@d@e@RUTQj@e@l@e@f@Yn@]j@W`@Od@Mf@M`@IBCf@K`@E\\EnAMlAMB?JCfFe@nBSdBOr@IbAITEb@G\\EDAx@Ol@OLETIl@Uf@S`Ag@l@]RMR[@CXU\\[|@w@\\[h@g@n@o@VY\\_@FIRUT]HOFKRc@JQTc@LWLWLYPe@Pc@FUHYJ_@F[Lk@He@D[DYB]D]B]@_@@Y@]@]?s@?_@A]?YA]Eo@C]E]Ga@Gg@SoAEYG]]qBc@gCMu@Gc@Ms@Gc@My@C]QaBMeBCcA@sCJs@NwBDc@BQFa@Lm@Ps@Ps@Z{@N_@HOJUFMFIT_@HMJONSV]h@o@RUPONQ@?d@e@p@i@XUNMVU~@m@d@YZOJG^QjAg@^Op@WJCRIzBw@bBi@t@U"
                     },
                     "start_location" : {
                        "lat" : 43.6936892,
                        "lng" : -79.61060619999999
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "1.3 km",
                        "value" : 1305
                     },
                     "duration" : {
                        "text" : "1 min",
                        "value" : 44
                     },
                     "end_location" : {
                        "lat" : 43.6541686,
                        "lng" : -79.5675753
                     },
                     "html_instructions" : "Keep \u003cb\u003eleft\u003c/b\u003e to stay on \u003cb\u003eON-427 S\u003c/b\u003e",
                     "maneuver" : "keep-left",
                     "polyline" : {
                        "points" : "ikoiGpotdNbNgEjDeAlEuA@?vBq@VIpC}@fA_@hA_@bDkA`@O^MhCcAd@Q^Mx@]fBs@vGmCVKNGJE"
                     },
                     "start_location" : {
                        "lat" : 43.66532660000001,
                        "lng" : -79.5725685
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "4.2 km",
                        "value" : 4209
                     },
                     "duration" : {
                        "text" : "2 mins",
                        "value" : 140
                     },
                     "end_location" : {
                        "lat" : 43.61795070000001,
                        "lng" : -79.55246729999999
                     },
                     "html_instructions" : "Keep \u003cb\u003eleft\u003c/b\u003e to stay on \u003cb\u003eON-427 S\u003c/b\u003e",
                     "maneuver" : "keep-left",
                     "polyline" : {
                        "points" : "qemiGjpsdNdSiIjBw@\\ONGXKhAc@`@OtAi@BAt@YnBs@NEdBo@lAa@\\M|@[vBu@^K\\Mz@YpAc@f@Oz@Y|@Wd@QvBo@tH}BHCbEmApAa@zAa@lA_@`Co@lA]nD{@bAWf@Mb@Ib@MPCb@MhDw@l@Ox@Sf@M`@Kd@Kl@OnA[zA_@jAYDC\\I`@Kv@Sr@QNEZIfCq@b@MLEVEpA]fA[VG\\KXIn@Qt@UDCzAa@JCRGFCPEj@Qz@Yn@QlA_@f@Qb@MNEpAc@fBk@`Bk@bA[|@[pAc@h@QxBw@zBw@r@Up@UpBq@VKHCxAg@d@OfFgBh@Q^M^Oj@Q^KLENGh@O\\KRGZKTG|@W"
                     },
                     "start_location" : {
                        "lat" : 43.6541686,
                        "lng" : -79.5675753
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "1.3 km",
                        "value" : 1320
                     },
                     "duration" : {
                        "text" : "1 min",
                        "value" : 51
                     },
                     "end_location" : {
                        "lat" : 43.6150502,
                        "lng" : -79.54044520000001
                     },
                     "html_instructions" : "Take the \u003cb\u003eGardiner Expressway\u003c/b\u003e exit on the \u003cb\u003eleft\u003c/b\u003e toward \u003cb\u003eToronto\u003c/b\u003e",
                     "maneuver" : "ramp-left",
                     "polyline" : {
                        "points" : "ecfiG|qpdNFK@ABABARGLCTGNEPEhA[`AWnD}@|@St@SNEPEJEJERKXONK\\YXWX]\\i@Xg@@CTk@Na@HYJe@Je@DWFq@Dg@@k@@[?M@a@Ai@AU?UG_AEm@I}@OeA?AKm@Ko@]sBc@sCY}ACe@y@yFa@oDKw@E_@C]Ei@MaBG[EMEI"
                     },
                     "start_location" : {
                        "lat" : 43.61795070000001,
                        "lng" : -79.55246729999999
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "12.2 km",
                        "value" : 12247
                     },
                     "duration" : {
                        "text" : "7 mins",
                        "value" : 448
                     },
                     "end_location" : {
                        "lat" : 43.6378294,
                        "lng" : -79.3993138
                     },
                     "html_instructions" : "Merge onto \u003cb\u003eGardiner Expy E\u003c/b\u003e",
                     "maneuver" : "merge",
                     "polyline" : {
                        "points" : "aqeiGxfndNe@kGCWEa@MqASiB?Cc@_E_@eDWuBCOkAqKY_Ca@kDCSe@_EOsAQsAGKAC?AMcAY_CAQMaAm@kF_@kDIk@[oCIu@{@wHcAsI_@iDq@}F]sCGm@ACk@cFaAoIe@mEiFgd@uByQa@eDKw@Gm@Ga@UiBoAqJKu@MeAg@kDAOAIAI?E?E?E}@gGAE{@aGIc@m@_Ea@oCiBwLQkASqAQgAGc@Km@QmAIe@q@sEO}@e@{Cm@}DM}@COGY{@}FAAo@}Dq@oDIg@YsBU{ACUGk@SgAEWKm@WkAOq@e@{Ac@sAg@iAg@aAKQ]m@a@q@c@o@iDuES[c@k@c@m@w@kAw@eAKSs@cAsBwCaBsCUe@We@CEQ_@[q@Wk@]w@]w@aAwB[q@i@iAu@{Ao@mAm@oAc@_Aq@sAq@uAa@w@EIISISO]w@yB[_Ae@qAo@qBCEIYm@eBs@_C[cAc@yA[kAa@_BOq@Me@Kk@WoAQ{@Ki@ACMy@QeAAGYkBEa@My@UsBOyAIaAIu@IcAK{AK{BI}ACwAA[CyA?GAq@?O?a@?q@?W?Y?_BB{ADkBBsABoAFcBDaAHcBJiBBUDq@Bc@JsAL{ARqBTuBTmBPmAD_@ZoBBQV}Ad@_CReAZwAVcARw@T{@Tw@Pm@HYVw@tGkSzDyLp@uBfAeDHUX{@j@kBPi@Tu@H[Ja@H_@Ls@Je@Hg@F]D]Fa@B[BQB[BS@O?IBWBc@@]@S@U@eA@]?UAa@?QAUAo@Ai@Cg@A_@C[Ca@E[ESASIm@Ik@Ks@Ki@AMAE?C?CCMEQAG?CCKESEUSaAYyAy@qEScAk@{CY_BCGIe@Km@WuAAGUmAWsA[eB]iBKm@wCgPk@}CiAkGY}A}AmIk@cDQ_Aa@yCSqBKgBEw@AYA[AiCAyBAuDCqBCoBCeBQcE{@_SGqBA_C@uBDaB@y@J{E@["
                     },
                     "start_location" : {
                        "lat" : 43.6150502,
                        "lng" : -79.54044520000001
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "0.6 km",
                        "value" : 570
                     },
                     "duration" : {
                        "text" : "1 min",
                        "value" : 58
                     },
                     "end_location" : {
                        "lat" : 43.6385515,
                        "lng" : -79.39237899999999
                     },
                     "html_instructions" : "Take the exit toward \u003cb\u003eSpadina Ave\u003c/b\u003e",
                     "maneuver" : "ramp-right",
                     "polyline" : {
                        "points" : "m_jiGttrcNHa@@ABuA@mA?m@@o@?Y?c@Ac@Aa@Ci@CWAMEg@O}AEWGw@I_ASoBEi@Gu@I{@Go@CYCWAGAWAICSAUEWC[COIm@Ge@"
                     },
                     "start_location" : {
                        "lat" : 43.6378294,
                        "lng" : -79.3993138
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "0.2 km",
                        "value" : 245
                     },
                     "duration" : {
                        "text" : "1 min",
                        "value" : 72
                     },
                     "end_location" : {
                        "lat" : 43.6405619,
                        "lng" : -79.392866
                     },
                     "html_instructions" : "Turn \u003cb\u003eleft\u003c/b\u003e onto \u003cb\u003eLower Spadina Ave\u003c/b\u003e/\u003cwbr/\u003e\u003cb\u003eSpadina Ave\u003c/b\u003e\u003cdiv style=\"font-size:0.9em\"\u003eContinue to follow Spadina Ave\u003c/div\u003e",
                     "maneuver" : "turn-left",
                     "polyline" : {
                        "points" : "}cjiGjiqcNG_@AM_A\\i@NUHSDc@Jc@HI@a@J_Cl@"
                     },
                     "start_location" : {
                        "lat" : 43.6385515,
                        "lng" : -79.39237899999999
                     },
                     "travel_mode" : "DRIVING"
                  },
                  {
                     "distance" : {
                        "text" : "0.6 km",
                        "value" : 566
                     },
                     "duration" : {
                        "text" : "2 mins",
                        "value" : 112
                     },
                     "end_location" : {
                        "lat" : 43.641677,
                        "lng" : -79.38665709999999
                     },
                     "html_instructions" : "Turn \u003cb\u003eright\u003c/b\u003e onto \u003cb\u003eBremner Blvd\u003c/b\u003e\u003cdiv style=\"font-size:0.9em\"\u003eDestination will be on the left\u003c/div\u003e",
                     "maneuver" : "turn-right",
                     "polyline" : {
                        "points" : "opjiGllqcNS_BKs@AW?KAG?I?I?K@I?UHY@MJgAJsALyAB[JcA@U@M@G?M@K?G?M?M?E?K?E?EAM?SCSAIAKAE?CCMAEAEAGAEAGAGEMGUCEAGCEEKCICGGMEIACCCGGiAuACEAACCA?C?A?MOS[MQIKIMEICC"
                     },
                     "start_location" : {
                        "lat" : 43.6405619,
                        "lng" : -79.392866
                     },
                     "travel_mode" : "DRIVING"
                  }
               ],
               "traffic_speed_entry" : [],
               "via_waypoint" : []
            }
         ],
         "overview_polyline" : {
            "points" : "iksiGxtzdNAXLpD\\rLFrDCxAMnEClBDbBDp@?bACl@Mv@a@dAU^qAdAYNi@LYDg@?eASa@ESAm@K_Cc@c@I_Dm@k@]cH}AwAY{@WcC}@wE{A_@]eCeAw@Yk@_@WO]_@g@m@a@w@Sk@Q{@KoADyAHi@\\sAVg@V_@\\YnAw@bFsCxFyCxDeBpD{Av@]xD}AfDuA|BkAZg@`Ai@l@]xBwA|DmCfByAhAmAbByBlAuCzA_E`AeCrAkD`@_Ap@kAn@}@dAuAx@{@`Aw@tA_AzAu@nBk@nB_@~Da@hMmApDa@b@GfB_@xBy@nBeARMR[ZYzAsAnCmCd@i@h@s@p@qA~@mBt@yBj@mCTqBHuB?oCKeCi@wDoAqHk@qDQwA_@gECcA@sCJs@NwBHu@ToAb@gBj@{Ad@}@z@qA`AmAd@e@hBaBh@c@vAcAlBcAhDsAhHaC~YcJhJyCnHiChGaCfLuEzWwKtCgA`N_FrFkBpFgBpOwEzJuCnEoA|FyArD}@vLsCbLsCfFsAp@ShBc@vCy@fEmA~GsBxNyEhb@uNjEqA|@WFK@Ah@O`Co@dJ}Bx@Wl@[l@e@r@u@v@qAVo@X{@VkALiAH}BAwBMmBYcCu@sE}@qF}@_Hw@eHSkCMi@EIe@kGIy@eA_KmF}d@a@gDIOi@wEkGwi@mGoj@mK_~@uBkPcAwHC_@{BuOcEkXyC_S{D_WaBmJc@{Cu@eFy@cEiAoDg@iAg@aAi@_AeAaBeGkIoDiFsBwCaBsCm@kAiAcCyCyGgJeRi@oAiD}JoBeG_A}C}@kDaAsEm@cDs@{E}@iISyBWwEMuDEuBAkB?cEPkJb@sJX_E`@mEj@cFv@oF|@}En@}CvAoFhIkWvK}\\t@sCj@_D^wDJmBDoCEyBKmCQeBk@wDC[Kk@c@wBsCkO{B{LkM{r@}@cFa@yCSqBQ_DCu@IkPGuEmAcYGqBA_CFwELuG@[Ha@DwA@{B?qCKqBc@uEeAmLYwC[aCiBl@i@NqAVaDx@_@sCCu@@u@Jg@V{C^oEDyAAe@G}@Oy@c@uASc@yAgBKEOOa@m@]g@"
         },
         "summary" : "ON-427 S and Gardiner Expy E",
         "warnings" : [],
         "waypoint_order" : []
      }
   ],
   "status" : "OK"
}
