p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
ciphertext = 15898528329836486259454280642537682745047492250031819804208947573732209296147142448425785475270839697919293976182333838349380319082449313123936042811917218253196274432195116911131311101664245124078266845291992250418272429673592762174381527121624558596357902629676671110003023710107905410987270486412752306303470410502366293287214002128769133995449197216690029130480234844827254205117539992852496638836353167147769854523276743309449394023887611024408163270210444112592577810624181267012402352918669635578760260278590557042623644240179185252741450067430771092134328724271261927055861090533852597204599189199436235384288
e = 65537
n = 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239
q = 156408916769576372285319235535320446340733908943564048157238512311891352879208957302116527435165097143521156600690562005797819820759620198602417583539668686152735534648541252847927334505648478214810780526425005943955838623325525300844493280040860604499838598837599791480284496210333200247148213274376422459183


t = (p - 1) * (q - 1)
d = pow(e, -1, t)
m = pow(ciphertext, d, n)

print (m)