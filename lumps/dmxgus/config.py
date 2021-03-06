#
# Copyright (c) 2013 Contributors to the Freedoom project.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of the freedoom project nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# --------------------------------------------------------------
#
# Config file for GUS config generator.
#

# Names of GUS instrument files to use for playing MIDI.
# These are the names of the .pat files in the \ultrasnd\midi directory
# that are loaded into the card.

GUS_INSTR_PATCHES = {
	  0: "acpiano",    # #001 - Acoustic Grand Piano
	  1: "britepno",   # #002 - Bright Acoustic Piano
	  2: "synpiano",   # #003 - Electric Grand Piano
	  3: "honky",      # #004 - Honky-tonk Piano
	  4: "epiano1",    # #005 - Electric Piano 1
	  5: "epiano2",    # #006 - Electric Piano 2
	  6: "hrpschrd",   # #007 - Harpsichord
	  7: "clavinet",   # #008 - Clavi
	  8: "celeste",    # #009 - Celesta
	  9: "glocken",    # #010 - Glockenspiel
	 10: "musicbox",   # #011 - Music Box
	 11: "vibes",      # #012 - Vibraphone
	 12: "marimba",    # #013 - Marimba
	 13: "xylophon",   # #014 - Xylophone
	 14: "tubebell",   # #015 - Tubular Bells
	 15: "santur",     # #016 - Dulcimer
	 16: "homeorg",    # #017 - Drawbar Organ
	 17: "percorg",    # #018 - Percussive Organ
	 18: "rockorg",    # #019 - Rock Organ
	 19: "church",     # #020 - Church Organ
	 20: "reedorg",    # #021 - Reed Organ
	 21: "accordn",    # #022 - Accordion
	 22: "harmonca",   # #023 - Harmonica
	 23: "concrtna",   # #024 - Tango Accordion
	 24: "nyguitar",   # #025 - Acoustic Guitar (nylon)
	 25: "acguitar",   # #026 - Acoustic Guitar (steel)
	 26: "jazzgtr",    # #027 - Electric Guitar (jazz)
	 27: "cleangtr",   # #028 - Electric Guitar (clean)
	 28: "mutegtr",    # #029 - Electric Guitar (muted)
	 29: "odguitar",   # #030 - Overdriven Guitar
	 30: "distgtr",    # #031 - Distortion Guitar
	 31: "gtrharm",    # #032 - Guitar harmonics
	 32: "acbass",     # #033 - Acoustic Bass
	 33: "fngrbass",   # #034 - Electric Bass (finger)
	 34: "pickbass",   # #035 - Electric Bass (pick)
	 35: "fretless",   # #036 - Fretless Bass
	 36: "slapbas1",   # #037 - Slap Bass 1
	 37: "slapbas2",   # #038 - Slap Bass 2
	 38: "synbass1",   # #039 - Synth Bass 1
	 39: "synbass2",   # #040 - Synth Bass 2
	 40: "violin",     # #041 - Violin
	 41: "viola",      # #042 - Viola
	 42: "cello",      # #043 - Cello
	 43: "contraba",   # #044 - Contrabass
	 44: "tremstr",    # #045 - Tremolo Strings
	 45: "pizzcato",   # #046 - Pizzicato Strings
	 46: "harp",       # #047 - Orchestral Harp
	 47: "timpani",    # #048 - Timpani
	 48: "marcato",    # #049 - String Ensemble 1
	 49: "slowstr",    # #050 - String Ensemble 2
	 50: "synstr1",    # #051 - SynthStrings 1
	 51: "synstr2",    # #052 - SynthStrings 2
	 52: "choir",      # #053 - Choir Aahs
	 53: "doo",        # #054 - Voice Oohs
	 54: "voices",     # #055 - Synth Voice
	 55: "orchhit",    # #056 - Orchestra Hit
	 56: "trumpet",    # #057 - Trumpet
	 57: "trombone",   # #058 - Trombone
	 58: "tuba",       # #059 - Tuba
	 59: "mutetrum",   # #060 - Muted Trumpet
	 60: "frenchrn",   # #061 - French Horn
	 61: "hitbrass",   # #062 - Brass Section
	 62: "synbras1",   # #063 - SynthBrass 1
	 63: "synbras2",   # #064 - SynthBrass 2
	 64: "sprnosax",   # #065 - Soprano Sax
	 65: "altosax",    # #066 - Alto Sax
	 66: "tenorsax",   # #067 - Tenor Sax
	 67: "barisax",    # #068 - Baritone Sax
	 68: "oboe",       # #069 - Oboe
	 69: "englhorn",   # #070 - English Horn
	 70: "bassoon",    # #071 - Bassoon
	 71: "clarinet",   # #072 - Clarinet
	 72: "piccolo",    # #073 - Piccolo
	 73: "flute",      # #074 - Flute
	 74: "recorder",   # #075 - Recorder
	 75: "woodflut",   # #076 - Pan Flute
	 76: "bottle",     # #077 - Blown Bottle
	 77: "shakazul",   # #078 - Shakuhachi
	 78: "whistle",    # #079 - Whistle
	 79: "ocarina",    # #080 - Ocarina
	 80: "sqrwave",    # #081 - Lead 1 (square)
	 81: "sawwave",    # #082 - Lead 2 (sawtooth)
	 82: "calliope",   # #083 - Lead 3 (calliope)
	 83: "chiflead",   # #084 - Lead 4 (chiff)
	 84: "charang",    # #085 - Lead 5 (charang)
	 85: "voxlead",    # #086 - Lead 6 (voice)
	 86: "lead5th",    # #087 - Lead 7 (fifths)
	 87: "basslead",   # #088 - Lead 8 (bass + lead)
	 88: "fantasia",   # #089 - Pad 1 (new age)
	 89: "warmpad",    # #090 - Pad 2 (warm)
	 90: "polysyn",    # #091 - Pad 3 (polysynth)
	 91: "ghostie",    # #092 - Pad 4 (choir)
	 92: "bowglass",   # #093 - Pad 5 (bowed)
	 93: "metalpad",   # #094 - Pad 6 (metallic)
	 94: "halopad",    # #095 - Pad 7 (halo)
	 95: "sweeper",    # #096 - Pad 8 (sweep)
	 96: "aurora",     # #097 - FX 1 (rain)
	 97: "soundtrk",   # #098 - FX 2 (soundtrack)
	 98: "crystal",    # #099 - FX 3 (crystal)
	 99: "atmosphr",   # #100 - FX 4 (atmosphere)
	100: "freshair",   # #101 - FX 5 (brightness)
	101: "unicorn",    # #102 - FX 6 (goblins)
	102: "echovox",    # #103 - FX 7 (echoes)
	103: "startrak",   # #104 - FX 8 (sci-fi)
	104: "sitar",      # #105 - Sitar
	105: "banjo",      # #106 - Banjo
	106: "shamisen",   # #107 - Shamisen
	107: "koto",       # #108 - Koto
	108: "kalimba",    # #109 - Kalimba
	109: "bagpipes",   # #110 - Bag pipe
	110: "fiddle",     # #111 - Fiddle
	111: "shannai",    # #112 - Shanai
	112: "carillon",   # #113 - Tinkle Bell
	113: "agogo",      # #114 - Agogo
	114: "steeldrm",   # #115 - Steel Drums
	115: "woodblk",    # #116 - Woodblock
	116: "taiko",      # #117 - Taiko Drum
	117: "toms",       # #118 - Melodic Tom
	118: "syntom",     # #119 - Synth Drum
	119: "revcym",     # #120 - Reverse Cymbal
	120: "fx-fret",    # #121 - Guitar Fret Noise
	121: "fx-blow",    # #122 - Breath Noise
	122: "seashore",   # #123 - Seashore
	123: "jungle",     # #124 - Bird Tweet
	124: "telephon",   # #125 - Telephone Ring
	125: "helicptr",   # #126 - Helicopter
	126: "applause",   # #127 - Applause
	127: "pistol",     # #128 - Gunshot
	128: "blank",
	162: "kick1",      # #35 Acoustic Bass Drum
	163: "kick2",      # #36 Bass Drum 1
	164: "stickrim",   # #37 Side Stick
	165: "snare1",     # #38 Acoustic Snare
	166: "claps",      # #39 Hand Clap
	167: "snare2",     # #40 Electric Snare
	168: "tomlo2",     # #41 Low Floor Tom
	169: "hihatcl",    # #42 Closed Hi Hat
	170: "tomlo1",     # #43 High Floor Tom
	171: "hihatpd",    # #44 Pedal Hi-Hat
	172: "tommid2",    # #45 Low Tom
	173: "hihatop",    # #46 Open Hi-Hat
	174: "tommid1",    # #47 Low-Mid Tom
	175: "tomhi2",     # #48 Hi-Mid Tom
	176: "cymcrsh1",   # #49 Crash Cymbal 1
	177: "tomhi1",     # #50 High Tom
	178: "cymride1",   # #51 Ride Cymbal 1
	179: "cymchina",   # #52 Chinese Cymbal
	180: "cymbell",    # #53 Ride Bell
	181: "tamborin",   # #54 Tambourine
	182: "cymsplsh",   # #55 Splash Cymbal
	183: "cowbell",    # #56 Cowbell
	184: "cymcrsh2",   # #57 Crash Cymbal 2
	185: "vibslap",    # #58 Vibraslap
	186: "cymride2",   # #59 Ride Cymbal 2
	187: "bongohi",    # #60 Hi Bongo
	188: "bongolo",    # #61 Low Bongo
	189: "congahi1",   # #62 Mute Hi Conga
	190: "congahi2",   # #63 Open Hi Conga
	191: "congalo",    # #64 Low Conga
	192: "timbaleh",   # #65 High Timbale
	193: "timbalel",   # #66 Low Timbale
	194: "agogohi",    # #67 High Agogo
	195: "agogolo",    # #68 Low Agogo
	196: "cabasa",     # #69 Cabasa
	197: "maracas",    # #70 Maracas
	198: "whistle1",   # #71 Short Whistle
	199: "whistle2",   # #72 Long Whistle
	200: "guiro1",     # #73 Short Guiro
	201: "guiro2",     # #74 Long Guiro
	202: "clave",      # #75 Claves
	203: "woodblk1",   # #76 Hi Wood Block
	204: "woodblk2",   # #77 Low Wood Block
	205: "cuica1",     # #78 Mute Cuica
	206: "cuica2",     # #79 Open Cuica
	207: "triangl1",   # #80 Mute Triangle
	208: "triangl2",   # #81 Open Triangle
}

# These are the data sizes of the patch files distributed with the
# GUS drivers. These are used to calculate the size in RAM of the
# generated patch sets to check that they are within the limits.
# and check it is within the limit.

PATCH_FILE_SIZES = {
	"acbass": 5248,      "accordn": 9616,     "acguitar": 26080,
	"acpiano": 32256,    "agogo": 13696,      "agogohi": 3488,
	"agogolo": 3488,     "altosax": 5616,     "applause": 30064,
	"atmosphr": 31360,   "aurora": 31088,     "bagpipes": 7760,
	"banjo": 32016,      "barisax": 10544,    "basslead": 26496,
	"bassoon": 8000,     "belltree": 31888,   "blank": 1520,
	"bongohi": 3456,     "bongolo": 4448,     "bottle": 12368,
	"bowglass": 24688,   "britepno": 36000,   "cabasa": 8448,
	"calliope": 22992,   "carillon": 5888,    "castinet": 6016,
	"celeste": 9936,     "cello": 9120,       "charang": 45056,
	"chiflead": 31536,   "choir": 22480,      "church": 2144,
	"claps": 5696,       "clarinet": 9184,    "clave": 2352,
	"clavinet": 1440,    "cleangtr": 22768,   "concrtna": 8784,
	"congahi1": 4224,    "congahi2": 4704,    "congalo": 4704,
	"contraba": 4704,    "cowbell": 3168,     "crystal": 30224,
	"cuica1": 9344,      "cuica2": 12848,     "cymbell": 17248,
	"cymchina": 24112,   "cymcrsh1": 31520,   "cymcrsh2": 31040,
	"cymride1": 17664,   "cymride2": 17664,   "cymsplsh": 31520,
	"distgtr": 18848,    "doo": 8464,         "echovox": 14976,
	"englhorn": 12096,   "epiano1": 7344,     "epiano2": 21936,
	"fantasia": 23456,   "fiddle": 5904,      "flute": 6032,
	"fngrbass": 9744,    "frenchrn": 14128,   "freshair": 28992,
	"fretless": 2640,    "fx-blow": 28688,    "fx-fret": 13648,
	"ghostie": 31488,    "glocken": 5184,     "gtrharm": 4928,
	"guiro1": 4128,      "guiro2": 9248,      "halopad": 29984,
	"harmonca": 7408,    "harp": 11728,       "helicptr": 25008,
	"highq": 1808,       "hihatcl": 4560,     "hihatop": 20048,
	"hihatpd": 1808,     "hitbrass": 31520,   "homeorg": 992,
	"honky": 65680,      "hrpschrd": 3584,    "jazzgtr": 27712,
	"jingles": 16944,    "jungle": 13616,     "kalimba": 2208,
	"kick1": 4544,       "kick2": 5024,       "koto": 20832,
	"lead5th": 6464,     "maracas": 4560,     "marcato": 61232,
	"marimba": 2064,     "metalpad": 30288,   "metbell": 112,
	"metclick": 112,     "musicbox": 15312,   "mutegtr": 17008,
	"mutetrum": 9168,    "nyguitar": 19200,   "oboe": 3952,
	"ocarina": 1616,     "odguitar": 12640,   "orchhit": 14208,
	"percorg": 7520,     "piccolo": 4320,     "pickbass": 16416,
	"pistol": 18144,     "pizzcato": 19888,   "polysyn": 30224,
	"recorder": 2656,    "reedorg": 1568,     "revcym": 13536,
	"rockorg": 30288,    "santur": 21760,     "sawwave": 27056,
	"scratch1": 4384,    "scratch2": 2288,    "seashore": 31040,
	"shakazul": 31136,   "shaker": 3104,      "shamisen": 13136,
	"shannai": 9792,     "sitar": 18288,      "slap": 5856,
	"slapbas1": 27872,   "slapbas2": 20592,   "slowstr": 18192,
	"snare1": 8544,      "snare2": 4096,      "soundtrk": 19888,
	"sprnosax": 7072,    "sqrclick": 112,     "sqrwave": 15056,
	"startrak": 27376,   "steeldrm": 11952,   "stickrim": 2848,
	"sticks": 4224,      "surdo1": 9600,      "surdo2": 9600,
	"sweeper": 31216,    "synbass1": 6160,    "synbass2": 2928,
	"synbras1": 30704,   "synbras2": 30160,   "synpiano": 5456,
	"synstr1": 31216,    "synstr2": 16416,    "syntom": 30512,
	"taiko": 18672,      "tamborin": 8944,    "telephon": 4416,
	"tenorsax": 8448,    "timbaleh": 5264,    "timbalel": 9728,
	"timpani": 7072,     "tomhi1": 6576,      "tomhi2": 6560,
	"tomlo1": 6560,      "tomlo2": 9600,      "tommid1": 6560,
	"tommid2": 6560,     "toms": 6576,        "tremstr": 61232,
	"triangl1": 2224,    "triangl2": 15792,   "trombone": 12896,
	"trumpet": 6608,     "tuba": 5760,        "tubebell": 9120,
	"unicorn": 30096,    "vibes": 10640,      "vibslap": 9456,
	"viola": 27952,      "violin": 12160,     "voices": 14976,
	"voxlead": 14992,    "warmpad": 18080,    "whistle": 5872,
	"whistle1": 2000,    "whistle2": 928,     "woodblk": 3680,
	"woodblk1": 2352,    "woodblk2": 3680,    "woodflut": 1936,
	"xylophon": 9376,
}

# Groups of "similar sounding" instruments. The first instrument in each
# group is the "leader" and will be used as the fallback for other
# instruments in the group if they are not popular enough to be included.

# These groups are based on inaccurate stereotypes about musical instruments.
# If you're looking to improve the config, here's where to start.

SIMILAR_GROUPS = [
	# Pianos.
	('acpiano', 'britepno', 'synpiano', 'honky', 'epiano1', 'epiano2',
	 'hrpschrd', 'clavinet', 'celeste', 'glocken'),
	# Xylophone etc.
	('marimba', 'musicbox', 'vibes', 'xylophon', 'tubebell', 'santur',
	 'kalimba'),
	# Organs.
	('homeorg', 'percorg', 'rockorg', 'church', 'reedorg', 'accordn',
	 'harmonca', 'concrtna'),
	# Guitars.
	('nyguitar', 'acguitar', 'jazzgtr', 'cleangtr', 'mutegtr', 'odguitar',
	 'distgtr', 'gtrharm'),
	# Basses.
	('synbass2', 'acbass', 'fngrbass', 'pickbass', 'fretless', 'slapbas1',
	 'slapbas2', 'synbass1'),
	# Violin and similar string instruments.
	('violin', 'viola', 'cello', 'contraba', 'tremstr', 'pizzcato', 'harp',
	 'timpani'),
	# Other stringed (?)
	('marcato', 'slowstr', 'synstr1', 'synstr2', 'choir', 'doo', 'voices',
	 'orchhit'),
	# Trumpet and other brass.
	('trumpet', 'trombone', 'tuba', 'mutetrum', 'frenchrn', 'hitbrass',
	 'synbras1', 'synbras2'),
	# Reed instruments.
	('sprnosax', 'altosax', 'tenorsax', 'barisax', 'oboe', 'englhorn',
	 'bassoon', 'clarinet'),
	# Pipe instruments.
	('flute', 'piccolo', 'recorder', 'woodflut', 'bottle', 'shakazul',
	 'whistle', 'ocarina', 'bagpipes', 'fiddle', 'shannai'),
	# Leads.
	('sqrwave', 'sawwave', 'calliope', 'chiflead', 'charang', 'voxlead',
	 'lead5th', 'basslead', 'sitar', 'banjo', 'shamisen', 'koto'),
	# Special effects. Blank unless popular enough to appear.
	('blank','fantasia', 'warmpad', 'polysyn', 'ghostie', 'bowglass',
	 'metalpad', 'halopad', 'sweeper', 'aurora', 'soundtrk', 'crystal',
	 'atmosphr', 'freshair', 'unicorn', 'echovox', 'startrak', 'fx-fret',
	 'fx-blow', 'seashore', 'jungle', 'telephon', 'helicptr', 'applause',
	 'pistol'),

	# -- Percussion effects. This is probably where the current config is
	#    worst and in dire need of improvement.

	# Conga/kick
	('kick1', 'steeldrm', 'taiko', 'kick2', 'congahi1', 'congahi2',
	 'congalo', 'clave'),
	# Snare drums
	('snare1', 'stickrim', 'claps', 'snare2', 'tamborin', 'vibslap',
	 'bongohi', 'bongolo', 'timbaleh', 'timbalel', 'maracas', 'woodblk1',
	 'woodblk2'),
	# Hi-hat
	('hihatpd', 'carillon', 'agogo', 'woodblk', 'hihatcl', 'hihatop',
	 'cowbell', 'agogohi', 'agogolo', 'cabasa', 'whistle1', 'whistle2',
	 'guiro1', 'guiro2', 'cuica1', 'cuica2', 'triangl1', 'triangl2'),
	# Toms
	('tommid1', 'toms', 'syntom', 'tomlo2', 'tomlo1', 'tommid2', 'tomhi2',
	 'tomhi1'),
	# Cymbals.
	('cymcrsh1', 'revcym', 'cymride1', 'cymchina', 'cymbell', 'cymsplsh',
	 'cymcrsh2', 'cymride2'),
]

