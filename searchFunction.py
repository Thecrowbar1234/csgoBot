def replaceWeaponName(weapon) :
	search = weapon.lower()
	#rifles
	if search.find("ak") != -1 or search.find("47") != -1 :
		return "AK-47%20"
	elif search.find("awp") != -1 :
		return "AWP%20"
	elif search.find("a1s") != -1 :
		return "M4A1-S%20"
	elif search.find("m4") != -1 :
		return "M4A4%20"
	elif search.find("ssg") != -1 or search.find("08") != -1 or search.find("scout") :
		return "SSG%2008%20"
	elif search.find("scar") != -1 or search.find("20") != -1 :
		return "SCAR-20%20"
	elif search.find("g3") != -1 or search.find("sg1") != -1 :
		return "G3SG1%20"
	elif search.find("aug") != -1 :
		return "AUG%20"
	elif search.find("sg") != -1 or search.find("553") != -1 :
		return "SG%20553%20"
	elif search.find("galil") != -1 or search.find("ar") != -1 :
		return "Galil%20AR%20"
	elif search.find("famas") != -1 :
		return "FAMAS%20"
	elif search.find("g3") or search.find("sg1") != -1 :
		return "G3SG1%20"
	#SMGs

def replaceWeaponWear(wear) :
	search = wear.lower()
	if search.find("fn") != -1 :
		return "%28Factory%20New%29"
	elif search.find("mw") != -1 :
		return "%28Minimal%20Wear%29"
	elif search.find("ft") != -1 :
		return "%28Field-Tested%29"
	elif search.find("ww") != -1 :
		return "%28Well-Worn%29"
	elif search.find("bs") != -1 :
		return "%28Battle-Scarred%29"