from sanskrit_parser.generator.pratyaya import *  # noqa: F403, F401
from sanskrit_parser.generator.dhatu import *  # noqa: F403, F401
from sanskrit_parser.generator.pratipadika import *  # noqa: F403, F401

viBakti = {}
prAtipadika = {}
encoding = {}
linga = {}


prAtipadika["rAma"] = rAma   # noqa: F405
viBakti["rAma"] = [
    ["रामः", "रामौ", "रामाः"],
    ["रामम्", "रामौ", "रामान्"],
    ["रामेण", "रामाभ्याम्", "रामैः"],
    ["रामाय", "रामाभ्याम्", "रामेभ्यः"],
    [["रामात्", "रामाद्"], "रामाभ्याम्", "रामेभ्यः"],
    ["रामस्य", "रामयोः", "रामाणाम्"],
    ["रामे", "रामयोः", "रामेषु"],
    ["राम", "रामौ", "रामाः"],
]

prAtipadika["sarva"] = sarva    # noqa: F405
viBakti["sarva"] = [
    ["सर्वः", "सर्वौ", "सर्वे"],
    ["सर्वम्", "सर्वौ", "सर्वान्"],
    ["सर्वेण", "सर्वाभ्याम्", "सर्वैः"],
    ["सर्वस्मै", "सर्वाभ्याम्", "सर्वेभ्यः"],
    [["सर्वस्मात्", "सर्वस्माद्"], "सर्वाभ्याम्", "सर्वेभ्यः"],
    ["सर्वस्य", "सर्वयोः", "सर्वेषाम्"],
    ["सर्वस्मिन्", "सर्वयोः", "सर्वेषु "],
]

prAtipadika["pAda"] = pAda    # noqa: F405
viBakti["pAda"] = [
    ["पादः", "पादौ", "पादाः"],
    ["पादम्", "पादौ", ["पादान्", "पदः"]],
    [["पादेन", "पदा"], ["पादाभ्याम्", "पद्भ्याम्"], ["पादैः", "पद्भिः"]],
    [["पादाय", "पदे"], ["पादाभ्याम्", "पद्भ्याम्"], ["पादेभ्यः", "पद्भ्यः"]],
    [["पादात्", "पादाद्", "पदः"], ["पादाभ्याम्", "पद्भ्याम्"], ["पादेभ्यः", "पद्भ्यः"]],
    [["पादस्य", "पदः"], ["पादयोः", "पदोः"], ["पादानाम्", "पदाम्"]],
    [["पादे", "पदि"], ["पादयोः", "पदोः"], ["पादेषु", "पत्सु"]],
    ["पाद", "पादौ", "पादाः"],
]

prAtipadika["yUza"] = yUza    # noqa: F405
viBakti["yUza"] = [
    ["यूषः", "यूषौ", "यूषाः"],
    ["यूषम्", "यूषौ", ["यूषान्", "यूष्णः"]],
    [["यूषेण", "यूष्णा"], ["यूषाभ्याम्", "यूषभ्याम्"], ["यूषैः", "यूषभिः"]],
    [["यूषाय", "यूष्णे"], ["यूषाभ्याम्", "यूषभ्याम्"], ["यूषेभ्यः", "यूषभ्यः"]],
    [["यूषात्", "यूषाद्", "यूष्णः"], ["यूषाभ्याम्", "यूषभ्याम्"], ["यूषेभ्यः", "यूषभ्यः"]],
    [["यूषस्य", "यूष्णः"], ["यूषयोः", "यूष्णोः"], ["यूषाणाम्", "यूष्णाम्"]],
    [["यूषे", "यूषणि", "यूष्णि"], ["यूषयोः", "यूष्णोः"], ["यूषेषु", "यूषसु"]],
    ["यूष", "यूषौ", "यूषाः"],
]
prAtipadika["viSvapA"] = viSvapA    # noqa: F405
viBakti["viSvapA"] = [
    ["विश्वपाः", "विश्वपौ", "विश्वपाः"],
    ["विश्वपाम्", "विश्वपौ", "विश्वपः"],
    ["विश्वपा", "विश्वपाभ्याम्", "विश्वपाभिः"],
    ["विश्वपे", "विश्वपाभ्याम्", "विश्वपाभ्यः"],
    ["विश्वपः", "विश्वपाभ्याम्", "विश्वपाभ्यः"],
    ["विश्वपः", "विश्वपोः", "विश्वपाम्"],
    ["विश्वपि", "विश्वपोः", "विश्वपासु"],
    ["विश्वपाः", "विश्वपौ", "विश्वपाः"],
]
prAtipadika["hAhA"] = hAhA    # noqa: F405
viBakti["hAhA"] = [
    ["हाहाः", "हाहौ", "हाहाः"],
    ["हाहाम्", "हाहौ", "हाहान्"],
    ["हाहा", "हाहाभ्याम्", "हाहाभिः"],
    ["हाहै", "हाहाभ्याम्", "हाहाभ्यः"],
    ["हाहाः", "हाहाभ्याम्", "हाहाभ्यः"],
    ["हाहाः", "हाहौः", "हाहाम्"],
    ["हाहे", "हाहौः", "हाहासु"],
    ["हाहाः", "हाहौ", "हाहाः"],
]

prAtipadika["hari"] = hari   # noqa: F405
viBakti["hari"] = [
    ["हरिः", "हरी", "हरयः"],
    ["हरिम्", "हरी", "हरीन्"],
    ["हरिणा", "हरिभ्याम्", "हरिभिः"],
    ["हरये", "हरिभ्याम्", "हरिभ्यः"],
    ["हरेः", "हरिभ्याम्", "हरिभ्यः"],
    ["हरेः", "हर्योः", "हरीणाम्"],
    ["हरौ", "हर्योः", "हरिषु"],
    ["हरे", "हरी", "हरयः"],
]

prAtipadika["saKi"] = saKi   # noqa: F405
viBakti["saKi"] = [
    ["सखा", "सखायौ", "सखायः"],
    ["सखायम्", "सखायौ", "सखीन्"],
    ["सख्या", "सखिभ्याम्", "सखिभिः"],
    ["सख्ये", "सखिभ्याम्", "सखिभ्यः"],
    ["सख्युः", "सखिभ्याम्", "सखिभ्यः"],
    ["सख्युः", "सख्योः", "सखीनाम्"],
    ["सख्यौ", "सख्योः", "सखिषु"],
    ["सखे", "सखायौ", "सखायः"],
]
prAtipadika["tri"] = tri   # noqa: F405
viBakti["tri"] = [
    [None, None, "त्रयः"],
    [None, None, "त्रीन्"],
    [None, None, "त्रिभिः"],
    [None, None, "त्रिभ्यः"],
    [None, None, "त्रिभ्यः"],
    [None, None, "त्रयाणाम्"],
    [None, None, "त्रिषु"],
    [None, None, "त्रयः"],
]

prAtipadika["kati"] = kati    # noqa: F405
viBakti["kati"] = [
    [None, None, "कति"],
    [None, None, "कति"],
    [None, None, "कतिभिः"],
    [None, None, "कतिभ्यः"],
    [None, None, "कतिभ्यः"],
    [None, None, "कतीनाम्"],
    [None, None, "कतिषु"],
    [None, None, "कति"],
]

prAtipadika["dvi"] = dvi    # noqa: F405
viBakti["dvi"] = [
    [None,  "द्वौ", None],
    [None,  "द्वौ", None],
    [None,  "द्वाभ्याम्", None],
    [None,  "द्वाभ्याम्", None],
    [None,  "द्वाभ्याम्", None],
    [None,  "द्वयोः", None],
    [None,  "द्वयोः", None],
    [None,  "द्वौ", None],
]
prAtipadika["pitf"] = pitf    # noqa: F405
viBakti["pitf"] = [
     ["पिता", "पितरौ", "पितरः"],
     ["पितरम्", "पितरौ", "पितॄन्"],
     ["पित्रा", "पितृभ्याम्", "पितृभिः"],
     ["पित्रे", "पितृभ्याम्", "पितृभ्यः"],
     ["पितुः", "पितृभ्याम्", "पितृभ्यः"],
     ["पितुः", "पित्रोः", "पितॄणाम्"],
     ["पितरि", "पित्रोः", "पितृषु"],
     ["पितः", "पितरौ", "पितरः"],
]

prAtipadika["tvazwf"] = tvazwf    # noqa: F405
viBakti["tvazwf"] = [
     ["त्वष्टा", "त्वष्टारौ", "त्वष्टारः"],
     ["त्वष्टारम्", "त्वष्टारौ", "त्वष्टॄन्"],
     ["त्वष्ट्रा", "त्वष्टृभ्याम्", "त्वष्टृभिः"],
     ["त्वष्ट्रे", "त्वष्टृभ्याम्", "त्वष्टृभ्यः"],
     ["त्वष्टुः", "त्वष्टृभ्याम्", "त्वष्टृभ्यः"],
     ["त्वष्टुः", "त्वष्ट्रोः", "त्वष्टॄणाम्"],
     ["त्वष्टरि", "त्वष्ट्रोः", "त्वष्टृषु"],
     ["त्वष्टः", "त्वष्टारौ", "त्वष्टारः"],
]

prAtipadika["mAtf"] = mAtf    # noqa: F405
viBakti["mAtf"] = [
     ["माता", "मातरौ", "मातरः"],
     ["मातरम्", "मातरौ", "मातॄः"],
     ["मात्रा", "मातृभ्याम्", "मातृभिः"],
     ["मात्रे", "मातृभ्याम्", "मातृभ्यः"],
     ["मातुः", "मातृभ्याम्", "मातृभ्यः"],
     ["मातुः", "मात्रोः", "मातॄणाम्"],
     ["मातरि", "मात्रोः", "मातृषु"],
     ["मातः", "मातरौ", "मातरः"],
]
prAtipadika["krozwu"] = krozwu    # noqa: F405
viBakti["krozwu"] = [
     ["क्रोष्टा", "क्रोष्टारौ", "क्रोष्टारः"],
     ["क्रोष्टारम्", "क्रोष्टारौ", "क्रोष्टून्"],
     [["क्रोष्ट्रा", "क्रोष्टुना"], "क्रोष्टुभ्याम्", "क्रोष्टुभिः"],
     [["क्रोष्ट्रे", "क्रोष्टवे"], "क्रोष्टुभ्याम्", "क्रोष्टुभ्यः"],
     [["क्रोष्टुः", "क्रोष्टोः"], "क्रोष्टुभ्याम्", "क्रोष्टुभ्यः"],
     [["क्रोष्टुः", "क्रोष्टोः"], ["क्रोष्ट्वोः", "क्रोष्ट्रोः"],  "क्रोष्टूनाम्"],
     [["क्रोष्टरि", "क्रोष्टौ"], ["क्रोष्ट्वोः", "क्रोष्ट्रोः"], "क्रोष्टुषु"],
     ["क्रोष्टो", "क्रोष्टारौ", "क्रोष्टारः"],
]

prAtipadika["go"] = go    # noqa: F405
viBakti["go"] = [
     ["गौः", "गावौ", "गावः"],
     ["गाम्", "गावौ", "गाः"],
     ["गवा", "गोभ्याम्", "गोभिः"],
     ["गवे", "गोभ्याम्", "गोभ्यः"],
     ["गोः", "गोभ्याम्", "गोभ्यः"],
     ["गोः", "गवोः", "गवाम्"],
     ["गवि", "गवोः", "गोषु"],
     ["गौः", "गावौ", "गावः"],
]

prAtipadika["SamBu"] = SamBu    # noqa: F405
viBakti["SamBu"] = [
     ["शम्भुः", "शम्भू", "शम्भवः"],
     ["शम्भुम्", "शम्भू", "शम्भून्"],
     ["शम्भुना", "शम्भुभ्याम्", "शम्भुभिः"],
     ["शम्भवे", "शम्भुभ्याम्", "शम्भुभ्यः"],
     ["शम्भोः", "शम्भुभ्याम्", "शम्भुभ्यः"],
     ["शम्भोः", "शम्भ्वोः", "शम्भूनाम्"],
     ["शम्भौ", "शम्भ्वोः", "शम्भुषु"],
     ["शम्भो", "शम्भू", "शम्भवः"],
]

prAtipadika["rE"] = rE   # noqa: F405
viBakti["rE"] = [
     ["राः", "रायौ", "रायः"],
     ["रायम्", "रायौ", "रायः"],
     ["राया", "राभ्याम्", "राभिः"],
     ["राये", "राभ्याम्", "राभ्यः"],
     ["रायः", "राभ्याम्", "राभ्यः"],
     ["रायः", "रायोः", "रायाम्"],
     ["रायि", "रायोः", "रासु"],
     ["राः", "रायौ", "रायः"],
]

prAtipadika["nadI"] = nadI   # noqa: F405
viBakti["nadI"] = [
     ["नदी", "नद्यौ", "नद्यः"],
     ["नदीम्", "नद्यौ", "नदीः"],
     ["नद्या", "नदीभ्याम्", "नदीभिः"],
     ["नद्यै", "नदीभ्याम्", "नदीभ्यः"],
     ["नद्याः", "नदीभ्याम्", "नदीभ्यः"],
     ["नद्याः", "नद्योः", "नदीनाम्"],
     ["नद्याम्", "नद्योः", "नदीषु"],
     ["नदि", "नद्यौ", "नद्यः"],
]

prAtipadika["ramA"] = ramA   # noqa: F405
viBakti["ramA"] = [
     ["रमा", "रमे", "रमाः"],
     ["रमाम्", "रमे", "रमाः"],
     ["रमया", "रमाभ्याम्", "रमाभिः"],
     ["रमायै", "रमाभ्याम्", "रमाभ्यः"],
     ["रमायाः", "रमाभ्याम्", "रमाभ्यः"],
     ["रमायाः", "रमयोः", "रमाणाम्"],
     ["रमायाम्", "रमयोः", "रमासु"],
     ["रमे", "रमे", "रमाः"]
]

prAtipadika["nAsikA"] = nAsikA    # noqa: F405
viBakti["nAsikA"] = [
    ['नासिका', 'नासिके', 'नासिकाः'],
    ['नासिकाम्', 'नासिके', ['नसः', 'नासिकाः']],
    [['नसा', 'नासिकया'], ['नासिकाभ्याम्', 'नोभ्याम्'], ['नासिकाभिः', 'नोभिः']],
    [['नसे', 'नासिकायै'], ['नासिकाभ्याम्', 'नोभ्याम्'], ['नासिकाभ्यः', 'नोभ्यः']],
    [['नसः', 'नासिकायाः'], ['नासिकाभ्याम्', 'नोभ्याम्'], ['नासिकाभ्यः', 'नोभ्यः']],
    [['नसः', 'नासिकायाः'], ['नसोः', 'नासिकयोः'], ['नसाम्', 'नासिकानाम्']],
    [['नासिकायाम्', 'नसि'], ['नसोः', 'नासिकयोः'], ['नासिकासु', 'नःसु', 'नस्सु']],
    ['नासिके', 'नासिके', 'नासिकाः'],
]

prAtipadika["niSA"] = niSA    # noqa: F405
viBakti["niSA"] = [
    ['निशा', 'निशे', 'निशाः'],
    ['निशाम्', 'निशे', ['निशः', 'निशाः']],
    [['निशा', 'निशया'], ['निशाभ्याम्', 'निड्भ्याम्'], ['निशाभिः', 'निड्भिः']],
    [['निशे', 'निशायै'], ['निशाभ्याम्', 'निड्भ्याम्'], ['निशाभ्यः', 'निड्भ्यः']],
    [['निशः', 'निशायाः'], ['निशाभ्याम्', 'निड्भ्याम्'], ['निशाभ्यः', 'निड्भ्यः']],
    [['निशः', 'निशायाः'], ['निशोः', 'निशयोः'], ['निशाम्', 'निशानाम्']],
    [['निशायाम्', 'निशि'], ['निशोः', 'निशयोः'], ['निशासु', 'निट्सु']],
    ['निशे', 'निशे', 'निशाः'],
]

prAtipadika["mati"] = mati   # noqa: F405
viBakti["mati"] = [
    ['मतिः', 'मती', 'मतयः'],
    ['मतिम्', 'मती', 'मतीः'],
    ['मत्या', 'मतिभ्याम्', 'मतिभिः'],
    [['मत्यै', 'मतये'], 'मतिभ्याम्', 'मतिभ्यः'],
    [['मत्याः', 'मतेः'], 'मतिभ्याम्', 'मतिभ्यः'],
    [['मत्याः', 'मतेः'], 'मत्योः', 'मतीनाम्'],
    [['मत्याम्', 'मतौ'], 'मत्योः', 'मतिषु'],
    ['मते', 'मती', 'मतयः'],
]

prAtipadika["lakzmI"] = lakzmI   # noqa: F405
viBakti["lakzmI"] = [
    ['लक्ष्मीः', 'लक्ष्म्यौ', 'लक्ष्म्यः'],
    ['लक्ष्मीम्', 'लक्ष्म्यौ', 'लक्ष्मीः'],
    ['लक्ष्म्या', 'लक्ष्मीभ्याम्', 'लक्ष्मीभिः'],
    ['लक्ष्म्यै', 'लक्ष्मीभ्याम्', 'लक्ष्मीभ्यः'],
    ['लक्ष्म्याः', 'लक्ष्मीभ्याम्', 'लक्ष्मीभ्यः'],
    ['लक्ष्म्याः', 'लक्ष्म्योः', 'लक्ष्मीणाम्'],
    ['लक्ष्म्याम्', 'लक्ष्म्योः', 'लक्ष्मीषु'],
    ['लक्ष्मि', 'लक्ष्म्यौ', 'लक्ष्म्यः'],
]

prAtipadika["strI"] = strI   # noqa: F405
viBakti["strI"] = [
    ['स्त्री', 'स्त्रियौ', 'स्त्रियः'],
    [['स्त्रियम्', 'स्त्रीम्'], 'स्त्रियौ', ['स्त्रियः', 'स्त्रीः']],
    ['स्त्रिया', 'स्त्रीभ्याम्', 'स्त्रीभिः'],
    ['स्त्रियै', 'स्त्रीभ्याम्', 'स्त्रीभ्यः'],
    ['स्त्रियाः', 'स्त्रीभ्याम्', 'स्त्रीभ्यः'],
    ['स्त्रियाः', 'स्त्रियोः', 'स्त्रीणाम्'],
    ['स्त्रियाम्', 'स्त्रियोः', 'स्त्रीषु'],
    ['स्त्रि', 'स्त्रियौ', 'स्त्रियः'],
]

prAtipadika["suDI"] = suDI   # noqa: F405
viBakti["suDI"] = [
    ['सुधीः', 'सुधियौ', 'सुधियः'],
    ['सुधियम्', 'सुधियौ', 'सुधियः'],
    ['सुधिया', 'सुधीभ्याम्', 'सुधीभिः'],
    [['सुधिये', 'सुधियै'], 'सुधीभ्याम्', 'सुधीभ्यः'],
    [['सुधियः', 'सुधियाः'], 'सुधीभ्याम्', 'सुधीभ्यः'],
    [['सुधियः', 'सुधियाः'], 'सुधियोः', ['सुधियाम्', 'सुधीनाम्']],
    [['सुधियाम्', 'सुधियि'], 'सुधियोः', 'सुधीषु'],
    ['सुधि', 'सुधियौ', 'सुधियः'],
]

prAtipadika["BrU"] = BrU   # noqa: F405
viBakti["BrU"] = [
    ['भ्रूः', 'भ्रुवौ', 'भ्रुवः'],
    ['भ्रुवम्', 'भ्रुवौ', 'भ्रुवः'],
    ['भ्रुवा', 'भ्रूभ्याम्', 'भ्रूभिः'],
    [['भ्रुवे', 'भ्रुवै'], 'भ्रूभ्याम्', 'भ्रूभ्यः'],
    [['भ्रुवः', 'भ्रुवाः'], 'भ्रूभ्याम्', 'भ्रूभ्यः'],
    [['भ्रुवः', 'भ्रुवाः'], 'भ्रुवोः', ['भ्रुवाम्', 'भ्रूणाम्']],
    [['भ्रुवाम्', 'भ्रुवि'], 'भ्रुवोः', 'भ्रूषु'],
    ['भ्रु', 'भ्रुवौ', 'भ्रुवः'],
]

prAtipadika["svayamBU"] = svayamBU   # noqa: F405
viBakti["svayamBU"] = [
    ['स्वयम्भूः', 'स्वयम्भुवौ', 'स्वयम्भुवः'],
    ['स्वयम्भुवम्', 'स्वयम्भुवौ', 'स्वयम्भुवः'],
    ['स्वयम्भुवा', 'स्वयम्भूभ्याम्', 'स्वयम्भूभिः'],
    [['स्वयम्भुवे', 'स्वयम्भुवै'], 'स्वयम्भूभ्याम्', 'स्वयम्भूभ्यः'],
    [['स्वयम्भुवः', 'स्वयम्भुवाः'], 'स्वयम्भूभ्याम्', 'स्वयम्भूभ्यः'],
    [['स्वयम्भुवः', 'स्वयम्भुवाः'], 'स्वयम्भुवोः', ['स्वयम्भुवाम्', 'स्वयम्भूनाम्']],
    [['स्वयम्भुवाम्', 'स्वयम्भुवि'], 'स्वयम्भुवोः', 'स्वयम्भूषु'],
    ['स्वयम्भूः', 'स्वयम्भुवौ', 'स्वयम्भुवः'],
]

prAtipadika["varzABU"] = varzABU   # noqa: F405
viBakti["varzABU"] = [
     ["वर्षाभूः", "वर्षाभ्वौ", "वर्षाभ्वः"],
     ["वर्षाभ्वम्", "वर्षाभ्वौ", "वर्षाभ्वः"],
     ["वर्षाभ्वा", "वर्षाभूभ्याम्", "वर्षाभूभिः"],
     ["वर्षाभ्वे", "वर्षाभूभ्याम्", "वर्षाभूभ्यः"],
     ["वर्षाभ्वः", "वर्षाभूभ्याम्", "वर्षाभूभ्यः"],
     ["वर्षाभ्वः", "वर्षाभ्वोः", "वर्षाभ्वाम्"],
     ["वर्षाभ्वि", "वर्षाभ्वोः", "वर्षाभूषु"],
     ["वर्षाभूः", "वर्षाभ्वौ", "वर्षाभ्वः"],
]

prAtipadika["KalapU"] = KalapU   # noqa: F405
viBakti["KalapU"] = [
     ["खलपूः", "खलप्वौ", "खलप्वः"],
     ["खलप्वम्", "खलप्वौ", "खलप्वः"],
     ["खलप्वा", "खलपूभ्याम्", "खलपूभिः"],
     ["खलप्वे", "खलपूभ्याम्", "खलपूभ्यः"],
     ["खलप्वः", "खलपूभ्याम्", "खलपूभ्यः"],
     ["खलप्वः", "खलप्वोः", "खलप्वाम्"],
     ["खलप्वि", "खलप्वोः", "खलपूषु"],
     ["खलपूः", "खलप्वौ", "खलप्वः"],
]

prAtipadika["senAnI"] = senAnI   # noqa: F405
viBakti["senAnI"] = [
     ["senAnIH", "senAnyO", "senAnyaH"],
     ["senAnyam", "senAnyO", "senAnyaH"],
     ["senAnyA", "senAnIByAm", "senAnIBiH"],
     ["senAnye", "senAnIByAm", "senAnIByaH"],
     ["senAnyaH", "senAnIByAm", "senAnIByaH"],
     ["senAnyaH", "senAnyoH", "senAnyAm"],
     ["senAnyAm", "senAnyoH", "senAnIzu"],
     ["senAnIH", "senAnyO", "senAnyaH"],
]
encoding["senAnI"] = SLP1   # noqa: F405

prAtipadika["nI"] = nI   # noqa: F405
viBakti["nI"] = [
    ['नीः', 'नियौ', 'नियः'],
    ['नियम्', 'नियौ', 'नियः'],
    ['निया', 'नीभ्याम्', 'नीभिः'],
    [['निये', 'नियै'], 'नीभ्याम्', 'नीभ्यः'],
    [['नियः', 'नियाः'], 'नीभ्याम्', 'नीभ्यः'],
    [['नियः', 'नियाः'], 'नियोः', ['नियाम्', 'नीनाम्']],
    [['नियाम्', 'नियाम्'], 'नियोः', 'नीषु'],
    ['नीः', 'नियौ', 'नियः'],
]

prAtipadika["SrI"] = SrI   # noqa: F405
viBakti["SrI"] = [
    ['श्रीः', 'श्रियौ', 'श्रियः'],
    ['श्रियम्', 'श्रियौ', 'श्रियः'],
    ['श्रिया', 'श्रीभ्याम्', 'श्रीभिः'],
    [['श्रिये', 'श्रियै'], 'श्रीभ्याम्', 'श्रीभ्यः'],
    [['श्रियः', 'श्रियाः'], 'श्रीभ्याम्', 'श्रीभ्यः'],
    [['श्रियः', 'श्रियाः'], 'श्रियोः', ['श्रियाम्', 'श्रीणाम्']],
    [['श्रियाम्', 'श्रियि'], 'श्रियोः', 'श्रीषु'],
    ['श्रि', 'श्रियौ', 'श्रियः'],
]

prAtipadika["Denu"] = Denu   # noqa: F405
viBakti["Denu"] = [
    ['धेनुः', 'धेनू', 'धेनवः'],
    ['धेनुम्', 'धेनू', 'धेनूः'],
    ['धेन्वा', 'धेनुभ्याम्', 'धेनुभिः'],
    [['धेनवे', 'धेन्वै'], 'धेनुभ्याम्', 'धेनुभ्यः'],
    [['धेनोः', 'धेन्वाः'], 'धेनुभ्याम्', 'धेनुभ्यः'],
    [['धेनोः', 'धेन्वाः'], 'धेन्वोः', 'धेनूनाम्'],
    [['धेनौ', 'धेन्वाम्'], 'धेन्वोः', 'धेनुषु'],
    ['धेनो', 'धेनू', 'धेनवः'],
]


prAtipadika["tisf"] = tisf   # noqa: F405
viBakti["tisf"] = [
    [None, None, 'तिस्रः'],
    [None, None, 'तिस्रः'],
    [None, None, 'तिसृभिः'],
    [None, None, 'तिसृभ्यः'],
    [None, None, 'तिसृभ्यः'],
    [None, None, 'तिसृणाम्'],
    [None, None, 'तिसृषु'],
    [None, None, 'तिस्रः'],
]

prAtipadika["anya"] = anya   # noqa: F405
viBakti["anya"] = [
    [['अन्यद्', 'अन्यत्'], 'अन्ये', 'अन्यानि'],
    [['अन्यद्', 'अन्यत्'], 'अन्ये', 'अन्यानि'],
    ['अन्येन', 'अन्याभ्याम्', 'अन्यैः'],
    ['अन्यस्मै', 'अन्याभ्याम्', 'अन्येभ्यः'],
    [['अन्यस्माद्', 'अन्यस्मात्'], 'अन्याभ्याम्', 'अन्येभ्यः'],
    ['अन्यस्य', 'अन्ययोः', 'अन्येषाम्'],
    ['अन्यस्मिन्', 'अन्ययोः', 'अन्येषु'],
    [['अन्यद्', 'अन्यत्'], 'अन्ये', 'अन्यानि'],
]

prAtipadika["vAri"] = vAri   # noqa: F405
viBakti["vAri"] = [
    ['वारि', 'वारिणी', 'वारीणि'],
    ['वारि', 'वारिणी', 'वारीणि'],
    ['वारिणा', 'वारिभ्याम्', 'वारिभिः'],
    ['वारिणे', 'वारिभ्याम्', 'वारिभ्यः'],
    ['वारिणः', 'वारिभ्याम्', 'वारिभ्यः'],
    ['वारिणः', 'वारिणोः', 'वारीणाम्'],
    ['वारिणि', 'वारिणोः', 'वारिषु'],
    ['वारि', 'वारिणी', 'वारीणि'],
]

prAtipadika["payas"] = payas   # noqa: F405
viBakti["payas"] = [
    ['पयः', 'पयसी', 'पयान्सि'],
    ['पयः', 'पयसी', 'पयान्सि'],
    ['पयसा', 'पयोभ्याम्', 'पयोभिः'],
    ['पयसे', 'पयोभ्याम्', 'पयोभ्यः'],
    ['पयसः', 'पयोभ्याम्', 'पयोभ्यः'],
    ['पयसः', 'पयसोः', 'पयसाम्'],
    ['पयसि', 'पयसोः', ['पयःसु', 'पयस्सु']],
    ['पयः', 'पयसी', 'पयान्सि'],
]

prAtipadika["SrIpA"] = SrIpA   # noqa: F405
viBakti["SrIpA"] = [
    ['श्रीपम्', 'श्रीपे', 'श्रीपाणि'],
    ['श्रीपम्', 'श्रीपे', 'श्रीपाणि'],
    ['श्रीपेण', 'श्रीपाभ्याम्', 'श्रीपैः'],
    ['श्रीपाय', 'श्रीपाभ्याम्', 'श्रीपेभ्यः'],
    [['श्रीपाद्', 'श्रीपात्'], 'श्रीपाभ्याम्', 'श्रीपेभ्यः'],
    ['श्रीपस्य', 'श्रीपयोः', 'श्रीपाणाम्'],
    ['श्रीपे', 'श्रीपयोः', 'श्रीपेषु'],
    ['श्रीपम्', 'श्रीपे', 'श्रीपाणि'],
]

prAtipadika["jYAna"] = jYAna   # noqa: F405
viBakti["jYAna"] = [
    ['ज्ञानम्', 'ज्ञाने', 'ज्ञानानि'],
    ['ज्ञानम्', 'ज्ञाने', 'ज्ञानानि'],
    ['ज्ञानेन', 'ज्ञानाभ्याम्', 'ज्ञानैः'],
    ['ज्ञानाय', 'ज्ञानाभ्याम्', 'ज्ञानेभ्यः'],
    [['ज्ञानाद्', 'ज्ञानात्'], 'ज्ञानाभ्याम्', 'ज्ञानेभ्यः'],
    ['ज्ञानस्य', 'ज्ञानयोः', 'ज्ञानानाम्'],
    ['ज्ञाने', 'ज्ञानयोः', 'ज्ञानेषु'],
    ['ज्ञानम्', 'ज्ञाने', 'ज्ञानानि'],
]

prAtipadika["akzi"] = akzi   # noqa: F405
viBakti["akzi"] = [
    ['अक्षि', 'अक्षिणी', 'अक्षीणि'],
    ['अक्षि', 'अक्षिणी', 'अक्षीणि'],
    ['अक्ष्णा', 'अक्षिभ्याम्', 'अक्षिभिः'],
    ['अक्ष्णे', 'अक्षिभ्याम्', 'अक्षिभ्यः'],
    ['अक्ष्णः', 'अक्षिभ्याम्', 'अक्षिभ्यः'],
    ['अक्ष्णः', 'अक्ष्णोः', 'अक्ष्णाम्'],
    [['अक्षणि', 'अक्ष्णि'], 'अक्ष्णोः', 'अक्षिषु'],
    ['अक्षि', 'अक्षिणी', 'अक्षीणि'],
]

prAtipadika["atinO"] = atinO   # noqa: F405
viBakti["atinO"] = [
    ['अतिनु', 'अतिनुनी', 'अतिनूनि'],
    ['अतिनु', 'अतिनुनी', 'अतिनूनि'],
    ['अतिनुना', 'अतिनुभ्याम्', 'अतिनुभिः'],
    ['अतिनुने', 'अतिनुभ्याम्', 'अतिनुभ्यः'],
    ['अतिनुनः', 'अतिनुभ्याम्', 'अतिनुभ्यः'],
    ['अतिनुनः', 'अतिनुनोः', 'अतिनूनाम्'],
    ['अतिनुनि', 'अतिनुनोः', 'अतिनुषु'],
    ['अतिनु', 'अतिनुनी', 'अतिनूनि'],
]

prAtipadika["lih"] = lih_kvip  # noqa: F405
viBakti["lih"] = [
    [['लिड्', 'लिट्'], 'लिहौ', 'लिहः'],
    ['लिहम्', 'लिहौ', 'लिहः'],
    ['लिहा', 'लिड्भ्याम्', 'लिड्भिः'],
    ['लिहे', 'लिड्भ्याम्', 'लिड्भ्यः'],
    ['लिहः', 'लिड्भ्याम्', 'लिड्भ्यः'],
    ['लिहः', 'लिहोः', 'लिहाम्'],
    ['लिहि', 'लिहोः', 'लिट्सु'],
    [['लिड्', 'लिट्'], 'लिहौ', 'लिहः'],
]

prAtipadika["duh"] = duh_kvip  # noqa: F405
viBakti["duh"] = [
    [['धुग्', 'धुक्'], 'दुहौ', 'दुहः'],
    ['दुहम्', 'दुहौ', 'दुहः'],
    ['दुहा', 'धुग्भ्याम्', 'धुग्भिः'],
    ['दुहे', 'धुग्भ्याम्', 'धुग्भ्यः'],
    ['दुहः', 'धुग्भ्याम्', 'धुग्भ्यः'],
    ['दुहः', 'दुहोः', 'दुहाम्'],
    ['दुहि', 'दुहोः', 'धुक्षु'],
    [['धुग्', 'धुक्'], 'दुहौ', 'दुहः'],
]

prAtipadika["druh"] = druh_kvip  # noqa: F405
viBakti["druh"] = [
    [['ध्रुग्', 'ध्रुड्', 'ध्रुक्', 'ध्रुट्'], 'द्रुहौ', 'द्रुहः'],
    ['द्रुहम्', 'द्रुहौ', 'द्रुहः'],
    ['द्रुहा', ['ध्रुग्भ्याम्', 'ध्रुड्भ्याम्'], ['ध्रुग्भिः', 'ध्रुड्भिः']],
    ['द्रुहे', ['ध्रुग्भ्याम्', 'ध्रुड्भ्याम्'], ['ध्रुग्भ्यः', 'ध्रुड्भ्यः']],
    ['द्रुहः', ['ध्रुग्भ्याम्', 'ध्रुड्भ्याम्'], ['ध्रुग्भ्यः', 'ध्रुड्भ्यः']],
    ['द्रुहः', 'द्रुहोः', 'द्रुहाम्'],
    ['द्रुहि', 'द्रुहोः', ['ध्रुक्षु', 'ध्रुट्सु']],
    [['ध्रुग्', 'ध्रुड्', 'ध्रुक्', 'ध्रुट्'], 'द्रुहौ', 'द्रुहः'],
]

ajanta = {"pum": [], "strI": [], "napum": []}
halanta = {"pum": [], "strI": [], "napum": []}

for p in prAtipadika:
    linga[p] = prAtipadika[p].linga
    if p[-1].lower() in "aeioufx":
        ajanta[linga[p]].append(p)
    else:
        halanta[linga[p]].append(p)
