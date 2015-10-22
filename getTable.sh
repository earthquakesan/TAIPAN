#!/bin/bash

TABLES="68779923_2_1000046510804975562.csv 14575591_0_5962885285845713108.csv 96971074_0_2380250642274572846.csv 9353071_0_969221250383056227.csv 94145647_0_4411495338698364870.csv 21547990_0_4278595903015489107.csv 15525140_24_4037246854219698153.csv 71137051_0_8039724067857124984.csv 9348099_0_390574653830621671.csv 76279179_0_1206538098393858428.csv 40387275_6_6191495397368895712.csv 7207849_0_1015109135224818932.csv 30103516_1_7626625507688323656.csv 28788428_0_7847978656182431680.csv 34119774_0_289423522044280059.csv 39650055_5_7135804139753401681.csv 20986241_116_7013408060096179711.csv 31872906_0_6106277903085193669.csv 64207896_0_3206705146602325658.csv 5002114_6_4320409333965117351.csv 64626513_0_6402630457637049755.csv 98786033_0_3931553788835402240.csv 90593344_0_8311455501234425088.csv 60527660_0_4311923120030730708.csv 83987849_0_5969920363690793217.csv 31135207_0_1440209822839624711.csv 87684775_0_3688301103288332064.csv 63504330_0_8522180319329276399.csv 52982899_0_5726315103246010014.csv 5920491_0_3348835015780600788.csv 75686837_0_7143521782053477488.csv 37222124_0_2523821086878486427.csv 41839679_0_3009344178474568371.csv 91412091_0_7825290509158569518.csv 67044147_3_2407225246443640173.csv 38825076_4_4240132090463534680.csv 48154773_2_8458867040172221682.csv 62225043_0_1859194456424768736.csv 34061753_1_7120939110353093152.csv 25596525_7_8049218440277756227.csv 43619692_1_8695615891377032939.csv 15432418_0_1240151322836769987.csv 17871230_1_6194965835407257694.csv 36011298_0_6854642860526463972.csv 31786950_6_6643972137715983094.csv 12125836_0_1134348206297032434.csv 2066887_0_746204117268168398.csv 44714784_0_9148174727002289290.csv 55150207_16_3215605693899991922.csv 23525318_0_7885756089060858697.csv 64453534_0_2231985329462980688.csv 36508695_2_4137125988909119946.csv 82726631_0_8916527354641308381.csv 17362344_1_5095929604749154053.csv 83532490_1_8333702357543616751.csv 15083191_0_8241448979933321195.csv 7866138_0_3576557501117896371.csv 14354060_0_2913685180675424978.csv 62958765_0_3674859967182781097.csv 17627487_0_7482364338839093515.csv 38552884_0_7504620928763706132.csv 73146534_0_2437590818976170846.csv 3876573_0_5902554158837152331.csv 73329570_0_6585265340512320118.csv 93282452_50_2022610686980235524.csv 53445890_1_3674988499038067538.csv 9155607_0_3860438754576233830.csv 66986032_1_2775601573719835514.csv 24859353_0_7027810986004269522.csv 89892933_0_8247479835926862600.csv 61714447_0_2408934031491056964.csv 41346299_0_5222632701245297340.csv 24074438_0_5878229540726224471.csv 60756411_0_463101439270968728.csv 61086277_0_5431539545753310611.csv 27411298_0_6391178424656872117.csv 58480457_0_4976666994701664315.csv 40643655_0_1197576731513171589.csv 27100349_0_4569354779422013472.csv 32936911_79_1142044601974469341.csv 28981185_0_4400650637320353140.csv 37856682_0_6818907050314633217.csv 20886950_0_139024002426598867.csv 92559788_0_507775366092031581.csv 29414811_13_8724394428539174350.csv 55961337_0_6548713781034932742.csv 44942480_0_2396126158991576450.csv 37766292_0_8154499853610546668.csv 66331605_0_697628901562774965.csv 34574938_0_498813987749776643.csv 19655010_0_660968701335909436.csv 81018286_0_4591208644539747649.csv 18036618_0_7337008284167773018.csv 59296459_0_4532872443713262457.csv 5873256_0_7795190905731964989.csv 23723517_0_6355329536965120157.csv 1092764_0_7623796846778750529.csv 30098333_0_6321221304321476486.csv 33832430_0_2157776220385390595.csv 12183399_0_6725061928072492226.csv"
for table in $TABLES
do
  echo $table
  python scripts/getPropertiesForTable.py $table
  read -p "Press [Enter] key to continue..."
done
