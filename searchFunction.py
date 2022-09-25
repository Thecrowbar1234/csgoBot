def replaceWeaponName(weapon) :
	search = weapon.lower()
	#rifles
	if search.find("ak") != -1 or search.find("47") != -1 :
		return "AK-47%20", "AK-47"
	elif search.find("awp") != -1 :
		return "AWP%20", "AWP"
	elif search.find("a1s") != -1 :
		return "M4A1-S%20", "M4A1-S"
	elif search.find("m4") != -1 :
		return "M4A4%20", "M4A4"
	elif search.find("ssg") != -1 or search.find("08") != -1 or search.find("scout") :
		return "SSG%2008%20", "SSG 08"
	elif search.find("scar") != -1 or search.find("20") != -1 :
		return "SCAR-20%20", "SCAR-20"
	elif search.find("g3") != -1 or search.find("sg1") != -1 :
		return "G3SG1%20", "G3SG1"
	elif search.find("aug") != -1 :
		return "AUG%20", "AUG"
	elif search.find("sg") != -1 or search.find("553") != -1 :
		return "SG%20553%20", "SG 553"
	elif search.find("galil") != -1 or search.find("ar") != -1 :
		return "Galil%20AR%20", "Galil AR"
	elif search.find("famas") != -1 :
		return "FAMAS%20", "FAMAS"
	#SMGs

def replaceWeaponWear(wear) :
	search = wear.lower()
	if search.find("fn") != -1 :
		return "%28Factory%20New%29", "(Factory New)"
	elif search.find("mw") != -1 :
		return "%28Minimal%20Wear%29", "(Minimal Wear)"
	elif search.find("ft") != -1 :
		return "%28Field-Tested%29", "(Field-Tested)"
	elif search.find("ww") != -1 :
		return "%28Well-Worn%29", "(Well-Worn)"
	elif search.find("bs") != -1 :
		return "%28Battle-Scarred%29", "(Battle-Scarred)"