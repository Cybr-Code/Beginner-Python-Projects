import os
class Text:
	paragraph = {
	'A' : r"""
 _____ 
|  _  |
|     |
|__|__|
       
	"""
, 
'B' : r"""
 _____ 
| __  |
| __ -|
|_____|
       
	"""
, 
	'C' : r"""
 _____ 
|     |
|   --|
|_____|
       
	"""
, 
	'D' : r"""
 ____  
|    \ 
|  |  |
|____/ 
       
	"""
, 
	'E' : r"""
 _____ 
|   __|
|   __|
|_____|
       
	"""
, 
	'F' : r"""
 _____ 
|   __|
|   __|
|__|   
       
	"""
, 
	'G' : r"""
 _____ 
|   __|
|  |  |
|_____|
       
	"""
, 
	'H' : r"""
 _____ 
|  |  |
|     |
|__|__|
       
	"""
, 
	'I' : r"""
 _____ 
|     |
|-   -|
|_____|
       
	"""
, 
	'J' : r"""
    __ 
 __|  |
|  |  |
|_____|
       
	"""
, 
	'K' : r"""
 _____ 
|  |  |
|    -|
|__|__|
       
	"""
, 
	'L' : r"""
 __    
|  |   
|  |__ 
|_____|
       
	"""
, 
	'M' : r"""
 _____ 
|     |
| | | |
|_|_|_|
       
	"""
, 
	'N' : r"""
 _____ 
|   | |
| | | |
|_|___|
       
	"""
, 
	'O' : r"""
 _____ 
|     |
|  |  |
|_____|
       
	"""
, 
	'P' : r"""
 _____ 
|  _  |
|   __|
|__|   
       
	"""
, 
	'Q' : r"""
 _____ 
|     |
|  |  |
|__  _|
   |__|
	"""
, 
	'R' : r"""
 _____ 
| __  |
|    -|
|__|__|
       
	"""
, 
	'S' : r"""
 _____ 
|   __|
|__   |
|_____|
       
	"""
, 
	'T' : r"""
 _____ 
|_   _|
  | |  
  |_|  
       
	"""
, 
	'U' : r"""
 _____ 
|  |  |
|  |  |
|_____|
       
	"""
, 
	'V' : r"""
 _____ 
|  |  |
|  |  |
 \___/ 
       
	"""
, 
	'W' : r"""
 _ _ _ 
| | | |
| | | |
|_____|
       
	"""
, 
	'X' : r"""
 __ __ 
|  |  |
|-   -|
|__|__|
       
	"""
, 
	'Y' : r"""
 __ __ 
|  |  |
|_   _|
  |_|  
       
	"""
, 
	'Z' : r"""
 _____ 
|__   |
|   __|
|_____|
       
	"""
, 
	'a' : r"""
     
 ___ 
| .'|
|__,|
     
	"""
, 
	'b' : r"""
 _   
| |_ 
| . |
|___|
     
	"""
, 
	'c' : r"""
     
 ___ 
|  _|
|___|
     
	"""
, 
	'd' : r"""
   _ 
 _| |
| . |
|___|
     
	"""
, 
	'e' : r"""
     
 ___ 
| -_|
|___|
     
	"""
, 
	'f' : r"""
 ___ 
|  _|
|  _|
|_|  
     
	"""
, 
	'g' : r"""
     
 ___ 
| . |
|_  |
|___|
	"""
, 
	'h' : r"""
 _   
| |_ 
|   |
|_|_|
     
	"""
, 
	'i' : r"""
 _ 
|_|
| |
|_|
   
	"""
, 
	'j' : r"""
   _ 
  |_|
  | |
 _| |
|___|
	"""
, 
	'k' : r"""
 _   
| |_ 
| '_|
|_,_|
     
	"""
, 
	'l' : r"""
 _ 
| |
| |
|_|
   
	"""
, 
	'm' : r"""
       
 _____ 
|     |
|_|_|_|
       
	"""
, 
	'n' : r"""
     
 ___ 
|   |
|_|_|
     
	"""
, 
	'o' : r"""
     
 ___ 
| . |
|___|
     
	"""
, 
	'p' : r"""
     
 ___ 
| . |
|  _|
|_|  
	"""
, 
	'q' : r"""
     
 ___ 
| . |
|_  |
  |_|
	"""
, 
	'r' : r"""
     
 ___ 
|  _|
|_|  
     
	"""
, 
	's' : r"""
     
 ___ 
|_ -|
|___|
     
	"""
, 
	't' : r"""
 _   
| |_ 
|  _|
|_|  
     
	"""
, 
	'u' : r"""
     
 _ _ 
| | |
|___|
     
	"""
, 
	'v' : r"""
     
 _ _ 
| | |
 \_/ 
     
	"""
, 
	'w' : r"""
       
 _ _ _ 
| | | |
|_____|
       
	"""
, 
	'x' : r"""
     
 _ _ 
|_'_|
|_,_|
     
	"""
, 
	'y' : r"""
     
 _ _ 
| | |
|_  |
|___|
	"""
, 
	'z' : r"""
     
 ___ 
|- _|
|___|
     
	"""
, 
	'?' : r"""
 _____ 
|___  |
  |  _|
  |_|  
  |_|  
	"""
, 
	'!' : r"""
 __ 
|  |
|  |
|__|
|__|
	"""
, 
	'.' : r"""
   
   
 _ 
|_|
   
	"""
, 
	',' : r"""
   
   
   
 __
/_/
	"""
, 
	' ' : r"""
    
    
    
    
    
	"""
, 
	'\'' : r"""
 _ 
| |
|_|
   
   
	"""
    }
def write(text = "Hello, World!", type = 'paragraph'):
	size = os.get_terminal_size()
	os_length = size.columns
	chars = dict()
	if type == 'paragraph':
		chars.update(Text.paragraph)
	all_lines = []
	comb_lines = []
	for i in text:
		lines = chars.get(i).splitlines()
		del lines[0]
		del lines[-1]
		all_lines.append(lines)
	letter_lengths = []
	for i in all_lines:
		letter_lengths.append(len(i[0]) + letter_lengths[-1] if len(letter_lengths) != 0 else len(i[0]) - 1)
	lengths = []
	for i in all_lines:
		lengths.append(len(i))
	max_h = max(lengths)
	for i in range(max_h):
		string = r""""""
		for lines in all_lines:
			string += lines[i]
		comb_lines.append(string)
	sp_ind = []
	del cutoff[-1]
	for index, i in enumerate(comb_lines[0]):
		if i == ' ':
			for cl in comb_lines[1::]:
				if cl[index] != ' ':
					break
				elif cl[index] == ' ' and comb_lines.index(cl) == max_h - 1:
					sp_ind.append(index)
	tmp = 3
	temp = []
	for i in sp_ind:
		if tmp == 3:
			temp.append(i)
			tmp = 0
			continue
		tmp += 1
	sp_ind.clear()
	for i in temp:
		sp_ind.append(i)
	temp.clear()
	cutoff.clear()
	cutoff.append(os_length)
	for i in sp_ind:
		if cutoff[0] < i:
			cutoff.append(sp_ind[sp_ind.index(i) - 1] + 3)
			break
	del cutoff[0]
	while cutoff[-1] + os_length  < len(comb_lines[0]):
		for idx, i in enumerate(sp_ind):
			if cutoff[-1] + os_length < i:
				cutoff.append(sp_ind[idx - 1] + 3)
				break
	letters = []
	for i in cutoff:
		letters.append(letter_lengths.index(i))
	letters.insert(0,0)
	letters.append(len(text))
	t = []
	for idx, i in enumerate(letters):
		start = i
		if len(letters) >= idx + 2:
			end = letters[idx+1]
		else:
			break
		t.append(text[start:end:])
	print(t)
	for thingamajig in t:
		all_lines = []
		for i in thingamajig:
			lines = chars.get(i).splitlines()
			all_lines.append(lines)
		lengths = []
		for i in all_lines:
			lengths.append(len(i))
		max_h = max(lengths)
		for i in range(max_h):
			string = r""""""
			for lines in all_lines:
				string += lines[i]
			print(string)
