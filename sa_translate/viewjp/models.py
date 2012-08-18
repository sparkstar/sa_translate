from django.db import models

# Create your models here.
hash = {
'7b2800297d' : '00',
'7b2801297d' : '01',
'7b2802297d' : '02',
'7b2803297d' : '03',
'7b2804297d' : '04',
'7b2805297d' : '05',
'7b2806297d' : '06',
'7b2807297d' : '07',
'7b2808297d' : '08',
'7b2809297d' : '09',
'7b280a297d' : '0a',
'7b280b297d' : '0b',
'7b280c297d' : '0c',
'7b280d297d' : '0d',
'7b280e297d' : '0e',
'7b280f297d' : '0f',
'7b2810297d' : '10',
'7b2811297d' : '11',
'7b2812297d' : '12',
'7b2813297d' : '13',
'7b2814297d' : '14',
'7b2815297d' : '15',
'7b2816297d' : '16',
'7b2817297d' : '17',
'7b2818297d' : '18',
'7b2819297d' : '19',
'7b281a297d' : '1a',
'7b281b297d' : '1b',
'7b281c297d' : '1c',
'7b281d297d' : '1d',
'7b281e297d' : '1e',
'7b281f297d' : '1f',
'7b2820297d' : '20',
'7b2821297d' : '21',
'7b2822297d' : '22',
'7b2823297d' : '23',
'7b2824297d' : '24',
'7b2825297d' : '25',
'7b2826297d' : '26',
'7b2827297d' : '27',
'7b2828297d' : '28',
'7b2829297d' : '29',
'7b282a297d' : '2a',
'7b282b297d' : '2b',
'7b282c297d' : '2c',
'7b282d297d' : '2d',
'7b282e297d' : '2e',
'7b282f297d' : '2f',
'7b2830297d' : '00',
'7b2831297d' : '01',
'7b2832297d' : '02',
'7b2833297d' : '03',
'7b2834297d' : '04',
'7b2835297d' : '05',
'7b2836297d' : '06',
'7b2837297d' : '07',
'7b2838297d' : '08',
'7b2839297d' : '09',
'7b283a297d' : '3a',
'7b283b297d' : '3b',
'7b283c297d' : '3c',
'7b283d297d' : '3d',
'7b283e297d' : '3e',
'7b283f297d' : '3f',
'7b2840297d' : '40',
'7b2841297d' : '0a',
'7b2842297d' : '0b',
'7b2843297d' : '0c',
'7b2844297d' : '0d',
'7b2845297d' : '0e',
'7b2846297d' : '0f',
'7b2847297d' : 'f92e',
'7b2848297d' : 'f92f',
'7b2849297d' : 'f932',
'7b284a297d' : 'f933',
'7b284b297d' : 'f942',
'7b284c297d' : 'f943',
'7b284d297d' : 'f944',
'7b284e297d' : 'f945',
'7b284f297d' : 'f946',
'7b2850297d' : 'f947',
'7b2851297d' : 'f948',
'7b2852297d' : 'f949',
'7b2853297d' : 'f936',
'7b2854297d' : 'f937',
'7b2855297d' : 'f938',
'7b2856297d' : 'f939',
'7b2857297d' : 'f93a',
'7b2858297d' : 'f93b',
'7b2859297d' : 'f93c',
'7b285a297d' : 'f93d',
'7b285b297d' : '5b',
'7b285c297d' : '5c',
'7b285d297d' : '5d',
'7b285e297d' : '5e',
'7b285f297d' : '5f',
'7b2860297d' : '60',
'7b2861297d' : '61',
'7b2862297d' : '62',
'7b2863297d' : '63',
'7b2864297d' : '64',
'7b2865297d' : '65',
'7b2866297d' : '66',
'7b2867297d' : '67',
'7b2868297d' : '68',
'7b2869297d' : '69',
'7b286a297d' : '6a',
'7b286b297d' : '6b',
'7b286c297d' : '6c',
'7b286d297d' : '6d',
'7b286e297d' : '6e',
'7b286f297d' : '6f',
'7b2870297d' : '70',
'7b2871297d' : '71',
'7b2872297d' : '72',
'7b2873297d' : '73',
'7b2874297d' : '74',
'7b2875297d' : '75',
'7b2876297d' : '76',
'7b2877297d' : '77',
'7b2878297d' : '78',
'7b2879297d' : '79',
'7b287a297d' : '7a',
'7b287b297d' : '7b',
'7b287c297d' : '7c',
'7b287d297d' : '7d',
'7b287e297d' : '7e',
'7b287f297d' : '7f',
'7b2880297d' : '80',
'7b2881297d' : '81',
'7b2882297d' : '82',
'7b2883297d' : '83',
'7b2884297d' : '84',
'7b2885297d' : '85',
'7b2886297d' : '86',
'7b2887297d' : '87',
'7b2888297d' : '88',
'7b2889297d' : '89',
'7b288a297d' : '8a',
'7b288b297d' : '8b',
'7b288c297d' : '8c',
'7b288d297d' : '8d',
'7b288e297d' : '8e',
'7b288f297d' : '8f',
'7b2890297d' : '90',
'7b2891297d' : '91',
'7b2892297d' : '92',
'7b2893297d' : '93',
'7b2894297d' : '94',
'7b2895297d' : '95',
'7b2896297d' : '96',
'7b2897297d' : '97',
'7b2898297d' : '98',
'7b2899297d' : '99',
'7b289a297d' : '9a',
'7b289b297d' : '9b',
'7b289c297d' : '9c',
'7b289d297d' : '9d',
'7b289e297d' : '9e',
'7b289f297d' : '9f',
'7b28a0297d' : 'a0',
'7b28a1297d' : 'a1',
'7b28a2297d' : 'a2',
'7b28a3297d' : 'a3',
'7b28a4297d' : 'a4',
'7b28a5297d' : 'a5',
'7b28a6297d' : 'a6',
'7b28a7297d' : 'a7',
'7b28a8297d' : 'a8',
'7b28a9297d' : 'a9',
'7b28aa297d' : 'aa',
'7b28ab297d' : 'ab',
'7b28ac297d' : 'ac',
'7b28ad297d' : 'ad',
'7b28ae297d' : 'ae',
'7b28af297d' : 'af',
'7b28b0297d' : 'b0',
'7b28b1297d' : 'b1',
'7b28b2297d' : 'b2',
'7b28b3297d' : 'b3',
'7b28b4297d' : 'b4',
'7b28b5297d' : 'b5',
'7b28b6297d' : 'b6',
'7b28b7297d' : 'b7',
'7b28b8297d' : 'b8',
'7b28b9297d' : 'b9',
'7b28ba297d' : 'ba',
'7b28bb297d' : 'bb',
'7b28bc297d' : 'bc',
'7b28bd297d' : 'bd',
'7b28be297d' : 'be',
'7b28bf297d' : 'bf',
'7b28c0297d' : 'c0',
'7b28c1297d' : 'c1',
'7b28c2297d' : 'c2',
'7b28c3297d' : 'c3',
'7b28c4297d' : 'c4',
'7b28c5297d' : 'c5',
'7b28c6297d' : 'c6',
'7b28c7297d' : 'c7',
'7b28c8297d' : 'c8',
'7b28c9297d' : 'c9',
'7b28ca297d' : 'ca',
'7b28cb297d' : 'cb',
'7b28cc297d' : 'cc',
'7b28cd297d' : 'cd',
'7b28ce297d' : 'ce',
'7b28cf297d' : 'cf',
'7b28d0297d' : 'd0',
'7b28d1297d' : 'd1',
'7b28d2297d' : 'd2',
'7b28d3297d' : 'd3',
'7b28d4297d' : 'd4',
'7b28d5297d' : 'd5',
'7b28d6297d' : 'd6',
'7b28d7297d' : 'd7',
'7b28d8297d' : 'd8',
'7b28d9297d' : 'd9',
'7b28da297d' : 'da',
'7b28db297d' : 'db',
'7b28dc297d' : 'dc',
'7b28dd297d' : 'dd',
'7b28de297d' : 'de',
'7b28df297d' : 'df',
'7b28e0297d' : 'e0',
'7b28e1297d' : 'e1',
'7b28e2297d' : 'e2',
'7b28e3297d' : 'e3',
'7b28e4297d' : 'e4',
'7b28e5297d' : 'e5',
'7b28e6297d' : 'e6',
'7b28e7297d' : 'e7',
'7b28e8297d' : 'e8',
'7b28e9297d' : 'e9',
'7b28ea297d' : 'ea',
'7b28eb297d' : 'eb',
'7b28ec297d' : 'ec',
'7b28ed297d' : 'ed',
'7b28ee297d' : 'ee',
'7b28ef297d' : 'ef',
'7b28f0297d' : 'f0',
'7b28f1297d' : 'f1',
'7b28f2297d' : 'f2',
'7b28f3297d' : 'f3',
'7b28f4297d' : 'f4',
'7b28f5297d' : 'f5',
'7b28f6297d' : 'f6',
'7b28f7297d' : 'f7',
'7b28f8297d' : 'f8',
'7b28f9297d' : 'f9',
'7b28fa297d' : 'fa',
'7b28fb297d' : 'fb',
'7b28fc297d' : 'fc',
'7b28fd297d' : 'fd',
'7b28fe297d' : 'fe',
        }


class Text(models.Model):
    textNumber = models.IntegerField()
    textPos = models.IntegerField()
    textPtr = models.IntegerField()
    unknown1 = models.IntegerField()
    unknown2 = models.IntegerField()
    hexString = models.CharField(max_length=255)

class translateText(models.Model):
    textNumber = models.IntegerField(null=False)
    userID = models.CharField(max_length=15, null=False)
    Contents = models.TextField(null=False)
    transDate = models.DateTimeField(auto_now_add=True, auto_now=True)
    choosed = models.BooleanField(null=False, default=False)


    