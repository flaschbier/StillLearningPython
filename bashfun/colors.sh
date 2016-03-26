# http://stackoverflow.com/questions/16843382/colored-shell-script-output-library

export ResetColor='\033[0m'

export Black='\033[0;30m'
export BoldBlack='\033[1;30m'
export UnderlinedBlack='\033[4;30m'
export IntenseBlack='\033[0;90m'
export BoldIntenseBlack='\033[1;90m'
export OnBlack='\033[40m'
export OnIntnenseBlack='\033[0;100m'

export Red='\033[0;31m'
export BoldRed='\033[1;31m'
export UnderlinedRed='\033[4;31m'
export IntenseRed='\033[0;91m'
export BoldIntenseRed='\033[1;91m'
export OnRed='\033[41m'
export OnIntenseRed='\033[0;101m'

export Green='\033[0;32m'
export BoldGreen='\033[1;32m'
export UnderlinedGreen='\033[4;32m'
export IntenseGreen='\033[0;92m'
export BoldIntenseGreen='\033[1;92m'
export OnGreen='\033[42m'
export OnIntenseGreen='\033[0;102m'

export Yellow='\033[0;33m'
export BoldYellow='\033[1;33m'
export UnderlinedYellow='\033[4;33m'
export IntenseYellow='\033[0;93m'
export BoldIntenseYellow='\033[1;93m'
export OnYellow='\033[43m'
export OnIntenseYellow='\033[0;103m'

export Blue='\033[0;34m'
export BoldBlue='\033[1;34m'
export UnderlinedBlue='\033[4;34m'
export IntenseBlue='\033[0;94m'
export BoldIntenseBlue='\033[1;94m'
export OnBlue='\033[44m'
export OnIntenseBlu='\033[0;104m'

export Purple='\033[0;35m'
export BoldPurple='\033[1;35m'
export UnderlinedPurple='\033[4;35m'
export IntensePurple='\033[0;95m'
export BoldIntensePurple='\033[1;95m'
export OnPurple='\033[45m'
export OnIntensePurple='\033[0;105m'

export Cyan='\033[0;36m'
export BoldCyan='\033[1;36m'
export UnderlinedCyan='\033[4;36m'
export IntenseCyan='\033[0;96m'
export BoldIntenseCyan='\033[1;96m'
export OnCyan='\033[46m'
export OnIntenseCyan='\033[0;106m';

export White='\033[0;37m'
export BoldWhite='\033[1;37m'
export UnderlinedWhite='\033[4;37m'
export IntenseWhite='\033[0;97m'
export BoldIntenseWhite='\033[1;97m'
export OnWhite='\033[47m'
export OnIntenseWhite='\033[0;107m'

echo -e "${BoldIntenseRed}Colors${ResetColor} ${IntenseYellow}at your${ResetColor} ${IntenseGreen}service${ResetColor} ${Black}${OnWhite}:3${ResetColor}"
