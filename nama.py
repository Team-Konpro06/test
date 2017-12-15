#PROGRAM EKSEKUSI WHILE
nama = ""

#konsep while (akan melakukan perulangan), hingga
#counter dari while terpenuhi, counter --> nama

#apabila nama tidak sama dengan python
while nama != "python" :
	#apabila (nama!="python") = true
	#kode dibawah akan di jalankan
	nama = raw_input("Masukan nama : ")
	print("Nama saya ",nama)
	if nama == "python":
		print("Goodbye ",nama)