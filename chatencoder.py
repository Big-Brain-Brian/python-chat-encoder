#/!\WARNING/!\ This program was made entirely by Alex Bedeaux.
#dont mess with the above text

#/!\WARNING/!\ DO NOT EDIT ANYTHING!!!
#the only thing you should edit is the keys
#to get new encrypted keys run the program then type "yes" when it asks you yes / no
#then you dont need to do anything unless you want new keys.
#/!\ HOW TO USE /!\
#Once you have gotten new keys or are using the pre installed ones
#run the program and enter a number from 1-16
#then enter the text you wanna encode
#then type e (for encoding)
#after, share the number you entered with the person you want to Message
#then share the encoded text and tell them to type d instead
#thats about it SEEYA

import random
#paste the keys in here
key0 = "tj@n:`i[1^},0rhq;4ed]ym.|-bz67v+9#ua35=)klcg28x!s$w%{*&( /of~p"
key1 = "at/{q]&*g !in}4;z7$yr|s0ov8x9d([c+w6~pfe.l5m%2:^`#3)ujk-b@h=1,"
key2 = "-[#+ov|@{/w.rgd9if2x(^1j3)n$&=y0*c;ekt6%l}amzu:b!`7sq5hp4,8]~ "
key3 = "oc{[]@9ptf0-;.4|*srkiy%!n#u,/&agm}381l)jw^h5(=:~7 ve6$+`zd2bxq"
key4 = "e*,y{b^132@ d4#}lq%`un5;im=c:oa-[r$8hx]7t(!0vps+&wf6~k)|9gzj/."
key5 = ")w](5~8eci0l|zub^d[,2;-m6`4!9.js{t+%#rvx1gqha7no&@:yp*$} /fk3="
key6 = "|a^z;2{5+:$l=1c`kg@b.yj~!}v7q(/[smuo6]#e- w48hr03f*dp9t)i&x,n%"
key7 = "6a*;h g.)|(y2qv8nz&1b@%~-,`ed^}4opuj379f+tsx5!c]=k0lm/riw[:{#$"
key8 = "k]p+#vuyg~d0o4%l=^t($5h`1!,j2czs7&.[*;6eia3-8b}/9@:m)x{frwq|n "
key9 = "bk$e&wv:c!os9@m7+;at0h-g],z*/q%n(36.8d^~y|{p1[fl=42ixu )r5`}j#"
keya = "!~29%#g7:4c@}=.]mjq1{w*e|(5yhv +t&albkp/-r[i83;)d$un,^0of`zx6s"
keyb = "}s($f dq!6)aw+olpg9h-8#[x`m1:/0.{%c5uity3kjn|,=]&~^r;4*b27z@ve"
keyc = "[n$v|`yhcfj1wd#gx498(:{^-3b %k}epzlmqs*7&,!)6u~2t@;5.i]0/=o+ra"
keyd = "&xgr1=!v.c~+f|#4be$[zp2,{h0-qi%tm*;/)`9kj}lsnud6] a(w3@^:75oy8"
keye = "`i3jvor{!1-uy@cgfeq8067zl]s5%2 &(n4ph~+=t#w}ax*d)$|.bk,^;m:/[9"
keyf = "ebph82dn;,+z~4%wr*!{-t|=3o1u^]`j&c#/l[ms5yq.@i(690 vx}ak:g$f)7"
alph = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-+=|[]{},.;:`~/ " #dont edit this
print("I recommend making 16 new keys then editing the keys in the file")
if "yes" == input("Do you want to generate new keys (yes / no): "): #makes new keys until program is closed
    while True:
        encodedlist = []
        loop = 0
        while loop != len(alph):
            randalph = random.choice(alph)
            while randalph in encodedlist:
                randalph = random.choice(alph)
            encodedlist.append(randalph)
            loop = loop + 1
        print(''.join(str(i) for i in encodedlist))
        nothing = input("")

while True:
    key = int(input("Starting chat key(1 - 16): "))
    msg = input("Message to decode / encode: ")
    code = input("encode / decode (e / d): ")
    emsg = ""
    if code == "e": #encoding part
        for i in msg:
            if key > 16:
                key = 1
            if key == 1:
                emsg = emsg + alph[key0.find(i)]
            if key == 2:
                emsg = emsg + alph[key1.find(i)]
            if key == 3:
                emsg = emsg + alph[key2.find(i)]
            if key == 4:
                emsg = emsg + alph[key3.find(i)]
            if key == 5:
                emsg = emsg + alph[key4.find(i)]
            if key == 6:
                emsg = emsg + alph[key5.find(i)]
            if key == 7:
                emsg = emsg + alph[key6.find(i)]
            if key == 8:
                emsg = emsg + alph[key7.find(i)]
            if key == 9:
                emsg = emsg + alph[key8.find(i)]
            if key == 10:
                emsg = emsg + alph[key9.find(i)]
            if key == 11:
                emsg = emsg + alph[keya.find(i)]
            if key == 12:
                emsg = emsg + alph[keyb.find(i)]
            if key == 13:
                emsg = emsg + alph[keyc.find(i)]
            if key == 14:
                emsg = emsg + alph[keyd.find(i)]
            if key == 15:
                emsg = emsg + alph[keye.find(i)]
            if key == 16:
                emsg = emsg + alph[keyf.find(i)]
            key = key + 1
    elif code == "d": #decoding part
        for i in msg:
            if key > 16:
                key = 1
            if key == 1:
                emsg = emsg + key0[alph.find(i)]
            if key == 2:
                emsg = emsg + key1[alph.find(i)]
            if key == 3:
                emsg = emsg + key2[alph.find(i)]
            if key == 4:
                emsg = emsg + key3[alph.find(i)]
            if key == 5:
                emsg = emsg + key4[alph.find(i)]
            if key == 6:
                emsg = emsg + key5[alph.find(i)]
            if key == 7:
                emsg = emsg + key6[alph.find(i)]
            if key == 8:
                emsg = emsg + key7[alph.find(i)]
            if key == 9:
                emsg = emsg + key8[alph.find(i)]
            if key == 10:
                emsg = emsg + key9[alph.find(i)]
            if key == 11:
                emsg = emsg + keya[alph.find(i)]
            if key == 12:
                emsg = emsg + keyb[alph.find(i)]
            if key == 13:
                emsg = emsg + keyc[alph.find(i)]
            if key == 14:
                emsg = emsg + keyd[alph.find(i)]
            if key == 15:
                emsg = emsg + keye[alph.find(i)]
            if key == 16:
                emsg = emsg + keyf[alph.find(i)]
            key = key + 1
    print(emsg)
