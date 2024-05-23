'''

encrypt(m1) * encrypt(m2) = ((m1**e) * (m2**e)) mod n = (m1 * m2)**e mod n = encrypt(m1 * m2)

'''

from Crypto.Util.number import long_to_bytes

n = 88390118739134450034927893834885074276553461158358176301041616933558884025049744219744824309991939935301136527607890448398448533875974826610388471394915948955649734609450295051057762840776117404133494850700351873342078958101560470408553044789072796389990279447204082467021213707357481171564499867989946729641
e = 65537
encrypt_m1 =  29567231752376132585223822553638360377328486326110542460457387641982925065404202264904908051884853479799798295173250256185008628221207676617873852810318746220622958211979056889874982852387208002576413932146156909564240732940553180365582584673807058202549925730748435634333572415303184620845450466186516261528

encrypt_m2 = pow(2, e, n)

m2 = 2

encrypt_m1_encrypt_m2 = encrypt_m1 * encrypt_m2

print (encrypt_m1_encrypt_m2)

m1_m2 = 580550060391700078946913236734911770139931497702556153513487440893406629034802718534645538074938502890769716268793877259514

m1 = m1_m2 // m2

print (long_to_bytes(m1))