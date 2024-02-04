#coding: utf-8

'''
Tabellen voor overeenkomsten
    Rang 0 komt overeen met de positie van de informatie in het MAESTRO-frame
    Rang 1 komt overeen met de titel gepubliceerd op de broker
    Rang 2 (optioneel) maakt het mogelijk om de code van het frame te vervangen door overeenkomstige tekstuele informatie
'''
RecuperoInfo=[
	[1,"Status van de kachel",[
						[0, "Uit"],
						[1, "Controle van de kachel koud / warm"],
						[2, "Koud Reinigen"],
						[3, "Koud Laden"],
						[4, "Start 1 Koud"],
						[5, "Start 2 Koud"],
						[6, "Warm Reinigen"],
						[7, "Warm Laden"],
						[8, "Start 1 Warm"],
						[9, "Start 2 Warm"],
						[10, "Stabilisatie"],
						[11, "Vermogen 1"],
						[12, "Vermogen 2"],
						[13, "Vermogen 3"],
						[14, "Vermogen 4"],
						[15, "Vermogen 5"],
						[30, "Diagnostische modus"],
						[31, "In werking"],
						[40, "Aan het uitschakelen"],
						[41, "Aan het afkoelen"],
						[42, "Reiniging bij laag vermogen"],
						[43, "Reiniging bij hoog vermogen"],
						[44, "Vijzel deblokkeren"],
						[45, "AUTO ECO"],
						[46, "Standby"],
						[48, "Diagnostiek"],
						[49, "VIJZEL LADEN"],
						[50, "Fout A01 - Ontsteking mislukt"],
						[51, "Fout A02 - Geen vlam"],
						[52, "Fout A03 - Oververhitting van de tank"],
						[53, "Fout A04 - Te hoge rookgastemperatuur"],
						[54, "Fout A05 - Verstopping afvoer - Ventilator"],
						[55, "Fout A06 - Slechte trek"],
						[56, "Fout A09 - Storing rookgassensor"],
						[57, "Fout A11 - Storing aandrijfmotor"],
						[58, "Fout A13 - Te hoge temperatuur moederbord"],
						[59, "Fout A14 - Actieve fout"],
						[60, "Fout A18 - Te hoge watertemperatuur"],
						[61, "Fout A19 - Storing watertemperatuursensor"],
						[62, "Fout A20 - Storing hulpsensor"],
						[63, "Fout A21 - Drukschakelaar alarm"],
						[64, "Fout A22 - Storing omgevingssensor"],
						[65, "Fout A23 - Storing sluiting vuurkorf"],
						[66, "Fout A12 - Storing aandrijfmotorregelaar"],
						[67, "Fout A17 - Vijzel verstopping"],
						[69, "Wachten op veiligheidsalarmen"],
						]],
	[2,"Status van de omgevingsventilator",[
										[0, "Uitgeschakeld"],
										[1, "Niveau 1"],
										[2, "Niveau 2"],
										[3, "Niveau 3"],
										[4, "Niveau 4"],
										[5, "Niveau 5"],
										[6, "Automatisch"],
										]],
	[3,"Status van de kanaalventilator 1",[
										[0, "Uitgeschakeld"],
										[1, "Niveau 1"],
										[2, "Niveau 2"],
										[3, "Niveau 3"],
										[4, "Niveau 4"],
										[5, "Niveau 5"],
										[6, "Automatisch"],
										]],
	[4,"Status van de kanaalventilator 2",[
										[0, "Uitgeschakeld"],
										[1, "Niveau 1"],
										[2, "Niveau 2"],
										[3, "Niveau 3"],
										[4, "Niveau 4"],
										[5, "Niveau 5"],
										[6, "Automatisch"],
										]],
	[5,"Temperatuur rookgassen"],
	[6,"Omgevingstemperatuur"],
	[7,"Puffertemperatuur"], # !=255 == Hydro
	[8,"Boilertemperatuur"],
	[9,"Temperatuur NTC3"], # !=255 == Hydro
	[10,"Status van de gloeibougie",[
					[0, "Ok"],
					[1, "Versleten"],
					]],
	[11,"ACTIVE - Set"],
	[12,"RPM - Rookgasventilator"],
	[13,"RPM - Vijzel - SET"],
	[14,"RPM - Vijzel - LIVE"],
	[17,"Vuurkorf",[
					[0, "OK"],
					[101, "Vuurkorf openen"],
					[100, "Vuurkorf sluiten"],
					]], # !==Matic
	[18,"Profiel",[
					[0, "Handmatig"],
					[1, "Dynamisch"],
					[2, "Overnacht"],
					[3, "Comfort"],
					[4, "Vermogen 110%"],
					[10, "Adaptieve modus"],
					]],
	[20,"Status actieve modus",[
					[0, "Uit"],
					[1, "Aan"],
					]],  #0: Uitgeschakeld, 1: Ingeschakeld
	[21,"ACTIVE - Live"],
	[22,"Regelmodus",[
							[0, "Handmatig"],
							[1, "Dynamisch"],
							]],
	[23,"ECO-modus",[
					[0, "Uit"],
					[1, "Aan"],
					]],
	[24,"Stille modus",[
					[0, "Uit"],
					[1, "Aan"],
					]],
	[25,"Chronothermostaatmodus",[
					[0, "Uit"],
					[1, "Aan"],
					]],
	[26,"TEMP - Instelpunt"],
	[27,"TEMP - Boiler"],
	[28,"TEMP - Moederbord"],
	[29,"Actief vermogen",[
							[11, "Vermogen 1"],
							[12, "Vermogen 2"],
							[13, "Vermogen 3"],
							[14, "Vermogen 4"],
							[15, "Vermogen 5"],
							]],
	[32,"Uur van de kachel (0-23)"],
	[33,"Minuten van de kachel (0-29)"],
	[34,"Dag van de kachel (1-31)"],
	[35,"Maand van de kachel (1-12)"],
	[36,"Jaar van de kachel"],
	[37,"Totale bedrijfsuren (s)"],
	[38,"Bedrijfsuren bij vermogen 1 (s)"],
	[39,"Bedrijfsuren bij vermogen 2 (s)"],
	[40,"Bedrijfsuren bij vermogen 3 (s)"],
	[41,"Bedrijfsuren bij vermogen 4 (s)"],
	[42,"Bedrijfsuren bij vermogen 5 (s)"],
	[43,"Uren voor onderhoud"],
	[44,"Minuten voor uitschakeling"],
	[45,"Aantal ontstekingen"],
	[47,"Pelletsonde",[
						[0, "Sonde niet actief"],
						[10, "Voldoende niveau"],
						[11, "Bijna leeg niveau"],
						]],
	[48,"Geluidseffect",[
					[0, "Uit"],
					[1, "Aan"],
					]],
	[49,"Status geluidseffecten",[
					[0, "Uit"],
					[1, "Aan"],
					]],
	[50,"Slaapmodus",[
					[0, "Uit"],
					[1, "Aan"],
					]],
	[51,"Modus",[
				[0, "Winter"],
				[1, "Zomer"],
				]],
	[52,"Wifi-temperatuursonde 1"],
	[53,"Wifi-temperatuursonde 2"],
	[54,"Wifi-temperatuursonde 3"],
	[55,"Onbekend"],
	[56,"Set Puffer"],
	[57,"Set Boiler"],
	[58,"Set Gezondheid"], # !==Hydro
	[59,"Retourtemperatuur"],
	[60,"Antivries",[
					[0, "Uit"],
					[1, "Aan"],
					]],
	]