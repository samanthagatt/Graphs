#!/usr/bin/python

friends_1 = {1: [1], 547: [1, 547], 614: [1, 614], 327: [1, 327], 811: [1, 811], 530: [1, 530], 52: [1, 52], 150: [1, 150]}
	
friends_2 = {42: [1, 547, 42], 791: [1, 547, 791], 398: [1, 614, 398], 117: [1, 614, 117], 105: [1, 614, 105], 393: [1, 327, 393], 870: [1, 327, 870], 841: [1, 811, 841], 368: [1, 811, 368], 949: [1, 811, 949], 694: [1, 811, 694], 667: [1, 811, 667], 416: [1, 530, 416], 809: [1, 530, 809], 908: [1, 530, 908], 887: [1, 530, 887], 245: [1, 530, 245], 726: [1, 530, 726], 598: [1, 530, 598], 822: [1, 530, 822], 22: [1, 530, 22], 126: [1, 530, 126], 831: [1, 530, 831], 185: [1, 52, 185], 879: [1, 52, 879], 116: [1, 52, 116], 217: [1, 52, 217], 170: [1, 150, 170], 258: [1, 150, 258], 404: [1, 150, 404], 224: [1, 547, 42, 224], 128: [1, 547, 42, 128], 99: [1, 547, 42, 99], 997: [1, 547, 42, 997], 234: [1, 547, 42, 234], 678: [1, 547, 791, 678], 395: [1, 547, 791, 395], 14: [1, 547, 791, 14], 534: [1, 547, 791, 534], 599: [1, 547, 791, 599], 537: [1, 547, 791, 537], 218: [1, 547, 791, 218], 797: [1, 547, 791, 797], 255: [1, 547, 791, 255], 160: [1, 614, 398, 160], 583: [1, 614, 398, 583], 727: [1, 614, 398, 727], 608: [1, 614, 117, 608], 778: [1, 614, 117, 778], 478: [1, 614, 117, 478], 857: [1, 614, 105, 857], 634: [1, 614, 105, 634], 853: [1, 614, 105, 853], 500: [1, 327, 393, 500], 253: [1, 327, 393, 253], 256: [1, 327, 870, 256], 795: [1, 327, 870, 795], 837: [1, 327, 870, 837], 545: [1, 811, 841, 545], 58: [1, 811, 841, 58], 103: [1, 811, 841, 103], 214: [1, 811, 841, 214], 442: [1, 811, 841, 442], 636: [1, 811, 841, 636], 447: [1, 811, 841, 447], 315: [1, 811, 368, 315], 747: [1, 811, 368, 747], 865: [1, 811, 949, 865], 260: [1, 811, 949, 260], 773: [1, 811, 949, 773], 138: [1, 811, 949, 138], 665: [1, 811, 949, 665], 31: [1, 811, 949, 31], 130: [1, 811, 694, 130], 585: [1, 811, 694, 585], 108: [1, 811, 694, 108], 846: [1, 811, 694, 846], 49: [1, 811, 694, 49], 51: [1, 811, 694, 51], 767: [1, 811, 667, 767], 467: [1, 811, 667, 467], 535: [1, 811, 667, 535], 960: [1, 530, 416, 960], 227: [1, 530, 416, 227], 771: [1, 530, 416, 771], 358: [1, 530, 416, 358], 905: [1, 530, 416, 905], 881: [1, 530, 416, 881], 927: [1, 530, 416, 927], 926: [1, 530, 416, 926], 63: [1, 530, 416, 63], 409: [1, 530, 809, 409], 933: [1, 530, 809, 933], 888: [1, 530, 908, 888], 210: [1, 530, 908, 210], 212: [1, 530, 908, 212], 779: [1, 530, 887, 779], 1000: [1, 530, 887, 1000], 290: [1, 530, 887, 290], 81: [1, 530, 245, 81], 914: [1, 530, 245, 914], 551: [1, 530, 245, 551], 353: [1, 530, 726, 353], 356: [1, 530, 726, 356], 838: [1, 530, 726, 838], 969: [1, 530, 726, 969], 909: [1, 530, 726, 909], 441: [1, 530, 726, 441], 386: [1, 530, 598, 386], 677: [1, 530, 598, 677], 457: [1, 530, 598, 457], 527: [1, 530, 598, 527], 284: [1, 530, 598, 284], 700: [1, 530, 598, 700], 228: [1, 530, 822, 228], 903: [1, 530, 822, 903], 507: [1, 530, 822, 507], 481: [1, 530, 22, 481], 686: [1, 530, 22, 686], 576: [1, 530, 126, 576], 289: [1, 530, 126, 289], 912: [1, 530, 126, 912], 978: [1, 530, 126, 978], 691: [1, 530, 126, 691], 697: [1, 530, 126, 697], 27: [1, 530, 126, 27], 444: [1, 530, 126, 444], 360: [1, 530, 831, 360], 570: [1, 530, 831, 570], 820: [1, 530, 831, 820], 605: [1, 52, 185, 605], 965: [1, 52, 185, 965], 141: [1, 52, 185, 141], 847: [1, 52, 185, 847], 251: [1, 52, 185, 251], 957: [1, 52, 185, 957], 496: [1, 52, 879, 496], 516: [1, 52, 879, 516], 93: [1, 52, 879, 93], 137: [1, 52, 116, 137], 362: [1, 52, 217, 362], 655: [1, 52, 217, 655], 609: [1, 150, 170, 609], 834: [1, 150, 170, 834], 923: [1, 150, 170, 923], 424: [1, 150, 170, 424], 43: [1, 150, 170, 43], 781: [1, 150, 170, 781], 84: [1, 150, 170, 84], 59: [1, 150, 170, 59], 932: [1, 150, 258, 932], 135: [1, 150, 258, 135], 724: [1, 150, 258, 724], 244: [1, 150, 258, 244], 510: [1, 150, 258, 510], 934: [1, 150, 404, 934], 112: [1, 150, 404, 112], 85: [1, 150, 404, 85]}
	
friends_3 = {995: [1, 547, 42, 224, 995], 392: [1, 547, 42, 224, 392], 819: [1, 547, 42, 224, 819], 723: [1, 547, 42, 224, 723], 595: [1, 547, 42, 224, 595], 666: [1, 547, 42, 224, 666], 732: [1, 547, 42, 224, 732], 738: [1, 547, 42, 128, 738], 742: [1, 547, 42, 128, 742], 589: [1, 547, 42, 128, 589], 494: [1, 547, 42, 128, 494], 376: [1, 547, 42, 128, 376], 861: [1, 547, 42, 128, 861], 490: [1, 547, 42, 99, 490], 717: [1, 547, 42, 99, 717], 45: [1, 547, 42, 99, 45], 925: [1, 547, 42, 99, 925], 833: [1, 547, 42, 997, 833], 517: [1, 547, 42, 997, 517], 851: [1, 547, 42, 997, 851], 213: [1, 547, 42, 997, 213], 54: [1, 547, 42, 997, 54], 536: [1, 547, 42, 997, 536], 347: [1, 547, 42, 997, 347], 736: [1, 547, 42, 234, 736], 784: [1, 547, 42, 234, 784], 947: [1, 547, 42, 234, 947], 348: [1, 547, 42, 234, 348], 715: [1, 547, 791, 678, 715], 740: [1, 547, 791, 395, 740], 70: [1, 547, 791, 395, 70], 812: [1, 547, 791, 395, 812], 461: [1, 547, 791, 395, 461], 399: [1, 547, 791, 395, 399], 660: [1, 547, 791, 395, 660], 411: [1, 547, 791, 395, 411], 541: [1, 547, 791, 395, 541], 337: [1, 547, 791, 14, 337], 622: [1, 547, 791, 14, 622], 521: [1, 547, 791, 534, 521], 241: [1, 547, 791, 534, 241], 979: [1, 547, 791, 534, 979], 630: [1, 547, 791, 534, 630], 624: [1, 547, 791, 599, 624], 459: [1, 547, 791, 537, 459], 236: [1, 547, 791, 537, 236], 372: [1, 547, 791, 537, 372], 377: [1, 547, 791, 537, 377], 426: [1, 547, 791, 218, 426], 271: [1, 547, 791, 218, 271], 310: [1, 547, 791, 218, 310], 503: [1, 547, 791, 218, 503], 15: [1, 547, 791, 797, 15], 546: [1, 547, 791, 255, 546], 548: [1, 547, 791, 255, 548], 298: [1, 547, 791, 255, 298], 267: [1, 547, 791, 255, 267], 529: [1, 547, 791, 255, 529], 61: [1, 547, 791, 255, 61], 419: [1, 614, 398, 160, 419], 579: [1, 614, 398, 160, 579], 493: [1, 614, 398, 160, 493], 991: [1, 614, 398, 583, 991], 314: [1, 614, 398, 583, 314], 511: [1, 614, 398, 583, 511], 388: [1, 614, 398, 727, 388], 946: [1, 614, 398, 727, 946], 26: [1, 614, 398, 727, 26], 796: [1, 614, 398, 727, 796], 198: [1, 614, 117, 608, 198], 566: [1, 614, 117, 608, 566], 87: [1, 614, 117, 608, 87], 641: [1, 614, 117, 778, 641], 514: [1, 614, 117, 778, 514], 229: [1, 614, 117, 778, 229], 840: [1, 614, 117, 778, 840], 181: [1, 614, 117, 778, 181], 151: [1, 614, 117, 778, 151], 363: [1, 614, 117, 478, 363], 390: [1, 614, 117, 478, 390], 3: [1, 614, 105, 857, 3], 877: [1, 614, 105, 857, 877], 816: [1, 614, 105, 857, 816], 600: [1, 614, 105, 857, 600], 729: [1, 614, 105, 857, 729], 92: [1, 614, 105, 857, 92], 606: [1, 614, 105, 857, 606], 132: [1, 614, 105, 634, 132], 168: [1, 614, 105, 634, 168], 620: [1, 614, 105, 634, 620], 952: [1, 614, 105, 634, 952], 316: [1, 614, 105, 634, 316], 858: [1, 614, 105, 634, 858], 474: [1, 614, 105, 853, 474], 5: [1, 614, 105, 853, 5], 552: [1, 327, 393, 500, 552], 588: [1, 327, 393, 500, 588], 434: [1, 327, 393, 500, 434], 278: [1, 327, 393, 500, 278], 156: [1, 327, 393, 500, 156], 998: [1, 327, 393, 253, 998], 19: [1, 327, 393, 253, 19], 148: [1, 327, 393, 253, 148], 792: [1, 327, 393, 253, 792], 569: [1, 327, 393, 253, 569], 287: [1, 327, 393, 253, 287], 868: [1, 327, 870, 256, 868], 292: [1, 327, 870, 256, 292], 431: [1, 327, 870, 256, 431], 639: [1, 327, 870, 256, 639], 817: [1, 327, 870, 795, 817], 406: [1, 327, 870, 795, 406], 153: [1, 327, 870, 795, 153], 898: [1, 327, 870, 837, 898], 146: [1, 327, 870, 837, 146], 122: [1, 327, 870, 837, 122], 556: [1, 811, 841, 545, 556], 763: [1, 811, 841, 545, 763], 281: [1, 811, 841, 58, 281], 706: [1, 811, 841, 103, 706], 652: [1, 811, 841, 103, 652], 300: [1, 811, 841, 103, 300], 495: [1, 811, 841, 103, 495], 992: [1, 811, 841, 214, 992], 391: [1, 811, 841, 214, 391], 9: [1, 811, 841, 214, 9], 394: [1, 811, 841, 214, 394], 334: [1, 811, 841, 214, 334], 693: [1, 811, 841, 214, 693], 711: [1, 811, 841, 442, 711], 689: [1, 811, 841, 442, 689], 753: [1, 811, 841, 442, 753], 408: [1, 811, 841, 442, 408], 526: [1, 811, 841, 636, 526], 917: [1, 811, 841, 636, 917], 769: [1, 811, 841, 447, 769], 540: [1, 811, 841, 447, 540], 389: [1, 811, 368, 315, 389], 264: [1, 811, 368, 315, 264], 169: [1, 811, 368, 315, 169], 24: [1, 811, 368, 315, 24], 62: [1, 811, 368, 747, 62], 674: [1, 811, 949, 865, 674], 707: [1, 811, 949, 865, 707], 520: [1, 811, 949, 865, 520], 852: [1, 811, 949, 865, 852], 246: [1, 811, 949, 865, 246], 994: [1, 811, 949, 260, 994], 261: [1, 811, 949, 260, 261], 604: [1, 811, 949, 260, 604], 381: [1, 811, 949, 260, 381], 587: [1, 811, 949, 773, 587], 848: [1, 811, 949, 773, 848], 854: [1, 811, 949, 773, 854], 189: [1, 811, 949, 773, 189], 807: [1, 811, 949, 138, 807], 553: [1, 811, 949, 138, 553], 405: [1, 811, 949, 138, 405], 744: [1, 811, 949, 665, 744], 533: [1, 811, 949, 665, 533], 961: [1, 811, 949, 31, 961], 573: [1, 811, 949, 31, 573], 335: [1, 811, 949, 31, 335], 528: [1, 811, 949, 31, 528], 317: [1, 811, 949, 31, 317], 222: [1, 811, 949, 31, 222], 352: [1, 811, 694, 130, 352], 326: [1, 811, 694, 130, 326], 430: [1, 811, 694, 130, 430], 448: [1, 811, 694, 585, 448], 66: [1, 811, 694, 585, 66], 798: [1, 811, 694, 585, 798], 69: [1, 811, 694, 108, 69], 777: [1, 811, 694, 108, 777], 690: [1, 811, 694, 108, 690], 757: [1, 811, 694, 108, 757], 120: [1, 811, 694, 108, 120], 986: [1, 811, 694, 108, 986], 94: [1, 811, 694, 108, 94], 681: [1, 811, 694, 846, 681], 387: [1, 811, 694, 49, 387], 484: [1, 811, 694, 49, 484], 13: [1, 811, 694, 49, 13], 987: [1, 811, 694, 49, 987], 581: [1, 811, 694, 51, 581], 134: [1, 811, 694, 51, 134], 432: [1, 811, 694, 51, 432], 291: [1, 811, 667, 767, 291], 645: [1, 811, 667, 767, 645], 458: [1, 811, 667, 767, 458], 208: [1, 811, 667, 767, 208], 786: [1, 811, 667, 767, 786], 850: [1, 811, 667, 767, 850], 414: [1, 811, 667, 767, 414], 219: [1, 811, 667, 467, 219], 336: [1, 811, 667, 467, 336], 211: [1, 811, 667, 467, 211], 487: [1, 811, 667, 535, 487], 106: [1, 811, 667, 535, 106], 304: [1, 811, 667, 535, 304], 564: [1, 811, 667, 535, 564], 959: [1, 811, 667, 535, 959], 223: [1, 811, 667, 535, 223], 967: [1, 530, 416, 960, 967], 680: [1, 530, 416, 960, 680], 843: [1, 530, 416, 960, 843], 653: [1, 530, 416, 960, 653], 821: [1, 530, 416, 960, 821], 662: [1, 530, 416, 960, 662], 637: [1, 530, 416, 960, 637], 499: [1, 530, 416, 227, 499], 549: [1, 530, 416, 227, 549], 750: [1, 530, 416, 227, 750], 644: [1, 530, 416, 771, 644], 616: [1, 530, 416, 771, 616], 237: [1, 530, 416, 771, 237], 790: [1, 530, 416, 771, 790], 522: [1, 530, 416, 358, 522], 974: [1, 530, 416, 358, 974], 760: [1, 530, 416, 358, 760], 351: [1, 530, 416, 358, 351], 776: [1, 530, 416, 905, 776], 754: [1, 530, 416, 905, 754], 531: [1, 530, 416, 905, 531], 647: [1, 530, 416, 881, 647], 714: [1, 530, 416, 881, 714], 129: [1, 530, 416, 927, 129], 421: [1, 530, 416, 927, 421], 977: [1, 530, 416, 927, 977], 574: [1, 530, 416, 927, 574], 867: [1, 530, 416, 926, 867], 330: [1, 530, 416, 926, 330], 215: [1, 530, 416, 926, 215], 975: [1, 530, 416, 63, 975], 498: [1, 530, 416, 63, 498], 692: [1, 530, 416, 63, 692], 664: [1, 530, 416, 63, 664], 675: [1, 530, 809, 409, 675], 72: [1, 530, 809, 409, 72], 180: [1, 530, 809, 933, 180], 320: [1, 530, 908, 888, 320], 7: [1, 530, 908, 210, 7], 202: [1, 530, 908, 210, 202], 823: [1, 530, 908, 210, 823], 849: [1, 530, 908, 212, 849], 485: [1, 530, 887, 779, 485], 695: [1, 530, 887, 779, 695], 302: [1, 530, 887, 779, 302], 469: [1, 530, 887, 779, 469], 127: [1, 530, 887, 779, 127], 543: [1, 530, 887, 779, 543], 67: [1, 530, 887, 1000, 67], 964: [1, 530, 887, 1000, 964], 826: [1, 530, 887, 1000, 826], 95: [1, 530, 887, 1000, 95], 293: [1, 530, 887, 290, 293], 464: [1, 530, 887, 290, 464], 79: [1, 530, 887, 290, 79], 299: [1, 530, 245, 81, 299], 248: [1, 530, 245, 81, 248], 669: [1, 530, 245, 81, 669], 578: [1, 530, 245, 914, 578], 57: [1, 530, 245, 914, 57], 280: [1, 530, 245, 551, 280], 338: [1, 530, 245, 551, 338], 346: [1, 530, 245, 551, 346], 802: [1, 530, 726, 356, 802], 6: [1, 530, 726, 356, 6], 157: [1, 530, 726, 356, 157], 97: [1, 530, 726, 838, 97], 162: [1, 530, 726, 838, 162], 590: [1, 530, 726, 838, 590], 559: [1, 530, 726, 838, 559], 321: [1, 530, 726, 969, 321], 41: [1, 530, 726, 909, 41], 333: [1, 530, 726, 909, 333], 272: [1, 530, 726, 909, 272], 53: [1, 530, 726, 909, 53], 101: [1, 530, 726, 441, 101], 283: [1, 530, 598, 386, 283], 78: [1, 530, 598, 677, 78], 502: [1, 530, 598, 677, 502], 186: [1, 530, 598, 677, 186], 670: [1, 530, 598, 677, 670], 713: [1, 530, 598, 457, 713], 973: [1, 530, 598, 457, 973], 8: [1, 530, 598, 527, 8], 30: [1, 530, 598, 527, 30], 886: [1, 530, 598, 284, 886], 400: [1, 530, 598, 700, 400], 497: [1, 530, 598, 700, 497], 183: [1, 530, 598, 700, 183], 319: [1, 530, 598, 700, 319], 295: [1, 530, 822, 228, 295], 902: [1, 530, 822, 903, 902], 422: [1, 530, 822, 903, 422], 331: [1, 530, 822, 507, 331], 719: [1, 530, 822, 507, 719], 953: [1, 530, 822, 507, 953], 167: [1, 530, 22, 481, 167], 380: [1, 530, 22, 481, 380], 591: [1, 530, 22, 686, 591], 274: [1, 530, 22, 686, 274], 696: [1, 530, 22, 686, 696], 28: [1, 530, 126, 576, 28], 462: [1, 530, 126, 576, 462], 544: [1, 530, 126, 289, 544], 803: [1, 530, 126, 289, 803], 423: [1, 530, 126, 289, 423], 525: [1, 530, 126, 289, 525], 916: [1, 530, 126, 289, 916], 286: [1, 530, 126, 289, 286], 193: [1, 530, 126, 912, 193], 810: [1, 530, 126, 912, 810], 883: [1, 530, 126, 912, 883], 990: [1, 530, 126, 912, 990], 483: [1, 530, 126, 691, 483], 98: [1, 530, 126, 697, 98], 200: [1, 530, 126, 697, 200], 89: [1, 530, 126, 697, 89], 159: [1, 530, 126, 697, 159], 249: [1, 530, 126, 27, 249], 188: [1, 530, 126, 27, 188], 427: [1, 530, 126, 444, 427], 82: [1, 530, 831, 360, 82], 309: [1, 530, 831, 360, 309], 633: [1, 530, 831, 360, 633], 782: [1, 530, 831, 570, 782], 443: [1, 530, 831, 570, 443], 735: [1, 530, 831, 570, 735], 235: [1, 530, 831, 820, 235], 983: [1, 530, 831, 820, 983], 855: [1, 530, 831, 820, 855], 701: [1, 530, 831, 820, 701], 56: [1, 52, 185, 605, 56], 412: [1, 52, 185, 605, 412], 378: [1, 52, 185, 605, 378], 192: [1, 52, 185, 965, 192], 361: [1, 52, 185, 965, 361], 944: [1, 52, 185, 965, 944], 766: [1, 52, 185, 965, 766], 513: [1, 52, 185, 141, 513], 962: [1, 52, 185, 141, 962], 429: [1, 52, 185, 141, 429], 305: [1, 52, 185, 141, 305], 789: [1, 52, 185, 847, 789], 438: [1, 52, 185, 847, 438], 725: [1, 52, 185, 251, 725], 939: [1, 52, 185, 957, 939], 901: [1, 52, 185, 957, 901], 739: [1, 52, 185, 957, 739], 50: [1, 52, 879, 496, 50], 659: [1, 52, 879, 496, 659], 163: [1, 52, 879, 516, 163], 463: [1, 52, 879, 516, 463], 86: [1, 52, 879, 516, 86], 889: [1, 52, 879, 516, 889], 571: [1, 52, 879, 516, 571], 672: [1, 52, 879, 93, 672], 813: [1, 52, 879, 93, 813], 17: [1, 52, 879, 93, 17], 632: [1, 52, 879, 93, 632], 154: [1, 52, 879, 93, 154], 709: [1, 52, 116, 137, 709], 743: [1, 52, 116, 137, 743], 231: [1, 52, 116, 137, 231], 301: [1, 52, 116, 137, 301], 646: [1, 52, 217, 362, 646], 712: [1, 52, 217, 362, 712], 238: [1, 52, 217, 362, 238], 473: [1, 52, 217, 362, 473], 382: [1, 52, 217, 362, 382], 225: [1, 52, 217, 655, 225], 657: [1, 52, 217, 655, 657], 259: [1, 150, 170, 609, 259], 805: [1, 150, 170, 609, 805], 365: [1, 150, 170, 609, 365], 982: [1, 150, 170, 834, 982], 435: [1, 150, 170, 923, 435], 23: [1, 150, 170, 923, 23], 679: [1, 150, 170, 424, 679], 187: [1, 150, 170, 43, 187], 354: [1, 150, 170, 43, 354], 560: [1, 150, 170, 781, 560], 203: [1, 150, 170, 781, 203], 554: [1, 150, 170, 84, 554], 615: [1, 150, 170, 84, 615], 907: [1, 150, 170, 59, 907], 906: [1, 150, 170, 59, 906], 610: [1, 150, 258, 932, 610], 582: [1, 150, 258, 932, 582], 761: [1, 150, 258, 135, 761], 121: [1, 150, 258, 724, 121], 472: [1, 150, 258, 244, 472], 196: [1, 150, 258, 510, 196], 619: [1, 150, 258, 510, 619], 958: [1, 150, 258, 510, 958], 872: [1, 150, 404, 934, 872], 12: [1, 150, 404, 934, 12]}
	
friends_4 = {774: [1, 150, 404, 934, 774], 676: [1, 150, 404, 112, 676], 580: [1, 150, 404, 112, 580], 279: [1, 150, 404, 112, 279], 572: [1, 150, 404, 112, 572], 577: [1, 150, 404, 85, 577], 107: [1, 150, 404, 85, 107], 915: [1, 150, 404, 85, 915], 124: [1, 547, 42, 224, 995, 124], 340: [1, 547, 42, 224, 995, 340], 332: [1, 547, 42, 224, 392, 332], 866: [1, 547, 42, 224, 723, 866], 230: [1, 547, 42, 224, 723, 230], 48: [1, 547, 42, 224, 723, 48], 16: [1, 547, 42, 224, 723, 16], 631: [1, 547, 42, 224, 723, 631], 39: [1, 547, 42, 224, 595, 39], 220: [1, 547, 42, 224, 666, 220], 919: [1, 547, 42, 224, 666, 919], 935: [1, 547, 42, 224, 732, 935], 891: [1, 547, 42, 128, 738, 891], 268: [1, 547, 42, 128, 738, 268], 366: [1, 547, 42, 128, 738, 366], 18: [1, 547, 42, 128, 738, 18], 602: [1, 547, 42, 128, 738, 602], 648: [1, 547, 42, 128, 742, 648], 592: [1, 547, 42, 128, 742, 592], 996: [1, 547, 42, 128, 589, 996], 650: [1, 547, 42, 128, 589, 650], 864: [1, 547, 42, 128, 376, 864], 161: [1, 547, 42, 128, 861, 161], 801: [1, 547, 42, 128, 861, 801], 936: [1, 547, 42, 99, 490, 936], 425: [1, 547, 42, 99, 490, 425], 60: [1, 547, 42, 99, 490, 60], 702: [1, 547, 42, 99, 717, 702], 285: [1, 547, 42, 99, 45, 285], 190: [1, 547, 42, 99, 45, 190], 454: [1, 547, 42, 99, 925, 454], 384: [1, 547, 42, 997, 833, 384], 68: [1, 547, 42, 997, 833, 68], 785: [1, 547, 42, 997, 833, 785], 940: [1, 547, 42, 997, 517, 940], 440: [1, 547, 42, 997, 517, 440], 144: [1, 547, 42, 997, 213, 144], 184: [1, 547, 42, 997, 213, 184], 563: [1, 547, 42, 997, 54, 563], 800: [1, 547, 42, 997, 536, 800], 74: [1, 547, 42, 997, 536, 74], 250: [1, 547, 42, 997, 536, 250], 745: [1, 547, 42, 997, 347, 745], 523: [1, 547, 42, 997, 347, 523], 276: [1, 547, 42, 997, 347, 276], 468: [1, 547, 42, 234, 736, 468], 501: [1, 547, 42, 234, 736, 501], 839: [1, 547, 42, 234, 784, 839], 453: [1, 547, 42, 234, 947, 453], 370: [1, 547, 42, 234, 348, 370], 21: [1, 547, 42, 234, 348, 21], 550: [1, 547, 791, 678, 715, 550], 518: [1, 547, 791, 395, 70, 518], 878: [1, 547, 791, 395, 70, 878], 623: [1, 547, 791, 395, 70, 623], 844: [1, 547, 791, 395, 812, 844], 407: [1, 547, 791, 395, 461, 407], 937: [1, 547, 791, 395, 399, 937], 930: [1, 547, 791, 395, 660, 930], 772: [1, 547, 791, 395, 660, 772], 143: [1, 547, 791, 395, 660, 143], 341: [1, 547, 791, 395, 411, 341], 603: [1, 547, 791, 395, 411, 603], 111: [1, 547, 791, 395, 541, 111], 34: [1, 547, 791, 14, 337, 34], 344: [1, 547, 791, 14, 622, 344], 721: [1, 547, 791, 534, 521, 721], 25: [1, 547, 791, 534, 521, 25], 492: [1, 547, 791, 534, 979, 492], 656: [1, 547, 791, 534, 979, 656], 479: [1, 547, 791, 534, 979, 479], 83: [1, 547, 791, 537, 459, 83], 954: [1, 547, 791, 537, 459, 954], 900: [1, 547, 791, 537, 236, 900], 950: [1, 547, 791, 537, 236, 950], 456: [1, 547, 791, 537, 372, 456], 596: [1, 547, 791, 537, 372, 596], 357: [1, 547, 791, 218, 426, 357], 663: [1, 547, 791, 218, 426, 663], 770: [1, 547, 791, 218, 271, 770], 206: [1, 547, 791, 218, 271, 206], 506: [1, 547, 791, 218, 310, 506], 445: [1, 547, 791, 218, 310, 445], 65: [1, 547, 791, 797, 15, 65], 621: [1, 547, 791, 255, 546, 621], 275: [1, 547, 791, 255, 546, 275], 104: [1, 547, 791, 255, 548, 104], 824: [1, 547, 791, 255, 548, 824], 197: [1, 547, 791, 255, 298, 197], 460: [1, 547, 791, 255, 298, 460], 539: [1, 547, 791, 255, 298, 539], 705: [1, 547, 791, 255, 267, 705], 265: [1, 547, 791, 255, 267, 265], 971: [1, 547, 791, 255, 267, 971], 885: [1, 547, 791, 255, 267, 885], 860: [1, 547, 791, 255, 267, 860], 195: [1, 547, 791, 255, 529, 195], 240: [1, 547, 791, 255, 529, 240], 759: [1, 547, 791, 255, 61, 759], 568: [1, 547, 791, 255, 61, 568], 345: [1, 547, 791, 255, 61, 345], 131: [1, 614, 398, 160, 419, 131], 374: [1, 614, 398, 160, 419, 374], 10: [1, 614, 398, 160, 579, 10], 207: [1, 614, 398, 160, 579, 207], 90: [1, 614, 398, 160, 493, 90], 470: [1, 614, 398, 583, 991, 470], 874: [1, 614, 398, 583, 314, 874], 475: [1, 614, 398, 583, 511, 475], 243: [1, 614, 398, 727, 388, 243], 480: [1, 614, 398, 727, 26, 480], 273: [1, 614, 398, 727, 26, 273], 565: [1, 614, 398, 727, 26, 565], 842: [1, 614, 398, 727, 796, 842], 77: [1, 614, 117, 608, 198, 77], 625: [1, 614, 117, 608, 198, 625], 118: [1, 614, 117, 608, 198, 118], 894: [1, 614, 117, 608, 198, 894], 171: [1, 614, 117, 608, 566, 171], 342: [1, 614, 117, 608, 566, 342], 519: [1, 614, 117, 608, 87, 519], 152: [1, 614, 117, 608, 87, 152], 756: [1, 614, 117, 778, 641, 756], 642: [1, 614, 117, 778, 229, 642], 618: [1, 614, 117, 778, 229, 618], 413: [1, 614, 117, 778, 229, 413], 640: [1, 614, 117, 778, 151, 640], 869: [1, 614, 117, 778, 151, 869], 661: [1, 614, 117, 778, 151, 661], 918: [1, 614, 117, 778, 151, 918], 482: [1, 614, 117, 478, 363, 482], 46: [1, 614, 117, 478, 363, 46], 836: [1, 614, 117, 478, 390, 836], 359: [1, 614, 117, 478, 390, 359], 114: [1, 614, 117, 478, 390, 114], 415: [1, 614, 117, 478, 390, 415], 142: [1, 614, 105, 857, 3, 142], 437: [1, 614, 105, 857, 3, 437], 355: [1, 614, 105, 857, 877, 355], 751: [1, 614, 105, 857, 877, 751], 897: [1, 614, 105, 857, 600, 897], 780: [1, 614, 105, 857, 729, 780], 11: [1, 614, 105, 857, 729, 11], 174: [1, 614, 105, 857, 729, 174], 247: [1, 614, 105, 857, 729, 247], 856: [1, 614, 105, 857, 729, 856], 47: [1, 614, 105, 857, 92, 47], 311: [1, 614, 105, 857, 92, 311], 673: [1, 614, 105, 634, 132, 673], 963: [1, 614, 105, 634, 168, 963], 139: [1, 614, 105, 634, 168, 139], 270: [1, 614, 105, 634, 168, 270], 876: [1, 614, 105, 634, 168, 876], 455: [1, 614, 105, 634, 620, 455], 875: [1, 614, 105, 634, 952, 875], 718: [1, 614, 105, 634, 952, 718], 145: [1, 614, 105, 634, 952, 145], 970: [1, 614, 105, 634, 858, 970], 830: [1, 614, 105, 634, 858, 830], 133: [1, 614, 105, 853, 474, 133], 752: [1, 614, 105, 853, 474, 752], 313: [1, 614, 105, 853, 474, 313], 733: [1, 614, 105, 853, 474, 733], 401: [1, 614, 105, 853, 5, 401], 88: [1, 614, 105, 853, 5, 88], 594: [1, 327, 393, 500, 552, 594], 658: [1, 327, 393, 500, 434, 658], 765: [1, 327, 393, 500, 278, 765], 100: [1, 327, 393, 500, 156, 100], 136: [1, 327, 393, 500, 156, 136], 737: [1, 327, 393, 253, 998, 737], 741: [1, 327, 393, 253, 998, 741], 175: [1, 327, 393, 253, 998, 175], 943: [1, 327, 393, 253, 148, 943], 71: [1, 327, 393, 253, 792, 71], 364: [1, 327, 393, 253, 792, 364], 452: [1, 327, 393, 253, 287, 452], 375: [1, 327, 870, 256, 292, 375], 252: [1, 327, 870, 256, 292, 252], 755: [1, 327, 870, 256, 431, 755], 683: [1, 327, 870, 795, 817, 683], 828: [1, 327, 870, 795, 153, 828], 586: [1, 327, 870, 795, 153, 586], 140: [1, 327, 870, 795, 153, 140], 205: [1, 327, 870, 837, 146, 205], 179: [1, 327, 870, 837, 146, 179], 226: [1, 327, 870, 837, 122, 226], 303: [1, 327, 870, 837, 122, 303], 113: [1, 811, 841, 545, 763, 113], 601: [1, 811, 841, 103, 652, 601], 37: [1, 811, 841, 103, 300, 37], 232: [1, 811, 841, 214, 992, 232], 611: [1, 811, 841, 214, 391, 611], 629: [1, 811, 841, 214, 391, 629], 734: [1, 811, 841, 214, 391, 734], 515: [1, 811, 841, 214, 9, 515], 863: [1, 811, 841, 214, 9, 863], 509: [1, 811, 841, 214, 9, 509], 383: [1, 811, 841, 214, 9, 383], 892: [1, 811, 841, 214, 394, 892], 829: [1, 811, 841, 214, 394, 829], 941: [1, 811, 841, 214, 334, 941], 80: [1, 811, 841, 214, 334, 80], 542: [1, 811, 841, 214, 334, 542], 710: [1, 811, 841, 214, 693, 710], 748: [1, 811, 841, 214, 693, 748], 793: [1, 811, 841, 636, 526, 793], 708: [1, 811, 841, 636, 526, 708], 269: [1, 811, 841, 636, 526, 269], 125: [1, 811, 841, 447, 769, 125], 981: [1, 811, 841, 447, 540, 981], 477: [1, 811, 841, 447, 540, 477], 749: [1, 811, 368, 315, 389, 749], 191: [1, 811, 368, 315, 264, 191], 575: [1, 811, 368, 315, 24, 575], 20: [1, 811, 368, 747, 62, 20], 418: [1, 811, 949, 865, 674, 418], 988: [1, 811, 949, 865, 674, 988], 38: [1, 811, 949, 865, 707, 38], 966: [1, 811, 949, 865, 520, 966], 654: [1, 811, 949, 865, 852, 654], 177: [1, 811, 949, 260, 381, 177], 123: [1, 811, 949, 260, 381, 123], 704: [1, 811, 949, 773, 587, 704], 165: [1, 811, 949, 773, 587, 165], 297: [1, 811, 949, 773, 587, 297], 322: [1, 811, 949, 773, 848, 322], 698: [1, 811, 949, 773, 189, 698], 896: [1, 811, 949, 138, 807, 896], 201: [1, 811, 949, 138, 553, 201], 367: [1, 811, 949, 138, 553, 367], 567: [1, 811, 949, 138, 553, 567], 699: [1, 811, 949, 138, 553, 699], 32: [1, 811, 949, 138, 405, 32], 164: [1, 811, 949, 665, 533, 164], 76: [1, 811, 949, 31, 961, 76], 873: [1, 811, 949, 31, 335, 873], 428: [1, 811, 949, 31, 335, 428], 929: [1, 811, 949, 31, 317, 929], 373: [1, 811, 949, 31, 222, 373], 385: [1, 811, 694, 130, 326, 385], 562: [1, 811, 694, 130, 326, 562], 257: [1, 811, 694, 130, 430, 257], 488: [1, 811, 694, 130, 430, 488], 685: [1, 811, 694, 130, 430, 685], 508: [1, 811, 694, 130, 430, 508], 471: [1, 811, 694, 585, 448, 471], 254: [1, 811, 694, 585, 66, 254], 904: [1, 811, 694, 108, 69, 904], 524: [1, 811, 694, 108, 69, 524], 239: [1, 811, 694, 108, 69, 239], 890: [1, 811, 694, 108, 69, 890], 746: [1, 811, 694, 108, 777, 746], 91: [1, 811, 694, 108, 777, 91], 396: [1, 811, 694, 108, 690, 396], 956: [1, 811, 694, 108, 690, 956], 149: [1, 811, 694, 108, 120, 149], 2: [1, 811, 694, 108, 986, 2], 688: [1, 811, 694, 108, 986, 688], 410: [1, 811, 694, 108, 986, 410], 859: [1, 811, 694, 108, 986, 859], 433: [1, 811, 694, 108, 94, 433], 827: [1, 811, 694, 846, 681, 827], 989: [1, 811, 694, 846, 681, 989], 417: [1, 811, 694, 49, 387, 417], 307: [1, 811, 694, 49, 387, 307], 794: [1, 811, 694, 49, 987, 794], 266: [1, 811, 694, 51, 432, 266], 306: [1, 811, 667, 767, 208, 306], 182: [1, 811, 667, 767, 208, 182], 466: [1, 811, 667, 767, 786, 466], 871: [1, 811, 667, 767, 414, 871], 109: [1, 811, 667, 767, 414, 109], 628: [1, 811, 667, 767, 414, 628], 555: [1, 811, 667, 467, 219, 555], 486: [1, 811, 667, 535, 106, 486], 768: [1, 811, 667, 535, 304, 768], 64: [1, 811, 667, 535, 304, 64], 36: [1, 811, 667, 535, 304, 36], 371: [1, 811, 667, 535, 564, 371], 985: [1, 811, 667, 535, 564, 985], 815: [1, 811, 667, 535, 959, 815], 643: [1, 811, 667, 535, 223, 643], 968: [1, 811, 667, 535, 223, 968], 818: [1, 811, 667, 535, 223, 818], 955: [1, 530, 416, 960, 967, 955], 682: [1, 530, 416, 960, 967, 682], 671: [1, 530, 416, 771, 644, 671], 720: [1, 530, 416, 358, 760, 720], 176: [1, 530, 416, 905, 754, 176], 35: [1, 530, 416, 927, 977, 35], 504: [1, 530, 416, 927, 574, 504], 627: [1, 530, 416, 926, 867, 627], 155: [1, 530, 416, 926, 867, 155], 764: [1, 530, 416, 63, 975, 764], 921: [1, 530, 416, 63, 975, 921], 913: [1, 530, 809, 409, 72, 913], 29: [1, 530, 809, 409, 72, 29], 557: [1, 530, 908, 888, 320, 557], 825: [1, 530, 908, 210, 823, 825], 558: [1, 530, 887, 779, 485, 558], 984: [1, 530, 887, 779, 485, 984], 505: [1, 530, 887, 779, 302, 505], 476: [1, 530, 887, 779, 302, 476], 716: [1, 530, 887, 779, 543, 716], 788: [1, 530, 887, 779, 543, 788], 277: [1, 530, 887, 779, 543, 277], 451: [1, 530, 887, 1000, 67, 451], 758: [1, 530, 887, 1000, 964, 758], 318: [1, 530, 887, 1000, 964, 318], 323: [1, 530, 887, 1000, 826, 323], 638: [1, 530, 887, 1000, 95, 638], 951: [1, 530, 887, 290, 464, 951], 512: [1, 530, 245, 81, 248, 512], 931: [1, 530, 245, 81, 248, 931], 350: [1, 530, 245, 81, 669, 350], 465: [1, 530, 245, 914, 57, 465], 262: [1, 530, 245, 551, 280, 262], 617: [1, 530, 245, 551, 280, 617], 403: [1, 530, 245, 551, 280, 403], 687: [1, 530, 726, 838, 590, 687], 938: [1, 530, 726, 909, 41, 938], 450: [1, 530, 726, 909, 333, 450], 339: [1, 530, 726, 909, 333, 339], 928: [1, 530, 726, 909, 53, 928], 835: [1, 530, 598, 527, 30, 835], 783: [1, 530, 598, 284, 886, 783], 328: [1, 530, 598, 700, 319, 328], 612: [1, 530, 822, 903, 422, 612], 845: [1, 530, 822, 903, 422, 845], 329: [1, 530, 22, 481, 167, 329], 282: [1, 530, 22, 686, 591, 282], 263: [1, 530, 22, 686, 696, 263], 369: [1, 530, 126, 576, 462, 369], 33: [1, 530, 126, 912, 193, 33], 862: [1, 530, 126, 691, 483, 862], 613: [1, 530, 126, 27, 188, 613], 55: [1, 530, 126, 27, 188, 55], 436: [1, 530, 831, 360, 309, 436], 204: [1, 530, 831, 360, 633, 204], 651: [1, 530, 831, 360, 633, 651], 775: [1, 530, 831, 570, 782, 775], 880: [1, 530, 831, 570, 443, 880], 489: [1, 52, 185, 605, 378, 489], 808: [1, 52, 185, 965, 766, 808], 402: [1, 52, 185, 141, 429, 402], 882: [1, 52, 185, 141, 305, 882], 166: [1, 52, 185, 847, 438, 166], 379: [1, 52, 185, 957, 901, 379], 420: [1, 52, 185, 957, 739, 420], 449: [1, 52, 879, 496, 659, 449], 491: [1, 52, 879, 516, 889, 491], 804: [1, 52, 879, 93, 813, 804], 922: [1, 52, 879, 93, 813, 922], 999: [1, 52, 879, 93, 154, 999], 199: [1, 52, 116, 137, 743, 199], 814: [1, 52, 116, 137, 301, 814], 296: [1, 150, 170, 834, 982, 296], 684: [1, 150, 170, 43, 187, 684], 787: [1, 150, 170, 781, 560, 787], 294: [1, 150, 170, 84, 554, 294], 312: [1, 150, 258, 135, 761, 312], 762: [1, 150, 258, 244, 472, 762], 924: [1, 150, 258, 510, 619, 924], 895: [1, 150, 258, 510, 958, 895], 538: [1, 150, 404, 934, 872, 538], 147: [1, 150, 404, 112, 279, 147]}

friends_5 = {730: [1, 547, 42, 224, 666, 919, 730], 731: [1, 547, 42, 128, 738, 18, 731], 209: [1, 547, 42, 128, 742, 648, 209], 722: [1, 547, 42, 997, 833, 384, 722], 325: [1, 547, 42, 997, 213, 184, 325], 635: [1, 547, 42, 997, 54, 563, 635], 728: [1, 547, 42, 997, 347, 276, 728], 308: [1, 547, 42, 234, 736, 468, 308], 96: [1, 547, 791, 678, 715, 550, 96], 884: [1, 547, 791, 678, 715, 550, 884], 910: [1, 547, 791, 395, 70, 623, 910], 242: [1, 547, 791, 395, 461, 407, 242], 115: [1, 547, 791, 395, 461, 407, 115], 948: [1, 547, 791, 395, 660, 930, 948], 920: [1, 547, 791, 14, 337, 34, 920], 178: [1, 547, 791, 14, 622, 344, 178], 972: [1, 547, 791, 534, 521, 721, 972], 980: [1, 547, 791, 537, 459, 83, 980], 597: [1, 547, 791, 537, 459, 83, 597], 233: [1, 547, 791, 218, 271, 770, 233], 561: [1, 547, 791, 218, 271, 206, 561], 945: [1, 547, 791, 218, 310, 506, 945], 216: [1, 547, 791, 797, 15, 65, 216], 172: [1, 547, 791, 255, 548, 824, 172], 110: [1, 547, 791, 255, 548, 824, 110], 158: [1, 547, 791, 255, 267, 860, 158], 288: [1, 614, 398, 160, 419, 131, 288], 173: [1, 614, 398, 160, 419, 374, 173], 899: [1, 614, 398, 160, 579, 10, 899], 976: [1, 614, 117, 608, 566, 342, 976], 668: [1, 614, 117, 778, 229, 413, 668], 832: [1, 614, 117, 778, 151, 640, 832], 324: [1, 614, 117, 478, 390, 114, 324], 649: [1, 614, 105, 857, 600, 897, 649], 397: [1, 614, 105, 853, 5, 88, 397], 221: [1, 811, 368, 315, 389, 749, 221], 911: [1, 811, 949, 260, 381, 177, 911], 446: [1, 811, 949, 138, 405, 32, 446], 349: [1, 811, 694, 130, 430, 257, 349], 439: [1, 811, 694, 585, 448, 471, 439], 102: [1, 811, 667, 767, 208, 182, 102], 194: [1, 530, 887, 1000, 964, 758, 194], 584: [1, 530, 726, 909, 41, 938, 584]}
	
friends_6 = {799: [1, 547, 791, 218, 271, 206, 561, 799], 942: [1, 547, 791, 797, 15, 65, 216, 942], 993: [1, 811, 694, 130, 430, 257, 349, 993]}
	
one = len(friends_1) * 1
two = len(friends_2) * 2
three = len(friends_3) * 3
four = len(friends_4) * 4
five = len(friends_5) * 5
six = len(friends_6) * 6
	
total = one + two + three + four + five + six
average = total / 1000

print(average)  ## 3.254